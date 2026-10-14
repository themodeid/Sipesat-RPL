import { Router } from 'express';
import bcrypt from 'bcryptjs';
import { prisma } from '../config/prisma';
import { authMiddleware, AuthenticatedRequest, requireRole } from '../middlewares/auth.middleware';

const router = Router();

router.get('/', authMiddleware, requireRole(['ADMIN', 'PETUGAS']), async (req: AuthenticatedRequest, res) => {
  try {
    const { search } = req.query as Record<string, string>;
    const where: any = { role: 'SISWA' };

    if (search && search.trim()) {
      const q = search.trim();
      where.OR = [
        { nama: { contains: q, mode: 'insensitive' } },
        { nisn: { contains: q, mode: 'insensitive' } },
        { kelas: { contains: q, mode: 'insensitive' } },
        { jurusan: { contains: q, mode: 'insensitive' } },
      ];
    }

    const siswaList = await prisma.user.findMany({
      where,
      orderBy: { nama: 'asc' },
      select: {
        id: true,
        nisn: true,
        nama: true,
        email: true,
        kelas: true,
        jurusan: true,
        noTelepon: true,
        alamat: true,
        createdAt: true,
        _count: {
          select: { pengajuan: true },
        },
      },
    });

    return res.json({ data: siswaList });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal mengambil data siswa' });
  }
});

router.post('/', authMiddleware, requireRole(['ADMIN', 'PETUGAS']), async (req: AuthenticatedRequest, res) => {
  try {
    const { nisn, nama, email, kelas, jurusan, noTelepon, alamat, password } = req.body;

    if (!nisn || !nama || !kelas) {
      return res.status(400).json({ error: 'NISN, Nama, dan Kelas wajib diisi' });
    }

    const existing = await prisma.user.findFirst({
      where: { nisn: nisn.trim() },
    });

    if (existing) {
      return res.status(400).json({ error: 'NISN sudah terdaftar' });
    }

    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(password || 'siswa123', salt);

    const created = await prisma.user.create({
      data: {
        nisn: nisn.trim(),
        nama,
        email: email || null,
        kelas,
        jurusan: jurusan || null,
        noTelepon: noTelepon || null,
        alamat: alamat || null,
        password: hashedPassword,
        role: 'SISWA',
      },
    });

    return res.status(201).json({ success: true, data: created });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal menambahkan siswa' });
  }
});

export default router;
