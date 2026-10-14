import { PrismaClient, Role, StatusPengajuan } from '@prisma/client';
import bcrypt from 'bcryptjs';

const prisma = new PrismaClient();

async function main() {
  console.log('--- Mulai Seeding Database Backend ---');

  await prisma.logAktivitas.deleteMany();
  await prisma.pengajuanSurat.deleteMany();
  await prisma.jenisSurat.deleteMany();
  await prisma.user.deleteMany();

  const salt = await bcrypt.genSalt(10);
  const adminPassword = await bcrypt.hash('admin123', salt);
  const petugasPassword = await bcrypt.hash('petugas123', salt);
  const siswaPassword = await bcrypt.hash('siswa123', salt);

  const admin = await prisma.user.create({
    data: {
      username: 'admin',
      nama: 'Drs. H. Mulyadi, M.Pd.',
      email: 'admin.tu@sekolah.sch.id',
      password: adminPassword,
      role: Role.ADMIN,
      noTelepon: '081234567890',
    },
  });

  const petugas = await prisma.user.create({
    data: {
      username: 'petugas',
      nama: 'Rina Kartika, S.AP.',
      email: 'rina.tu@sekolah.sch.id',
      password: petugasPassword,
      role: Role.PETUGAS,
      noTelepon: '081298765432',
    },
  });

  const siswa1 = await prisma.user.create({
    data: {
      nisn: '0061234567',
      nama: 'Ahmad Fauzi Pratama',
      email: 'ahmad.fauzi@siswa.sch.id',
      password: siswaPassword,
      role: Role.SISWA,
      kelas: 'XII RPL 1',
      jurusan: 'Rekayasa Perangkat Lunak',
      noTelepon: '085711223344',
      alamat: 'Jl. Merak No. 12, Kelurahan Cibadak',
    },
  });

  const siswa2 = await prisma.user.create({
    data: {
      nisn: '0067654321',
      nama: 'Siti Nurhaliza Putri',
      email: 'siti.nurhaliza@siswa.sch.id',
      password: siswaPassword,
      role: Role.SISWA,
      kelas: 'XII RPL 2',
      jurusan: 'Rekayasa Perangkat Lunak',
      noTelepon: '085722334455',
      alamat: 'Komp. Graha Indah Blok B3, Sukamaju',
    },
  });

  const siswa3 = await prisma.user.create({
    data: {
      nisn: '0071122334',
      nama: 'Budi Santoso',
      email: 'budi.santoso@siswa.sch.id',
      password: siswaPassword,
      role: Role.SISWA,
      kelas: 'XI TKJ 1',
      jurusan: 'Teknik Komputer & Jaringan',
      noTelepon: '085733445566',
      alamat: 'Jl. Melati No. 45, Karanganyar',
    },
  });

  const suratAktif = await prisma.jenisSurat.create({
    data: {
      kodeSurat: 'SK-AKTIF',
      namaSurat: 'Surat Keterangan Siswa Aktif',
      deskripsi: 'Surat yang menerangkan bahwa siswa masih berstatus aktif belajar di sekolah untuk keperluan BPJS, tunjangan orang tua, dll.',
      persyaratan: '1. Fotokopi Kartu Tanda Pelajar (KTPel)\n2. Tidak memiliki tanggungan administrasi',
      formatNomor: '421.3/{NOMOR}/SMKN1/SK-AKTIF/{BULAN_ROMAWI}/{TAHUN}',
      templateIsi: 'Menerangkan bahwa nama tersebut di atas adalah benar siswa aktif yang terdaftar di sekolah ini pada Tahun Ajaran 2026/2027.',
      isActive: true,
    },
  });

  const suratDispensasi = await prisma.jenisSurat.create({
    data: {
      kodeSurat: 'SI-DISPEN',
      namaSurat: 'Surat Izin / Dispensasi Kegiatan',
      deskripsi: 'Surat izin meninggalkan kegiatan belajar mengajar karena mengikuti perlombaan, kegiatan organisasi resmi, atau urusan penting.',
      persyaratan: '1. Surat Undangan / Keterangan dari instansi penyelenggara kegiatan\n2. Tanda tangan rekomendasi pembina ekstrakurikuler/wali kelas',
      formatNomor: '421.3/{NOMOR}/SMKN1/DISPEN/{BULAN_ROMAWI}/{TAHUN}',
      templateIsi: 'Memberikan dispensasi kepada siswa yang bersangkutan untuk mengikuti agenda kegiatan resmi di luar sekolah.',
      isActive: true,
    },
  });

  const suratBeasiswa = await prisma.jenisSurat.create({
    data: {
      kodeSurat: 'SR-BEASISWA',
      namaSurat: 'Surat Rekomendasi Beasiswa',
      deskripsi: 'Surat rekomendasi dari pihak sekolah untuk pengajuan beasiswa prestasi atau bantuan pendidikan dari pemerintah/swasta.',
      persyaratan: '1. Fotokopi Rapor semester terakhir\n2. Surat permohonan tertulis ditujukan kepada Kepala Sekolah',
      formatNomor: '421.3/{NOMOR}/SMKN1/REK-BEASISWA/{BULAN_ROMAWI}/{TAHUN}',
      templateIsi: 'Memberikan rekomendasi penuh kepada siswa tersebut atas dedikasi dan prestasi akademik/non-akademik yang diraih.',
      isActive: true,
    },
  });

  const suratKelakuan = await prisma.jenisSurat.create({
    data: {
      kodeSurat: 'SK-KELAKUAN',
      namaSurat: 'Surat Keterangan Berkelakuan Baik',
      deskripsi: 'Surat keterangan dari pihak bimbingan konseling dan kesiswaan bahwa siswa berkelakuan baik dan tidak pernah melanggar tata tertib.',
      persyaratan: '1. Bebas dari catatan pelanggaran kesiswaan (poin pelanggaran 0)\n2. Rekomendasi Guru BK',
      formatNomor: '421.3/{NOMOR}/SMKN1/SKBB/{BULAN_ROMAWI}/{TAHUN}',
      templateIsi: 'Menerangkan bahwa selama menjadi siswa sekolah ini senantiasa berkelakuan baik, rajin, dan tertib.',
      isActive: true,
    },
  });

  const suratPKL = await prisma.jenisSurat.create({
    data: {
      kodeSurat: 'SP-PKL',
      namaSurat: 'Surat Pengantar Praktik Kerja Lapangan (PKL)',
      deskripsi: 'Surat pengantar resmi kepada Dunia Usaha / Dunia Industri (DU/DI) tempat siswa melaksanakan magang/PKL.',
      persyaratan: '1. Telah mengisi form konfirmasi penerimaan dari DU/DI\n2. Surat pernyataan izin orang tua/wali',
      formatNomor: '421.3/{NOMOR}/SMKN1/PENGANTAR-PKL/{BULAN_ROMAWI}/{TAHUN}',
      templateIsi: 'Memohon kesediaan pimpinan perusahaan untuk menerima siswa bersangkutan dalam program PKL/Magang industri.',
      isActive: true,
    },
  });

  const req1 = await prisma.pengajuanSurat.create({
    data: {
      nomorPengajuan: 'REQ-202609-0001',
      siswaId: siswa1.id,
      jenisSuratId: suratAktif.id,
      keperluan: 'Pengurusan perpanjangan tunjangan gaji orang tua (PNS) di Dinas Pendidikan.',
      keterangan: 'Mohon dibantu segera karena batas akhir pengumpulan akhir pekan ini.',
      status: StatusPengajuan.DISETUJUI,
      nomorSuratResmi: '421.3/088/SMKN1/SK-AKTIF/IX/2026',
      petugasId: petugas.id,
      catatanPetugas: 'Surat telah diverifikasi dan ditandatangani secara resmi. Silakan cetak mandiri atau ambil cap basah di ruang TU.',
      tanggalPengajuan: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000),
      tanggalSelesai: new Date(),
    },
  });

  await prisma.logAktivitas.create({
    data: {
      pengajuanId: req1.id,
      userId: siswa1.id,
      statusSesudah: StatusPengajuan.MENUNGGU,
      catatan: 'Pengajuan surat dibuat oleh siswa',
    },
  });

  await prisma.logAktivitas.create({
    data: {
      pengajuanId: req1.id,
      userId: petugas.id,
      statusSebelum: StatusPengajuan.MENUNGGU,
      statusSesudah: StatusPengajuan.DISETUJUI,
      catatan: 'Disetujui dan diterbitkan Nomor Surat 421.3/088/SMKN1/SK-AKTIF/IX/2026',
    },
  });

  const req2 = await prisma.pengajuanSurat.create({
    data: {
      nomorPengajuan: 'REQ-202609-0002',
      siswaId: siswa2.id,
      jenisSuratId: suratBeasiswa.id,
      keperluan: 'Pendaftaran Beasiswa Prestasi Talenta Muda Nasional Kemendikbud.',
      keterangan: 'Lampiran piagam juara LKS RPL tingkat kota sudah disertakan.',
      status: StatusPengajuan.DIPROSES,
      petugasId: admin.id,
      catatanPetugas: 'Sedang diverifikasi oleh Kepala Sekolah untuk penandatanganan.',
      tanggalPengajuan: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000),
    },
  });

  await prisma.logAktivitas.create({
    data: {
      pengajuanId: req2.id,
      userId: siswa2.id,
      statusSesudah: StatusPengajuan.MENUNGGU,
      catatan: 'Pengajuan surat dibuat oleh siswa',
    },
  });

  const req3 = await prisma.pengajuanSurat.create({
    data: {
      nomorPengajuan: 'REQ-202609-0003',
      siswaId: siswa3.id,
      jenisSuratId: suratDispensasi.id,
      keperluan: 'Mengikuti seleksi turnamen Futsal Piala Pelajar tingkat Provinsi.',
      keterangan: 'Pelaksanaan selama 2 hari, tanggal 16-17 September 2026.',
      status: StatusPengajuan.MENUNGGU,
      tanggalPengajuan: new Date(),
    },
  });

  await prisma.logAktivitas.create({
    data: {
      pengajuanId: req3.id,
      userId: siswa3.id,
      statusSesudah: StatusPengajuan.MENUNGGU,
      catatan: 'Pengajuan surat baru masuk',
    },
  });

  console.log('--- Seeding Backend Selesai Sukses! ---');
}

main()
  .catch((e) => {
    console.error('Error saat seeding:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
