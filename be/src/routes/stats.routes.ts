import { Router } from 'express';
import { prisma } from '../config/prisma';
import { authMiddleware, AuthenticatedRequest } from '../middlewares/auth.middleware';

const router = Router();

router.get('/', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    const isSiswa = user.role === 'SISWA';
    const filterWhere = isSiswa ? { siswaId: user.id } : {};

    const [total, pending, diproses, disetujui, ditolak, totalSiswa, totalJenis] = await Promise.all([
      prisma.pengajuanSurat.count({ where: filterWhere }),
      prisma.pengajuanSurat.count({ where: { ...filterWhere, status: 'MENUNGGU' } }),
      prisma.pengajuanSurat.count({ where: { ...filterWhere, status: 'DIPROSES' } }),
      prisma.pengajuanSurat.count({ where: { ...filterWhere, status: 'DISETUJUI' } }),
      prisma.pengajuanSurat.count({ where: { ...filterWhere, status: 'DITOLAK' } }),
      prisma.user.count({ where: { role: 'SISWA' } }),
      prisma.jenisSurat.count({ where: { isActive: true } }),
    ]);

    const recent = await prisma.pengajuanSurat.findMany({
      where: filterWhere,
      take: 6,
      orderBy: { tanggalPengajuan: 'desc' },
      include: {
        siswa: {
          select: {
            nama: true,
            nisn: true,
            kelas: true,
          },
        },
        jenisSurat: {
          select: {
            namaSurat: true,
            kodeSurat: true,
          },
        },
      },
    });

    return res.json({
      stats: {
        total,
        pending,
        diproses,
        disetujui,
        ditolak,
        totalSiswa,
        totalJenis,
      },
      recent,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal memuat statistik' });
  }
});

export default router;
