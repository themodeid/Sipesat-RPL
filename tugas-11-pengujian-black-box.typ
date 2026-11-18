#set document(
  title: "Tugas 11 RPL: Pengujian Perangkat Lunak (Black Box Testing) - SIPESAT",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)

#set text(font: "Times New Roman", size: 10.5pt, lang: "id")
#set page(
  paper: "a4",
  margin: (left: 4cm, top: 4cm, right: 3cm, bottom: 3cm),
  header: none,
  footer: context align(center)[#text(size: 9.5pt)[#counter(page).display("1")]]
)

#set par(justify: true, leading: 0.75em, first-line-indent: 1cm)

#align(center)[
  #text(size: 13.5pt, weight: "bold")[
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\
    TUGAS 11: PENGUJIAN PERANGKAT LUNAK (BLACK BOX TESTING)
  ]
  #v(0.6cm)
  #text(size: 11.5pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\
    #text(size: 10.5pt, weight: "regular")[_Pengujian Fungsionalitas Kotak Hitam (Black Box) Berbasis Skenario Nyata_]
  ]
  #v(1.0cm)
  #rect(width: 5.5cm, height: 3.8cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt)[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[UNIVERSITAS\ INDRAPRASTA PGRI\ (UNINDRA)]
      #v(5pt)
      #text(size: 9pt, fill: rgb("#475569"))[FAKULTAS TEKNIK & ILMU KOMPUTER\ TEKNIK INFORMATIKA]
    ]
  ]
  #v(1.0cm)
  #text(size: 11pt, weight: "bold")[Disusun Oleh (Kelompok 7 / Kelas RPL_XD):]
  #v(0.2cm)
  #table(
    columns: (0.8cm, 8.5cm, 3.5cm),
    align: (center, left, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else { none },
    table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Anggota]*], [*#text(fill: white)[NPM]*]),
    [1], [Adam Wahyu Kurniawan (Lead Architect & SWE)], [202343500510],
    [2], [Fathu Rahman (Business Analyst)], [202343500467],
    [3], [Surya Edi Saputra (QA & Testing Specialist)], [202343500468],
    [4], [Rizqi Muh. Al Hakimi (Database Specialist & UI/UX)], [202343500449],
  )
  #v(0.8cm)
  #text(size: 11pt, weight: "bold")[JAKARTA\ 2026/2027]
]

#pagebreak()

= BAB I: PENDAHULUAN & METODOLOGI PENGUJIAN

== 1.1 Latar Belakang & Posisi Pengujian dalam SDLC
Pengujian Perangkat Lunak (_Software Testing_) merupakan tahap verifikasi dan validasi kritis dalam siklus hidup rekayasa perangkat lunak (_Software Development Life Cycle_ - SDLC). Tahap ini bertujuan menjamin bahwa sistem yang telah dibangun pada tahap Konstruksi (Tugas 10) benar-benar beroperasi sesuai dengan spesifikasi kebutuhan fungsional yang tertuang dalam dokumen SRS (Tugas 2) serta mematuhi alur bisnis pada diagram UML (Tugas 3 s.d. 6).

Pada sistem *SIPESAT (Sistem Informasi Pengajuan Surat Siswa Berbasis Web)*, pengujian difokuskan untuk memastikan bahwa alur birokrasi persuratan—mulai dari permohonan surat oleh siswa, validasi kelayakan dokumen, verifikasi dan disposisi oleh Petugas Tata Usaha (TU), hingga penomoran otomatis dan penerbitan dokumen digital PDF ber-QR Code—berjalan secara presisi, deterministik, dan kebal dari celah validasi (_input boundary errors_) maupun kebocoran otorisasi (_unauthorized privilege escalation_).

== 1.2 Metodologi Black Box Testing
Metodologi pengujian yang digunakan adalah *Black Box Testing (Pengujian Kotak Hitam)*. Pendekatan ini berfokus pada fungsionalitas eksternal perangkat lunak tanpa memeriksa struktur kode internal secara langsung. Teknik yang diterapkan mencakup:
1. *Equivalence Partitioning (EP)*: Membagi rentang masukan data menjadi partisi valid dan tidak valid untuk menguji respons sistem terhadap masukan yang sah dan masukan yang menyimpang.
2. *Boundary Value Analysis (BVA)*: Menguji nilai batas ekstrem pada form input (misalnya ukuran berkas unggahan maksimal 2 MB, kelengkapan kolom wajib).
3. *Role-Based Access Control (RBAC) Testing*: Memastikan pemisahan ketat hak akses antara peran Siswa dan peran Petugas TU.

