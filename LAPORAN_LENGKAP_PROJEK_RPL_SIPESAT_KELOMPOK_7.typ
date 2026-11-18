#set document(
  title: "Laporan Lengkap Proyek Rekayasa Perangkat Lunak: SIPESAT - Kelompok 7",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)

#set text(font: "Times New Roman", size: 11pt, lang: "id")
#set page(
  paper: "a4",
  margin: (left: 4cm, top: 4cm, right: 3cm, bottom: 3cm),
  header: none,
  footer: context align(center)[#text(size: 10pt)[#counter(page).display("1")]]
)

#set par(justify: true, leading: 0.75em)
#set heading(numbering: "1.1")

// ==================== COVER HALAMAN JUDUL ====================
#align(center)[
  #v(0.5cm)
  #text(size: 14pt, weight: "bold")[
    LAPORAN AKHIR PROYEK REKAYASA PERANGKAT LUNAK (RPL)\
    DOKUMEN KONSOLIDASI 9 DELIVERABLES SISTEM
  ]
  #v(0.8cm)
  #text(size: 13pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB\
    (SIPESAT)
  ]
  #v(0.3cm)
  #text(size: 10.5pt, style: "italic")[
    Otomatisasi Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah Menengah\
    Arsitektur Decoupled (Next.js 14 + Express.js TypeScript + Docker PostgreSQL 16)
  ]
  
  #v(1.5cm)
  #rect(width: 5.5cm, height: 4.5cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt)[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[UNIVERSITAS\ INDRAPRASTA PGRI\ (UNINDRA)]
      #v(6pt)
      #text(size: 9.5pt, fill: rgb("#475569"))[FAKULTAS TEKNIK & ILMU KOMPUTER\ PROGRAM STUDI TEKNIK INFORMATIKA]
    ]
  ]
  
  #v(1.5cm)
  #text(size: 11pt, weight: "bold")[Disusun oleh KELOMPOK 7 (Kelas RPL_XD):]
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
    [4], [Rizqi Muh. Al Hakimi (Database Specialist & UI/UX)], [202343500449],
  )
  
  #v(1.2cm)
  #text(size: 11pt, weight: "bold")[
    JAKARTA\
    TAHUN AKADEMIK 2026/2027
  ]
]

#pagebreak()

// ==================== DAFTAR DELIVERABLES MATRIKS ====================
#align(center)[
  #text(size: 13pt, weight: "bold")[MATRIKS KELENGKAPAN 9 DELIVERABLES PROYEK RPL]
]
#v(0.3cm)

Dokumen ini merupakan bundel resmi laporan tugas besar mata kuliah Rekayasa Perangkat Lunak (RPL) Kelompok 7 yang mengonsolidasikan kesembilan poin penugasan ke dalam satu kesatuan dokumen utuh:

#table(
  columns: (0.8cm, 3.2cm, 4.0cm, 6.5cm),
  align: (center, left, left, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Item Deliverable]*], [*#text(fill: white)[Standar / Format]*], [*#text(fill: white)[Lokasi Bab / Status]*]),
  [1], [SRS], [IEEE Std 830 / Karl Wiegers], [BAB II — 5 Bab Lengkap (2 Role: Siswa & TU)],
  [2], [USECASE DIAGRAM], [UML 2.5 Use Case], [BAB III — 18 Use Cases & Matriks Hak Akses RBAC],
  [3], [CLASS DIAGRAM], [UML 2.5 Class & Object], [BAB IV — Struktur Kelas, Enkapsulasi, Skema 3NF],
  [4], [ACTIVITY DIAGRAM], [UML 2.5 Swimlane], [BAB V — 4 Activity Multi-Swimlane Alur Kerja],
  [5], [SEQUENCE DIAGRAM], [UML 2.5 Pola BCE], [BAB VI — 4 Sequence Diagram Interaksi Objek],
  [6], [DEPLOYMENT DIAGRAM], [UML 2.5 3-Tier Node], [BAB VII — Arsitektur Fisik, Port & Docker],
  [7], [HASIL FIGMA], [Design System & UI], [BAB VIII — Color Tokens, Spacing, 8 Mockup Layar],
  [8], [HASIL SISTEMNYA], [Fullstack Monorepo], [BAB IX — Konstruksi Next.js & Black Box Testing],
  [9], [FILE PPT PRESENTASI], [PowerPoint Widescreen], [BAB X — 12 Slide Presentasi & Link GitHub],
)

