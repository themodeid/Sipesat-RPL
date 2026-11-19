#set document(
  title: "Tugas 11 RPL: Pengujian Perangkat Lunak (Black Box Testing) - SIPESAT",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)

#set text(font: "Times New Roman", size: 10.5pt, lang: "id")
#set page(
  paper: "a4",
  margin: (left: 3.5cm, top: 3.5cm, right: 3cm, bottom: 3cm),
  header: none,
  footer: context align(center)[#text(size: 9.5pt)[#counter(page).display("1")]]
)

#set par(justify: true, leading: 0.72em, first-line-indent: 0pt)
#set heading(numbering: none)
#show heading.where(level: 1): it => block(above: 1.4em, below: 0.7em)[
  #text(size: 12.5pt, weight: "bold")[#it.body]
]
#show heading.where(level: 2): it => block(above: 1.1em, below: 0.5em)[
  #text(size: 11pt, weight: "bold")[#it.body]
]

#align(center)[
  #v(0.3cm)
  #text(size: 13.5pt, weight: "bold")[
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\
    TUGAS 11: PENGUJIAN PERANGKAT LUNAK (BLACK BOX TESTING)
  ]
  #v(0.5cm)
  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB\
    (SIPESAT)
  ]
  #v(0.2cm)
  #text(size: 10.5pt, style: "italic")[
    Pengujian Fungsionalitas Kotak Hitam (Black Box) Berbasis Skenario Nyata (Versi Revisi)
  ]
  #v(0.8cm)
  #image("assets/logo_unindra.png", width: 4.2cm)
  #v(0.2cm)
  #text(size: 13pt, weight: "bold")[
    UNIVERSITAS INDRAPRASTA PGRI\
    (UNINDRA)
  ]
  #v(0.8cm)
  #text(size: 11pt, weight: "bold")[Disusun Oleh (Kelompok 7 / Kelas RPL_XD):]
  #v(0.2cm)
  #table(
    columns: (1cm, 1fr, 3.5cm),
    align: (center + horizon, left + horizon, center + horizon),
    inset: 7pt,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else { none },
    table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Anggota]*], [*#text(fill: white)[NPM]*]),
    [1], [Adam Wahyu Kurniawan (Lead Architect & SWE)], [202343500510],
    [2], [Fathu Rahman (Business Analyst)], [202343500467],
    [3], [Surya Edi Saputra (QA & Technical Writer)], [202343500468],
    [4], [Rizqi Muh. Al Hakimi (Database Specialist & UI/UX)], [202343500449],
  )
  #v(0.9cm)
  #text(size: 11pt, weight: "bold")[
    FAKULTAS TEKNIK & ILMU KOMPUTER\
    PROGRAM STUDI TEKNIK INFORMATIKA\
    JAKARTA 2026/2027
  ]
]

#pagebreak()

= BAB I: PENDAHULUAN & METODOLOGI PENGUJIAN

== 1.1 Latar Belakang & Posisi Pengujian dalam SDLC
Pengujian Perangkat Lunak (_Software Testing_) merupakan tahap verifikasi dan validasi kritis dalam siklus hidup rekayasa perangkat lunak (_Software Development Life Cycle_ - SDLC). Tahap ini bertujuan menjamin bahwa sistem yang telah dibangun pada tahap Konstruksi (Tugas 10) benar-benar beroperasi sesuai dengan spesifikasi kebutuhan fungsional yang tertuang dalam dokumen SRS (Tugas 2) serta mematuhi alur bisnis pada diagram UML (Tugas 3 s.d. 7).

Pada sistem *SIPESAT (Sistem Informasi Pengajuan Surat Siswa Berbasis Web)*, pengujian difokuskan untuk memastikan bahwa alur birokrasi persuratan—mulai dari permohonan surat oleh siswa, validasi kelayakan dokumen, verifikasi dan keputusan oleh Petugas Tata Usaha (TU), hingga penomoran otomatis dan penerbitan dokumen digital PDF ber-QR Code—berjalan secara presisi, deterministik, dan kebal dari celah validasi (_input boundary errors_) maupun kebocoran otorisasi (_unauthorized privilege escalation_).