== 1.3 Lingkungan Pengujian (Testing Environment)
- *Perangkat Keras (Hardware)*: Processor Intel Core i5 / AMD Ryzen 5, RAM 16 GB DDR4, SSD NVMe 512 GB.
- *Sistem Operasi*: Windows 11 Pro 64-bit / Linux Ubuntu 22.04 LTS.
- *Peramban Web (Browser)*: Google Chrome Version 128+ & Microsoft Edge.
- *Database & Server*: PostgreSQL 16 (Docker Port 5432), Express Backend Server (Port 5000), Next.js Frontend Server (Port 3000).
- *Akun Uji*: Siswa (`siswa_adam` / `siswa123`) dan Petugas TU (`admin` / `admin`).

#pagebreak()

= BAB II: TABEL MATRIKS PENGUJIAN SISTEM SIPESAT (BLACK BOX TESTING)

Pengujian dilakukan mengadopsi format matriks resmi UNINDRA dengan kolom: *No*, *Skenario Pengujian*, *Test Case*, *Hasil yang Diharapkan*, *Hasil Pengujian*, dan *Kesimpulan* (dengan aksen warna header merah muda/pink khas panduan akademik):

== 2.1 Modul 1: Autentikasi, Login, & Hak Akses Multi-Role

#table(
  columns: (0.8cm, 3.8cm, 2.8cm, 3.8cm, 1.8cm, 1.5cm),
  align: (center, left, left, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#f472b6") } else if calc.odd(row) { rgb("#fdf2f8") } else { none },
  table.header(
    [*#text(size: 9pt, weight: "bold")[No]*],
    [*#text(size: 9pt, weight: "bold")[Skenario Pengujian]*],
    [*#text(size: 9pt, weight: "bold")[Test Case]*],
    [*#text(size: 9pt, weight: "bold")[Hasil yang Diharapkan]*],
    [*#text(size: 9pt, weight: "bold")[Hasil]*],
    [*#text(size: 9pt, weight: "bold")[Kesimpulan]*],
  ),
  [1], [Username dan Password tidak diisi kemudian klik tombol Login], [Username: (kosong)\ Password: (kosong)], [Sistem menolak dan menampilkan pesan "Harap isi username dan password"], [Sesuai harapan], [*Valid*],
  [2], [Mengetikkan Username, dan password tidak diisi atau kosong kemudian klik tombol Login], [Username: admin\ Password: (kosong)], [Sistem menolak dan menampilkan pesan "Password belum diisi"], [Sesuai harapan], [*Valid*],
  [3], [Mengetikkan Password, dan username tidak diisi atau kosong kemudian klik tombol Login], [Username: (kosong)\ Password: admin], [Sistem menolak dan menampilkan pesan "Username belum diisi"], [Sesuai harapan], [*Valid*],
  [4], [Mengetikkan Username dan/atau password tidak sesuai, kemudian klik tombol Login], [Username: adm\ Password: adm123], [Sistem menolak dan menampilkan pesan "Username atau Password yang anda masukan salah"], [Sesuai harapan], [*Valid*],
  [5], [Mengetikkan Username dan password benar akun Petugas TU, kemudian klik tombol Login], [Username: admin\ Password: admin], [Sistem menerima akses login dan menampilkan dashboard Petugas TU (`/admin/dashboard`)], [Sesuai harapan], [*Valid*],
  [6], [Mengetikkan Username dan password benar akun Siswa, kemudian klik tombol Login], [Username: siswa_adam\ Password: siswa123], [Sistem menerima akses login dan menampilkan portal permohonan siswa (`/siswa/pengajuan`)], [Sesuai harapan], [*Valid*],
  [7], [Mengklik tombol Logout dari sesi pengguna aktif], [Sesi: Siswa / TU aktif\ Aksi: Klik Logout], [Sistem memusnahkan sesi token JWT dan mengalihkan halaman ke `/login`], [Sesuai harapan], [*Valid*],
)

== 2.2 Modul 2: Formulir Pengajuan Surat Mandiri Siswa

#table(
  columns: (0.8cm, 3.8cm, 2.8cm, 3.8cm, 1.8cm, 1.5cm),
  align: (center, left, left, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#f472b6") } else if calc.odd(row) { rgb("#fdf2f8") } else { none },
  table.header(
    [*#text(size: 9pt, weight: "bold")[No]*],
    [*#text(size: 9pt, weight: "bold")[Skenario Pengujian]*],
    [*#text(size: 9pt, weight: "bold")[Test Case]*],
    [*#text(size: 9pt, weight: "bold")[Hasil yang Diharapkan]*],
    [*#text(size: 9pt, weight: "bold")[Hasil]*],
    [*#text(size: 9pt, weight: "bold")[Kesimpulan]*],
  ),
  [8], [Mengirim formulir pengajuan tanpa memilih jenis surat], [Jenis: (Belum dipilih)\ Keperluan: Beasiswa\ File: berkas.pdf], [Sistem menolak submit dan memunculkan peringatan "Pilih jenis surat yang diajukan"], [Sesuai harapan], [*Valid*],
  [9], [Mengisi formulir dengan kolom keperluan kosong], [Jenis: Surat Siswa Aktif\ Keperluan: (kosong)\ File: berkas.pdf], [Sistem menolak submit dan memunculkan peringatan "Keperluan pengajuan wajib diisi"], [Sesuai harapan], [*Valid*],
  [10], [Mengunggah berkas persyaratan dengan ukuran melebihi batas (> 2 MB)], [File: scan_rapor_besar.pdf (Ukuran 4,5 MB)], [Sistem menolak file dan menampilkan notifikasi "Ukuran file maksimal 2 MB"], [Sesuai harapan], [*Valid*],
  [11], [Mengunggah berkas persyaratan dengan format terlarang (.exe, .php)], [File: script_jahat.exe (Ukuran 300 KB)], [Sistem memblokir berkas dengan pesan "Format tidak diizinkan. Hanya PDF, JPG, PNG"], [Sesuai harapan], [*Valid*],
  [12], [Mengisi formulir lengkap dengan berkas valid (< 2 MB)], [Jenis: Surat Siswa Aktif\ Keperluan: Beasiswa\ File: kartu_pelajar.pdf (800 KB)], [Sistem menyimpan data, menerbitkan ID Registrasi, status "Menunggu Verifikasi"], [Sesuai harapan], [*Valid*],
)

#pagebreak()

== 2.3 Modul 3: Pelacakan Status Surat (Tracking & Timeline Stepper)

#table(
  columns: (0.8cm, 3.8cm, 2.8cm, 3.8cm, 1.8cm, 1.5cm),
  align: (center, left, left, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#f472b6") } else if calc.odd(row) { rgb("#fdf2f8") } else { none },
  table.header(
    [*#text(size: 9pt, weight: "bold")[No]*],
    [*#text(size: 9pt, weight: "bold")[Skenario Pengujian]*],
    [*#text(size: 9pt, weight: "bold")[Test Case]*],
    [*#text(size: 9pt, weight: "bold")[Hasil yang Diharapkan]*],
    [*#text(size: 9pt, weight: "bold")[Hasil]*],
    [*#text(size: 9pt, weight: "bold")[Kesimpulan]*],
  ),
  [13], [Mengecek status permohonan dengan nomor tiket kosong], [Nomor Registrasi: (kosong)\ Aksi: Klik Lacak], [Sistem menampilkan pesan "Harap masukkan nomor registrasi pengajuan surat"], [Sesuai harapan], [*Valid*],
  [14], [Melacak status dengan nomor registrasi yang tidak terdaftar], [Nomor: `REG-9999-XXXX` (Fiktif)], [Sistem menampilkan notifikasi "Nomor registrasi tidak ditemukan. Periksa kembali tiket Anda"], [Sesuai harapan], [*Valid*],
  [15], [Melacak surat valid yang berstatus "Menunggu Verifikasi"], [Nomor: `REG-2026-0001`\ Status: Menunggu], [Sistem menampilkan data pemohon dan stepper aktif pada "Menunggu Verifikasi TU"], [Sesuai harapan], [*Valid*],
  [16], [Melacak surat yang berstatus "Ditolak" beserta catatan revisi], [Nomor: `REG-2026-0002`\ Status: Ditolak], [Sistem menampilkan alert merah "Pengajuan Ditolak" beserta alasan revisi], [Sesuai harapan], [*Valid*],
  [17], [Melacak surat yang berstatus "Selesai / Disetujui"], [Nomor: `REG-2026-0003`\ Status: Selesai], [Sistem menampilkan stepper hijau lengkap dan tombol "Unduh Surat PDF Resmi"], [Sesuai harapan], [*Valid*],
)

== 2.4 Modul 4: Verifikasi & Disposisi Berkas oleh Petugas TU

#table(
  columns: (0.8cm, 3.8cm, 2.8cm, 3.8cm, 1.8cm, 1.5cm),
  align: (center, left, left, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#f472b6") } else if calc.odd(row) { rgb("#fdf2f8") } else { none },
  table.header(
    [*#text(size: 9pt, weight: "bold")[No]*],
    [*#text(size: 9pt, weight: "bold")[Skenario Pengujian]*],
    [*#text(size: 9pt, weight: "bold")[Test Case]*],
    [*#text(size: 9pt, weight: "bold")[Hasil yang Diharapkan]*],
    [*#text(size: 9pt, weight: "bold")[Hasil]*],
    [*#text(size: 9pt, weight: "bold")[Kesimpulan]*],
  ),
  [18], [Petugas TU membuka inbox permohonan surat masuk], [Akun: Petugas TU\ Menu: Inbox Surat Masuk], [Sistem memuat daftar permohonan masuk secara real-time dengan status dan badge tanggal], [Sesuai harapan], [*Valid*],
  [19], [Petugas TU melakukan pratinjau berkas persyaratan siswa], [Aksi: Klik tombol "Lihat Dokumen" pada baris siswa], [Sistem membuka modal pratinjau PDF/gambar secara aman tanpa keluar dari halaman utama], [Sesuai harapan], [*Valid*],
  [20], [Petugas TU menolak permohonan tanpa mengisi catatan alasan], [Aksi: Tolak Pengajuan\ Catatan: (kosong)], [Sistem memblokir aksi penolakan: "Alasan penolakan wajib diisi"], [Sesuai harapan], [*Valid*],
  [21], [Petugas TU menolak permohonan dengan mengisi catatan revisi], [Aksi: Tolak Pengajuan\ Catatan: "Scan KK buram"], [Sistem memperbarui status menjadi "Ditolak", menyimpan log audit, dan mengirim pesan], [Sesuai harapan], [*Valid*],
  [22], [Petugas TU menyetujui permohonan surat yang memenuhi syarat], [Aksi: Klik "Setujui & Terbitkan Surat"], [Sistem memperbarui status menjadi "Disetujui", memicu nomor surat, dan siap cetak], [Sesuai harapan], [*Valid*],
)

== 2.5 Modul 5: Penomoran Otomatis & Cetak Surat Digital PDF ber-QR Code

#table(
  columns: (0.8cm, 3.8cm, 2.8cm, 3.8cm, 1.8cm, 1.5cm),
  align: (center, left, left, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#f472b6") } else if calc.odd(row) { rgb("#fdf2f8") } else { none },
  table.header(
    [*#text(size: 9pt, weight: "bold")[No]*],
    [*#text(size: 9pt, weight: "bold")[Skenario Pengujian]*],
    [*#text(size: 9pt, weight: "bold")[Test Case]*],
    [*#text(size: 9pt, weight: "bold")[Hasil yang Diharapkan]*],
    [*#text(size: 9pt, weight: "bold")[Hasil]*],
    [*#text(size: 9pt, weight: "bold")[Kesimpulan]*],
  ),
  [23], [Pengujian otomasi penomoran surat resmi sekolah], [Trigger: Surat disetujui Nov 2026 urutan ke-5], [Sistem menghasilkan nomor surat terformat: `005/SMK-PSKD/XI/2026` secara otomatis], [Sesuai harapan], [*Valid*],
  [24], [Pengujian konversi bulan kalender ke angka romawi], [Bulan: November (Bulan ke-11)], [Sistem mengonversi bulan 11 menjadi romawi "XI" secara presisi tanpa offset], [Sesuai harapan], [*Valid*],
  [25], [Pengujian pembuatan QR Code tanda tangan digital], [Input: ID Pengajuan `SURAT-2026-005`], [Sistem menghasilkan QR Code dinamis yang memuat URL verifikasi otentikasi dokumen], [Sesuai harapan], [*Valid*],
  [26], [Pengunduhan dokumen PDF surat resmi oleh pengguna], [Aksi: Klik tombol "Unduh PDF"], [Sistem mengunduh berkas PDF A4 resmi lengkap dengan kop, nomor, isi, stempel & QR], [Sesuai harapan], [*Valid*],
  [27], [Pemindaian QR Code pada surat PDF menggunakan kamera HP], [Aksi: Scan QR Code di lembar surat fisik/PDF], [Peramban membuka portal verifikasi SIPESAT: "Dokumen Asli Terverifikasi"], [Sesuai harapan], [*Valid*],
)

#pagebreak()

== 2.6 Modul 6: Manajemen Data Master Persuratan & Rekapitulasi Laporan

#table(
  columns: (0.8cm, 3.8cm, 2.8cm, 3.8cm, 1.8cm, 1.5cm),
  align: (center, left, left, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#f472b6") } else if calc.odd(row) { rgb("#fdf2f8") } else { none },
  table.header(
    [*#text(size: 9pt, weight: "bold")[No]*],
    [*#text(size: 9pt, weight: "bold")[Skenario Pengujian]*],
    [*#text(size: 9pt, weight: "bold")[Test Case]*],
    [*#text(size: 9pt, weight: "bold")[Hasil yang Diharapkan]*],
    [*#text(size: 9pt, weight: "bold")[Hasil]*],
    [*#text(size: 9pt, weight: "bold")[Kesimpulan]*],
  ),
  [28], [Petugas TU menambahkan jenis layanan surat baru], [Nama: Surat Izin Observasi\ Format: `{NOMOR}/OBS/SMK/{BULAN_ROMAWI}/{TAHUN}`], [Sistem menyimpan jenis surat baru ke database dan langsung aktif di portal siswa], [Sesuai harapan], [*Valid*],
  [29], [Petugas TU menonaktifkan jenis surat lama (Soft Deactivation)], [Aksi: Ubah status jenis surat menjadi "Nonaktif"], [Siswa tidak dapat memilih jenis surat tersebut, arsip riwayat lama tetap terpelihara], [Sesuai harapan], [*Valid*],
  [30], [Penyaringan laporan persuratan berdasarkan rentang tanggal], [Filter: Tanggal 01 Nov 2026 s.d. 30 Nov 2026], [Sistem menyaring tabel dan hanya menampilkan permohonan dalam periode November 2026], [Sesuai harapan], [*Valid*],
  [31], [Ekspor laporan rekapitulasi persuratan ke spreadsheet], [Aksi: Klik tombol "Ekspor Data (Excel/CSV)"], [Sistem mengunduh berkas spreadsheet rekapitulasi data pemohon, jenis surat, dan status], [Sesuai harapan], [*Valid*],
)

== 2.7 Modul 7: Pengujian Keamanan & Hak Akses (Route Guard & Security)

#table(
  columns: (0.8cm, 3.8cm, 2.8cm, 3.8cm, 1.8cm, 1.5cm),
  align: (center, left, left, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#f472b6") } else if calc.odd(row) { rgb("#fdf2f8") } else { none },
  table.header(
    [*#text(size: 9pt, weight: "bold")[No]*],
    [*#text(size: 9pt, weight: "bold")[Skenario Pengujian]*],
    [*#text(size: 9pt, weight: "bold")[Test Case]*],
    [*#text(size: 9pt, weight: "bold")[Hasil yang Diharapkan]*],
    [*#text(size: 9pt, weight: "bold")[Hasil]*],
    [*#text(size: 9pt, weight: "bold")[Kesimpulan]*],
  ),
  [32], [Siswa mencoba mengakses paksa halaman admin lewat URL], [Role: Siswa\ Aksi: Akses `/admin/dashboard` langsung], [Sistem memblokir akses (HTTP 403 Forbidden) dan mengalihkan siswa ke `/siswa/pengajuan`], [Sesuai harapan], [*Valid*],
  [33], [Akses endpoint API private tanpa menyertakan token JWT], [Request: `GET /api/admin/pengajuan`\ Header: Tanpa Authorization], [Backend menolak request dengan status HTTP 401 Unauthorized ("Token tidak ditemukan")], [Sesuai harapan], [*Valid*],
  [34], [Siswa mencoba mengunduh surat milik siswa lain via ganti ID], [Akun: Siswa A\ Aksi: Akses URL unduh file milik Siswa B], [Sistem memverifikasi kepemilikan data (Data Isolation) dan menolak akses dengan HTTP 403], [Sesuai harapan], [*Valid*],
  [35], [Uji serangan Cross-Site Scripting (XSS) pada form alasan], [Input: `<script>alert('XSS_ATTACK')</script>`], [Sistem mensterilkan tag HTML/JS sehingga tersimpan sebagai string teks biasa yang aman], [Sesuai harapan], [*Valid*],
)

#pagebreak()

= BAB III: ANALISIS HASIL PENGUJIAN & METRIK KUALITAS

== 3.1 Rekapitulasi Metrik Pengujian
Berdasarkan eksekusi 35 skenario pengujian fungsionalitas kotak hitam (_Black Box Testing_) pada sistem SIPESAT, diperoleh rekapitulasi metrik pengujian sebagai berikut:

#table(
  columns: (7.0cm, 2.2cm, 2.2cm, 2.0cm, 2.5cm),
  align: (left, center, center, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if row == 8 { rgb("#f1f5f9") } else { none },
  table.header(
    [*#text(fill: white, size: 9pt)[Kategori Modul Pengujian]*],
    [*#text(fill: white, size: 9pt)[Total Test]*],
    [*#text(fill: white, size: 9pt)[Pass]*],
    [*#text(fill: white, size: 9pt)[Fail]*],
    [*#text(fill: white, size: 9pt)[Persentase]*],
  ),
  [Modul 1: Autentikasi & Hak Akses Multi-Role], [7], [7], [0], [100%],
  [Modul 2: Formulir Pengajuan Surat Mandiri Siswa], [5], [5], [0], [100%],
  [Modul 3: Pelacakan Status Surat (Tracking Stepper)], [5], [5], [0], [100%],
  [Modul 4: Verifikasi & Disposisi Petugas TU], [5], [5], [0], [100%],
  [Modul 5: Penomoran Otomatis & Cetak PDF QR Code], [5], [5], [0], [100%],
  [Modul 6: Manajemen Data Master & Laporan], [4], [4], [0], [100%],
  [Modul 7: Keamanan & Hak Akses (Route Guard)], [4], [4], [0], [100%],
  [*TOTAL KESELURUHAN PENGUJIAN*], [*35*], [*35*], [*0*], [*100% (SEMPURNA)*],
)

== 3.2 Analisis Kesiapan Sistem
1. *Validasi Batas Beroperasi Sempurna*: Seluruh penanganan kondisi input kosong, format berkas menyimpang, maupun batas ukuran berkas ($> 2" MB"$) berhasil ditolak secara konsisten oleh sistem dengan pesan ramah pengguna.
2. *Integritas Penomoran & Tanda Tangan Digital*: Fungsi pembentukan nomor surat resmi (`generateNomorSuratResmi`) dan generator QR Code terbukti menghasilkan dokumen dinamis yang unik, tertelusur, dan bebas dari duplikasi nomor surat.
3. *Pemisahan Hak Akses Ketat (RBAC)*: Pengujian penetrasi sederhana pada rute administratif (`/admin/*`) dan isolasi kepemilikan data antar-siswa membuktikan bahwa middleware autentikasi JWT berhasil melindungi data sensitif sekolah dari akses tanpa hak.

= BAB IV: KESIMPULAN & TAUTAN KODE SUMBER

== 4.1 Kesimpulan
Pengujian perangkat lunak sistem *SIPESAT (Sistem Informasi Pengajuan Surat Siswa Berbasis Web)* menggunakan metode _Black Box Testing_ telah diselesaikan secara tuntas. Dari 35 kasus pengujian yang mencakup seluruh modul operasional siswa dan petugas tata usaha:
- *Tingkat Keberhasilan Pengujian*: *100% Valid (Pass)*.
- *Kepadatan Cacat (_Defect Density_)*: *0 Critical Bugs*.
Sistem dinyatakan telah memenuhi seluruh spesifikasi kebutuhan perangkat lunak (SRS IEEE 830), aman dari kerentanan input dasar, serta berada dalam status *Siap Produksi (_Production Ready_)* untuk diimplementasikan di lingkungan sekolah.

== 4.2 Tautan Repositori GitHub Resmi
Sesuai arahan dosen pengampu mata kuliah Rekayasa Perangkat Lunak (RPL), seluruh kode program frontend, backend, skema database Prisma, dan berkas laporan tugas dapat diakses secara publik dan transparan pada repositori GitHub resmi berikut:

*URL Repositori GitHub*:  
#link("https://github.com/themodeid/Sipesat-RPL")[https://github.com/themodeid/Sipesat-RPL]

---
_Disusun dan disahkan oleh Kelompok RPL 7 (Adam Wahyu Kurniawan dkk) untuk memenuhi penilaian resmi Tugas Pertemuan 11 Mata Kuliah Rekayasa Perangkat Lunak - Universitas Indraprasta PGRI (UNINDRA)._