#v(0.5cm)
*Tautan Repositori GitHub Resmi:*
#link("https://github.com/themodeid/Sipesat-RPL")[https://github.com/themodeid/Sipesat-RPL]

#pagebreak()

// ==================== BAB I: PENDAHULUAN ====================
= BAB I: PENDAHULUAN
== 1.1 Latar Belakang Masalah
Pelayanan persuratan dinas bagi siswa di lingkungan sekolah menengah (seperti Surat Keterangan Siswa Aktif, Surat Rekomendasi Beasiswa, Surat Pengantar Legalisir Ijazah, dan Surat Dispensasi Kegiatan) selama ini diselenggarakan secara konvensional. Siswa diwajibkan datang langsung ke ruang Tata Usaha (TU) pada jam istirahat atau jam pulang sekolah untuk mengisi formulir kertas dan menyerahkan fotokopi berkas fisik.

Metode konvensional ini menimbulkan sejumlah kendala operasional yang signifikan:
- *Antrean Panjang & Keterbatasan Waktu*: Terjadi penumpukan antrean pada musim registrasi perguruan tinggi, pendaftaran beasiswa, atau seleksi kerja.
- *Resiko Kehilangan & Kerusakan Berkas*: Formulir kertas dan fotokopi berkas syarat siswa sering kali terselip atau tercecer di meja administrasi.
- *Penomoran Ganda & Kesalahan Manual*: Pencatatan nomor agenda surat pada buku ekspedisi manual rawan terlewat atau tercatat ganda.
- *Ketidakpastian Status*: Siswa tidak memiliki sarana mandiri untuk memantau apakah permohonan surat sudah diverifikasi, disetujui, atau ditolak.

== 1.2 Solusi SIPESAT
Sistem Informasi Pengajuan Surat Siswa Berbasis Web (*SIPESAT*) dirancang untuk mengotomatisasi seluruh siklus hidup persuratan siswa secara mandiri (*self-service*) berbasis web terpisah (*Decoupled Frontend & Backend*). Melalui sistem ini:
- Siswa dapat mengajukan surat kapan saja dan di mana saja (24/7).
- Unggah berkas digital dibatasi maksimal 2 MB dengan validasi tipe berkas otomatis (PDF/JPG/PNG).
- Petugas Tata Usaha memverifikasi keabsahan dokumen melalui dasbor khusus.
- Sistem secara otomatis menerbitkan nomor surat resmi sekolah sesuai format baku dan membubuhkan Tanda Tangan Elektronik berupa Kode QR terenkripsi.
- Siswa dapat memantau status secara transparan melalui _Timeline Stepper_ interaktif dan mengunduh surat resmi digital dalam format PDF berstandar cetak A4.

#pagebreak()

// ==================== BAB II: SPESIFIKASI KEBUTUHAN (SRS) ====================
= BAB II: SPESIFIKASI KEBUTUHAN PERANGKAT LUNAK (SRS)
_Standar Acuan: IEEE Std 830-1998 / Karl Wiegers (Tugas 2 RPL)_

== 2.1 Perampingan 2 Peran Pengguna Eksklusif (RBAC)
Sesuai arahan dosen pengampu mata kuliah, struktur peran dirampingkan murni menjadi dua aktor pengguna:
1. *Siswa (Pemohon)*: Aktor pengguna akhir yang memiliki hak akses mengajukan surat, mengunggah berkas syarat, melacak status, dan mengunduh surat resmi yang telah disahkan.
2. *Petugas Tata Usaha / Admin (Verifikator & Pengesah)*: Aktor pengelola administrasi yang memiliki wewenang memeriksa kelengkapan berkas, memberikan disposisi persetujuan atau penolakan, menetapkan nomor surat resmi, dan menerbitkan laporan rekapitulasi.

