import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'SIPESAT - Sistem Pengajuan Surat Siswa',
  description: 'Sistem Informasi Pelayanan Pengajuan Surat Administrasi Siswa Berbasis Web',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="id">
      <body className="antialiased min-h-screen bg-surface-light text-slate-800">
        {children}
      </body>
    </html>
  );
}
