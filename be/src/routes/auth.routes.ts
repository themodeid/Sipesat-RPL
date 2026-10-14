import { Router } from 'express';
import bcrypt from 'bcryptjs';
import { prisma } from '../config/prisma';
import { signToken } from '../utils/jwt';
import { authMiddleware, AuthenticatedRequest } from '../middlewares/auth.middleware';

const router = Router();

router.post('/login', async (req, res) => {
  try {
    const { roleType, identifier, password } = req.body;

    if (!identifier || !password) {
      return res.status(400).json({ error: 'Mohon isi semua data yang dibutuhkan!' });
    }

    let user;
    if (roleType === 'SISWA') {
      user = await prisma.user.findFirst({
        where: {
          nisn: identifier.trim(),
          role: 'SISWA',
        },
      });
    } else {
      user = await prisma.user.findFirst({
        where: {
          OR: [
            { username: identifier.trim() },
            { email: identifier.trim() },
          ],
          role: { in: ['ADMIN', 'PETUGAS'] },
        },
      });
    }

    if (!user) {
      return res.status(401).json({ error: 'Akun tidak ditemukan. Periksa kembali NISN/Username Anda.' });
    }

    const isValidPassword = await bcrypt.compare(password, user.password);
    if (!isValidPassword) {
      return res.status(401).json({ error: 'Kata sandi yang dimasukkan salah.' });
    }

    const sessionPayload = {
      id: user.id,
      nama: user.nama,
      role: user.role,
      username: user.username,
      nisn: user.nisn,
      email: user.email,
      kelas: user.kelas,
      jurusan: user.jurusan,
    };

    const token = signToken(sessionPayload);

    return res.json({
      success: true,
      message: 'Login berhasil',
      token,
      user: sessionPayload,
    });
  } catch (error) {
    console.error('Error login Express:', error);
    return res.status(500).json({ error: 'Terjadi kesalahan sistem pada server.' });
  }
});

router.get('/me', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const userId = req.user!.id;
    const user = await prisma.user.findUnique({
      where: { id: userId },
      select: {
        id: true,
        nama: true,
        role: true,
        username: true,
        nisn: true,
        email: true,
        kelas: true,
        jurusan: true,
        noTelepon: true,
        alamat: true,
      },
    });

    if (!user) {
      return res.status(401).json({ authenticated: false, user: null });
    }

    return res.json({
      authenticated: true,
      user,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal memuat profil' });
  }
});

export default router;