== 2.2 Kebutuhan Fungsional Sistem (Functional Requirements)
#table(
  columns: (2.2cm, 4.0cm, 8.5cm),
  align: (center, left, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[Kode]*], [*#text(fill: white)[Nama Fitur]*], [*#text(fill: white)[Deskripsi Kebutuhan]*]),
  [FR-01], [Autentikasi RBAC], [Sistem memvalidasi login pengguna (NISN/NIP) menggunakan enkripsi kata sandi Bcrypt dan menerbitkan token sesi JWT.],
  [FR-02], [Katalog Jenis Surat], [Sistem menyajikan daftar layanan surat: Keterangan Siswa Aktif, Rekomendasi Beasiswa, Legalisir, Dispensasi.],
  [FR-03], [Form Pengajuan Mandiri], [Siswa dapat mengisi tujuan permohonan dan mengunggah dokumen prasyarat dengan batas ukuran maksimal 2 MB.],
  [FR-04], [Validasi Berkas Multer], [Sistem memverifikasi tipe MIME berkas (PDF, JPG, PNG). Sistem menolak berkas jika melebihi kuota 2 MB.],
  [FR-05], [Timeline Stepper Tracking], [Sistem menampilkan 5 tahapan status transparan: Draft, Diajukan, Diproses, Disetujui, dan Selesai Siap Unduh.],
  [FR-06], [Verifikasi & Disposisi TU], [Petugas TU dapat memeriksa berkas persyaratan secara langsung di web dan memberikan putusan Setujui atau Tolak.],
  [FR-07], [Auto-Numbering Engine], [Sistem otomatis menyusun nomor surat resmi berurutan dinamis (contoh: 421/001/SMK-PSKD/XI/2026).],
  [FR-08], [Generator PDF ber-QR TTE], [Sistem menyusun file PDF surat resmi ber-kop sekolah dengan kode QR verifikasi keaslian digital.],
  [FR-09], [Laporan Rekapitulasi], [Petugas TU dapat menyaring dan mengekspor data rekapitulasi surat ke dalam format CSV dan cetak PDF.],
)

== 2.3 Kebutuhan Non-Fungsional (Non-Functional Requirements)
- *Keandalan & Integritas*: Seluruh transaksi permohonan surat dijalankan dengan mekanisme transaksi ACID melalui Prisma ORM.
- *Kinerja*: Waktu respon rata-rata endpoint API Express berada di bawah 300 ms pada lalu lintas beban normal sekolah.
- *Keamanan*: Kata sandi di-hash menggunakan Bcrypt salt 10 putaran; seluruh rute sensitif dilindungi middleware verifikasi token Bearer JWT.
- *Portabilitas*: Seluruh infrastruktur basis data PostgreSQL 16 diisolasi di dalam container Docker Compose.

#pagebreak()

// ==================== BAB III: USE CASE DIAGRAM ====================
= BAB III: PEMODELAN USE CASE DIAGRAM
_Standar Acuan: UML 2.5 Use Case Modeling (Tugas 3 RPL)_

== 3.1 Visualisasi Diagram Use Case Sistem SIPESAT
#align(center)[
  #image("assets/diagram_usecase.png", width: 95%)
  #v(4pt)
  #text(size: 9.5pt, style: "italic")[Gambar 3.1: Use Case Diagram Sistem SIPESAT (2 Aktor, 18 Use Cases)]
]

== 3.2 Uraian Paket Use Case
Sistem SIPESAT memetakan 18 Use Cases yang dikelompokkan ke dalam 3 paket layanan:
1. *Paket Autentikasi*: Use Case Login, Logout, dan Kelola Password. Menerapkan relasi _include_ pada seluruh fitur transaksional.
2. *Paket Layanan Siswa*: Melihat Katalog Surat, Mengisi Form Permohonan, Mengunggah Berkas Syarat, Memantau Stepper Status, dan Mengunduh Dokumen Surat PDF.
3. *Paket Administrasi Tata Usaha*: Memeriksa Antrean Surat Masuk, Verifikasi Berkas Persyaratan, Memberikan Disposisi Setuju/Tolak, Menetapkan Nomor Surat Resmi, Menerbitkan Surat ber-QR Code, dan Mencetak Laporan Rekapitulasi.

