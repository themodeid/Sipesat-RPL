import { Router } from 'express';
import { prisma } from '../config/prisma';
import { authMiddleware, AuthenticatedRequest } from '../middlewares/auth.middleware';
import { StatusPengajuan } from '@prisma/client';
import { generateNomorSuratResmi } from '../utils/format';

const router = Router();

router.get('/', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    const { status, search, jenisSuratId, startDate, endDate } = req.query as Record<string, string>;

    const where: any = {};

    if (user.role === 'SISWA') {
      where.siswaId = user.id;
    }

    if (status && status !== 'SEMUA') {
      where.status = status as StatusPengajuan;
    }

    if (jenisSuratId) {
      where.jenisSuratId = jenisSuratId;
    }

    if (startDate || endDate) {
      where.tanggalPengajuan = {};
      if (startDate) {
        where.tanggalPengajuan.gte = new Date(startDate);
      }
      if (endDate) {
        const end = new Date(endDate);
        end.setHours(23, 59, 59, 999);
        where.tanggalPengajuan.lte = end;
      }
    }

    if (search && search.trim()) {
      const q = search.trim();
      where.OR = [
        { nomorPengajuan: { contains: q, mode: 'insensitive' } },
        { nomorSuratResmi: { contains: q, mode: 'insensitive' } },
        { keperluan: { contains: q, mode: 'insensitive' } },
        {
          siswa: {
            OR: [
              { nama: { contains: q, mode: 'insensitive' } },
              { nisn: { contains: q, mode: 'insensitive' } },
              { kelas: { contains: q, mode: 'insensitive' } },
            ],
          },
        },
      ];
    }

    const pengajuanList = await prisma.pengajuanSurat.findMany({
      where,
      orderBy: { tanggalPengajuan: 'desc' },
      include: {
        siswa: {
          select: {
            id: true,
            nama: true,
            nisn: true,
            kelas: true,
            jurusan: true,
            noTelepon: true,
          },
        },
        jenisSurat: {
          select: {
            id: true,
            kodeSurat: true,
            namaSurat: true,
            formatNomor: true,
            templateIsi: true,
          },
        },
        petugas: {
          select: {
            id: true,
            nama: true,
            username: true,
          },
        },
      },
    });

    return res.json({ data: pengajuanList });
  } catch (error) {
    console.error('Error get pengajuan:', error);
    return res.status(500).json({ error: 'Gagal mengambil data pengajuan' });
  }
});

router.post('/', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    const { jenisSuratId, keperluan, keterangan, lampiran, siswaId: reqSiswaId } = req.body;

    if (!jenisSuratId || !keperluan) {
      return res.status(400).json({ error: 'Jenis surat dan keperluan wajib diisi!' });
    }

    const targetSiswaId = user.role === 'SISWA' ? user.id : (reqSiswaId || user.id);

    const now = new Date();
    const yearMonth = `${now.getFullYear()}${String(now.getMonth() + 1).padStart(2, '0')}`;
    const todayCount = await prisma.pengajuanSurat.count();
    const nomorPengajuan = `REQ-${yearMonth}-${String(todayCount + 1).padStart(4, '0')}`;

    const newPengajuan = await prisma.pengajuanSurat.create({
      data: {
        nomorPengajuan,
        siswaId: targetSiswaId,
        jenisSuratId,
        keperluan,
        keterangan: keterangan || null,
        lampiran: lampiran || null,
        status: StatusPengajuan.MENUNGGU,
      },
      include: {
        jenisSurat: true,
        siswa: true,
      },
    });

    await prisma.logAktivitas.create({
      data: {
        pengajuanId: newPengajuan.id,
        userId: user.id,
        statusSesudah: StatusPengajuan.MENUNGGU,
        catatan: `Pengajuan surat baru dibuat oleh ${user.nama}`,
      },
    });

    return res.status(201).json({
      success: true,
      message: 'Pengajuan surat berhasil dikirim!',
      data: newPengajuan,
    });
  } catch (error) {
    console.error('Error post pengajuan:', error);
    return res.status(500).json({ error: 'Gagal membuat pengajuan surat.' });
  }
});

