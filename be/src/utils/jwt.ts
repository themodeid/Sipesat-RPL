import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.JWT_SECRET || 'rahasia-kunci-surat-siswa-2026-sekolah-aman';

export interface TokenPayload {
  id: string;
  nama: string;
  role: 'ADMIN' | 'PETUGAS' | 'SISWA';
  username?: string | null;
  nisn?: string | null;
  email?: string | null;
  kelas?: string | null;
  jurusan?: string | null;
}

export function signToken(payload: TokenPayload): string {
  return jwt.sign(payload, JWT_SECRET, { expiresIn: '7d' });
}

export function verifyToken(token: string): TokenPayload | null {
  try {
    return jwt.verify(token, JWT_SECRET) as TokenPayload;
  } catch (err) {
    return null;
  }
}