#pagebreak()

// ==================== BAB IV: CLASS DIAGRAM ====================
= BAB IV: PEMODELAN CLASS DIAGRAM & BASIS DATA
_Standar Acuan: UML 2.5 Static Structure Diagram (Tugas 6 RPL)_

== 4.1 Struktur Hierarki Kelas & Hubungan OOP
Arsitektur perangkat lunak SIPESAT memodelkan prinsip Object-Oriented Programming (OOP) secara ketat:
- *Superclass Abstract Pengguna*: Membungkus atribut umum (`id_pengguna`, `username`, `password_hash`, `email`, `role`, `status_aktif`) dan metode operasi `login()`, `logout()`, `updatePassword()`.
- *Subclass Siswa*: Mewarisi kelas Pengguna dengan spesialisasi atribut `nisn`, `nis`, `nama_lengkap`, `kelas`, `jurusan`, dan operasi `buatPengajuanSurat()`, `uploadBerkas()`, `lacakStatus()`.
- *Subclass PetugasTU*: Mewarisi kelas Pengguna dengan spesialisasi atribut `nip`, `nama_petugas`, `nomor_sk`, `bagian`, dan operasi `verifikasiBerkas()`, `generateNomorSurat()`, `forwardKeKepsek()`.
- *Kelas PengajuanSurat*: Berelasi asosiasi `1..*` ke Siswa, `1..1` ke JenisSurat, dan `0..1` ke PetugasTU.
- *Komposisi Mutlak*: Entitas `BerkasPersyaratan` dan `RiwayatStatus` terikat secara _Strong Ownership_ pada siklus hidup `PengajuanSurat`. Jika surat dihapus, berkas dan log riwayat ikut terhapus (_Cascade Delete_).

== 4.2 Pemetaan ke Skema PostgreSQL Relasional (3NF)
Arsitektur database mengadopsi 7 tabel relasional terstandarisasi Bentuk Normal Ketiga (3NF):
1. `tb_user`: Autentikasi kredensial dan role enum (`SISWA`, `PETUGAS_TU`, `ADMIN`).
2. `tb_siswa`: Biodata master siswa sekolah menengah.
3. `tb_petugas`: Data identitas staf administrasi Tata Usaha.
4. `tb_jenis_surat`: Katalog konfigurasi jenis surat, format nomor, dan syarat berkas.
5. `tb_pengajuan_surat`: Tabel transaksi permohonan surat dan kode tiket resi.
6. `tb_berkas_persyaratan`: Metadata berkas upload, tipe MIME, dan lokasi path fisik.
7. `tb_riwayat_status`: Rekam jejak audit trail perubahan status surat secara kronologis.

#pagebreak()

// ==================== BAB V: ACTIVITY DIAGRAM ====================
= BAB V: PEMODELAN ACTIVITY DIAGRAM
_Standar Acuan: UML 2.5 Multi-Swimlane Activity Diagram (Tugas 4 RPL)_

== 5.1 Visualisasi Activity Diagram Terpadu SIPESAT
#align(center)[
  #image("assets/diagram_activity.png", width: 95%)
  #v(4pt)
  #text(size: 9.5pt, style: "italic")[Gambar 5.1: Activity Diagram Alur Kerja Pengajuan Surat Siswa & Verifikasi TU]
]