router.get('/:id', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    const { id } = req.params;

    const pengajuan = await prisma.pengajuanSurat.findUnique({
      where: { id },
      include: {
        siswa: true,
        jenisSurat: true,
        petugas: {
          select: {
            id: true,
            nama: true,
            username: true,
            role: true,
          },
        },
        logs: {
          orderBy: { createdAt: 'desc' },
          include: {
            user: {
              select: {
                nama: true,
                role: true,
              },
            },
          },
        },
      },
    });

    if (!pengajuan) {
      return res.status(404).json({ error: 'Pengajuan surat tidak ditemukan' });
    }

    if (user.role === 'SISWA' && pengajuan.siswaId !== user.id) {
      return res.status(403).json({ error: 'Akses ditolak' });
    }

    return res.json({ data: pengajuan });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal mengambil detail' });
  }
});

router.patch('/:id', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    if (user.role === 'SISWA') {
      return res.status(403).json({ error: 'Hanya petugas tata usaha atau admin yang berwenang memverifikasi status.' });
    }

    const { id } = req.params;
    const { status, catatanPetugas, nomorSuratResmi } = req.body;

    const existing = await prisma.pengajuanSurat.findUnique({
      where: { id },
      include: { jenisSurat: true },
    });

    if (!existing) {
      return res.status(404).json({ error: 'Pengajuan tidak ditemukan' });
    }

    let finalNomorSurat = nomorSuratResmi || existing.nomorSuratResmi;
    let tanggalSelesai = existing.tanggalSelesai;

    if (status === StatusPengajuan.DISETUJUI) {
      tanggalSelesai = new Date();
      if (!finalNomorSurat) {
        const approvedCount = await prisma.pengajuanSurat.count({
          where: {
            status: StatusPengajuan.DISETUJUI,
            jenisSuratId: existing.jenisSuratId,
          },
        });
        finalNomorSurat = generateNomorSuratResmi(
          existing.jenisSurat.formatNomor,
          approvedCount + 1
        );
      }
    }

    const updated = await prisma.pengajuanSurat.update({
      where: { id },
      data: {
        status: status as StatusPengajuan,
        petugasId: user.id,
        catatanPetugas: catatanPetugas !== undefined ? catatanPetugas : existing.catatanPetugas,
        nomorSuratResmi: finalNomorSurat,
        tanggalSelesai,
      },
      include: {
        siswa: true,
        jenisSurat: true,
        petugas: true,
      },
    });

    let logNote = `Status diubah dari ${existing.status} ke ${status} oleh ${user.nama}`;
    if (catatanPetugas) {
      logNote += ` (Catatan: "${catatanPetugas}")`;
    }
    if (finalNomorSurat && status === StatusPengajuan.DISETUJUI) {
      logNote += ` [No. Surat: ${finalNomorSurat}]`;
    }

    await prisma.logAktivitas.create({
      data: {
        pengajuanId: id,
        userId: user.id,
        statusSebelum: existing.status,
        statusSesudah: status as StatusPengajuan,
        catatan: logNote,
      },
    });

    return res.json({
      success: true,
      message: 'Status pengajuan berhasil diperbarui',
      data: updated,
    });
  } catch (error) {
    console.error('Error patch pengajuan:', error);
    return res.status(500).json({ error: 'Gagal memperbarui status' });
  }
});

router.delete('/:id', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    const { id } = req.params;

    const existing = await prisma.pengajuanSurat.findUnique({ where: { id } });
    if (!existing) {
      return res.status(404).json({ error: 'Pengajuan tidak ditemukan' });
    }

    if (user.role === 'SISWA') {
      if (existing.siswaId !== user.id || existing.status !== StatusPengajuan.MENUNGGU) {
        return res.status(403).json({ error: 'Pengajuan tidak dapat dibatalkan.' });
      }
    }

    await prisma.pengajuanSurat.delete({ where: { id } });
    return res.json({ success: true, message: 'Pengajuan surat berhasil dibatalkan.' });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal menghapus pengajuan' });
  }
});

export default router;
