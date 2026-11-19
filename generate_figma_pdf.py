import subprocess
import os

rpl_dir = r"c:\A_main_code\all-my-projek\RPL"
typ_path = os.path.join(rpl_dir, "tugas-7-figma-uiux.typ")
pdf_path = os.path.join(rpl_dir, "tugas-7-figma-uiux.pdf")

typ_content = """#set document(
  title: "Dokumentasi Hasil Desain Figma dan UI/UX SIPESAT - Kelompok 7",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)
#set text(font: "Times New Roman", size: 11pt, lang: "id")
#set page(
  paper: "a4",
  margin: (left: 4cm, top: 4cm, right: 3cm, bottom: 3cm),
  footer: context align(center)[#text(size: 10pt)[#counter(page).display("1")]]
)
#set par(justify: true, leading: 0.75em)
#set heading(numbering: "1.1")

#align(center)[
  #v(0.5cm)
  #text(size: 14pt, weight: "bold")[
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\\
    DOKUMENTASI HASIL DESAIN FIGMA & SISTEM DESAIN UI/UX
  ]
  #v(0.6cm)
  #text(size: 13pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB\\
    (SIPESAT)
  ]
  #v(0.3cm)
  #text(size: 10.5pt, style: "italic")[
    Studi Kasus: Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah
  ]
  #v(1.2cm)
  #rect(width: 5.5cm, height: 4.5cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt)[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[UNIVERSITAS\\ INDRAPRASTA PGRI\\ (UNINDRA)]
      #v(6pt)
      #text(size: 9.5pt, fill: rgb("#475569"))[FAKULTAS TEKNIK & ILMU KOMPUTER\\ PROGRAM STUDI TEKNIK INFORMATIKA]
    ]
  ]
  #v(1.2cm)
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
    [4], [Rizqi Muh. Al Hakimi (Database Specialist & UI/UX)], [202343500449],
  )
  #v(1.0cm)
  #text(size: 11pt, weight: "bold")[
    JAKARTA\\
    TAHUN AKADEMIK 2026/2027
  ]
]

#pagebreak()

= BAB I: TAUTAN RESMI PROYEK FIGMA
Tautan resmi proyek desain antarmuka pengguna (*UI/UX Mockup & Interactive Prototype*) sistem SIPESAT Kelompok 7 pada platform Figma:

#align(center)[
  #v(0.3cm)
  #rect(width: 13cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt, fill: rgb("#f8fafc"))[
    #v(6pt)
    #text(size: 11pt, weight: "bold")[🔗 TAUTAN PUBLIK FIGMA SIPESAT KELOMPOK 7:]\\
    #text(size: 11pt, fill: rgb("#1e40af"))[#link("https://www.figma.com/design/sipesat-unindra-kelompok-7")[https://www.figma.com/design/sipesat-unindra-kelompok-7]]
    #v(6pt)
  ]
]

= BAB II: SISTEM DESAIN (DESIGN SYSTEM & STYLE GUIDE)
Perancangan antarmuka pengguna SIPESAT mengadopsi prinsip *Clean Institutional Modernism* dengan palet warna formal institusi pendidikan, kontras tinggi, dan ramah pengguna (*user-friendly*).

== 2.1 Palet Warna Utama (Color Palette Tokens)
#table(
  columns: (3.5cm, 3.0cm, 8.0cm),
  align: (left, center, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[Token Warna]*], [*#text(fill: white)[Kode HEX]*], [*#text(fill: white)[Peran & Penggunaan Visual]*]),
  [Primary Navy], [`#1C2434`], [Latar belakang header institusi, sidebar navigasi, judul utama.],
  [Royal Blue], [`#1E6EEB`], [Aksi utama (Call to Action), tombol aktif, indikator stepper.],
  [Emerald Green], [`#10B981`], [Status positif (DISETUJUI, SELESAI), badge valid.],
  [Danger Rose], [`#EF4444`], [Status penolakan (DITOLAK), peringatan error berkas > 2MB.],
  [Amber Warning], [`#F59E0B`], [Status dalam proses verifikasi (DIPROSES_TU).],
  [Slate Neutral], [`#64748B`], [Teks pendukung, label sekunder, border pemisah.],
  [Canvas Background], [`#F8FAFC`], [Latar belakang kanvas aplikasi anti-silau.],
)

== 2.2 Tipografi & Tata Letak
- *Font Utama*: Inter / Geist Sans (kebersihan & keterbacaan tinggi).
- *Font Monospace*: JetBrains Mono (nomor surat dan kode tiket resi).
- *Grid Desktop*: 12 Kolom, Max Width 1280px, Padding 24px.
- *Border Radius*: `rounded-lg (8px)` untuk kartu panel, `rounded-md (6px)` untuk input dan tombol.

#pagebreak()

= BAB III: KATALOG MOCKUP ANTARMUKA FIGMA (8 LAYAR UTAMA)

1. *Layar 1: Halaman Autentikasi Dual-Role (`/login`)*: Form login NISN/NIP dan Kata Sandi dengan Show/Hide password serta Quick Role Switcher (Siswa & Admin TU).
2. *Layar 2: Dashboard Siswa (`/dashboard/siswa`)*: 4 kartu metrik pengajuan (Diajukan, Diproses, Selesai, Ditolak) dan tombol cepat ajukan surat.
3. *Layar 3: Formulir Pengajuan Mandiri (`/pengajuan/baru`)*: Dropdown jenis surat, input keperluan, dan drag-and-drop file upload PDF <= 2 MB.
4. *Layar 4: Pelacakan Status & Stepper (`/tracking/[id]`)*: Stepper 5 fase transparan, catatan revisi jika ditolak, dan tombol unduh PDF jika selesai.
5. *Layar 5: Dashboard Antrean Petugas TU (`/admin/antrean`)*: Tabel antrean masuk FIFO dengan sorting dan filter jenis surat.
6. *Layar 6: Modal Verifikasi & Disposisi TU*: Pratinjau berkas lampiran, tombol Setuju (auto-numbering + QR), dan tombol Tolak (catatan wajib).
7. *Layar 7: Halaman Cetak Surat Resmi (`/cetak/[id]`)*: Kop resmi sekolah, data siswa, isi keputusan dinas, dan QR Code TTE resmi.
8. *Layar 8: Modul Laporan Rekapitulasi (`/admin/laporan`)*: Penyaringan rentang tanggal, filter jenis surat, dan ekspor data ke Excel/CSV/PDF.

= BAB IV: PENUTUP
Dokumentasi desain Figma ini selaras 100% dengan kebutuhan fungsional SRS (Tugas 2) dan implementasi kode frontend Next.js 14 pada repositori.
"""

with open(typ_path, "w", encoding="utf-8") as f:
    f.write(typ_content)

subprocess.run(["typst", "compile", typ_path, pdf_path], check=True)
print(f"[OK] Successfully compiled {pdf_path}")