== 1.2 Metodologi Black Box Testing
Metodologi pengujian yang digunakan adalah *Black Box Testing (Pengujian Kotak Hitam)*. Pendekatan ini berfokus pada fungsionalitas eksternal perangkat lunak tanpa memeriksa struktur kode internal secara langsung. Teknik yang diterapkan mencakup:
+ *Equivalence Partitioning (EP)*: Membagi rentang masukan data menjadi partisi valid dan tidak valid untuk menguji respons sistem terhadap masukan yang sah dan masukan yang menyimpang.
+ *Boundary Value Analysis (BVA)*: Menguji nilai batas ekstrem pada form input (misalnya ukuran berkas unggahan maksimal 2 MB dan kelengkapan kolom wajib).
+ *Role-Based Access Control (RBAC) Testing*: Memastikan pemisahan ketat hak akses antara dua peran utama: Siswa dan Petugas TU.

== 1.3 Lingkungan Pengujian (Testing Environment)
- *Perangkat Keras (Hardware)*: Processor Intel Core i5 / AMD Ryzen 5, RAM 16 GB DDR4, SSD NVMe 512 GB.
- *Sistem Operasi*: Windows 11 Pro 64-bit / Linux Ubuntu 22.04 LTS.
- *Peramban Web (Browser)*: Google Chrome Version 128+ & Microsoft Edge.
- *Database & Server*: PostgreSQL 16 (Docker Port 5432), Express Backend Server (Port 5000), Next.js 14 Frontend Server (Port 3000).
- *Akun Uji*: Siswa (`0061234567` / `siswa123`) dan Petugas TU (`admin` / `admin123`).

= BAB II: TABEL MATRIKS PENGUJIAN SISTEM SIPESAT (BLACK BOX TESTING)

Pengujian dilakukan mengadopsi format matriks resmi UNINDRA dengan kolom: *No*, *Skenario Pengujian*, *Test Case*, *Hasil yang Diharapkan*, *Hasil*, dan *Kesimpulan*:

#let bb_table(..rows) = {
  set par(justify: false, first-line-indent: 0pt, leading: 0.55em)
  set text(size: 9pt)
  table(
    columns: (0.8cm, 1.25fr, 1.05fr, 1.35fr, 1.55cm, 1.75cm),
    align: (center + top, left + top, left + top, left + top, center + top, center + top),
    inset: (x: 5pt, y: 5pt),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#f472b6") } else if calc.odd(row) { rgb("#fdf2f8") } else { none },
    table.header(
      [*No*],
      [*Skenario Pengujian*],
      [*Test Case*],
      [*Hasil yang Diharapkan*],
      [*Hasil*],
      [*Kesimpulan*],
    ),
    ..rows
  )
}

== 2.1 Modul 1: Autentikasi, Login, & Hak Akses Multi-Role
#bb_table(
  [1], [Username dan Password tidak diisi kemudian klik tombol Login], [Username: (kosong)\ Password: (kosong)], [Sistem menolak dan menampilkan pesan "Harap isi username dan password"], [Sesuai harapan], [*Valid*],
  [2], [Mengetikkan Username, dan password dikosongkan kemudian klik Login], [Username: `admin`\ Password: (kosong)], [Sistem menolak dan menampilkan pesan "Password belum diisi"], [Sesuai harapan], [*Valid*],
  [3], [Mengetikkan Password, dan username dikosongkan kemudian klik Login], [Username: (kosong)\ Password: `admin123`], [Sistem menolak dan menampilkan pesan "Username belum diisi"], [Sesuai harapan], [*Valid*],
  [4], [Mengetikkan Username atau password salah kemudian klik tombol Login], [Username: `adm`\ Password: `adm123`], [Sistem menolak dengan pesan generik "Username atau Password yang Anda masukkan salah"], [Sesuai harapan], [*Valid*],
  [5], [Mengetikkan Username dan password benar akun Petugas TU lalu klik Login], [Username: `admin`\ Password: `admin123`], [Sistem menerima akses login dan mengarahkan ke dashboard Petugas TU (`/admin/dashboard`)], [Sesuai harapan], [*Valid*],
  [6], [Mengetikkan NISN dan password benar akun Siswa lalu klik Login], [NISN: `0061234567`\ Password: `siswa123`], [Sistem menerima akses login dan mengarahkan ke portal siswa (`/siswa/pengajuan`)], [Sesuai harapan], [*Valid*],
  [7], [Mengklik tombol Logout dari sesi pengguna aktif], [Sesi: Siswa / TU aktif\ Aksi: Klik Logout], [Sistem menghapus sesi token JWT dan mengalihkan halaman ke `/login`], [Sesuai harapan], [*Valid*],
)

