#set document(
  title: "Tugas 2 RPL: SRS Standar IEEE / Karl Wiegers - SIPESAT",
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
    TUGAS 2: SPESIFIKASI KEBUTUHAN PERANGKAT LUNAK (SRS)
  ]
  #v(1.0cm)
  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\
    #text(size: 10.5pt, weight: "regular")[_Standar Dokumentasi: IEEE Std 830-1998 / Karl Wiegers SRS Template_]
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

= BAB I: PENDAHULUAN & RUANG LINGKUP PRODUK
== 1.1 Tujuan Dokumen
Dokumen Spesifikasi Kebutuhan Perangkat Lunak (*Software Requirements Specification - SRS*) ini disusun sebagai kontrak formal dan acuan tunggal (*single source of truth*) dalam pengembangan *Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)*.

== 1.2 Cakupan Produk
SIPESAT mendigitalkan rantai pengajuan surat keterangan siswa secara mandiri, mengeliminasi formulir kertas manual, dan mempercepat validasi oleh Tata Usaha sekolah hingga penerbitan surat berformat PDF resmi dengan stempel kode QR dinamis.

#pagebreak()

= BAB II: RANCANGAN DIAGRAM ARSITEKTUR & USE CASE
== 2.1 Use Case Diagram Terpadu (Draw.io Native)
Rancangan fungsionalitas sistem dipetakan ke dalam Use Case Diagram standar UML 2.5 dengan pemisahan peran yang tegas antara Aktor Siswa (pemohon) dan Petugas TU (verifikator & pengelola):

#align(center)[
  #image("assets/diagram_usecase.png", width: 100%)
  #v(4pt)
  #text(size: 9.5pt, style: "italic")[Gambar 2.1: Use Case Diagram SIPESAT Standar UML 2.5 (100% Bebas Tabrakan)]
]

#v(0.5cm)
== 2.2 Lampiran Berkas Master Draw.io
Seluruh diagram rancangan SRS dapat disunting langsung pada berkas Draw.io master:
- *`tugas-2-srs-wiegers.drawio`* (Format XML Native Draw.io: Tab 1 Diagram Konteks Arsitektur Produk & Tab 2 Use Case SRS Lampiran B).
