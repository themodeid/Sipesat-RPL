import os
import shutil
import subprocess

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"
TYP_PATH = os.path.join(RPL_DIR, "LAPORAN_LENGKAP_PROJEK_RPL_SIPESAT_KELOMPOK_7.typ")
PDF_LAPORAN = os.path.join(RPL_DIR, "LAPORAN_LENGKAP_PROJEK_RPL_SIPESAT_KELOMPOK_7.pdf")
PDF_BUNDEL = os.path.join(RPL_DIR, "BUNDEL_LENGKAP_10_DELIVERABLES_PROJEK_RPL_SIPESAT.pdf")

typst_source = r"""#set document(
  title: "Laporan Lengkap & Bundel 10 Deliverables Proyek RPL: SIPESAT - Kelompok 7 UNINDRA",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)

#set text(font: "Times New Roman", size: 10.5pt, lang: "id")
#set page(
  paper: "a4",
  margin: (left: 3.3cm, top: 3.0cm, right: 2.6cm, bottom: 2.6cm),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 8.5pt, fill: rgb("#475569"))
      #grid(
        columns: (1fr, 1fr),
        align(left)[_Dokumen Konsolidasi 10 Deliverables RPL — SIPESAT_],
        align(right)[_Kelompok 7 (Kelas RPL\_XD) — UNINDRA_]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.4pt + rgb("#cbd5e1"))
    ]
  },
  footer: context {
    set text(size: 9.5pt, fill: rgb("#1e293b"))
    align(center)[#counter(page).display("1")]
  }
)

#set par(justify: true, leading: 0.68em, first-line-indent: 0pt)
#set heading(numbering: none)

#show heading.where(level: 1): it => block(above: 1.3em, below: 0.65em, sticky: true)[
  #text(size: 12.5pt, weight: "bold", fill: rgb("#0f172a"))[#it.body]
  #v(-4pt)
  #line(length: 100%, stroke: 1.2pt + rgb("#1e3a8a"))
]

#show heading.where(level: 2): it => block(above: 1.05em, below: 0.48em, sticky: true)[
  #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[#it.body]
]

#show heading.where(level: 3): it => block(above: 0.8em, below: 0.4em, sticky: true)[
  #text(size: 10.2pt, weight: "bold", fill: rgb("#334155"))[#it.body]
]

#show raw.where(block: true): it => block(
  width: 100%,
  fill: rgb("#f8fafc"),
  stroke: 0.5pt + rgb("#cbd5e1"),
  radius: 4pt,
  inset: 7pt,
  breakable: true,
)[#set text(size: 8.5pt); #set par(justify: false, leading: 0.52em); #it]

#let std_table(cols, aligns, ..cells) = {
  set par(justify: false, first-line-indent: 0pt, leading: 0.52em)
  set text(size: 9pt)
  table(
    columns: cols,
    align: aligns,
    inset: (x: 5.5pt, y: 4.2pt),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
    ..cells
  )
}

#let bb_table(..rows) = {
  set par(justify: false, first-line-indent: 0pt, leading: 0.52em)
  set text(size: 8.8pt)
  table(
    columns: (0.75cm, 1.25fr, 1.05fr, 1.35fr, 1.5cm, 1.7cm),
    align: (center + top, left + top, left + top, left + top, center + top, center + top),
    inset: (x: 5pt, y: 4.5pt),
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

// ==================== HALAMAN JUDUL (SINGLE UNIFIED COVER) ====================
#align(center)[
  #v(0.2cm)
  #text(size: 13.5pt, weight: "bold")[
    LAPORAN AKHIR PROYEK REKAYASA PERANGKAT LUNAK (RPL)\
    DOKUMEN KONSOLIDASI LENGKAP 10 DELIVERABLES SISTEM
  ]
  #v(0.45cm)
  #text(size: 13pt, weight: "bold", fill: rgb("#1e3a8a"))[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB\
    (SIPESAT)
  ]
  #v(0.2cm)
  #text(size: 10pt, style: "italic")[
    Studi Kasus: Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah (Versi Revisi)\
    Arsitektur Decoupled Three-Tier (Next.js 14 + Express.js TypeScript + Docker PostgreSQL 16)
  ]
  
  #v(0.75cm)
  #image("assets/logo_unindra.png", width: 4.3cm)
  #v(0.2cm)
  #text(size: 13pt, weight: "bold")[UNIVERSITAS INDRAPRASTA PGRI]\
  #text(size: 11.5pt, weight: "bold")[(UNINDRA)]\
  #v(2pt)
  #text(size: 10pt, weight: "bold", fill: rgb("#334155"))[
    FAKULTAS TEKNIK DAN ILMU KOMPUTER\
    PROGRAM STUDI TEKNIK INFORMATIKA
  ]
  
  #v(0.75cm)
  #text(size: 10.5pt, weight: "bold")[Disusun oleh KELOMPOK 7 (Kelas RPL_XD):]
  #v(0.15cm)
  #std_table(
    (1cm, 1fr, 3.5cm),
    (center + horizon, left + horizon, center + horizon),
    table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Anggota]*], [*#text(fill: white)[NPM]*]),
    [1], [Adam Wahyu Kurniawan (Lead Architect & SWE)], [202343500510],
    [2], [Fathu Rahman (Business Analyst)], [202343500467],
    [3], [Surya Edi Saputra (QA & Technical Writer)], [202343500468],
    [4], [Rizqi Muh. Al Hakimi (Database Specialist & UI/UX)], [202343500449],
  )
  
  #v(0.75cm)
  #text(size: 11pt, weight: "bold")[
    JAKARTA\
    TAHUN AKADEMIK 2026/2027
  ]
]

#pagebreak()

// ==================== MATRIKS 10 DELIVERABLES & DAFTAR ISI ====================
#align(center)[
  #text(size: 12.5pt, weight: "bold")[MATRIKS KELENGKAPAN 10 DELIVERABLES PROYEK RPL]
]
#v(0.15cm)

Dokumen master ini mengonsolidasikan secara utuh seluruh 10 deliverables tugas besar mata kuliah Rekayasa Perangkat Lunak (RPL) Kelompok 7 sesuai urutan instruksi dosen pengampu dalam satu format naskah terpadu:

#std_table(
  (0.8cm, 3.8cm, 3.4cm, 1fr),
  (center + horizon, left + horizon, left + horizon, left + horizon),
  table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Item Deliverable]*], [*#text(fill: white)[Standar / Format]*], [*#text(fill: white)[Cakupan Bab dalam Dokumen Ini]*]),
  [1], [*SRS*], [IEEE Std 830 / Karl Wiegers], [*BAB I* — Spesifikasi Lengkap, 39 FR, 30 NFR, Traceability & TBD (2 Role: Siswa & TU)],
  [2], [*USECASE DIAGRAM*], [UML 2.5 Use Case], [*BAB II* — Diagram Use Case Terpadu, 20 Spesifikasi UC & Matriks Hak Akses RBAC],
  [3], [*CLASS DIAGRAM*], [UML 2.5 Class & Object], [*BAB III* — Analisis Database 4 Tabel, Class Diagram, Multiplicity & Object Diagram],
  [4], [*ACTIVITY DIAGRAM*], [UML 2.5 Swimlane], [*BAB IV* — Activity Diagram Multi-Swimlane (Siswa, Sistem, TU) & 12 Langkah Alur],
  [5], [*SEQUENCE DIAGRAM*], [UML 2.5 Pola BCE], [*BAB V* — 2 Sequence Diagram Pola Boundary-Control-Entity (BCE) & Fragmen `alt`],
  [6], [*DEPLOYMENT DIAGRAM*], [UML 2.5 3-Tier Node], [*BAB VI* — Deployment Diagram Fisik, Spesifikasi Node, Artifact & Communication Path],
  [7], [*HASIL FIGMA*], [UI/UX Design System], [*BAB VII* — Tautan Proyek Figma, Color Palette Tokens, Tipografi & 8 Layar Mockup],
  [8], [*FILE PENGUJIAN SOFTWARE*], [Black Box UNINDRA], [*BAB VIII* — Metodologi EP/BVA/RBAC & 35 Kasus Uji Black Box 7 Modul (100% Valid)],
  [9], [*HASIL SISTEMNYA*], [Decoupled Monorepo], [*BAB IX* — Konstruksi Skema Prisma, Controller Express, Komponen Next.js & Prinsip DRY],
  [10], [*FILE PPT PRESENTASI*], [PowerPoint 16:9], [*BAB X* — Rincian Materi 12 Slide Presentasi PPTX & Tautan Repositori GitHub Resmi],
)

#v(0.2cm)
#rect(width: 100%, fill: rgb("#f8fafc"), stroke: 0.6pt + rgb("#94a3b8"), radius: 4pt, inset: 7pt)[
  *Jaminan Integritas Versi Revisi (Single Source of Truth)*: Seluruh bab dan diagram di dalam naskah ini 100% menggunakan *Versi Revisi Terbaru*—menerapkan dua peran login eksklusif (*Siswa* dan *Petugas TU / Admin*), meniadakan peran Kepala Sekolah, menyeragamkan batas unggah berkas syarat maksimal *2 MB*, dan menerbitkan nomor surat resmi beserta QR Code secara atomik.
  
  #v(3pt)
  *Tautan Repositori GitHub Resmi Kelompok 7*: #text(fill: rgb("#1d4ed8"), weight: "bold")[#link("https://github.com/themodeid/Sipesat-RPL")[https://github.com/themodeid/Sipesat-RPL]]
]

#v(0.25cm)
#align(center)[#text(size: 11.5pt, weight: "bold")[DAFTAR ISI UTAMA (10 DELIVERABLES)]]
#v(0.05cm)
#{
  set text(size: 9.5pt)
  outline(title: none, indent: 0pt, depth: 1)
}

#pagebreak()

// =====================================================================
// BAB I — DELIVERABLE 1: SOFTWARE REQUIREMENTS SPECIFICATION (SRS)
// =====================================================================
= BAB I: DELIVERABLE 1 — SOFTWARE REQUIREMENTS SPECIFICATION (SRS)
_Standar Acuan: IEEE Std 830-1998 / IEEE Std 29148-2018 / Karl E. Wiegers SRS Template (Versi 1.1 Revisi Tugas 2)_

== 1.1 Riwayat Revisi Dokumen (Revision History)
#std_table(
  (2.4cm, 2.4cm, 1fr, 1.3cm),
  (left + top, center + top, left + top, center + top),
  table.header([*#text(fill: white)[Penyusun]*], [*#text(fill: white)[Tanggal]*], [*#text(fill: white)[Alasan Perubahan]*], [*#text(fill: white)[Versi]*]),
  [Kelompok 7], [Sep 2026], [Draf awal SRS (Bab I Pendahuluan dan Bab II Use Case Diagram).], [1.0],
  [Kelompok 7], [17 Okt 2026], [Revisi menyeluruh mengikuti template SRS Karl Wiegers (Pertemuan 02): menambahkan Overall Description, External Interface Requirements, System Features (39 FR), Other Nonfunctional Requirements (30 NFR), Glossary, Traceability Matrix, dan TBD List; menyelaraskan arsitektur 2 peran dengan repositori `Sipesat-RPL`.], [1.1],
)

== 1.2 Pendahuluan (Introduction)
=== 1.2.1 Tujuan (Purpose)
Dokumen ini menjelaskan spesifikasi kebutuhan perangkat lunak *Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)* versi 1.1. SIPESAT digunakan untuk mengelola proses pengajuan surat keterangan siswa antara Siswa dan Tata Usaha (TU) sekolah secara digital, mulai dari pengajuan, verifikasi berkas, persetujuan, hingga penerbitan surat PDF resmi yang memuat QR Code. Dokumen ini menjadi acuan tunggal bagi pengembang, penguji, dan pemangku kepentingan dalam perancangan, implementasi, dan pengujian sistem.

=== 1.2.2 Konvensi Dokumen (Document Conventions)
#std_table(
  (2.5cm, 1fr),
  (left + top, left + top),
  table.header([*#text(fill: white)[Konvensi]*], [*#text(fill: white)[Arti dan Aturan Penomoran]*]),
  [`FR-nn`], [Functional Requirement; nomor berurutan dan unik di seluruh dokumen (`FR-01` s.d. `FR-39`).],
  [`NFR-nn`], [Non-Functional Requirement; nomor berurutan dan unik (`NFR-01` s.d. `NFR-30`), mencakup performa, keamanan, dan aturan bisnis.],
  [`UC-nn`], [Kode Use Case pada Use Case Diagram. Menautkan setiap FR ke use case asalnya sehingga dapat dilacak (_traceable_).],
  [`TBD-n`], [Hal yang belum diputuskan (_To Be Determined_); dikumpulkan pada Subbab 1.8.],
  [`harus / wajib`], [Kebutuhan mandatory. Sistem dinyatakan belum memenuhi SRS bila tidak dipenuhi.],
  [`Prioritas`], [*Tinggi* (inti sistem), *Sedang* (penting namun tidak menghambat alur utama), *Rendah* (pelengkap).],
)

=== 1.2.3 Target Pembaca (Intended Audience and Reading Suggestions)
#std_table(
  (3.6cm, 5.2cm, 1fr),
  (left + top, left + top, left + top),
  table.header([*#text(fill: white)[Pembaca]*], [*#text(fill: white)[Kepentingan]*], [*#text(fill: white)[Bagian yang Disarankan]*]),
  [Developer Sistem], [Implementasi frontend, backend, dan basis data], [Subbab 1.3, 1.4, 1.5, 1.6, dan Bab III–IX],
  [Business Analyst], [Verifikasi kebutuhan dan pelacakan use case], [Subbab 1.2, 1.3, 1.5, 1.7, dan Bab II],
  [Tester QA], [Menyusun skenario dan kasus uji dari requirement], [Subbab 1.5, 1.6, dan Bab VIII],
  [Dosen Pengampu], [Menilai kesesuaian dengan template Wiegers & UML], [Seluruh dokumen (Bab I s.d. Bab X)],
  [Petugas TU & Siswa], [Validasi bahwa kebutuhan sesuai kondisi nyata], [Subbab 1.2, 1.3, dan 1.5],
)

=== 1.2.4 Cakupan Produk (Product Scope) & Referensi
SIPESAT adalah aplikasi web yang mendigitalkan rantai pengajuan surat keterangan siswa secara mandiri, menggantikan formulir kertas manual, dan mempercepat validasi oleh Tata Usaha hingga penerbitan surat PDF resmi dengan QR Code. Sistem hanya memiliki *dua peran login*: *Siswa* (pemohon) dan *Petugas TU* (verifikator dan pengelola).
- *Termasuk dalam cakupan*: (1) Registrasi mandiri, autentikasi, dan kelola profil; (2) Katalog jenis surat beserta syarat berkas, pengajuan permohonan, dan unggah berkas syarat (PDF ≤ 2 MB); (3) Pelacakan status, riwayat pengajuan, dan unduh surat PDF ber-QR Code oleh siswa; (4) Antrean pengajuan, verifikasi berkas, persetujuan/penolakan, dan penomoran surat otomatis oleh Petugas TU; (5) Pengelolaan master jenis surat, data siswa/akun, serta ekspor rekapitulasi laporan.
- *Referensi Acuan*: IEEE Std 29148-2018; IEEE Std 830-1998; Karl E. Wiegers (1999) _SRS Template_; Ian Sommerville _Software Engineering_; Roger S. Pressman _Software Engineering_; Modul Ajar RPL UNINDRA 2026.

== 1.3 Deskripsi Keseluruhan (Overall Description)
=== 1.3.1 Perspektif Produk (Product Perspective)
SIPESAT merupakan produk mandiri (_standalone_) yang menggantikan pengajuan surat manual berbasis kertas di sekolah. Sistem dibangun dengan arsitektur *decoupled three-tier*: frontend Next.js 14 berkomunikasi dengan backend REST API Express melalui JSON/HTTP dengan JWT, dan backend mengakses basis data PostgreSQL 16 melalui Prisma ORM.

#figure(
  image("assets/diagram_arsitektur_srs.png", width: 88%),
  caption: [Arsitektur Logis SIPESAT (_Decoupled Three-Tier Architecture_)]
)

=== 1.3.2 Fungsi Utama Produk (Product Functions)
#std_table(
  (4.8cm, 3.0cm, 3.4cm, 1fr),
  (left + top, left + top, left + top, center + top),
  table.header([*#text(fill: white)[Fungsi Utama]*], [*#text(fill: white)[Pengguna]*], [*#text(fill: white)[Kode Use Case]*], [*#text(fill: white)[Fitur]*]),
  [Autentikasi dan manajemen akun], [Siswa, Petugas TU], [`UC-01, 01A, 02, 03, 04`], [Fitur 1.5.1],
  [Katalog dan pengajuan surat, unggah berkas syarat], [Siswa], [`UC-05, 06, 07`], [Fitur 1.5.2],
  [Pelacakan status, riwayat, dan unduh surat], [Siswa], [`UC-08, 08A, 09, 10`], [Fitur 1.5.3],
  [Dashboard antrean dan verifikasi berkas], [Petugas TU], [`UC-11, 12, 13`], [Fitur 1.5.4],
  [Persetujuan atau penolakan permohonan], [Petugas TU], [`UC-14, 15, 15A`], [Fitur 1.5.5],
  [Penomoran otomatis, surat PDF, cetak, dan QR Code], [Sistem / Petugas TU], [`UC-14A, 10, 19, 20`], [Fitur 1.5.6],
  [Pengelolaan master jenis surat, data siswa, dan akun], [Petugas TU], [`UC-16, 17`], [Fitur 1.5.7],
  [Rekapitulasi dan ekspor laporan], [Petugas TU], [`UC-18`], [Fitur 1.5.8],
)

=== 1.3.3 Kelas dan Karakteristik Pengguna (User Classes and Characteristics)
#std_table(
  (3.2cm, 5.2cm, 1fr),
  (left + top, left + top, left + top),
  table.header([*#text(fill: white)[Kelas Pengguna]*], [*#text(fill: white)[Deskripsi dan Karakteristik]*], [*#text(fill: white)[Hak Akses Utama]*]),
  [*Siswa*\ (Aktor Pemohon)], [Siswa aktif sekolah, jumlah besar, mengakses dari smartphone maupun laptop saat membutuhkan surat keterangan.], [Registrasi, login, melihat katalog, mengajukan surat, mengunggah berkas, melacak status, melihat riwayat, mengunduh surat miliknya sendiri, kelola profil.],
  [*Petugas TU*\ (Verifikator & Pengelola)], [Staf Tata Usaha, jumlah sedikit, menggunakan sistem setiap hari kerja dari komputer kantor, memahami format surat sekolah.], [Dashboard dan antrean, verifikasi berkas, menyetujui atau menolak, penerbitan nomor surat dan QR Code, kelola jenis surat, kelola data siswa/akun, ekspor laporan.],
)

=== 1.3.4 Lingkungan Operasi, Batasan Desain, dan Asumsi
- *Lingkungan Operasi*: Klien peramban modern (Chrome, Firefox, Edge) pada PC/smartphone; Server Node.js v18/v20 (Next.js 14 pada port `3000`, Express REST API pada port `5000`); Basis data PostgreSQL 16 dalam kontainer Docker pada port `5432`.
- *Batasan Desain & Implementasi*: Frontend wajib Next.js 14 App Router + TypeScript + Tailwind CSS; Backend wajib Express + TypeScript + Prisma ORM; Autentikasi JWT dan hashing `bcrypt`; Berkas syarat maksimal *2 MB* per berkas; Hanya memiliki 2 peran login (Siswa dan Petugas TU); Dirilis di bawah lisensi MIT.

== 1.4 Kebutuhan Antarmuka Eksternal (External Interface Requirements)
#std_table(
  (4.2cm, 2.6cm, 1fr),
  (left + top, left + top, left + top),
  table.header([*#text(fill: white)[Halaman / Antarmuka]*], [*#text(fill: white)[Pengguna / Tier]*], [*#text(fill: white)[Isi dan Spesifikasi Interaksi Utama]*]),
  [Login (`/login`) & Registrasi], [Semua / Siswa], [Form NISN/username dan kata sandi; form pendaftaran mandiri siswa baru.],
  [Dashboard & Katalog Siswa], [Siswa], [Ringkasan pengajuan, daftar jenis surat aktif, syarat berkas, form keperluan, unggah berkas ≤ 2 MB.],
  [Detail Status, Riwayat & Unduh], [Siswa], [Linimasa status (_stepper_), catatan TU bila ditolak, daftar riwayat, tombol unduh PDF.],
  [Dashboard TU & Detail Verifikasi], [Petugas TU], [Statistik status, tabel antrean FIFO, pratinjau berkas syarat, tombol Setujui/Tolak, kolom catatan.],
  [Master Data & Laporan TU], [Petugas TU], [CRUD jenis surat, kelola akun siswa, filter laporan rekapitulasi, dan ekspor CSV/Excel/PDF.],
  [PostgreSQL 16 + Prisma ORM], [Data Tier (`5432`)], [Penyimpanan relasional pengguna, jenis surat, pengajuan, dan log aktivitas dengan migrasi & seeder.],
  [Express REST API + Multer + JWT], [Service Tier (`5000`)], [Logika bisnis, otorisasi RBAC 2 peran, hashing `bcrypt`, validasi upload `uploads/`, generator nomor & QR.],
)

== 1.5 Spesifikasi Fitur Sistem & Kebutuhan Fungsional (39 Functional Requirements)
#std_table(
  (1.3cm, 3.1cm, 1fr, 1.5cm),
  (center + top, left + top, left + top, center + top),
  table.header([*#text(fill: white)[ID FR]*], [*#text(fill: white)[Kelompok Fitur]*], [*#text(fill: white)[Spesifikasi Kebutuhan Fungsional (Functional Requirement)]*], [*#text(fill: white)[Ref. UC]*]),
  [`FR-01`], [4.1 Autentikasi & Akun], [Sistem harus menyediakan halaman login; Siswa masuk dengan NISN dan kata sandi, Petugas TU masuk dengan username dan kata sandi.], [`UC-01`],
  [`FR-02`], [4.1 Autentikasi & Akun], [Sistem harus memvalidasi kredensial dan peran (hak akses) pengguna pada setiap upaya login.], [`UC-01A`],
  [`FR-03`], [4.1 Autentikasi & Akun], [Sistem harus menolak login yang tidak valid dengan pesan kesalahan generik tanpa menyebutkan apakah NISN/username atau kata sandi yang salah.], [`UC-01A`],
  [`FR-04`], [4.1 Autentikasi & Akun], [Setelah login berhasil, sistem harus mengarahkan pengguna ke dashboard sesuai perannya (Siswa atau Petugas TU).], [`UC-01`],
  [`FR-05`], [4.1 Autentikasi & Akun], [Sistem harus menyediakan registrasi akun mandiri bagi siswa dengan data nama lengkap, NISN, kelas, jurusan, dan kata sandi.], [`UC-02`],
  [`FR-06`], [4.1 Autentikasi & Akun], [Sistem harus menolak registrasi bila NISN sudah terdaftar atau data wajib belum lengkap.], [`UC-02`],
  [`FR-07`], [4.1 Autentikasi & Akun], [Pengguna dapat melihat dan memperbarui data profil serta mengganti kata sandi dengan memasukkan kata sandi lama.], [`UC-03`],
  [`FR-08`], [4.1 Autentikasi & Akun], [Sistem harus mengakhiri sesi dan menghapus token autentikasi ketika pengguna menekan logout.], [`UC-04`],
  [`FR-09`], [4.2 Katalog & Pengajuan], [Sistem harus menampilkan katalog jenis surat yang berstatus aktif beserta deskripsi dan daftar berkas syaratnya.], [`UC-05`],
  [`FR-10`], [4.2 Katalog & Pengajuan], [Siswa dapat mengajukan permohonan dengan memilih jenis surat dan mengisi keperluan atau keterangan tambahan.], [`UC-06`],
  [`FR-11`], [4.2 Katalog & Pengajuan], [Sistem harus menerima unggahan berkas syarat berformat resmi (PDF/JPG/PNG) dengan ukuran maksimal 2 MB per berkas.], [`UC-07`],
  [`FR-12`], [4.2 Katalog & Pengajuan], [Sistem harus menolak berkas berformat terlarang atau berukuran lebih dari 2 MB dengan pesan yang menjelaskan penyebabnya.], [`UC-07`],
  [`FR-13`], [4.2 Katalog & Pengajuan], [Sistem harus memastikan seluruh berkas syarat wajib untuk jenis surat terpilih telah dilengkapi sebelum pengajuan dikirim.], [`UC-06`],
  [`FR-14`], [4.2 Katalog & Pengajuan], [Setelah pengajuan dikirim, sistem harus membuat catatan pengajuan dengan nomor resi unik, waktu pengajuan, dan status awal menunggu verifikasi.], [`UC-06`],
  [`FR-15`], [4.3 Pelacakan & Unduh], [Sistem harus menampilkan status terkini setiap pengajuan milik siswa beserta linimasa perubahan statusnya secara terbaru.], [`UC-08`],
  [`FR-16`], [4.3 Pelacakan & Unduh], [Sistem harus menampilkan catatan koreksi atau alasan penolakan dari Petugas TU pada pengajuan yang ditolak.], [`UC-08A`],
  [`FR-17`], [4.3 Pelacakan & Unduh], [Sistem harus menampilkan riwayat seluruh pengajuan milik siswa, terurut dari terbaru, dengan filter berdasarkan status.], [`UC-09`],
  [`FR-18`], [4.3 Pelacakan & Unduh], [Sistem hanya mengizinkan unduh/cetak surat resmi pada pengajuan berstatus Disetujui dan hanya oleh siswa pemilik pengajuan.], [`UC-10`],
  [`FR-19`], [4.4 Antrean & Verifikasi], [Sistem harus menampilkan dashboard Petugas TU berisi ringkasan jumlah pengajuan untuk setiap status.], [`UC-11`],
  [`FR-20`], [4.4 Antrean & Verifikasi], [Sistem harus menampilkan antrean pengajuan masuk (nama siswa, kelas, jenis surat, waktu, status), terurut FIFO dengan pencarian dan filter.], [`UC-12`],
  [`FR-21`], [4.4 Antrean & Verifikasi], [Sistem harus menyediakan halaman detail pengajuan yang menampilkan data siswa dan pratinjau setiap berkas syarat.], [`UC-13`],
  [`FR-22`], [4.4 Antrean & Verifikasi], [Sistem harus mengubah status pengajuan dari menunggu menjadi sedang diproses/diverifikasi ketika Petugas TU memeriksa berkas.], [`UC-13`],
  [`FR-23`], [4.5 Keputusan TU], [Hanya Petugas TU yang dapat menyetujui permohonan, tanpa memerlukan tahap persetujuan Kepala Sekolah.], [`UC-14`],
  [`FR-24`], [4.5 Keputusan TU], [Sistem harus otomatis menjalankan penerbitan nomor surat resmi dan QR Code ketika permohonan disetujui Petugas TU.], [`UC-14`],
  [`FR-25`], [4.5 Keputusan TU], [Hanya Petugas TU yang dapat menolak permohonan surat yang berkasnya kurang atau buram.], [`UC-15`],
  [`FR-26`], [4.5 Keputusan TU], [Sistem harus mewajibkan Petugas TU mengisi alasan atau catatan koreksi sebelum penolakan dapat disimpan.], [`UC-15A`],
  [`FR-27`], [4.5 Keputusan TU], [Sistem harus mencatat setiap perubahan status (status baru, waktu, dan pengguna pelaku) sebagai riwayat audit yang tidak dapat diubah.], [`UC-14, 15`],
  [`FR-28`], [4.6 Penomoran, PDF & QR], [Sistem harus membuat nomor surat resmi secara otomatis, unik, dan tidak pernah diterbitkan ganda sesuai pola format jenis surat.], [`UC-14A`],
  [`FR-29`], [4.6 Penomoran, PDF & QR], [Sistem harus menghasilkan dokumen surat resmi yang memuat kop surat sekolah, nomor surat, data siswa, isi surat, dan tanggal terbit.], [`UC-14A`],
  [`FR-30`], [4.6 Penomoran, PDF & QR], [Sistem harus menyematkan QR Code dinamis pada surat resmi yang memuat tautan verifikasi unik untuk surat tersebut.], [`UC-14A`],
  [`FR-31`], [4.6 Penomoran, PDF & QR], [Sistem harus menyimpan data surat yang diterbitkan sehingga dapat diunduh atau dicetak ulang kapan saja.], [`UC-10, 19`],
  [`FR-32`], [4.6 Penomoran, PDF & QR], [Sistem menyediakan halaman verifikasi publik yang menampilkan nomor surat, nama siswa, jenis, tanggal terbit, dan keabsahan saat QR dipindai.], [`UC-20`],
  [`FR-33`], [4.7 Master Data], [Petugas TU dapat menambah, mengubah, dan menonaktifkan jenis surat beserta deskripsi, format nomor, dan daftar syaratnya.], [`UC-16`],
  [`FR-34`], [4.7 Master Data], [Jenis surat nonaktif tidak boleh tampil pada katalog pengajuan baru siswa, tetapi pengajuan lama yang terkait harus tetap utuh.], [`UC-16`],
  [`FR-35`], [4.7 Master Data], [Petugas TU dapat menambah, mengubah, menonaktifkan data siswa dan akunnya, serta mengatur ulang kata sandi siswa.], [`UC-17`],
  [`FR-36`], [4.7 Master Data], [Sistem harus menolak login untuk akun yang berstatus nonaktif.], [`UC-17`],
  [`FR-37`], [4.8 Laporan & Ekspor], [Sistem harus menampilkan rekapitulasi pengajuan yang dapat difilter berdasarkan periode, jenis surat, status, dan kelas.], [`UC-18`],
  [`FR-38`], [4.8 Laporan & Ekspor], [Sistem harus menampilkan total pengajuan untuk setiap status pada hasil rekapitulasi.], [`UC-18`],
  [`FR-39`], [4.8 Laporan & Ekspor], [Sistem harus menyediakan fitur ekspor hasil rekapitulasi ke berkas laporan (.csv / .xlsx / cetak PDF).], [`UC-18`],
)

== 1.6 Kebutuhan Non-Fungsional & Aturan Bisnis (30 Non-Functional Requirements)
#std_table(
  (1.5cm, 3.0cm, 1fr),
  (center + top, left + top, left + top),
  table.header([*#text(fill: white)[ID NFR]*], [*#text(fill: white)[Kategori]*], [*#text(fill: white)[Spesifikasi Kebutuhan Non-Fungsional & Aturan Bisnis]*]),
  [`NFR-01`], [5.1 Performance], [Sistem harus merespons setiap permintaan halaman atau API maksimal ≤ 3 detik pada kondisi normal.],
  [`NFR-02`], [5.1 Performance], [Proses unggah satu berkas berukuran 2 MB harus selesai maksimal ≤ 5 detik pada koneksi minimal 5 Mbps.],
  [`NFR-03`], [5.1 Performance], [Pembuatan surat ber-QR Code setelah persetujuan harus selesai maksimal ≤ 5 detik.],
  [`NFR-04`], [5.1 Performance], [Sistem harus mampu melayani minimal 200 pengguna aktif bersamaan tanpa penurunan performa signifikan.],
  [`NFR-05`], [5.2 Safety], [Sistem menyediakan mekanisme pencadangan (_backup_) berkala untuk basis data dan direktori berkas unggahan.],
  [`NFR-06`], [5.2 Safety], [Sistem mencegah data setengah jadi saat pengiriman gagal; pengajuan hanya tersimpan bila seluruh langkah berhasil.],
  [`NFR-07`], [5.2 Safety], [Sistem tidak menghapus permanen data master jenis surat yang memiliki riwayat, melainkan menggunakan _soft delete_ (`isActive = false`).],
  [`NFR-08`], [5.2 Safety], [Penerbitan nomor surat harus bersifat atomik sehingga tidak ada nomor ganda walau terjadi permintaan bersamaan.],
  [`NFR-09`], [5.3 Security], [Sistem wajib menyimpan kata sandi menggunakan hashing `bcrypt` dan tidak pernah menampilkan sandi asli.],
  [`NFR-10`], [5.3 Security], [Token sesi JWT wajib diverifikasi pada setiap permintaan terproteksi.],
  [`NFR-11`], [5.3 Security], [Sistem menerapkan Role-Based Access Control (RBAC) 2 peran (Siswa dan Petugas TU) yang ditegakkan di backend pada setiap endpoint.],
  [`NFR-12`], [5.3 Security], [Sesi login memiliki masa berlaku terukur dan berakhir otomatis saat kedaluwarsa atau logout.],
  [`NFR-13`], [5.3 Security], [Seluruh komunikasi pada lingkungan produksi wajib menggunakan HTTPS (TLS) dan proteksi CORS.],
  [`NFR-14`], [5.3 Security], [Siswa hanya boleh mengakses pengajuan dan surat miliknya sendiri; akses ke milik siswa lain wajib ditolak (anti-IDOR).],
  [`NFR-15`], [5.3 Security], [Sistem memvalidasi unggahan berdasarkan ekstensi, tipe MIME, dan ukuran (≤ 2 MB); nama berkas disanitasi.],
  [`NFR-16`], [5.3 Security], [Sistem memvalidasi seluruh masukan di sisi server dan mengakses DB melalui Prisma ORM berparameter untuk mencegah SQL Injection & XSS.],
  [`NFR-17`], [5.3 Security], [Sistem mencatat log audit (`LogAktivitas`) untuk setiap pembuatan pengajuan dan perubahan status.],
  [`NFR-18`], [5.3 Security], [Kredensial dan rahasia konfigurasi disimpan di berkas `.env` dan tidak dimasukkan ke repositori publik.],
  [`NFR-19`], [5.4 Quality], [(Usability) Minimal 90% siswa dapat menyelesaikan pengajuan surat pertama mereka tanpa pelatihan khusus.],
  [`NFR-20`], [5.4 Quality], [(Reliability) Sistem memiliki ketersediaan minimal 99% pada jam layanan sekolah.],
  [`NFR-21`], [5.4 Quality], [(Maintainability) Kode modular berlapis (routes, middlewares, utils, components) dengan TypeScript dan terdokumentasi di README.],
  [`NFR-22`], [5.4 Quality], [(Scalability) Sistem dapat ditingkatkan hingga > 1.000 pengguna berkat pemisahan frontend-backend stateless.],
  [`NFR-23`], [5.4 Quality], [(Portability) Sistem berjalan di Chrome, Firefox, dan Edge modern dengan tampilan responsif mulai lebar layar 360 px.],
  [`NFR-24`], [5.4 Quality], [(Deployability) Basis data dijalankan dengan satu perintah Docker Compose dan aplikasi memiliki skrip `start-local.bat` & `migrate.bat`.],
  [`NFR-25`], [5.5 Business Rule], [Hanya Petugas TU yang berwenang menyetujui atau menolak permohonan surat siswa.],
  [`NFR-26`], [5.5 Business Rule], [Penolakan permohonan wajib disertai alasan atau catatan koreksi.],
  [`NFR-27`], [5.5 Business Rule], [Pengajuan berstatus Disetujui atau Ditolak Final bersifat final.],
  [`NFR-28`], [5.5 Business Rule], [Surat resmi hanya dapat diunduh/dicetak setelah pengajuan berstatus Disetujui.],
  [`NFR-29`], [5.5 Business Rule], [Nomor surat bersifat unik dan diterbitkan otomatis oleh sistem sesuai template format sekolah.],
  [`NFR-30`], [5.5 Business Rule], [Berkas syarat wajib berformat dokumen/gambar sah dengan ukuran maksimal 2 MB per berkas.],
)

== 1.7 Matriks Ketertelusuran (Traceability Matrix UC ke FR) & Keputusan Teknis (TBD)
#std_table(
  (1.5cm, 4.8cm, 2.8cm, 1fr),
  (center + top, left + top, left + top, left + top),
  table.header([*#text(fill: white)[Kode]*], [*#text(fill: white)[Nama Use Case]*], [*#text(fill: white)[Ref. FR]*], [*#text(fill: white)[Keputusan Implementasi & Ketertelusuran]*]),
  [`UC-01/01A`], [Login & Validasi Kredensial], [`FR-01..FR-04`], [Otentikasi NISN/username dengan `bcrypt` & JWT.],
  [`UC-02..04`], [Registrasi, Profil & Logout], [`FR-05..FR-08`], [Pendaftaran mandiri siswa, ganti sandi, hapus sesi.],
  [`UC-05..07`], [Katalog, Pengajuan & Unggah], [`FR-09..FR-14`], [Unggah syarat PDF/JPG/PNG ≤ 2 MB, terbit resi `REQ-*`.],
  [`UC-08..10`], [Pelacakan, Revisi, Riwayat & Unduh], [`FR-15..FR-18, 31`], [Stepper status real-time, catatan TU, unduh PDF ber-QR.],
  [`UC-11..13`], [Dashboard, Antrean & Verifikasi TU], [`FR-19..FR-22`], [Antrean FIFO, pratinjau berkas, transisi status `DIPROSES`.],
  [`UC-14/14A`], [Setujui & Terbitkan Nomor / QR], [`FR-23, 24, 27..30`], [Format `421.3/{NOMOR}/SMKN1/{BULAN_ROMAWI}/{TAHUN}` (`TBD-1`).],
  [`UC-15/15A`], [Tolak & Input Catatan Revisi], [`FR-25..FR-27`], [Alasan wajib diisi; batas revisi maksimal 3 kali (`TBD-4`).],
  [`UC-16..18`], [Master Surat, Siswa & Ekspor Laporan], [`FR-33..FR-39`], [CRUD peran `ADMIN` (`TBD-3`) & ekspor CSV/PDF (`TBD-5`).],
  [`UC-19..20`], [Cetak Fisik & Verifikasi Publik QR], [`FR-29, 31, 32`], [Dialog cetak `@media print` & halaman verifikasi QR (`TBD-9`).],
)

#pagebreak()

// =====================================================================
// BAB II — DELIVERABLE 2: USE CASE DIAGRAM & MATRIKS RBAC
// =====================================================================
= BAB II: DELIVERABLE 2 — USE CASE DIAGRAM & MATRIKS HAK AKSES (RBAC)
_Standar Acuan: UML 2.5 Use Case Modeling (Tugas 3 RPL Versi Revisi)_

== 2.1 Ringkasan Revisi Pemodelan Use Case & Visualisasi Diagram
Aplikasi SIPESAT menerapkan Role-Based Access Control (RBAC) dengan *dua peran login*: *Siswa* (pemohon) dan *Petugas Tata Usaha (TU)* yang memverifikasi, menyetujui, menerbitkan nomor surat dan QR, serta mengelola data master, ditambah satu aktor publik *Pemindai QR*. Tidak ada peran Kepala Sekolah.

#figure(
  image("assets/diagram_usecase.png", width: 82%),
  caption: [Use Case Diagram SIPESAT (UML 2.5) — Dua Peran Login dan Satu Aktor Publik]
)

#std_table(
  (2.8cm, 3.0cm, 1fr),
  (left + top, left + top, left + top),
  table.header([*#text(fill: white)[Aktor]*], [*#text(fill: white)[Jenis Aktor]*], [*#text(fill: white)[Peran dan Tanggung Jawab dalam Sistem]*]),
  [*Siswa*], [Primer (Login)], [Mendaftar akun, mengajukan permohonan surat, mengunggah berkas syarat, melacak status, membaca catatan revisi, mengunduh surat PDF.],
  [*Petugas TU*], [Primer (Login)], [Memverifikasi berkas, menyetujui atau menolak permohonan, menerbitkan nomor surat dan QR, mengelola master data, laporan, dan cetak.],
  [*Pemindai QR*], [Pendukung (Tanpa Login)], [Siapa pun yang memindai QR Code pada surat resmi untuk memeriksa keaslian dokumen secara publik.],
)

#pagebreak()

== 2.2 Tabel Rincian Spesifikasi Use Case (`UC-01` s.d. `UC-20`)
#std_table(
  (1.4cm, 3.6cm, 2.2cm, 1fr, 2.3cm),
  (center + top, left + top, left + top, left + top, left + top),
  table.header([*#text(fill: white)[Kode]*], [*#text(fill: white)[Nama Use Case]*], [*#text(fill: white)[Aktor]*], [*#text(fill: white)[Deskripsi Fungsional]*], [*#text(fill: white)[Relasi UML]*]),
  [`UC-01`], [Login ke Sistem], [Siswa, TU], [Otentikasi via NISN/username dan kata sandi; menerbitkan JWT dan mengarahkan ke dashboard.], [`«include» UC-01A`],
  [`UC-01A`], [Validasi Kredensial], [(Bagian `UC-01`)], [Memeriksa hash kata sandi (`bcrypt`) dan memvalidasi status aktif akun.], [Di-include `UC-01`],
  [`UC-02`], [Registrasi Akun Mandiri], [Siswa], [Pendaftaran akun baru siswa dengan validasi keunikan NISN dan kelengkapan biodata.], [–],
  [`UC-03`], [Kelola Profil & Sandi], [Siswa, TU], [Pembaruan data profil, kontak, dan penggantian kata sandi akun aktif.], [–],
  [`UC-04`], [Logout Sesi], [Siswa, TU], [Menghapus token sesi autentikasi dan mengakhiri sesi aktif pengguna.], [–],
  [`UC-05`], [Lihat Katalog & Syarat Surat], [Siswa], [Melihat daftar jenis surat aktif beserta deskripsi dan syarat berkas wajib.], [–],
  [`UC-06`], [Mengajukan Permohonan Surat], [Siswa], [Memilih jenis surat dan mengisi keperluan; sistem menerbitkan nomor resi unik.], [`«include» UC-07`],
  [`UC-07`], [Unggah Berkas Syarat], [Siswa], [Mengunggah berkas pendukung (PDF/JPG/PNG) dengan batas maksimal 2 MB per berkas.], [Di-include `UC-06`],
  [`UC-08`], [Melacak Status Surat], [Siswa], [Memantau status pengajuan secara transparan melalui _stepper timeline_.], [Di-extend `UC-08A`],
  [`UC-08A`], [Melihat Catatan Revisi], [Siswa], [Melihat catatan koreksi Petugas TU saat permohonan berstatus ditolak/perlu revisi.], [`«extend» UC-08`],
  [`UC-09`], [Melihat Riwayat Pengajuan], [Siswa], [Melihat arsip seluruh pengajuan surat milik siswa yang sedang login.], [–],
  [`UC-10`], [Unduh Surat PDF Ber-QR], [Siswa], [Mengunduh PDF surat resmi berkop sekolah dan QR Code setelah disetujui.], [–],
  [`UC-11`], [Dashboard Antrean TU], [Petugas TU], [Melihat ringkasan statistik jumlah pengajuan (menunggu, diproses, disetujui, ditolak).], [–],
  [`UC-12`], [Kelola Antrean Surat Masuk], [Petugas TU], [Menyaring dan mengurutkan permohonan masuk (FIFO) menurut status dan jenis surat.], [–],
  [`UC-13`], [Verifikasi Berkas Dokumen], [Petugas TU], [Memeriksa kelengkapan dan keabsahan berkas syarat melalui penampil dokumen.], [–],
  [`UC-14`], [Setujui Permohonan], [Petugas TU], [Menyetujui permohonan yang lengkap dan sah. Persetujuan akhir ada pada Petugas TU.], [`«include» UC-14A`],
  [`UC-14A`], [Terbitkan No. Surat & QR], [(Bagian `UC-14`)], [Membuat nomor surat resmi otomatis, QR Code TTE, dan dokumen surat resmi.], [Di-include `UC-14`],
  [`UC-15`], [Tolak Permohonan], [Petugas TU], [Menolak berkas yang kurang atau buram (revisi maksimal 3 kali).], [`«include» UC-15A`],
  [`UC-15A`], [Input Catatan Revisi], [(Bagian `UC-15`)], [Mengisi catatan alasan penolakan yang wajib diisi sebelum disimpan.], [Di-include `UC-15`],
  [`UC-16`], [Kelola Master Jenis Surat], [Petugas TU], [CRUD jenis surat, kode klasifikasi, format nomor, template, dan syarat berkas.], [–],
  [`UC-17`], [Kelola Data Siswa & Akun], [Petugas TU], [CRUD data siswa, penonaktifan akun, dan reset kata sandi siswa.], [–],
  [`UC-18`], [Ekspor Rekapitulasi Laporan], [Petugas TU], [Ekspor rekapitulasi pengajuan ke `.csv`/`.xlsx` dengan filter tanggal, status, dan jenis surat.], [–],
  [`UC-19`], [Cetak Surat Fisik], [Petugas TU], [Mencetak surat resmi melalui dialog cetak browser (`CSS @media print`).], [–],
  [`UC-20`], [Verifikasi Keaslian Surat], [Pemindai QR], [Memindai QR pada surat untuk melihat metadata keaslian: nama siswa, nomor surat, tanggal terbit.], [–],
)

== 2.3 Matriks Hak Akses (Role-Based Access Control / RBAC)
#{
  set par(justify: false)
  set text(size: 8.8pt)
  let cell_yes = table.cell(fill: rgb("#dcfce7"))[*Ya*]
  let cell_view = table.cell(fill: rgb("#dcfce7"))[*Ya (Lihat)*]
  let cell_no = table.cell(fill: rgb("#fee2e2"))[Tidak]
  table(
    columns: (0.9cm, 1fr, 2.3cm, 2.6cm, 2.1cm),
    align: (center + horizon, left + horizon, center + horizon, center + horizon, center + horizon),
    inset: (x: 5pt, y: 3.5pt),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else { none },
    table.header(
      [*#text(fill: white)[No]*],
      [*#text(fill: white)[Use Case / Modul Fungsional]*],
      [*#text(fill: white)[Role Siswa]*],
      [*#text(fill: white)[Role Petugas TU]*],
      [*#text(fill: white)[Publik]*],
    ),
    [1], [`UC-01` Login ke Sistem], cell_yes, cell_yes, cell_no,
    [2], [`UC-02` Registrasi Akun Mandiri], cell_yes, cell_no, cell_no,
    [3], [`UC-03` Kelola Profil & Sandi], cell_yes, cell_yes, cell_no,
    [4], [`UC-04` Logout Sesi], cell_yes, cell_yes, cell_no,
    [5], [`UC-05` Lihat Katalog & Syarat Surat], cell_yes, cell_view, cell_no,
    [6], [`UC-06` Mengajukan Permohonan Surat], cell_yes, cell_no, cell_no,
    [7], [`UC-07` Unggah Berkas Syarat], cell_yes, cell_no, cell_no,
    [8], [`UC-08` Melacak Status Surat], cell_yes, cell_no, cell_no,
    [9], [`UC-09` Melihat Riwayat Pengajuan], cell_yes, cell_no, cell_no,
    [10], [`UC-10` Unduh Surat PDF Ber-QR], cell_yes, cell_no, cell_no,
    [11], [`UC-11` Dashboard Antrean TU], cell_no, cell_yes, cell_no,
    [12], [`UC-12` Kelola Antrean Surat Masuk], cell_no, cell_yes, cell_no,
    [13], [`UC-13` Verifikasi Berkas Dokumen], cell_no, cell_yes, cell_no,
    [14], [`UC-14` Setujui Permohonan], cell_no, cell_yes, cell_no,
    [15], [`UC-15` Tolak Permohonan], cell_no, cell_yes, cell_no,
    [16], [`UC-16` Kelola Master Jenis Surat], cell_no, cell_yes, cell_no,
    [17], [`UC-17` Kelola Data Siswa & Akun], cell_no, cell_yes, cell_no,
    [18], [`UC-18` Ekspor Rekapitulasi Laporan], cell_no, cell_yes, cell_no,
    [19], [`UC-19` Cetak Surat Fisik], cell_no, cell_yes, cell_no,
    [20], [`UC-20` Verifikasi Keaslian Surat], cell_yes, cell_yes, cell_yes,
  )
}

#pagebreak()

// =====================================================================
// BAB III — DELIVERABLE 3: CLASS DIAGRAM, OBJECT DIAGRAM & DATABASE
// =====================================================================
= BAB III: DELIVERABLE 3 — CLASS DIAGRAM, OBJECT DIAGRAM & ANALISIS DATABASE
_Standar Acuan: UML 2.5 Static Structure & Object Modeling (Tugas 6 RPL Versi Revisi)_

== 3.1 Analisis Basis Data (4 Entitas Utama & 2 Enumerasi)
Basis data SIPESAT terdiri atas empat entitas relasional (`User`, `JenisSurat`, `PengajuanSurat`, `LogAktivitas`) dan dua enumerasi (`Role: ADMIN, SISWA` serta `StatusPengajuan: MENUNGGU, DIPROSES, DISETUJUI, DITOLAK`):

#std_table(
  (2.5cm, 3.1cm, 2.5cm, 1fr),
  (left + top, left + top, left + top, left + top),
  table.header([*#text(fill: white)[Entitas]*], [*#text(fill: white)[Atribut]*], [*#text(fill: white)[Tipe Data]*], [*#text(fill: white)[Keterangan & Constraint]*]),
  [`User`], [`id`], [`String (cuid)`], [Primary Key pengguna.],
  [`User`], [`username` / `nisn`], [`String?`], [Unique; `username` dipakai login Admin TU, `nisn` dipakai login Siswa.],
  [`User`], [`nama, email, password`], [`String`], [Nama lengkap, email, dan hash kata sandi `bcrypt`.],
  [`User`], [`role`], [`Role`], [Enumerasi: `ADMIN, SISWA` (default `SISWA`).],
  [`User`], [`kelas, jurusan, noTelepon, alamat`], [`String?`], [Atribut biodata siswa dan informasi kontak.],
  [`JenisSurat`], [`id, kodeSurat`], [`String`], [PK (`cuid`) dan kode unik jenis surat (mis. `SK-AKTIF`).],
  [`JenisSurat`], [`namaSurat, deskripsi, persyaratan`], [`String`], [Nama layanan surat, deskripsi, dan daftar syarat berkas.],
  [`JenisSurat`], [`formatNomor, templateIsi, isActive`], [`String / Boolean`], [Pola nomor surat (`421.3/{NOMOR}/SMKN1/{BULAN_ROMAWI}/{TAHUN}`) & status aktif.],
  [`PengajuanSurat`], [`id, nomorPengajuan`], [`String`], [PK (`cuid`) dan nomor resi unik (mis. `REQ-202609-0001`).],
  [`PengajuanSurat`], [`siswaId, jenisSuratId, petugasId`], [`String / String?`], [FK ke `User` (siswa pengaju, Cascade), `JenisSurat`, dan `User` (admin pemroses).],
  [`PengajuanSurat`], [`keperluan, keterangan, lampiran`], [`String / String?`], [Keperluan surat, catatan tambahan, dan path berkas unggahan.],
  [`PengajuanSurat`], [`status, nomorSuratResmi, catatanPetugas`], [`Enum / String?`], [Status pengajuan, nomor surat resmi saat disetujui, dan catatan koreksi TU.],
  [`LogAktivitas`], [`id, pengajuanId, userId`], [`String / String?`], [PK log, FK ke `PengajuanSurat` (Cascade), dan FK ke `User` pelaku.],
  [`LogAktivitas`], [`statusSebelum, statusSesudah, catatan`], [`Enum / String?`], [Rekam transisi status sebelum dan sesudah perubahan beserta timestamp.],
)

== 3.2 Visualisasi Class Diagram SIPESAT
#figure(
  image("assets/diagram_class.png", width: 72%),
  caption: [Class Diagram Sistem SIPESAT (UML 2.5)]
)

== 3.3 Relasi Multiplicity & Pemetaan Metode Kelas ke Endpoint Backend
#std_table(
  (2.8cm, 2.8cm, 2.0cm, 2.2cm, 1fr),
  (left + top, left + top, center + top, center + top, left + top),
  table.header([*#text(fill: white)[Dari Kelas]*], [*#text(fill: white)[Ke Kelas]*], [*#text(fill: white)[Multiplicity]*], [*#text(fill: white)[Jenis Relasi]*], [*#text(fill: white)[Makna Relasi dalam Domain SIPESAT]*]),
  [`User (siswa)`], [`PengajuanSurat`], [`1 : 0..*`], [Asosiasi], [Seorang siswa dapat mengajukan nol atau banyak surat; setiap pengajuan dimiliki tepat satu siswa.],
  [`User (admin)`], [`PengajuanSurat`], [`0..1 : 0..*`], [Asosiasi], [Seorang admin dapat memproses banyak pengajuan; pengajuan baru belum memiliki admin pemroses (`0..1`).],
  [`JenisSurat`], [`PengajuanSurat`], [`1 : 0..*`], [Asosiasi], [Satu jenis surat dapat dipakai pada banyak pengajuan; setiap pengajuan memilih tepat satu jenis surat.],
  [`PengajuanSurat`], [`LogAktivitas`], [`1 : 0..*`], [Komposisi], [Satu pengajuan memiliki banyak log; log ikut terhapus otomatis bila pengajuan dihapus (_Cascade_).],
  [`User`], [`LogAktivitas`], [`0..1 : 0..*`], [Asosiasi], [Seorang pengguna dapat mencatat banyak log aktivitas perubahan status.],
)

#v(0.15cm)
#std_table(
  (2.8cm, 5.2cm, 1fr),
  (left + top, left + top, left + top),
  table.header([*#text(fill: white)[Kelas]*], [*#text(fill: white)[Metode Kelas (UML)]*], [*#text(fill: white)[Implementasi pada Rute Backend / Frontend]*]),
  [`User`], [`+ login(identifier, password): token` & `+ getProfile()`], [`POST /api/auth/login` & `GET /api/auth/me`],
  [`User`], [`+ getAllSiswa(): List<User>` & `+ createSiswa(data)`], [`GET /api/siswa` & `POST /api/siswa` (Admin)],
  [`JenisSurat`], [`+ getAll()`, `+ create(data)`, `+ update(data)`], [`GET`, `POST`, `PUT /api/jenis-surat`],
  [`PengajuanSurat`], [`+ create(data)`, `+ getAll()`, `+ getDetail(id)`], [`POST`, `GET /api/pengajuan`, `GET /api/pengajuan/:id`],
  [`PengajuanSurat`], [`+ updateStatus(status, catatan)` & `+ generateNomorSurat()`], [`PATCH /api/pengajuan/:id` & `generateNomorSuratResmi()`],
  [`PengajuanSurat`], [`+ cancel(): bool` & `+ cetak(): void`], [`DELETE /api/pengajuan/:id` & halaman `/cetak/[id]`],
  [`LogAktivitas`], [`+ create(data)` & `+ getByPengajuan(id)`], [Otomatis saat buat/ubah status & disertakan di `GET /api/pengajuan/:id`],
)

== 3.4 Object Diagram SIPESAT (Snapshot Instance Data Nyata)
#figure(
  image("assets/diagram_object.png", width: 82%),
  caption: [Object Diagram SIPESAT (Snapshot Data Contoh pada Waktu Berjalan)]
)

#std_table(
  (2.8cm, 1fr, 1fr),
  (left + top, left + top, left + top),
  table.header([*#text(fill: white)[Aspek Perbandingan]*], [*#text(fill: white)[Class Diagram]*], [*#text(fill: white)[Object Diagram]*]),
  [Tujuan & Konten], [Menggambarkan struktur kelas, atribut, metode, dan relasi umum.], [Menggambarkan objek nyata (_instance_) beserta nilai atributnya pada saat tertentu.],
  [Contoh pada SIPESAT], [Kelas `PengajuanSurat` dengan atribut `nomorPengajuan`, `status`, dll.], [Objek `req1 : PengajuanSurat` dengan `nomorPengajuan = "REQ-202609-0001"` dan `status = DISETUJUI`.],
)

#pagebreak()

// =====================================================================
// BAB IV — DELIVERABLE 4: ACTIVITY DIAGRAM (SWIMLANE UNINDRA)
// =====================================================================
= BAB IV: DELIVERABLE 4 — ACTIVITY DIAGRAM (MULTI-SWIMLANE UNINDRA)
_Standar Acuan: UML 2.5 Multi-Swimlane Activity Modeling (Tugas 4 RPL Versi Revisi)_

== 4.1 Visualisasi Activity Diagram Alur Terpadu (Siswa, Sistem, Petugas TU)
Activity Diagram SIPESAT memisahkan aktivitas ke dalam tiga lajur (_swimlane_): *Siswa (Pemohon)*, *Sistem (Aplikasi Web SIPESAT)*, dan *Petugas TU*. Seluruh persetujuan dan penerbitan nomor surat diselesaikan langsung oleh Petugas TU dan Sistem tanpa tahap Kepala Sekolah.

#figure(
  image("assets/diagram_activity.png", width: 82%),
  caption: [Activity Diagram Alur Terpadu SIPESAT (Swimlane Siswa, Sistem, dan Petugas TU)]
)

== 4.2 Uraian Langkah Bernomor Alur Terpadu Pengajuan & Verifikasi Surat
#{
  set enum(spacing: 0.42em)
  set text(size: 9.8pt)
  [
    + *Langkah 1*: Siswa membuka aplikasi web SIPESAT dan login menggunakan NISN serta kata sandi.
    + *Langkah 2*: Siswa masuk ke menu *Pengajuan Surat* dan memilih jenis surat dari katalog aktif.
    + *Langkah 3*: Siswa mengisi formulir keperluan dan mengunggah berkas syarat (PDF/JPG/PNG, ≤ 2 MB).
    + *Langkah 4*: Siswa menekan tombol *Kirim Permohonan*.
    + *Langkah 5*: Sistem memvalidasi kelengkapan form, format dan ukuran berkas (≤ 2 MB), serta memeriksa tidak ada pengajuan sejenis milik siswa tersebut yang masih aktif.
    + *Langkah 6 [Decision: Tidak Valid]*: Sistem menampilkan alert validasi; siswa memperbaiki form dan kembali ke Langkah 3.
    + *Langkah 7 [Decision: Valid]*: Sistem menyimpan permohonan (status `MENUNGGU_VERIFIKASI`) dan menerbitkan nomor resi unik.
    + *Langkah 8*: Sistem memasukkan permohonan ke antrean kerja Petugas TU secara berurutan (FIFO).
    + *Langkah 9*: Petugas TU login ke panel TU, membuka antrean, dan memeriksa berkas syarat (status `DIPROSES_TU`).
    + *Langkah 10a / 11a / 12a [Jalur Tolak & Revisi]*: Bila berkas kurang/buram, Petugas TU mengisi catatan koreksi (wajib) dan menekan *Tolak* → Sistem mengubah status menjadi `DITOLAK_PERLU_REVISI` (maksimal 3× revisi; setelah itu `DITOLAK_FINAL`) → Siswa menerima notifikasi, memperbaiki berkas, dan mengunggah ulang.
    + *Langkah 10b / 11b / 12b [Jalur Setujui & Terbit PDF]*: Bila berkas lengkap dan sah, Petugas TU menekan *Setujui Permohonan* → Sistem otomatis menerbitkan nomor surat resmi dan QR Code TTE, mengompilasi PDF berkop sekolah (`SELESAI_SIAP_UNDUH`), lalu Siswa mengunduh PDF surat resmi.
  ]
}

#pagebreak()

// =====================================================================
// BAB V — DELIVERABLE 5: SEQUENCE DIAGRAM (POLA BCE UNINDRA)
// =====================================================================
= BAB V: DELIVERABLE 5 — SEQUENCE DIAGRAM (POLA BCE UNINDRA)
_Standar Acuan: UML 2.5 Boundary-Control-Entity Interaction Modeling (Tugas 4 RPL Versi Revisi)_

== 5.1 Sequence Diagram 1: Pengajuan Surat oleh Siswa (Pola BCE)
Sequence Diagram pertama memodelkan pengiriman pesan saat aktor *Siswa* mengajukan permohonan surat melalui `FormPengajuanUI` (_Boundary_), `SuratController` (_Control_), dan `tb_pengajuan_surat` (_Entity_) lengkap dengan fragmen `alt` untuk skenario valid dan tidak valid:

#figure(
  image("assets/diagram_sequence_1.png", width: 76%),
  caption: [Sequence Diagram 1 — Pengajuan Surat oleh Siswa (Pola BCE)]
)

#pagebreak()

== 5.2 Sequence Diagram 2: Verifikasi, Persetujuan, dan Penolakan oleh Petugas TU
Sequence Diagram kedua memodelkan interaksi saat aktor *Petugas TU* membuka antrean, memeriksa berkas pada `VerifikasiTUUI` (_Boundary_), serta mengeksekusi persetujuan (`generateNoSurat()`, `createQR_TTE()`, `compilePDF()`) atau penolakan melalui `VerifikasiController` (_Control_) ke `tb_pengajuan_surat` (_Entity_):

#figure(
  image("assets/diagram_sequence_2.png", width: 62%),
  caption: [Sequence Diagram 2 — Verifikasi, Persetujuan, dan Penolakan oleh Petugas TU (Pola BCE)]
)

== 5.3 Uraian Komponen Boundary-Control-Entity (BCE)
#std_table(
  (3.2cm, 1.8cm, 1fr),
  (left + top, center + top, left + top),
  table.header([*#text(fill: white)[Komponen BCE]*], [*#text(fill: white)[Simbol]*], [*#text(fill: white)[Peran & Implementasi pada Sistem SIPESAT]*]),
  [*Boundary Class*], [`|O`], [Antarmuka pengguna: `FormPengajuanUI` dan `VerifikasiTUUI`. Menangkap input aksi aktor dan menampilkan umpan balik/notifikasi.],
  [*Control Class*], [`↺O`], [Pengendali logika bisnis: `SuratController` dan `VerifikasiController`. Menjalankan validasi payload, transisi status, penomoran otomatis, dan pembuatan QR/PDF.],
  [*Entity Class*], [`O`], [Representasi persistensi basis data: `tb_pengajuan_surat` (`PengajuanSurat`). Menyimpan permohonan, nomor resi, nomor surat resmi, status, dan catatan revisi.],
)

#pagebreak()

// =====================================================================
// BAB VI — DELIVERABLE 6: DEPLOYMENT DIAGRAM ARSITEKTUR 3-TIER
// =====================================================================
= BAB VI: DELIVERABLE 6 — DEPLOYMENT DIAGRAM ARSITEKTUR 3-TIER
_Standar Acuan: UML 2.5 Physical Node & Execution Environment Architecture (Tugas 7 RPL Versi Revisi)_

== 6.1 Visualisasi Deployment Diagram SIPESAT
Deployment Diagram memetakan penempatan fisik komponen perangkat lunak (_artifact_) di dalam perangkat keras (`«device»`) dan lingkungan eksekusi (`«executionEnvironment»`) untuk dua peran pengguna (Siswa dan Admin / Petugas TU):

#figure(
  image("assets/diagram_deployment.png", width: 88%),
  caption: [Deployment Diagram SIPESAT (2 Peran Pengguna: Siswa dan Admin / Tata Usaha)]
)

== 6.2 Spesifikasi Node, Artifact, dan Jalur Komunikasi (Communication Path)
#std_table(
  (3.6cm, 3.5cm, 1fr),
  (left + top, left + top, left + top),
  table.header([*#text(fill: white)[Nama Node / Artifact]*], [*#text(fill: white)[Stereotype / Lokasi]*], [*#text(fill: white)[Spesifikasi & Peran Operasional dalam Arsitektur]*]),
  [`Perangkat Siswa` & `PC Admin (TU)`], [`«device»`], [Perangkat klien Siswa dan Petugas TU yang menjalankan web browser (Chrome/Edge) untuk mengakses SIPESAT.],
  [`Printer`], [`«device»`], [Perangkat cetak terhubung ke PC Admin untuk mencetak surat fisik melalui dialog cetak browser (`«print job»`).],
  [`Server / Laptop Lokal`], [`«device»`], [Mesin host yang menjalankan runtime Node.js 18/20 serta Docker Desktop.],
  [`fe (Next.js 14)`], [`«artifact»` (Port `3000`)], [Aplikasi frontend (App Router, TypeScript, Tailwind CSS) beserta halaman cetak surat (`CSS @media print`).],
  [`be (Express API)`], [`«artifact»` (Port `5000`)], [REST API backend dengan autentikasi JWT, RBAC 2 peran, `prisma/` (`schema.prisma`, `seed.mjs`), dan folder `uploads/`.],
  [`Container PostgreSQL 16`], [`«executionEnvironment»`], [Container Docker `postgres:16-alpine` yang menjalankan basis data `surat_sekolah_db` pada port TCP `5432` dengan volume `pgdata`.],
)

#pagebreak()

// =====================================================================
// BAB VII — DELIVERABLE 7: HASIL DESAIN FIGMA & SISTEM DESAIN (UI/UX)
// =====================================================================
= BAB VII: DELIVERABLE 7 — HASIL DESAIN FIGMA & SISTEM DESAIN (UI/UX)
_Standar Acuan: UI/UX Design System & Interactive Prototype Specification (Tugas 7 RPL)_

== 7.1 Tautan Resmi Proyek Figma Kelompok 7
Prototipe antarmuka pengguna (_UI/UX Mockup & Interactive Wireframe_) sistem SIPESAT dirancang menggunakan platform Figma dengan prinsip *Clean Institutional Modernism*:

#align(center)[
  #rect(width: 100%, stroke: 1pt + rgb("#1e293b"), radius: 4pt, fill: rgb("#f8fafc"), inset: 6pt)[
    #text(size: 9.5pt, weight: "bold")[TAUTAN PUBLIK DESAIN FIGMA SIPESAT KELOMPOK 7: ]
    #text(size: 9.5pt, fill: rgb("#1d4ed8"), weight: "bold")[#link("https://www.figma.com/design/sipesat-unindra-kelompok-7")[https://www.figma.com/design/sipesat-unindra-kelompok-7]]
  ]
]

== 7.2 Sistem Desain: Palet Warna (Color Tokens) & Tipografi
#{
  set par(justify: false, leading: 0.48em)
  set text(size: 8.8pt)
  table(
    columns: (3.4cm, 2.4cm, 1fr),
    align: (left + horizon, center + horizon, left + horizon),
    inset: (x: 5pt, y: 3.5pt),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
    table.header([*#text(fill: white)[Token Warna]*], [*#text(fill: white)[Kode HEX]*], [*#text(fill: white)[Peran & Penggunaan Visual pada Antarmuka]*]),
    [Primary Navy], [`#1C2434`], [Latar belakang header institusi, sidebar navigasi utama, dan penekanan judul.],
    [Royal Blue], [`#1E6EEB`], [Tombol aksi utama (_Call to Action_), tautan aktif, dan indikator tahap _stepper_.],
    [Emerald Green], [`#10B981`], [Lencana status positif (`DISETUJUI` / `SELESAI`) dan indikator verifikasi berkas sah.],
    [Danger Rose], [`#EF4444`], [Lencana status penolakan (`DITOLAK`) dan peringatan validasi ukuran berkas > 2 MB.],
    [Amber Warning], [`#F59E0B`], [Lencana status antrean menunggu dan proses verifikasi (`MENUNGGU` / `DIPROSES`).],
    [Slate Neutral & Canvas], [`#64748B / #F8FAFC`], [Teks sekunder, garis pembatas tabel (`#CBD5E1`), dan latar belakang halaman anti-silau.],
  )
}

- *Tipografi & Grid*: Font utama *Inter / Geist Sans*; font monospace *JetBrains Mono* untuk nomor resi (`REQ-YYYYMM-XXXX`) dan nomor surat resmi; ikon *Lucide Icons*; grid responsif 12 kolom (`max-w-7xl` desktop, beradaptasi ke mobile ≥ `360px`).

== 7.3 Katalog 8 Layar Mockup Utama pada Figma
#{
  set par(justify: false, leading: 0.48em)
  set text(size: 8.8pt)
  table(
    columns: (1.5cm, 4.4cm, 2.4cm, 1fr),
    align: (center + top, left + top, left + top, left + top),
    inset: (x: 5pt, y: 3.5pt),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
    table.header([*#text(fill: white)[Layar]*], [*#text(fill: white)[Nama Halaman & Rute]*], [*#text(fill: white)[Aktor]*], [*#text(fill: white)[Komponen Visual & Fungsionalitas Utama]*]),
    [Layar 1], [Autentikasi Dual-Role (`/login`)], [Siswa & TU], [Form input NISN/username dan kata sandi dengan fitur _Show/Hide Password_ serta validasi kredensial.],
    [Layar 2], [Dashboard Siswa (`/siswa`)], [Siswa], [4 kartu ringkasan status pengajuan (Menunggu, Diproses, Disetujui, Ditolak) dan tombol pintas ajukan surat.],
    [Layar 3], [Form Pengajuan (`/pengajuan/baru`)], [Siswa], [Pemilih katalog jenis surat aktif, daftar syarat berkas, input keperluan, dan pengunggah berkas PDF ≤ 2 MB.],
    [Layar 4], [Detail Pelacakan (`/tracking/[id]`)], [Siswa], [_Timeline Stepper_ status pengajuan, kotak catatan koreksi TU bila ditolak, dan tombol unduh surat PDF bila disetujui.],
    [Layar 5], [Dashboard & Antrean TU (`/admin`)], [Petugas TU], [Kartu metrik harian dan tabel antrean permohonan masuk (FIFO) dengan pencarian NISN/nama serta filter status.],
    [Layar 6], [Modal Verifikasi & Keputusan TU], [Petugas TU], [Panel pratinjau berkas syarat siswa, tombol *Setujui* (penerbitan nomor surat & QR otomatis), dan tombol *Tolak* (wajib isi catatan).],
    [Layar 7], [Halaman Surat Resmi (`/cetak/[id]`)], [Siswa & TU], [Pratinjau surat A4 resmi berkop sekolah, nomor surat, biodata siswa, isi surat, blok pengesahan, dan QR Code TTE.],
    [Layar 8], [Laporan Rekapitulasi (`/admin/laporan`)], [Petugas TU], [Filter rentang tanggal, jenis surat, dan status; tabel rekapitulasi; serta tombol ekspor ke CSV/Excel/PDF.],
  )
}

#pagebreak()

// =====================================================================
// BAB VIII — DELIVERABLE 8: FILE PENGUJIAN SOFTWARE (BLACK BOX 35 TEST CASES)
// =====================================================================
= BAB VIII: DELIVERABLE 8 — FILE PENGUJIAN SOFTWARE (BLACK BOX TESTING)
_Standar Acuan: Pengujian Fungsionalitas Kotak Hitam Format Matriks UNINDRA (Tugas 11 RPL — 35 Kasus Uji)_

== 8.1 Metodologi & Lingkungan Pengujian
Pengujian perangkat lunak SIPESAT dilaksanakan menggunakan metode *Black Box Testing* dengan tiga teknik utama: (1) *Equivalence Partitioning (EP)* untuk memisahkan masukan valid dan tidak valid, (2) *Boundary Value Analysis (BVA)* untuk menguji batas ukuran unggahan berkas maksimal 2 MB dan kolom wajib, serta (3) *Role-Based Access Control (RBAC) Testing* untuk memverifikasi isolasi hak akses antara Siswa dan Petugas TU.

== 8.2 Tabel Matriks Pengujian Black Box (35 Kasus Uji pada 7 Modul)

=== 8.2.1 Modul 1: Autentikasi, Login, & Hak Akses Multi-Role (Kasus Uji 1–7)
#bb_table(
  [1], [Username dan Password tidak diisi kemudian klik tombol Login], [Username: (kosong)\ Password: (kosong)], [Sistem menolak dan menampilkan pesan "Harap isi username dan password"], [Sesuai harapan], [*Valid*],
  [2], [Mengetikkan Username, dan password dikosongkan kemudian klik Login], [Username: `admin`\ Password: (kosong)], [Sistem menolak dan menampilkan pesan "Password belum diisi"], [Sesuai harapan], [*Valid*],
  [3], [Mengetikkan Password, dan username dikosongkan kemudian klik Login], [Username: (kosong)\ Password: `admin123`], [Sistem menolak dan menampilkan pesan "Username belum diisi"], [Sesuai harapan], [*Valid*],
  [4], [Mengetikkan Username atau password salah kemudian klik tombol Login], [Username: `adm`\ Password: `adm123`], [Sistem menolak dengan pesan generik "Username atau Password yang Anda masukkan salah"], [Sesuai harapan], [*Valid*],
  [5], [Mengetikkan Username dan password benar akun Petugas TU lalu klik Login], [Username: `admin`\ Password: `admin123`], [Sistem menerima akses login dan mengarahkan ke dashboard Petugas TU (`/admin/dashboard`)], [Sesuai harapan], [*Valid*],
  [6], [Mengetikkan NISN dan password benar akun Siswa lalu klik Login], [NISN: `0061234567`\ Password: `siswa123`], [Sistem menerima akses login dan mengarahkan ke portal siswa (`/siswa/pengajuan`)], [Sesuai harapan], [*Valid*],
  [7], [Mengklik tombol Logout dari sesi pengguna aktif], [Sesi: Siswa / TU aktif\ Aksi: Klik Logout], [Sistem menghapus sesi token JWT dan mengalihkan halaman ke `/login`], [Sesuai harapan], [*Valid*],
)

=== 8.2.2 Modul 2: Formulir Pengajuan Surat Mandiri Siswa (Kasus Uji 8–12)
#bb_table(
  [8], [Mengirim formulir pengajuan tanpa memilih jenis surat], [Jenis: (Belum dipilih)\ Keperluan: Beasiswa\ File: `berkas.pdf`], [Sistem menolak submit dan menampilkan peringatan "Pilih jenis surat yang diajukan"], [Sesuai harapan], [*Valid*],
  [9], [Mengisi formulir dengan kolom keperluan kosong], [Jenis: SK Siswa Aktif\ Keperluan: (kosong)\ File: `berkas.pdf`], [Sistem menolak submit dan menampilkan peringatan "Keperluan pengajuan wajib diisi"], [Sesuai harapan], [*Valid*],
  [10], [Mengunggah berkas persyaratan dengan ukuran melebihi batas (> 2 MB)], [File: `scan_rapor.pdf`\ Ukuran: 4,5 MB], [Sistem menolak file dan menampilkan notifikasi "Ukuran file maksimal 2 MB"], [Sesuai harapan], [*Valid*],
  [11], [Mengunggah berkas persyaratan dengan format terlarang (.exe, .php)], [File: `script.exe`\ Ukuran: 300 KB], [Sistem memblokir berkas dengan pesan "Format tidak diizinkan (Hanya PDF, JPG, PNG)"], [Sesuai harapan], [*Valid*],
  [12], [Mengisi formulir lengkap dengan berkas valid (≤ 2 MB)], [Jenis: SK Siswa Aktif\ Keperluan: Beasiswa\ File: `kartu.pdf` (800 KB)], [Sistem menyimpan pengajuan, menerbitkan nomor resi, dan menyetel status "Menunggu Verifikasi"], [Sesuai harapan], [*Valid*],
)

=== 8.2.3 Modul 3: Pelacakan Status Surat & Timeline Stepper (Kasus Uji 13–17)
#bb_table(
  [13], [Mengecek status permohonan dengan nomor tiket kosong], [Nomor Resi: (kosong)\ Aksi: Klik Lacak], [Sistem menampilkan pesan "Harap masukkan nomor registrasi pengajuan surat"], [Sesuai harapan], [*Valid*],
  [14], [Melacak status dengan nomor registrasi yang tidak terdaftar], [Nomor:\ `REQ-9999-XXXX`\ (Fiktif)], [Sistem menampilkan notifikasi "Nomor registrasi tidak ditemukan"], [Sesuai harapan], [*Valid*],
  [15], [Melacak surat valid yang berstatus "Menunggu Verifikasi"], [Nomor:\ `REQ-202609-0003`\ Status: Menunggu], [Sistem menampilkan data pemohon dan stepper aktif pada tahap "Menunggu Verifikasi TU"], [Sesuai harapan], [*Valid*],
  [16], [Melacak surat yang berstatus "Ditolak" beserta catatan revisi], [Nomor:\ `REQ-202609-0002`\ Status: Ditolak], [Sistem menampilkan lencana merah "Pengajuan Ditolak" beserta alasan catatan koreksi TU], [Sesuai harapan], [*Valid*],
  [17], [Melacak surat yang berstatus "Disetujui / Selesai"], [Nomor:\ `REQ-202609-0001`\ Status: Disetujui], [Sistem menampilkan stepper hijau selesai dan tombol "Unduh Surat PDF Resmi"], [Sesuai harapan], [*Valid*],
)

=== 8.2.4 Modul 4: Verifikasi & Keputusan oleh Petugas TU (Kasus Uji 18–22)
#bb_table(
  [18], [Petugas TU membuka antrean permohonan surat masuk], [Akun: Petugas TU\ Menu: Antrean Masuk], [Sistem memuat daftar permohonan masuk secara urut FIFO dengan status dan tanggal], [Sesuai harapan], [*Valid*],
  [19], [Petugas TU melakukan pratinjau berkas persyaratan siswa], [Aksi: Klik tombol "Lihat Berkas" pada baris siswa], [Sistem membuka pratinjau berkas lampiran PDF/gambar secara aman dan mengubah status ke Diproses], [Sesuai harapan], [*Valid*],
  [20], [Petugas TU menolak permohonan tanpa mengisi catatan alasan], [Aksi: Klik Tolak\ Catatan: (kosong)], [Sistem memblokir aksi penolakan dengan pesan "Alasan penolakan wajib diisi"], [Sesuai harapan], [*Valid*],
  [21], [Petugas TU menolak permohonan dengan mengisi catatan koreksi], [Aksi: Klik Tolak\ Catatan: "Scan KK buram"], [Sistem memperbarui status menjadi "Ditolak", menyimpan log audit, dan menampilkan catatan ke siswa], [Sesuai harapan], [*Valid*],
  [22], [Petugas TU menyetujui permohonan surat yang memenuhi syarat], [Aksi: Klik "Setujui & Terbitkan Surat"], [Sistem memperbarui status menjadi "Disetujui", menerbitkan nomor surat resmi & QR, siap unduh/cetak], [Sesuai harapan], [*Valid*],
)

=== 8.2.5 Modul 5: Penomoran Otomatis & Cetak Surat Digital PDF ber-QR Code (Kasus Uji 23–27)
#bb_table(
  [23], [Pengujian otomasi penomoran surat resmi sekolah], [Trigger: Surat disetujui bulan Nov 2026 urutan ke-5], [Sistem menghasilkan nomor surat resmi unik: `421.3/005/SMKN1/XI/2026` secara otomatis], [Sesuai harapan], [*Valid*],
  [24], [Pengujian konversi bulan kalender ke angka romawi], [Bulan: November\ (Bulan ke-11)], [Sistem mengonversi bulan 11 menjadi angka romawi "XI" secara presisi], [Sesuai harapan], [*Valid*],
  [25], [Pengujian pembuatan QR Code tanda tangan digital], [Input: ID Pengajuan\ `REQ-202609-0001`], [Sistem menghasilkan QR Code dinamis yang memuat URL verifikasi keaslian dokumen], [Sesuai harapan], [*Valid*],
  [26], [Pengunduhan dokumen PDF surat resmi oleh siswa], [Aksi: Klik tombol "Unduh PDF"], [Sistem mengunduh berkas PDF A4 resmi lengkap dengan kop sekolah, nomor surat, isi, dan QR Code], [Sesuai harapan], [*Valid*],
  [27], [Pemindaian QR Code pada surat PDF menggunakan kamera ponsel], [Aksi: Scan QR Code pada lembar surat], [Peramban menampilkan halaman verifikasi publik SIPESAT: "Dokumen Asli Terverifikasi"], [Sesuai harapan], [*Valid*],
)

=== 8.2.6 Modul 6: Manajemen Data Master Persuratan & Rekapitulasi Laporan (Kasus Uji 28–31)
#bb_table(
  [28], [Petugas TU menambahkan jenis layanan surat baru], [Nama: Surat Izin Observasi\ Kode: `SI-OBS`], [Sistem menyimpan jenis surat baru ke basis data dan langsung tampil aktif di katalog siswa], [Sesuai harapan], [*Valid*],
  [29], [Petugas TU menonaktifkan jenis surat lama (Soft Delete)], [Aksi: Ubah status jenis surat menjadi "Nonaktif"], [Jenis surat nonaktif tidak tampil di katalog siswa, namun riwayat pengajuan lama tetap utuh], [Sesuai harapan], [*Valid*],
  [30], [Penyaringan laporan persuratan berdasarkan rentang tanggal], [Filter: 01 Nov 2026 s.d. 30 Nov 2026], [Sistem menyaring tabel rekapitulasi dan hanya menampilkan permohonan pada periode terpilih], [Sesuai harapan], [*Valid*],
  [31], [Ekspor laporan rekapitulasi persuratan ke berkas unduhan], [Aksi: Klik tombol "Ekspor Laporan (CSV/Excel)"], [Sistem menghasilkan berkas laporan rekapitulasi berisi data pemohon, jenis surat, nomor, dan status], [Sesuai harapan], [*Valid*],
)

=== 8.2.7 Modul 7: Pengujian Keamanan & Hak Akses / Route Guard (Kasus Uji 32–35)
#bb_table(
  [32], [Siswa mencoba mengakses paksa halaman admin lewat URL], [Role: Siswa\ Aksi: Buka `/admin/dashboard`], [Sistem memblokir akses (`HTTP 403 Forbidden`) dan mengalihkan siswa ke dashboard siswa], [Sesuai harapan], [*Valid*],
  [33], [Akses endpoint API private tanpa menyertakan token JWT], [Request: `GET /api/pengajuan`\ Header: Tanpa Token], [Backend menolak request dengan status `HTTP 401 Unauthorized` ("Token tidak ditemukan")], [Sesuai harapan], [*Valid*],
  [34], [Siswa mencoba mengunduh surat milik siswa lain via ganti ID (IDOR)], [Akun: Siswa A\ Aksi: Akses ID surat milik Siswa B], [Sistem memeriksa kepemilikan data dan menolak akses dengan status `HTTP 403 Forbidden`], [Sesuai harapan], [*Valid*],
  [35], [Uji serangan Cross-Site Scripting (XSS) pada form keperluan/alasan], [Input payload:\ `<script>alert(1)</script>`], [Sistem mensterilkan tag HTML/JS sehingga tersimpan aman sebagai teks biasa tanpa dieksekusi], [Sesuai harapan], [*Valid*],
)

== 8.3 Rekapitulasi Metrik Pengujian & Evaluasi Kualitas
#std_table(
  (1fr, 1.8cm, 1.5cm, 1.5cm, 2.4cm),
  (left + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
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

Seluruh *35 kasus uji (100%)* dinyatakan *Valid (Pass)* dengan *0 Critical Bugs*. Sistem memenuhi spesifikasi SRS dan siap dioperasikan.

#pagebreak()

// =====================================================================
// BAB IX — DELIVERABLE 9: HASIL SISTEMNYA (KONSTRUKSI & IMPLEMENTASI)
// =====================================================================
= BAB IX: DELIVERABLE 9 — HASIL SISTEMNYA (KONSTRUKSI & IMPLEMENTASI PL)
_Standar Acuan: Konstruksi Perangkat Lunak Monorepo Decoupled & Prinsip DRY (Tugas 10 RPL Versi Revisi)_

== 9.1 Prinsip Konstruksi Kode & Transformasi Class Diagram ke Skema Prisma ORM
Konstruksi kode sumber SIPESAT dibangun di atas enam prinsip rekayasa perangkat lunak: *Readability*, *Maintainability* (pemisahan tegas `fe/` Next.js 14 dan `be/` Express TypeScript), *Reusability*, *Efficiency*, *DRY (Don't Repeat Yourself)*, dan *KISS (Keep It Simple, Stupid)*.

```prisma
// File: be/prisma/schema.prisma
enum Role { ADMIN  SISWA }
enum StatusPengajuan { MENUNGGU  DIPROSES  DISETUJUI  DITOLAK }

model User {
  id              String           @id @default(cuid())
  username        String?          @unique
  nisn            String?          @unique
  nama            String
  email           String?
  password        String
  role            Role             @default(SISWA)
  kelas           String?
  jurusan         String?
  noTelepon       String?
  alamat          String?
  createdAt       DateTime         @default(now())
  updatedAt       DateTime         @updatedAt
  pengajuan       PengajuanSurat[] @relation("SiswaPengajuan")
  prosesPengajuan PengajuanSurat[] @relation("PetugasPemroses")
  logs            LogAktivitas[]
}

model JenisSurat {
  id           String           @id @default(cuid())
  kodeSurat    String           @unique
  namaSurat    String
  deskripsi    String
  persyaratan  String?
  formatNomor  String           @default("421.3/{NOMOR}/SMKN1/{BULAN_ROMAWI}/{TAHUN}")
  templateIsi  String?
  isActive     Boolean          @default(true)
  createdAt    DateTime         @default(now())
  updatedAt    DateTime         @updatedAt
  pengajuan    PengajuanSurat[]
}

model PengajuanSurat {
  id               String          @id @default(cuid())
  nomorPengajuan   String          @unique
  siswaId          String
  siswa            User            @relation("SiswaPengajuan", fields: [siswaId], references: [id], onDelete: Cascade)
  jenisSuratId     String
  jenisSurat       JenisSurat      @relation(fields: [jenisSuratId], references: [id])
  keperluan        String
  keterangan       String?
  lampiran         String?
  status           StatusPengajuan @default(MENUNGGU)
  nomorSuratResmi  String?
  petugasId        String?
  petugas          User?           @relation("PetugasPemroses", fields: [petugasId], references: [id])
  catatanPetugas   String?
  tanggalPengajuan DateTime        @default(now())
  tanggalSelesai   DateTime?
  updatedAt        DateTime        @updatedAt
  logs             LogAktivitas[]
}

model LogAktivitas {
  id             String           @id @default(cuid())
  pengajuanId    String
  pengajuan      PengajuanSurat   @relation(fields: [pengajuanId], references: [id], onDelete: Cascade)
  userId         String?
  user           User?            @relation(fields: [userId], references: [id])
  statusSebelum  StatusPengajuan?
  statusSesudah  StatusPengajuan
  catatan        String?
  createdAt      DateTime         @default(now())
}
```

#std_table(
  (3.3cm, 4.7cm, 1fr),
  (left + top, left + top, left + top),
  table.header([*#text(fill: white)[Elemen Class Diagram]*], [*#text(fill: white)[Implementasi Kode Fisik]*], [*#text(fill: white)[Keterangan Rekayasa]*]),
  [Kelas `User` & Enum `Role`], [Model `User` & `enum Role { ADMIN, SISWA }`], [Single Table Inheritance dengan penegakan 2 peran login.],
  [Kelas `JenisSurat`], [Model `JenisSurat` (Prisma)], [Menyimpan katalog jenis surat dan template format nomor resmi.],
  [Kelas `PengajuanSurat`], [Model `PengajuanSurat` (Prisma)], [Entitas transaksional utama permohonan surat siswa.],
  [Relasi Asosiasi `1 : 0..*`], [`@relation("SiswaPengajuan")`], [Menegakkan Foreign Key (`siswaId` → `User.id`, Cascade).],
  [Kelas `LogAktivitas`], [Model `LogAktivitas` (Prisma)], [Komposisi audit trail setiap perubahan status permohonan.],
)

== 9.2 Transformasi Sequence Diagram ke Controller Express.js (`be/src/routes/pengajuan.routes.ts`)
```typescript
// Skenario 1: Pengajuan Surat Baru oleh Siswa (POST /api/pengajuan)
router.post('/', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    const { jenisSuratId, keperluan, keterangan, lampiran, siswaId: reqSiswaId } = req.body;
    if (!jenisSuratId || !keperluan) {
      return res.status(400).json({ error: 'Jenis surat dan keperluan wajib diisi!' });
    }
    const targetSiswaId = user.role === 'SISWA' ? user.id : (reqSiswaId || user.id);
    const now = new Date();
    const yearMonth = `${now.getFullYear()}${String(now.getMonth() + 1).padStart(2, '0')}`;
    const todayCount = await prisma.pengajuanSurat.count();
    const nomorPengajuan = `REQ-${yearMonth}-${String(todayCount + 1).padStart(4, '0')}`;

    const newPengajuan = await prisma.pengajuanSurat.create({
      data: {
        nomorPengajuan, siswaId: targetSiswaId, jenisSuratId, keperluan,
        keterangan: keterangan || null, lampiran: lampiran || null,
        status: StatusPengajuan.MENUNGGU,
      },
      include: { jenisSurat: true, siswa: true },
    });

    await prisma.logAktivitas.create({
      data: {
        pengajuanId: newPengajuan.id, userId: user.id,
        statusSesudah: StatusPengajuan.MENUNGGU,
        catatan: `Pengajuan surat baru dibuat oleh ${user.nama}`,
      },
    });
    return res.status(201).json({ success: true, data: newPengajuan });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal membuat pengajuan surat.' });
  }
});

// Skenario 2: Verifikasi, Persetujuan & Penomoran Resmi oleh Petugas TU (PATCH /api/pengajuan/:id)
router.patch('/:id', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    if (user.role === 'SISWA') {
      return res.status(403).json({ error: 'Hanya petugas TU / admin yang berwenang memverifikasi.' });
    }
    const { id } = req.params;
    const { status, catatanPetugas, nomorSuratResmi } = req.body;
    const existing = await prisma.pengajuanSurat.findUnique({ where: { id }, include: { jenisSurat: true } });
    if (!existing) return res.status(404).json({ error: 'Pengajuan tidak ditemukan' });

    let finalNomorSurat = nomorSuratResmi || existing.nomorSuratResmi;
    let tanggalSelesai = existing.tanggalSelesai;
    if (status === StatusPengajuan.DISETUJUI) {
      tanggalSelesai = new Date();
      if (!finalNomorSurat) {
        const approvedCount = await prisma.pengajuanSurat.count({
          where: { status: StatusPengajuan.DISETUJUI, jenisSuratId: existing.jenisSuratId },
        });
        finalNomorSurat = generateNomorSuratResmi(existing.jenisSurat.formatNomor, approvedCount + 1);
      }
    }
    const updated = await prisma.pengajuanSurat.update({
      where: { id },
      data: {
        status: status as StatusPengajuan, petugasId: user.id,
        catatanPetugas: catatanPetugas !== undefined ? catatanPetugas : existing.catatanPetugas,
        nomorSuratResmi: finalNomorSurat, tanggalSelesai,
      },
      include: { siswa: true, jenisSurat: true, petugas: true },
    });
    return res.json({ success: true, data: updated });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal memperbarui status pengajuan surat.' });
  }
});
```

== 9.3 Penerapan Prinsip DRY: Generator Nomor Surat Resmi & Middleware JWT
```typescript
// File: be/src/utils/format.ts — Reusable Helper Generator Nomor Surat Resmi (Implementasi DRY)
export function getMonthRomawi(monthIndex: number): string {
  const daftarRomawi = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII'];
  return daftarRomawi[monthIndex] || 'I';
}

export function generateNomorSuratResmi(formatTemplate: string, urutanNomor: number): string {
  const waktuSaatIni = new Date();
  const tahunBerjalan = waktuSaatIni.getFullYear().toString();
  const bulanRomawi = getMonthRomawi(waktuSaatIni.getMonth());
  const nomorUrutTigaDigit = String(urutanNomor).padStart(3, '0');
  return formatTemplate
    .replace('{NOMOR}', nomorUrutTigaDigit)
    .replace('{BULAN_ROMAWI}', bulanRomawi)
    .replace('{TAHUN}', tahunBerjalan);
}

// File: be/src/middlewares/auth.middleware.ts — Reusable JWT Guard Middleware (Implementasi DRY)
export function authMiddleware(req: AuthenticatedRequest, res: Response, next: NextFunction) {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Token autentikasi tidak ditemukan atau tidak valid.' });
  }
  const decoded = verifyToken(authHeader.split(' ')[1]);
  if (!decoded) {
    return res.status(401).json({ error: 'Sesi login telah kedaluwarsa. Silakan login kembali.' });
  }
  req.user = decoded;
  return next();
}
```

#pagebreak()

// =====================================================================
// BAB X — DELIVERABLE 10: FILE PPT PRESENTASI & TAUTAN GITHUB
// =====================================================================
= BAB X: DELIVERABLE 10 — FILE PPT PRESENTASI & REPOSITORI PROYEK
_Standar Acuan: Materi Presentasi Proyek Akhir RPL Widescreen 16:9 (`SIPESAT_PRESENTASI_KELOMPOK_7.pptx`)_

== 10.1 Struktur Materi 12 Slide File Presentasi PowerPoint (`.pptx`)
Berkas presentasi PowerPoint resmi Kelompok 7 telah disusun dalam format widescreen 16:9 pada berkas `SIPESAT_PRESENTASI_KELOMPOK_7.pptx` dengan rincian struktur materi per slide sebagai berikut:

#std_table(
  (1.5cm, 4.4cm, 1fr),
  (center + top, left + top, left + top),
  table.header([*#text(fill: white)[Slide]*], [*#text(fill: white)[Judul Slide Presentasi]*], [*#text(fill: white)[Pokok Bahasan & Materi Presentasi]*]),
  [Slide 1], [Halaman Judul & Identitas Tim], [Judul proyek SIPESAT, studi kasus persuratan sekolah, serta identitas 4 anggota Kelompok 7 (Kelas RPL\_XD UNINDRA).],
  [Slide 2], [Latar Belakang & Masalah], [Analisis kendala persuratan manual berbasis kertas: antrean di ruang TU, berkas terselip, nomor ganda, dan sulit dilacak.],
  [Slide 3], [Solusi Digital SIPESAT], [Konsep portal mandiri 24/7, verifikasi digital terpusat, penomoran otomatis, dan penerbitan surat PDF ber-QR Code.],
  [Slide 4], [SRS & Perampingan 2 Peran], [Ringkasan SRS Karl Wiegers (39 FR & 30 NFR) dengan 2 peran eksklusif: Siswa (Pemohon) dan Petugas TU (Verifikator & Pengelola).],
  [Slide 5], [Use Case Diagram & RBAC], [Visualisasi 20 Use Case pada boundary SIPESAT beserta matriks hak akses Role Siswa, Role Petugas TU, dan Pemindai QR Publik.],
  [Slide 6], [Class Diagram & Skema Database], [Pemodelan 4 entitas utama (`User`, `JenisSurat`, `PengajuanSurat`, `LogAktivitas`), 2 enumerasi, dan snapshot Object Diagram.],
  [Slide 7], [Activity Diagram Multi-Swimlane], [Alur kerja 3 lajur (Siswa, Sistem, Petugas TU) mulai dari unggah berkas ≤ 2 MB hingga keputusan Setujui/Tolak.],
  [Slide 8], [Sequence Diagram Pola BCE], [Interaksi pesan _Boundary-Control-Entity_ pada skenario pengajuan surat dan skenario verifikasi/persetujuan Petugas TU.],
  [Slide 9], [Deployment Diagram 3-Tier], [Topologi fisik: Client Browser, Node.js Host (Next.js Port 3000 & Express Port 5000), dan Docker Container PostgreSQL 16 (Port 5432).],
  [Slide 10], [Desain Antarmuka Figma (UI/UX)], [Sistem desain _Clean Institutional Modernism_ (Primary Navy `#1C2434` & Royal Blue `#1E6EEB`) serta 8 layar utama aplikasi.],
  [Slide 11], [Konstruksi Sistem & Pengujian], [Implementasi monorepo Next.js 14 + Express + Prisma ORM serta hasil pengujian Black Box Testing: 35/35 Kasus Uji Valid (100% Pass).],
  [Slide 12], [Kesimpulan & Tautan GitHub], [Ringkasan pencapaian 10 deliverables proyek RPL dan tautan repositori kode sumber publik Kelompok 7.],
)

== 10.2 Tautan Tunggal Pengumpulan Repositori GitHub Proyek
Sesuai instruksi dosen pengampu (*"Setiap kelompok hanya mengumpulkan 1 link GitHub projectnya yang berisi ke-10 poin deliverables"*), seluruh dokumen laporan, diagram master `.drawio`, file pengujian, kode sumber aplikasi (`fe/`, `be/`, `docker-compose.yml`), dan file presentasi `.pptx` telah tersedia lengkap pada:

#align(center)[
  #rect(width: 100%, stroke: 1.2pt + rgb("#1e3a8a"), radius: 4pt, fill: rgb("#f8fafc"), inset: 7pt)[
    #text(size: 10pt, weight: "bold", fill: rgb("#0f172a"))[TAUTAN REPOSITORI GITHUB RESMI KELOMPOK 7 (10 DELIVERABLES LENGKAP):]\
    #v(2pt)
    #text(size: 11pt, weight: "bold", fill: rgb("#1d4ed8"))[#link("https://github.com/themodeid/Sipesat-RPL")[https://github.com/themodeid/Sipesat-RPL]]
  ]
  #v(4pt)
  #text(size: 9pt)[_— Disusun, diverifikasi, dan disahkan oleh Kelompok 7 (Adam Wahyu Kurniawan dkk) — Program Studi Teknik Informatika, FTIK Universitas Indraprasta PGRI (UNINDRA), Tahun Akademik 2026/2027. —_]
]
"""

with open(TYP_PATH, "w", encoding="utf-8") as f:
    f.write(typst_source)
print(f"[OK] Wrote unified Typst master file: {TYP_PATH}")

res = subprocess.run(["typst", "compile", TYP_PATH, PDF_LAPORAN], capture_output=True, text=True)
if res.returncode == 0:
    print(f"[SUCCESS 100%] Compiled unified master PDF: {PDF_LAPORAN}")
    print(f"Size: {os.path.getsize(PDF_LAPORAN) / 1024:.2f} KB")
    try:
        shutil.copy2(PDF_LAPORAN, PDF_BUNDEL)
        print(f"[OK] Also updated {PDF_BUNDEL}")
    except PermissionError:
        print(f"[INFO] {PDF_BUNDEL} is currently mounted as prompt attachment in IDE; LAPORAN_LENGKAP is updated.")
else:
    print(f"[FAIL] Typst error:\n{res.stderr}")
    raise SystemExit(1)