== 2.2 Modul 2: Formulir Pengajuan Surat Mandiri Siswa
#bb_table(
  [8], [Mengirim formulir pengajuan tanpa memilih jenis surat], [Jenis: (Belum dipilih)\ Keperluan: Beasiswa\ File: `berkas.pdf`], [Sistem menolak submit dan menampilkan peringatan "Pilih jenis surat yang diajukan"], [Sesuai harapan], [*Valid*],
  [9], [Mengisi formulir dengan kolom keperluan kosong], [Jenis: SK Siswa Aktif\ Keperluan: (kosong)\ File: `berkas.pdf`], [Sistem menolak submit dan menampilkan peringatan "Keperluan pengajuan wajib diisi"], [Sesuai harapan], [*Valid*],
  [10], [Mengunggah berkas persyaratan dengan ukuran melebihi batas (> 2 MB)], [File: `scan_rapor.pdf`\ Ukuran: 4,5 MB], [Sistem menolak file dan menampilkan notifikasi "Ukuran file maksimal 2 MB"], [Sesuai harapan], [*Valid*],
  [11], [Mengunggah berkas persyaratan dengan format terlarang (.exe, .php)], [File: `script.exe`\ Ukuran: 300 KB], [Sistem memblokir berkas dengan pesan "Format tidak diizinkan (Hanya PDF, JPG, PNG)"], [Sesuai harapan], [*Valid*],
  [12], [Mengisi formulir lengkap dengan berkas valid (≤ 2 MB)], [Jenis: SK Siswa Aktif\ Keperluan: Beasiswa\ File: `kartu.pdf` (800 KB)], [Sistem menyimpan pengajuan, menerbitkan nomor resi, dan menyetel status "Menunggu Verifikasi"], [Sesuai harapan], [*Valid*],
)

== 2.3 Modul 3: Pelacakan Status Surat (Tracking & Timeline Stepper)
#bb_table(
  [13], [Mengecek status permohonan dengan nomor tiket kosong], [Nomor Resi: (kosong)\ Aksi: Klik Lacak], [Sistem menampilkan pesan "Harap masukkan nomor registrasi pengajuan surat"], [Sesuai harapan], [*Valid*],
  [14], [Melacak status dengan nomor registrasi yang tidak terdaftar], [Nomor:\ `REQ-9999-XXXX`\ (Fiktif)], [Sistem menampilkan notifikasi "Nomor registrasi tidak ditemukan"], [Sesuai harapan], [*Valid*],
  [15], [Melacak surat valid yang berstatus "Menunggu Verifikasi"], [Nomor:\ `REQ-202609-0003`\ Status: Menunggu], [Sistem menampilkan data pemohon dan stepper aktif pada tahap "Menunggu Verifikasi TU"], [Sesuai harapan], [*Valid*],
  [16], [Melacak surat yang berstatus "Ditolak" beserta catatan revisi], [Nomor:\ `REQ-202609-0002`\ Status: Ditolak], [Sistem menampilkan lencana merah "Pengajuan Ditolak" beserta alasan catatan koreksi TU], [Sesuai harapan], [*Valid*],
  [17], [Melacak surat yang berstatus "Disetujui / Selesai"], [Nomor:\ `REQ-202609-0001`\ Status: Disetujui], [Sistem menampilkan stepper hijau selesai dan tombol "Unduh Surat PDF Resmi"], [Sesuai harapan], [*Valid*],
)

== 2.4 Modul 4: Verifikasi & Keputusan oleh Petugas TU
#bb_table(
  [18], [Petugas TU membuka antrean permohonan surat masuk], [Akun: Petugas TU\ Menu: Antrean Masuk], [Sistem memuat daftar permohonan masuk secara urut FIFO dengan status dan tanggal], [Sesuai harapan], [*Valid*],
  [19], [Petugas TU melakukan pratinjau berkas persyaratan siswa], [Aksi: Klik tombol "Lihat Berkas" pada baris siswa], [Sistem membuka pratinjau berkas lampiran PDF/gambar secara aman dan mengubah status ke Diproses], [Sesuai harapan], [*Valid*],
  [20], [Petugas TU menolak permohonan tanpa mengisi catatan alasan], [Aksi: Klik Tolak\ Catatan: (kosong)], [Sistem memblokir aksi penolakan dengan pesan "Alasan penolakan wajib diisi"], [Sesuai harapan], [*Valid*],
  [21], [Petugas TU menolak permohonan dengan mengisi catatan koreksi], [Aksi: Klik Tolak\ Catatan: "Scan KK buram"], [Sistem memperbarui status menjadi "Ditolak", menyimpan log audit, dan menampilkan catatan ke siswa], [Sesuai harapan], [*Valid*],
  [22], [Petugas TU menyetujui permohonan surat yang memenuhi syarat], [Aksi: Klik "Setujui & Terbitkan Surat"], [Sistem memperbarui status menjadi "Disetujui", menerbitkan nomor surat resmi & QR, siap unduh/cetak], [Sesuai harapan], [*Valid*],
)

