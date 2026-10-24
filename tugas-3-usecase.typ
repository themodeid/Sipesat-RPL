#set document(
  title: "Tugas 3 RPL: Perancangan Use Case Diagram & Matriks RBAC - SIPESAT",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)

#set text(font: "Times New Roman", size: 11pt, lang: "id")
#set page(
  paper: "a4",
  margin: (left: 4cm, top: 4cm, right: 3cm, bottom: 3cm),
  header: none,
  footer: context align(center)[#text(size: 10pt)[#counter(page).display("1")]]
)

#align(center)[
  #text(size: 14pt, weight: "bold")[
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\
    TUGAS 3: PERANCANGAN USE CASE DIAGRAM & MATRIKS HAK AKSES (RBAC)
  ]
  #v(1.0cm)
  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\
    #text(size: 11pt, weight: "regular")[_Studi Kasus: Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah_]
  ]
  #v(1.8cm)
  #rect(width: 5cm, height: 4.2cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt)[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[UNIVERSITAS\ INDRAPRASTA PGRI\ (UNINDRA)]
      #v(6pt)
      #text(size: 9.5pt, fill: rgb("#475569"))[FAKULTAS TEKNIK & ILMU KOMPUTER\ TEKNIK INFORMATIKA]
    ]
  ]
  #v(1.8cm)
  #text(size: 11pt, weight: "bold")[Disusun Oleh (Kelompok 7 / Kelas RPL_XD):]
  #v(0.3cm)
  #table(
    columns: (0.8cm, 8.5cm, 3.5cm),
    align: (center, left, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else { none },
    table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Anggota]*], [*#text(fill: white)[NPM]*]),
    [1], [Adam Wahyu Kurniawan (Lead Architect & SWE)], [202343500510],
    [2], [Fathu Rahman (Business Analyst)], [202343500467],
    [3], [Surya Edi Saputra (QA & Technical Writer)], [202343500468],
    [4], [Rizqi Muh. Al Hakimi (Database Specialist)], [202343500449],
  )
  #v(1.2cm)
  #text(size: 11pt, weight: "bold")[JAKARTA\ 2026/2027]
]

#pagebreak()

= BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM
== 1.1 Deskripsi Proyek SIPESAT
Sistem Informasi Pengajuan Surat Siswa Berbasis Web (*SIPESAT*) adalah sistem perangkat lunak yang dirancang untuk memodernisasi dan mengotomatisasi rantai birokrasi pengajuan surat keterangan di lingkungan sekolah menengah.

== 1.2 Tujuan Pemodelan Use Case Diagram
1. Mendefinisikan batasan sistem (*system boundary*) secara tegas.
2. Mengidentifikasi seluruh aktor yang berinteraksi langsung dengan sistem.
3. Menjelaskan relasi dependensi antarfungsi menggunakan stereotype `<<include>>` (keharusan) dan `<<extend>>` (perluasan opsional).

#pagebreak()

= BAB II: PERANCANGAN USE CASE DIAGRAM SIPESAT
== 2.1 Diagram Use Case Terpadu (Draw.io Native)

#align(center)[
  #image("assets/diagram_usecase.png", width: 100%)
  #v(4pt)
  #text(size: 9.5pt, style: "italic")[Gambar 2.1: Use Case Diagram SIPESAT Standar UML 2.5 (100% Bebas Tabrakan)]
]