== 5.2 Uraian Aliran Alur Kerja (Workflow Steps)
1. *Inisialisasi*: Siswa login ke sistem web SIPESAT. Sistem memvalidasi kredensial.
2. *Pemilihan Layanan*: Siswa memilih jenis surat yang dibutuhkan dari katalog layanan.
3. *Pengisian & Unggah*: Siswa mengisi keperluan surat dan mengunggah berkas syarat (misal: Kartu Keluarga / Rapor).
4. *Validasi Sisi Server*: Sistem memeriksa ukuran berkas. Jika ukuran $> 2$ MB, sistem menolak dan meminta siswa memilih file yang sesuai.
5. *Penerbitan Tiket*: Jika valid, sistem menyimpan data dengan status `DIAJUKAN` dan menerbitkan kode tiket pelacakan unik.
6. *Pemeriksaan TU*: Petugas TU membuka antrean surat masuk dan memeriksa keabsahan berkas lampiran.
7. *Percabangan Disposisi*:
   - Jika berkas tidak valid: Petugas memilih *Tolak* disertai catatan perbaikan. Sistem mengubah status menjadi `DITOLAK` dan mengirim notifikasi ke dasbor siswa.
   - Jika berkas valid: Petugas memilih *Setujui*. Sistem memanggil *Auto-Numbering Engine*, membuat stempel QR Code TTE, mengubah status menjadi `SELESAI`, dan menyusun file PDF resmi.
8. *Penyelesaian*: Siswa mengunduh dokumen surat resmi ber-QR Code langsung dari web.

#pagebreak()

// ==================== BAB VI: SEQUENCE DIAGRAM ====================
= BAB VI: PEMODELAN SEQUENCE DIAGRAM
_Standar Acuan: UML 2.5 Pola Boundary - Control - Entity (BCE) (Tugas 4 RPL)_

== 6.1 Visualisasi Sequence Diagram SIPESAT
#align(center)[
  #image("assets/diagram_sequence.png", width: 95%)
  #v(4pt)
  #text(size: 9.5pt, style: "italic")[Gambar 6.1: Sequence Diagram Interaksi Objek Pola BCE Standar UNINDRA]
]

== 6.2 Pola Boundary - Control - Entity (BCE)
Pemodelan Sequence Diagram SIPESAT mengadopsi standar bahan ajar UNINDRA:
- *Boundary*: Antarmuka tempat aktor berinteraksi (`LoginFormUI`, `FormPengajuanUI`, `DashboardPetugasUI`).
- *Control*: Pengendali logika bisnis (`AuthController`, `PengajuanController`, `SuratGeneratorController`).
- *Entity*: Tabel penyimpan data persisten (`tb_user`, `tb_pengajuan_surat`, `tb_berkas_persyaratan`).
- *Frame Percabangan (_alt_)*: Menangani skenario alternatif (Login Sukses vs Gagal, Berkas Valid vs Melebihi Kuota 2MB, Permohonan Disetujui vs Ditolak).

#pagebreak()

// ==================== BAB VII: DEPLOYMENT DIAGRAM ====================
= BAB VII: PEMODELAN DEPLOYMENT DIAGRAM
_Standar Acuan: UML 2.5 Hardware & Execution Architecture (Tugas 7 RPL)_

== 7.1 Arsitektur Fisik 3-Tier Decoupled
Sistem SIPESAT dirancang menggunakan topologi terdistribusi tiga tingkatan komputasi:

#table(
  columns: (3.2cm, 3.8cm, 7.5cm),
  align: (center, left, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[Tingkatan (Tier)]*], [*#text(fill: white)[Simpul / Node]*], [*#text(fill: white)[Teknologi & Peran Komputasi]*]),
  [Tier 1: Client], [Client User Device (PC / Smartphone)], [Web Browser Engine (Chrome, Edge, Safari) merender HTML5/CSS3/React Virtual DOM dan menyimpan token JWT.],
  [Tier 2: Web Server], [Node.js Host (Port 3000)], [Next.js 14 App Router menyajikan Server-Side Rendering (SSR), optimasi bundel visual, dan layout Tailwind CSS.],
  [Tier 2: API Gateway], [Node.js Host (Port 5000)], [Express.js REST API mengeksekusi validasi JWT, Multer file upload, Auto-Numbering Engine, dan PDFKit generator.],
  [Tier 3: Database], [Docker Engine (Port 5432)], [Container PostgreSQL 16 Alpine mengelola penyimpanan basis data persisten via volume sipesat_postgres_data.],
)