== 2.5 Modul 5: Penomoran Otomatis & Cetak Surat Digital PDF ber-QR Code
#bb_table(
  [23], [Pengujian otomasi penomoran surat resmi sekolah], [Trigger: Surat disetujui bulan Nov 2026 urutan ke-5], [Sistem menghasilkan nomor surat resmi unik: `421.3/005/SMKN1/XI/2026` secara otomatis], [Sesuai harapan], [*Valid*],
  [24], [Pengujian konversi bulan kalender ke angka romawi], [Bulan: November\ (Bulan ke-11)], [Sistem mengonversi bulan 11 menjadi angka romawi "XI" secara presisi], [Sesuai harapan], [*Valid*],
  [25], [Pengujian pembuatan QR Code tanda tangan digital], [Input: ID Pengajuan\ `REQ-202609-0001`], [Sistem menghasilkan QR Code dinamis yang memuat URL verifikasi keaslian dokumen], [Sesuai harapan], [*Valid*],
  [26], [Pengunduhan dokumen PDF surat resmi oleh siswa], [Aksi: Klik tombol "Unduh PDF"], [Sistem mengunduh berkas PDF A4 resmi lengkap dengan kop sekolah, nomor surat, isi, dan QR Code], [Sesuai harapan], [*Valid*],
  [27], [Pemindaian QR Code pada surat PDF menggunakan kamera ponsel], [Aksi: Scan QR Code pada lembar surat], [Peramban menampilkan halaman verifikasi publik SIPESAT: "Dokumen Asli Terverifikasi"], [Sesuai harapan], [*Valid*],
)

== 2.6 Modul 6: Manajemen Data Master Persuratan & Rekapitulasi Laporan
#bb_table(
  [28], [Petugas TU menambahkan jenis layanan surat baru], [Nama: Surat Izin Observasi\ Kode: `SI-OBS`], [Sistem menyimpan jenis surat baru ke basis data dan langsung tampil aktif di katalog siswa], [Sesuai harapan], [*Valid*],
  [29], [Petugas TU menonaktifkan jenis surat lama (Soft Delete)], [Aksi: Ubah status jenis surat menjadi "Nonaktif"], [Jenis surat nonaktif tidak tampil di katalog siswa, namun riwayat pengajuan lama tetap utuh], [Sesuai harapan], [*Valid*],
  [30], [Penyaringan laporan persuratan berdasarkan rentang tanggal], [Filter: 01 Nov 2026 s.d. 30 Nov 2026], [Sistem menyaring tabel rekapitulasi dan hanya menampilkan permohonan pada periode terpilih], [Sesuai harapan], [*Valid*],
  [31], [Ekspor laporan rekapitulasi persuratan ke berkas unduhan], [Aksi: Klik tombol "Ekspor Laporan (CSV/Excel)"], [Sistem menghasilkan berkas laporan rekapitulasi berisi data pemohon, jenis surat, nomor, dan status], [Sesuai harapan], [*Valid*],
)

== 2.7 Modul 7: Pengujian Keamanan & Hak Akses (Route Guard & Security)
#bb_table(
  [32], [Siswa mencoba mengakses paksa halaman admin lewat URL], [Role: Siswa\ Aksi: Buka `/admin/dashboard`], [Sistem memblokir akses (`HTTP 403 Forbidden`) dan mengalihkan siswa ke dashboard siswa], [Sesuai harapan], [*Valid*],
  [33], [Akses endpoint API private tanpa menyertakan token JWT], [Request: `GET /api/pengajuan`\ Header: Tanpa Token], [Backend menolak request dengan status `HTTP 401 Unauthorized` ("Token tidak ditemukan")], [Sesuai harapan], [*Valid*],
  [34], [Siswa mencoba mengunduh surat milik siswa lain via ganti ID (IDOR)], [Akun: Siswa A\ Aksi: Akses ID surat milik Siswa B], [Sistem memeriksa kepemilikan data dan menolak akses dengan status `HTTP 403 Forbidden`], [Sesuai harapan], [*Valid*],
  [35], [Uji serangan Cross-Site Scripting (XSS) pada form keperluan/alasan], [Input payload:\ `<script>alert(1)</script>`], [Sistem mensterilkan tag HTML/JS sehingga tersimpan aman sebagai teks biasa tanpa dieksekusi], [Sesuai harapan], [*Valid*],
)

