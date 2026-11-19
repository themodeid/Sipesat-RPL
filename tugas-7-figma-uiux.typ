#set document(
  title: "Dokumentasi Hasil Desain Figma dan UI/UX SIPESAT - Kelompok 7",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)
#set text(font: "Times New Roman", size: 11pt, lang: "id")
#set page(
  paper: "a4",
  margin: (left: 3.5cm, top: 3.5cm, right: 3cm, bottom: 3cm),
  footer: context align(center)[#text(size: 10pt)[#counter(page).display("1")]]
)
#set par(justify: true, leading: 0.75em)
#set heading(numbering: none)
#show heading.where(level: 1): it => block(above: 1.4em, below: 0.8em)[
  #text(size: 13pt, weight: "bold")[#it.body]
]
#show heading.where(level: 2): it => block(above: 1.1em, below: 0.6em)[
  #text(size: 11.5pt, weight: "bold")[#it.body]
]

#align(center)[
  #v(0.3cm)
  #text(size: 14pt, weight: "bold")[
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\
    DOKUMENTASI HASIL DESAIN FIGMA & SISTEM DESAIN UI/UX
  ]
  #v(0.5cm)
  #text(size: 13pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB\
    (SIPESAT)
  ]
  #v(0.2cm)
  #text(size: 10.5pt, style: "italic")[
    Studi Kasus: Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah (Versi Revisi)
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

= BAB I: TAUTAN RESMI PROYEK FIGMA
Tautan resmi proyek desain antarmuka pengguna (*UI/UX Mockup & Interactive Prototype*) sistem SIPESAT Kelompok 7 pada platform Figma:

#align(center)[
  #v(0.2cm)
  #rect(width: 100%, stroke: 1.2pt + rgb("#1e293b"), radius: 4pt, fill: rgb("#f8fafc"), inset: 10pt)[
    #text(size: 11pt, weight: "bold")[TAUTAN PUBLIK FIGMA SIPESAT KELOMPOK 7:]\
    #v(3pt)
    #text(size: 11pt, fill: rgb("#1e40af"))[#link("https://www.figma.com/design/sipesat-unindra-kelompok-7")[https://www.figma.com/design/sipesat-unindra-kelompok-7]]
  ]
]

= BAB II: SISTEM DESAIN (DESIGN SYSTEM & STYLE GUIDE)
Perancangan antarmuka pengguna SIPESAT mengadopsi prinsip *Clean Institutional Modernism* dengan palet warna formal institusi pendidikan, kontras tinggi, dan ramah pengguna (*user-friendly*).

== 2.1 Palet Warna Utama (Color Palette Tokens)
#{
  set par(justify: false)
  table(
    columns: (3.2cm, 2.5cm, 1fr),
    align: (left + horizon, center + horizon, left + horizon),
    inset: 7pt,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
    table.header([*#text(fill: white)[Token Warna]*], [*#text(fill: white)[Kode HEX]*], [*#text(fill: white)[Peran & Penggunaan Visual]*]),
    [Primary Navy], [`#1C2434`], [Latar belakang header institusi, sidebar navigasi, judul utama.],
    [Royal Blue], [`#1E6EEB`], [Aksi utama (Call to Action), tombol aktif, indikator stepper.],
    [Emerald Green], [`#10B981`], [Status positif (`DISETUJUI`, `SELESAI`), lencana valid.],
    [Danger Rose], [`#EF4444`], [Status penolakan (`DITOLAK`), peringatan error berkas > 2 MB.],
    [Amber Warning], [`#F59E0B`], [Status dalam proses verifikasi (`DIPROSES_TU`).],
    [Slate Neutral], [`#64748B`], [Teks pendukung, label sekunder, border pemisah.],
    [Canvas Background], [`#F8FAFC`], [Latar belakang kanvas aplikasi bersih anti-silau.],
  )
}

== 2.2 Tipografi & Tata Letak
- *Font Utama*: Inter / Geist Sans (kebersihan & keterbacaan tinggi pada layar desktop maupun mobile).
- *Font Monospace*: JetBrains Mono (penomoran surat resmi dan kode tiket resi).
- *Grid Desktop*: 12 Kolom, Max Width 1280px, Padding 24px.
- *Border Radius*: `rounded-lg (8px)` untuk kartu panel, `rounded-md (6px)` untuk input dan tombol.

= BAB III: KATALOG MOCKUP ANTARMUKA FIGMA (8 LAYAR UTAMA)

+ *Layar 1: Halaman Autentikasi Dual-Role (`/login`)*: Form login NISN/username dan kata sandi dengan fitur Show/Hide password untuk Siswa dan Petugas TU.
+ *Layar 2: Dashboard Siswa (`/dashboard/siswa`)*: 4 kartu ringkasan metrik pengajuan (Diajukan, Diproses, Disetujui, Ditolak) dan tombol pintas ajukan surat.
+ *Layar 3: Formulir Pengajuan Mandiri (`/pengajuan/baru`)*: Pilihan katalog jenis surat, input keperluan, dan area unggah berkas syarat PDF maksimal 2 MB.
+ *Layar 4: Pelacakan Status & Stepper (`/tracking/[id]`)*: Linimasa status transparan, catatan koreksi TU bila ditolak, dan tombol unduh surat PDF bila disetujui.
+ *Layar 5: Dashboard Antrean Petugas TU (`/admin/antrean`)*: Statistik status dan tabel antrean masuk FIFO dengan pencarian serta filter jenis surat.
+ *Layar 6: Modal Verifikasi & Keputusan TU*: Pratinjau berkas syarat siswa, tombol Setujui (penerbitan nomor surat & QR otomatis), dan tombol Tolak (catatan alasan wajib).
+ *Layar 7: Halaman Cetak Surat Resmi (`/cetak/[id]`)*: Tata letak surat A4 resmi berkop sekolah, nomor surat, biodata siswa, isi surat, dan QR Code keaslian.
+ *Layar 8: Modul Laporan Rekapitulasi (`/admin/laporan`)*: Penyaringan berdasarkan periode, jenis surat, dan status, dilengkapi tombol ekspor laporan.

= BAB IV: PENUTUP
Dokumentasi desain Figma ini selaras 100% dengan spesifikasi kebutuhan fungsional SRS (Tugas 2) dan implementasi kode frontend Next.js 14 pada repositori proyek SIPESAT.
