export type Role = 'ADMIN' | 'PETUGAS' | 'SISWA';
export type StatusPengajuan = 'MENUNGGU' | 'DIPROSES' | 'DISETUJUI' | 'DITOLAK';

export interface UserSession {
  id: string;
  nama: string;
  role: Role;
  username?: string | null;
  nisn?: string | null;
  email?: string | null;
  kelas?: string | null;
  jurusan?: string | null;
  noTelepon?: string | null;
}

export interface JenisSuratItem {
  id: string;
  kodeSurat: string;
  namaSurat: string;
  deskripsi: string;
  persyaratan?: string | null;
  formatNomor: string;
  templateIsi?: string | null;
  isActive: boolean;
  createdAt: string | Date;
  _count?: {
    pengajuan: number;
  };
}

export interface PengajuanItem {
  id: string;
  nomorPengajuan: string;
  siswaId: string;
  siswa: {
    id: string;
    nama: string;
    nisn?: string | null;
    kelas?: string | null;
    jurusan?: string | null;
    noTelepon?: string | null;
  };
  jenisSuratId: string;
  jenisSurat: {
    id: string;
    kodeSurat: string;
    namaSurat: string;
    formatNomor: string;
    templateIsi?: string | null;
  };
  keperluan: string;
  keterangan?: string | null;
  lampiran?: string | null;
  status: StatusPengajuan;
  nomorSuratResmi?: string | null;
  petugasId?: string | null;
  petugas?: {
    id: string;
    nama: string;
    username?: string | null;
  } | null;
  catatanPetugas?: string | null;
  tanggalPengajuan: string | Date;
  tanggalSelesai?: string | Date | null;
  updatedAt: string | Date;
  logs?: Array<{
    id: string;
    statusSebelum?: StatusPengajuan | null;
    statusSesudah: StatusPengajuan;
    catatan?: string | null;
    createdAt: string | Date;
    user?: {
      nama: string;
      role: Role;
    } | null;
  }>;
}