= BAB III: ANALISIS HASIL PENGUJIAN & METRIK KUALITAS

== 3.1 Rekapitulasi Metrik Pengujian
Berdasarkan eksekusi 35 skenario pengujian fungsionalitas kotak hitam (_Black Box Testing_) pada sistem SIPESAT, diperoleh rekapitulasi metrik pengujian sebagai berikut:

#{
  set par(justify: false, first-line-indent: 0pt)
  set text(size: 9.5pt)
  table(
    columns: (1fr, 1.8cm, 1.5cm, 1.5cm, 2.3cm),
    align: (left + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
    inset: 6pt,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else if row == 8 { rgb("#f1f5f9") } else if calc.even(row) { rgb("#f8fafc") } else { none },
    table.header(
      [*#text(fill: white)[Kategori Modul Pengujian]*],
      [*#text(fill: white)[Total Uji]*],
      [*#text(fill: white)[Pass]*],
      [*#text(fill: white)[Fail]*],
      [*#text(fill: white)[Persentase]*],
    ),
    [Modul 1: Autentikasi & Hak Akses Multi-Role], [7], [7], [0], [100%],
    [Modul 2: Formulir Pengajuan Surat Mandiri Siswa], [5], [5], [0], [100%],
    [Modul 3: Pelacakan Status Surat (Tracking Stepper)], [5], [5], [0], [100%],
    [Modul 4: Verifikasi & Keputusan Petugas TU], [5], [5], [0], [100%],
    [Modul 5: Penomoran Otomatis & Cetak PDF QR Code], [5], [5], [0], [100%],
    [Modul 6: Manajemen Data Master & Laporan], [4], [4], [0], [100%],
    [Modul 7: Keamanan & Hak Akses (Route Guard)], [4], [4], [0], [100%],
    [*TOTAL KESELURUHAN PENGUJIAN*], [*35*], [*35*], [*0*], [*100% (Valid)*],
  )
}

== 3.2 Analisis Kesiapan Sistem
+ *Validasi Batas Beroperasi Sempurna*: Seluruh penanganan kondisi input kosong, format berkas menyimpang, maupun batas ukuran berkas (> 2 MB) berhasil ditolak secara konsisten oleh sistem dengan pesan yang jelas.
+ *Integritas Penomoran & Tanda Tangan Digital*: Fungsi pembentukan nomor surat resmi (`generateNomorSuratResmi`) dan generator QR Code terbukti menghasilkan dokumen dinamis yang unik, tertelusur, dan bebas dari duplikasi nomor surat.
+ *Pemisahan Hak Akses Ketat (RBAC 2 Peran)*: Pengujian pada rute administratif (`/admin/*`) dan isolasi kepemilikan data antar-siswa membuktikan bahwa middleware autentikasi JWT berhasil melindungi data sekolah dari akses tanpa hak.

= BAB IV: KESIMPULAN & TAUTAN KODE SUMBER

== 4.1 Kesimpulan
Pengujian perangkat lunak sistem *SIPESAT (Sistem Informasi Pengajuan Surat Siswa Berbasis Web)* menggunakan metode _Black Box Testing_ telah diselesaikan secara tuntas. Dari 35 kasus pengujian yang mencakup seluruh modul operasional Siswa dan Petugas Tata Usaha:
- *Tingkat Keberhasilan Pengujian*: *100% Valid (35/35 Pass)*.
- *Kepadatan Cacat (_Defect Density_)*: *0 Critical Bugs*.
Sistem dinyatakan telah memenuhi seluruh spesifikasi kebutuhan perangkat lunak (SRS IEEE 830 / Karl Wiegers), aman dari kerentanan input dasar, serta berada dalam status *Siap Produksi (_Production Ready_)*.

== 4.2 Tautan Repositori GitHub Resmi
Seluruh kode program frontend, backend, skema database Prisma, dan berkas laporan tugas dapat diakses pada repositori GitHub resmi Kelompok 7:
- *URL Repositori GitHub*: #link("https://github.com/themodeid/Sipesat-RPL")[https://github.com/themodeid/Sipesat-RPL]