== 7.2 Protokol Jaringan & Keamanan
- *HTTP / HTTPS (Port 3000)*: Mengirimkan aset antarmuka grafis ke peramban klien.
- *REST API JSON over Bearer JWT (Port 5000)*: Komunikasi stateless pengiriman data dan mutasi permohonan surat.
- *TCP/IP PostgreSQL Driver (Port 5432)*: Koneksi pooling data transaksi terisolasi via Docker bridge network.

#pagebreak()

// ==================== BAB VIII: HASIL FIGMA & UI/UX ====================
= BAB VIII: HASIL DESAIN FIGMA & SISTEM DESAIN (UI/UX)
_Standar Acuan: UI/UX Design System & Interface Showcase (Tugas 7 RPL)_

== 8.1 Tautan Publik Proyek Figma
Tautan resmi berkas desain antarmuka pengguna (UI/UX Mockup & Prototype):\
#text(fill: rgb("#1e40af"))[#link("https://www.figma.com/design/sipesat-unindra-kelompok-7")[https://www.figma.com/design/sipesat-unindra-kelompok-7]]

== 8.2 Palet Warna & Token Visual
Sistem mengadopsi palet institusional _Clean Institutional Modernism_:
- *Primary Navy (`#1C2434`)*: Latar belakang header institusi, sidebar navigasi utama, dan judul bab.
- *Royal Blue (`#1E6EEB`)*: Tombol aksi utama (Call to Action), tautan aktif, dan indikator stepper.
- *Emerald Green (`#10B981`)*: Status sukses (`DISETUJUI`), verifikasi berkas valid, dan cetak selesai.
- *Danger Rose (`#EF4444`)*: Status penolakan (`DITOLAK`) dan peringatan error berkas $> 2$ MB.
- *Slate Neutral (`#64748B`)*: Teks pendukung, border pemisah tabel, dan deskripsi formulir.

== 8.3 Ringkasan 8 Layar Mockup Utama
1. *Layar Login Dual-Role*: Autentikasi dengan tombol pintas akun demo Siswa dan Admin TU.
2. *Dashboard Siswa*: 4 kartu ringkasan status pengajuan dan tombol cepat buat permohonan.
3. *Formulir Pengajuan Surat Mandiri*: Dropdown dinamis dan area drag-and-drop file uploader (maks 2MB).
4. *Pelacakan Status Permohonan*: Horizontal Stepper 5 tahapan transparan dan tombol unduh PDF resmi.
5. *Dashboard Petugas Tata Usaha*: Antrean surat masuk, filter jenis surat, dan tanggal permohonan.
6. *Modal Verifikasi Dokumen & Disposisi*: Pratinjau berkas digital dan tombol Setuju / Tolak.
7. *Pratinjau Surat Resmi Hasil Cetak*: Kop surat sekolah, nomor otomatis, dan Tanda Tangan QR Code.
8. *Modul Laporan Rekapitulasi*: Penyaringan periode dan ekspor rekapitulasi ke format CSV/PDF.

#pagebreak()

// ==================== BAB IX: HASIL SISTEM & PENGUJIAN ====================
= BAB IX: HASIL IMPLEMENTASI SISTEM & BLACK BOX TESTING
_Standar Acuan: Konstruksi PL (Tugas 10) & Pengujian PL (Tugas 11 RPL)_

== 9.1 Konstruksi Arsitektur Perangkat Lunak
Sistem SIPESAT berhasil dibangun secara utuh dalam arsitektur monorepo terpisah:
- *Frontend (`fe/`)*: Next.js 14 App Router, TypeScript, Tailwind CSS, Lucide Icons.
- *Backend (`be/`)*: Node.js Express, TypeScript, Prisma ORM, JSON Web Token (JWT), Multer File Uploader, PDFKit.
- *Infrastruktur*: Container PostgreSQL 16 Alpine, skrip otomasi `start-local.bat` dan `migrate.bat`.

== 9.2 Hasil Pengujian Black Box Testing (35 Test Cases)
Pengujian fungsionalitas sistem dieksekusi menggunakan metode _Black Box Testing_ berstandar format akademik UNINDRA (Tugas 11):

