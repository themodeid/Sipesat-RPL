import { Router } from 'express';
import { prisma } from '../config/prisma';
import { authMiddleware, AuthenticatedRequest, requireRole } from '../middlewares/auth.middleware';

const router = Router();

router.get('/', authMiddleware, async (req, res) => {
  try {
    const jenisSurat = await prisma.jenisSurat.findMany({
      orderBy: { namaSurat: 'asc' },
      include: {
        _count: {
          select: { pengajuan: true },
        },
      },
    });
    return res.json({ data: jenisSurat });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal mengambil data jenis surat' });
  }
});

router.post('/', authMiddleware, requireRole(['ADMIN', 'PETUGAS']), async (req: AuthenticatedRequest, res) => {
  try {
    const { kodeSurat, namaSurat, deskripsi, persyaratan, formatNomor, templateIsi } = req.body;

    if (!kodeSurat || !namaSurat || !deskripsi) {
      return res.status(400).json({ error: 'Kode, Nama, dan Deskripsi surat wajib diisi' });
    }

    const existing = await prisma.jenisSurat.findUnique({
      where: { kodeSurat: kodeSurat.trim().toUpperCase() },
    });

    if (existing) {
      return res.status(400).json({ error: 'Kode surat sudah terdaftar' });
    }

    const created = await prisma.jenisSurat.create({
      data: {
        kodeSurat: kodeSurat.trim().toUpperCase(),
        namaSurat,
        deskripsi,
        persyaratan,
        formatNomor: formatNomor || '421.3/{NOMOR}/SMKN1/{BULAN_ROMAWI}/{TAHUN}',
        templateIsi,
        isActive: true,
      },
    });

    return res.status(201).json({ success: true, data: created });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal menambahkan jenis surat' });
  }
});

router.put('/', authMiddleware, requireRole(['ADMIN', 'PETUGAS']), async (req: AuthenticatedRequest, res) => {
  try {
    const { id, kodeSurat, namaSurat, deskripsi, persyaratan, formatNomor, templateIsi, isActive } = req.body;

    if (!id) {
      return res.status(400).json({ error: 'ID jenis surat diperlukan' });
    }

    const updated = await prisma.jenisSurat.update({
      where: { id },
      data: {
        kodeSurat: kodeSurat ? kodeSurat.trim().toUpperCase() : undefined,
        namaSurat,
        deskripsi,
        persyaratan,
        formatNomor,
        templateIsi,
        isActive: isActive !== undefined ? isActive : undefined,
      },
    });

    return res.json({ success: true, data: updated });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal memperbarui jenis surat' });
  }
});

export default router;