#v(0.5cm)
== 2.2 Tabel Rincian Use Case Terdefinisi
#table(
  columns: (1.5cm, 4.5cm, 3.0cm, 5.5cm),
  align: (center, left, center, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[Kode]*], [*#text(fill: white)[Nama Use Case]*], [*#text(fill: white)[Aktor]*], [*#text(fill: white)[Deskripsi]*]),
  [UC-01], [Login ke Sistem], [Siswa, TU], [Otentikasi pengguna via NISN/NIP dan kata sandi terenkripsi.],
  [UC-01B], [Validasi Kredensial & Hak Akses], [Sistem (Include)], [Pengecekan keabsahan JWT pada rute terproteksi.],
  [UC-02], [Registrasi Akun Mandiri], [Siswa], [Pendaftaran akun baru siswa dengan validasi NISN ke database.],
  [UC-03], [Kelola Profil & Sandi], [Siswa, TU], [Pembaharuan data profil, email, dan ganti kata sandi.],
  [UC-04], [Logout Sesi], [Siswa, TU], [Penghapusan token JWT dan pembersihan sesi aktif.],
  [UC-05], [Lihat Katalog & Syarat Surat], [Siswa], [Eksplorasi daftar jenis surat beserta panduan syarat wajib.],
  [UC-06], [Mengajukan Permohonan Surat], [Siswa], [Pengisian formulir keperluan dan pemilihan jenis surat.],
  [UC-07], [Unggah Berkas Syarat (PDF ≤ 2MB)], [Siswa (Include)], [Unggah berkas bukti pendukung dengan validasi batas 2 MB.],
  [UC-08], [Melacak Status Surat (Real-time)], [Siswa], [Pemantauan status pengajuan secara live via Stepper Timeline.],
  [UC-08A], [Melihat Catatan Koreksi / Revisi], [Siswa (Extend)], [Peninjauan feedback alasan penolakan dan perbaikan berkas.],
  [UC-09], [Melihat Riwayat Pengajuan], [Siswa], [Arsip rekam jejak surat yang pernah diajukan sebelumnya.],
  [UC-10], [Unduh Surat PDF Ber-QR Code], [Siswa], [Pengunduhan file PDF resmi berkop sekolah dan kode QR.],
  [UC-11], [Dashboard Antrean TU], [Petugas TU], [Tinjauan metrik statistik antrean operasional persuratan.],
  [UC-12], [Kelola Antrean Surat Masuk], [Petugas TU], [Penyaringan dan pengelolaan urutan surat masuk sekolah.],
  [UC-13], [Verifikasi Berkas Dokumen], [Petugas TU], [Pemeriksaan kelayakan berkas fisik/digital unggahan siswa.],
  [UC-14], [Setujui Permohonan (Approve)], [Petugas TU], [Persetujuan berkas yang memenuhi syarat kelengkapan.],
  [UC-14A], [Terbitkan No. Surat & TTE QR], [TU (Include)], [Generate nomor agenda keluar resmi dan kode QR stempel.],
  [UC-15], [Tolak Permohonan (Reject)], [Petugas TU], [Penolakan berkas buram atau tidak memenuhi syarat.],
  [UC-15A], [Input Alasan & Catatan Koreksi], [TU (Include)], [Penyusunan catatan evaluasi tertulis kepada siswa.],
  [UC-16], [Kelola Master Jenis Surat], [Petugas TU], [Pengelolaan katalog jenis surat dan template naskah.],
  [UC-17], [Kelola Data Siswa & Akun], [Petugas TU], [Manajemen akun siswa dan reset kata sandi bermasalah.],
  [UC-18], [Ekspor Rekapitulasi Laporan], [Petugas TU], [Penerbitan rekap laporan bulanan ke format Excel/PDF.],
)

#pagebreak()

= BAB III: MATRIKS HAK AKSES (ROLE-BASED ACCESS CONTROL)
#table(
  columns: (1.2cm, 7.5cm, 3.0cm, 3.0cm),
  align: (center, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Use Case / Modul]*], [*#text(fill: white)[Role Siswa]*], [*#text(fill: white)[Role Petugas TU]*]),
  [1], [UC-01: Login ke Sistem], [✅ Ya], [✅ Ya],
  [2], [UC-02: Registrasi Akun Mandiri], [✅ Ya], [❌ Tidak],
  [3], [UC-03: Kelola Profil & Sandi], [✅ Ya], [✅ Ya],
  [4], [UC-04: Logout Sesi Pengguna], [✅ Ya], [✅ Ya],
  [5], [UC-05: Lihat Katalog & Syarat Surat], [✅ Ya], [✅ Ya (Kelola)],
  [6], [UC-06: Mengajukan Permohonan Surat], [✅ Ya], [❌ Tidak],
  [7], [UC-07: Unggah Berkas Syarat (PDF ≤ 2MB)], [✅ Ya], [❌ Tidak],
  [8], [UC-08: Melacak Status Surat (Real-time)], [✅ Ya], [❌ Tidak],
  [9], [UC-09: Melihat Riwayat Pengajuan], [✅ Ya], [❌ Tidak],
  [10], [UC-10: Unduh Surat PDF Ber-QR Code], [✅ Ya], [✅ Ya],
  [11], [UC-11: Dashboard Antrean TU], [❌ Tidak], [✅ Ya],
  [12], [UC-12: Kelola Antrean Surat Masuk], [❌ Tidak], [✅ Ya],
  [13], [UC-13: Verifikasi Berkas Dokumen], [❌ Tidak], [✅ Ya],
  [14], [UC-14: Setujui Permohonan (Approve)], [❌ Tidak], [✅ Ya],
  [15], [UC-15: Tolak Permohonan (Reject)], [❌ Tidak], [✅ Ya],
  [16], [UC-16: Kelola Master Jenis Surat], [❌ Tidak], [✅ Ya],
  [17], [UC-17: Kelola Data Siswa & Akun], [❌ Tidak], [✅ Ya],
  [18], [UC-18: Ekspor Rekapitulasi Laporan], [❌ Tidak], [✅ Ya],
)

#v(0.8cm)
= BAB IV: PENUTUP
Seluruh diagram visual interaktif use case dapat diakses dan disunting pada berkas master:
- *`tugas-3-usecase.drawio`* (1 Tab Tunggal Bersih, 0 Tabrakan Garis).