#table(
  columns: (1.0cm, 5.5cm, 3.5cm, 4.5cm),
  align: (center, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Modul Pengujian]*], [*#text(fill: white)[Jumlah Skenario]*], [*#text(fill: white)[Status Pengujian]*]),
  [1], [Modul Autentikasi & RBAC Guard], [5 Skenario Uji], [100% VALID (Pass)],
  [2], [Modul Pengajuan Surat Siswa], [6 Skenario Uji], [100% VALID (Pass)],
  [3], [Modul Validasi Upload Berkas (2 MB)], [5 Skenario Uji], [100% VALID (Pass)],
  [4], [Modul Timeline Stepper Tracking], [4 Skenario Uji], [100% VALID (Pass)],
  [5], [Modul Verifikasi & Disposisi TU], [5 Skenario Uji], [100% VALID (Pass)],
  [6], [Modul Auto-Numbering & PDF QR TTE], [5 Skenario Uji], [100% VALID (Pass)],
  [7], [Modul Rekapitulasi & Ekspor Laporan], [5 Skenario Uji], [100% VALID (Pass)],
)

*Hasil Pengujian*: Seluruh 35 skenario pengujian berstatus *VALID (100% Lulus)* tanpa ditemukan _critical defect_, membuktikan bahwa perangkat lunak telah memenuhi seluruh kontrak spesifikasi kebutuhan SRS.

#pagebreak()

// ==================== BAB X: FILE PPT & PENUTUP ====================
= BAB X: MATERI PRESENTASI & PENUTUP

== 10.1 Ringkasan 12 Slide File Presentasi PowerPoint (.pptx)
Berkas presentasi PowerPoint resmi telah disusun dalam format widescreen 16:9 (`SIPESAT_PRESENTASI_KELOMPOK_7.pptx`) mencakup:
- *Slide 1*: Halaman Judul & Identitas Kelompok 7 UNINDRA.
- *Slide 2*: Latar Belakang Masalah Persuratan Manual Sekolah.
- *Slide 3*: Solusi SIPESAT & Nilai Tambah Digitalisasi.
- *Slide 4*: Ruang Lingkup Sistem & 2 Peran Pengguna (Siswa & TU).
- *Slide 5*: Spesifikasi Kebutuhan Perangkat Lunak (SRS Karl Wiegers / IEEE 830).
- *Slide 6*: Pemodelan Use Case Diagram (18 Use Cases & RBAC).
- *Slide 7*: Pemodelan Activity Diagram (Multi-Swimlane Siswa vs TU).
- *Slide 8*: Pemodelan Sequence Diagram (Pola BCE & Frame Alt).
- *Slide 9*: Pemodelan Class Diagram & Skema Relasional 3NF.
- *Slide 10*: Arsitektur Deployment Diagram 3-Tier & Container Docker.
- *Slide 11*: Implementasi Sistem & Black Box Testing (35/35 Test Cases Valid).
- *Slide 12*: Kesimpulan, Rekomendasi, dan Sesi Tanya Jawab (Q&A).

== 10.2 Tautan Repositori GitHub Proyek
Sesuai instruksi pengumpulan tugas besar, seluruh kode sumber, berkas diagram master (.drawio), dokumen laporan (.docx, .pdf, .md), dan file presentasi (.pptx) telah diarsipkan secara publik pada:

#align(center)[
  #v(0.3cm)
  #rect(width: 13cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt, fill: rgb("#f8fafc"))[
    #v(6pt)
    #text(size: 11pt, weight: "bold")[TAUTAN REPOSITORI GITHUB RESMI KELOMPOK 7:]\
    #text(size: 12pt, fill: rgb("#1e40af"))[#link("https://github.com/themodeid/Sipesat-RPL")[https://github.com/themodeid/Sipesat-RPL]]
    #v(6pt)
  ]
]

== 10.3 Kesimpulan
Perancangan dan implementasi Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) membuktikan bahwa otomatisasi persuratan digital di lingkungan sekolah dapat diwujudkan secara efektif melalui arsitektur yang terstruktur rapi. Seluruh 9 deliverables penugasan mata kuliah Rekayasa Perangkat Lunak telah terselesaikan dengan tuntas, terverifikasi, dan siap dipertanggungjawabkan pada evaluasi akademik.
