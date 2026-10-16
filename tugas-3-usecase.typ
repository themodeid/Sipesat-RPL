#set document(
  title: "Tugas 3 RPL: Perancangan Use Case Diagram & Matriks RBAC - SIPESAT",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)

#set text(
  font: "Times New Roman",
  size: 11pt,
  lang: "id"
)

#set page(
  paper: "a4",
  margin: (left: 4cm, top: 4cm, right: 3cm, bottom: 3cm),
  header: none,
  footer: context align(center)[#text(size: 10pt)[#counter(page).display("1")]]
)

// COVER PAGE
#align(center)[
  #text(size: 14pt, weight: "bold")[
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\
    TUGAS 3: PERANCANGAN USE CASE DIAGRAM & MATRIKS HAK AKSES (RBAC)
  ]

  #v(1.2cm)

  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\
    #text(size: 11pt, weight: "regular")[_Studi Kasus: Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah_]
  ]

  #v(2.0cm)

  #rect(
    width: 5cm,
    height: 4.5cm,
    stroke: 1.5pt + rgb("#1e293b"),
    radius: 4pt
  )[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[
        UNIVERSITAS\
        INDRAPRASTA PGRI\
        (UNINDRA)
      ]
      #v(6pt)
      #text(size: 9.5pt, fill: rgb("#475569"))[
        FAKULTAS TEKNIK & ILMU KOMPUTER\
        TEKNIK INFORMATIKA
      ]
    ]
  ]

  #v(2.0cm)

  #text(size: 11pt, weight: "bold")[Disusun Oleh (Kelompok 7 / Kelas RPL_XD):]
  #v(0.3cm)

  #table(
    columns: (0.8cm, 8.5cm, 3.5cm),
    align: (center, left, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else { none },
    table.header(
      [*#text(fill: white)[No]*],
      [*#text(fill: white)[Nama Anggota]*],
      [*#text(fill: white)[NPM]*]
    ),
    [1], [Adam Wahyu Kurniawan (Lead Architect & SWE)], [202343500510],
    [2], [Fathu Rahman (Business Analyst)], [202343500467],
    [3], [Surya Edi Saputra (QA & Technical Writer)], [202343500468],
    [4], [Rizqi Muh. Al Hakimi (Database Specialist)], [202343500449],
  )

  #v(1.5cm)
  #text(size: 11pt, weight: "bold")[JAKARTA\ 2026/2027]
]

#pagebreak()

// BAB I
#heading(level: 1)[BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM]

== 1.1 Deskripsi Proyek SIPESAT
Sistem Informasi Pengajuan Surat Siswa Berbasis Web (*SIPESAT*) adalah sistem perangkat lunak yang dirancang untuk memodernisasi dan mengotomatisasi rantai birokrasi pengajuan surat keterangan di lingkungan sekolah menengah. Sebelum adanya sistem ini, siswa harus datang langsung ke ruang Tata Usaha (TU), mengisi formulir kertas manual, dan menunggu proses verifikasi berhari-hari tanpa kejelasan status.

SIPESAT memotong hambatan tersebut dengan menyediakan portal mandiri daring bagi siswa untuk mengajukan surat, mengunggah berkas persyaratan secara digital, memantau posisi surat secara transparan (_real-time status tracking_), dan mengunduh berkas surat resmi berformat PDF yang telah dilengkapi nomor register resmi serta kode QR tanda tangan elektronik.

== 1.2 Tujuan Pemodelan Use Case Diagram
Use Case Diagram dalam Unified Modeling Language (UML) berfungsi memetakan fungsi sistem dari sudut pandang aktor eksternal. Tujuan pemodelan meliputi:
1. Mendefinisikan batasan sistem (_system boundary_) secara tegas.
2. Mengidentifikasi seluruh aktor pengguna yang berinteraksi langsung dengan sistem.
3. Memetakan kebutuhan fungsional ke dalam use case terdefinisi.
4. Menjelaskan relasi dependensi menggunakan stereotype `<<include>>` dan `<<extend>>`.

#v(0.5cm)
// BAB II
#heading(level: 1)[BAB II: PERANCANGAN USE CASE DIAGRAM SIPESAT]

== 2.1 Identifikasi Aktor Sistem
Sistem SIPESAT menerapkan pemisahan hak akses berbasis peran (RBAC) yang terdiri dari 2 aktor utama:
1. *Siswa (Aktor Pemohon)*: Peserta didik aktif yang mengajukan surat, mengunggah bukti syarat, memantau proses, dan mengunduh surat PDF hasil verifikasi.
2. *Petugas TU / Admin (Aktor Pengelola & Verifikator)*: Staf administrasi sekolah yang memverifikasi kelayakan berkas permohonan, menerbitkan nomor agenda keluar, mengesahkan surat resmi, dan mencetak laporan rekapitulasi.

== 2.2 Rincian Use Case Terdefinisi

#table(
  columns: (1.5cm, 4.2cm, 2.5cm, 6.5cm),
  align: (center, left, center, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header(
    [*#text(fill: white)[Kode]*],
    [*#text(fill: white)[Nama Use Case]*],
    [*#text(fill: white)[Aktor]*],
    [*#text(fill: white)[Deskripsi Singkat]*]
  ),
  [UC-01], [Login ke Sistem], [Siswa, TU], [Otentikasi akun pengguna menggunakan NISN/NIP dan kata sandi terenkripsi.],
  [UC-01B], [Validasi Token JWT], [Sistem (Inc)], [Pengecekan keabsahan tanda tangan token JWT pada rute terproteksi.],
  [UC-02], [Registrasi Akun Siswa], [Siswa], [Pendaftaran mandiri siswa dengan verifikasi NISN ke database sekolah.],
  [UC-03], [Kelola Profil & Sandi], [Siswa, TU], [Pembaharuan data kontak telepon, email, dan pergantian kata sandi.],
  [UC-04], [Logout Sesi], [Siswa, TU], [Penghapusan cookie sesi HttpOnly dan pembatalan token aktif di server.],
  [UC-05], [Katalog & Syarat Surat], [Siswa], [Eksplorasi daftar template surat dan persyaratan berkas wajib.],
  [UC-06], [Ajukan Permohonan Surat], [Siswa], [Pengisian formulir keperluan surat dan penentuan tujuan pembuatan.],
  [UC-07], [Unggah Berkas Syarat], [Siswa (Inc)], [Pengunggahan berkas bukti scan dokumen (PDF/JPG maksimal 2 MB).],
  [UC-08], [Lacak Status Surat], [Siswa], [Pemantauan posisi tahapan surat secara transparan via status stepper.],
  [UC-08A], [Periksa Catatan Revisi], [Siswa (Ext)], [Pembacaan catatan feedback penolakan dan instruksi koreksi dari TU.],
  [UC-09], [Riwayat Arsip Pengajuan], [Siswa], [Peninjauan seluruh rekam jejak surat yang pernah diajukan sebelumnya.],
  [UC-10], [Unduh Surat Resmi PDF], [Siswa], [Pengunduhan stream berkas PDF surat resmi berkop dan ber-QR Code.],
  [UC-11], [Dashboard Statistik TU], [Petugas TU], [Tinjauan metrik: total surat masuk, verifikasi, selesai, dan ditolak.],
  [UC-12], [Kelola Antrean Masuk], [Petugas TU], [Pengurutan dan penyaringan permohonan surat berdasarkan tanggal.],
  [UC-13], [Verifikasi Berkas Siswa], [Petugas TU], [Pemeriksaan keabsahan dokumen berkas lampiran siswa.],
  [UC-14], [Setujui Permohonan], [Petugas TU], [Persetujuan administratif surat permohonan yang telah valid.],
  [UC-14A], [Terbitkan No. & QR Code], [TU (Inc)], [Generate otomatis nomor agenda resmi sekolah dan hash QR Code.],
  [UC-15], [Tolak Permohonan], [Petugas TU], [Penolakan permohonan yang berkasnya buram atau tidak lengkap.],
  [UC-15A], [Input Catatan Revisi], [TU (Inc)], [Penyusunan alasan koreksi tertulis untuk diperbaiki oleh siswa.],
  [UC-16], [Kelola Master Surat], [Petugas TU], [Manajemen jenis surat, perubahan syarat, dan template naskah.],
  [UC-17], [Kelola Akun Pengguna], [Petugas TU], [Pengawasan akun, pembukaan blokir akun, dan reset kata sandi.],
  [UC-18], [Ekspor Rekap Laporan], [Petugas TU], [Pembuatan laporan rekapitulasi persuratan ke format Excel/PDF.],
)

#pagebreak()

// BAB III
#heading(level: 1)[BAB III: MATRIKS HAK AKSES (ROLE-BASED ACCESS CONTROL)]

Untuk menjamin keamanan sistem dan integritas data persuratan sekolah, setiap fungsi sistem dipagari oleh otorisasi berbasis peran (RBAC):

#table(
  columns: (1.2cm, 7.5cm, 3.0cm, 3.0cm),
  align: (center, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header(
    [*#text(fill: white)[No]*],
    [*#text(fill: white)[Nama Use Case / Modul]*],
    [*#text(fill: white)[Role Siswa]*],
    [*#text(fill: white)[Role Petugas TU]*]
  ),
  [1], [UC-01: Login ke Sistem], [✅ Ya], [✅ Ya],
  [2], [UC-02: Registrasi Akun Siswa Baru], [✅ Ya], [❌ Tidak],
  [3], [UC-03: Kelola Profil & Sandi], [✅ Ya], [✅ Ya],
  [4], [UC-04: Logout Sesi Pengguna], [✅ Ya], [✅ Ya],
  [5], [UC-05: Katalog & Syarat Surat], [✅ Ya], [✅ Ya (Kelola)],
  [6], [UC-06: Pengajuan Surat Baru], [✅ Ya], [❌ Tidak],
  [7], [UC-07: Unggah Berkas Persyaratan], [✅ Ya], [❌ Tidak],
  [8], [UC-08: Lacak Status Surat (Tracking)], [✅ Ya], [❌ Tidak],
  [9], [UC-09: Riwayat Pengajuan Mandiri], [✅ Ya], [❌ Tidak],
  [10], [UC-10: Unduh Surat PDF Ber-QR Code], [✅ Ya], [✅ Ya],
  [11], [UC-11: Dashboard Statistik TU], [❌ Tidak], [✅ Ya],
  [12], [UC-12: Kelola Antrean Surat Masuk], [❌ Tidak], [✅ Ya],
  [13], [UC-13: Verifikasi Berkas Siswa], [❌ Tidak], [✅ Ya],
  [14], [UC-14: Persetujuan Permohonan (Approve)], [❌ Tidak], [✅ Ya],
  [15], [UC-15: Penolakan Permohonan (Reject)], [❌ Tidak], [✅ Ya],
  [16], [UC-16: Kelola Master Jenis Surat], [❌ Tidak], [✅ Ya],
  [17], [UC-17: Kelola Master Akun Pengguna], [❌ Tidak], [✅ Ya],
  [18], [UC-18: Ekspor Rekapitulasi Laporan], [❌ Tidak], [✅ Ya],
)

#v(0.8cm)
// BAB IV
#heading(level: 1)[BAB IV: KESIMPULAN & BERKAS DIAGRAM]

Perancangan Use Case Diagram dan Matriks Hak Akses (RBAC) pada sistem SIPESAT telah diselaraskan secara komprehensif dengan:
1. *SRS Standar IEEE Std 830-1998 (Tugas 2)*: Menjaga konsistensi identifikasi fungsionalitas sistem dari spesifikasi awal.
2. *Kaidah Akademik UNINDRA*: Batasan sistem tegas, relasi use case baku (`<<include>>` dan `<<extend>>`), serta skenario formal.
3. *Integrasi Draw.io Native*: Seluruh diagram visual interaktif dapat diakses dan disunting pada berkas master:
   - *tugas-3-usecase.drawio* (2 Tab: Use Case Diagram & Matriks RBAC).
