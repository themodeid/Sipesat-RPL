#set document(
  title: "Tugas 4 RPL: Activity Diagram & Sequence Diagram - SIPESAT",
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
    TUGAS 4: ACTIVITY DIAGRAM & SEQUENCE DIAGRAM
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
Sistem Informasi Pengajuan Surat Siswa Berbasis Web (*SIPESAT*) membagi hak akses ke dalam 3 peran pengguna utama: Siswa (pemohon), Staf Tata Usaha (verifikator & pengelola), dan Kepala Sekolah (pengesah tanda tangan digital QR Code).

== 1.2 Standar Kaidah Modul UNINDRA (Pertemuan 04)
1. *Activity Diagram*: Wajib menerapkan format Swimlane serta teks uraian langkah proses bernomor.
2. *Sequence Diagram*: Wajib menerapkan pola arsitektur Boundary-Control-Entity (BCE) dengan kotak pembatas *`alt`* untuk memisahkan skenario valid versus tidak valid.

#pagebreak()

= BAB II: PERANCANGAN ACTIVITY DIAGRAM (SWIMLANE UNINDRA)
== 2.1 Diagram Alur Terpadu Pengajuan Surat Siswa (Draw.io Native)

#align(center)[
  #image("assets/diagram_activity.png", width: 100%)
  #v(4pt)
  #text(size: 9.5pt, style: "italic")[Gambar 2.1: Activity Diagram Alur Terpadu SIPESAT Standar UNINDRA (100% Bebas Tabrakan)]
]

#v(0.4cm)
== 2.2 Uraian Langkah Bernomor Alur Terpadu
1. Siswa membuka web SIPESAT dan melakukan login menggunakan NISN dan kata sandi.
2. Masuk menu 'Pengajuan Surat' dan pilih jenis surat yang diperlukan.
3. Isi formulir keperluan dan unggah dokumen syarat (PDF/JPG $<= 2$ MB).
4. Klik tombol 'Kirim Permohonan'.
5. Sistem memvalidasi kelengkapan formulir dan ukuran berkas dokumen.
6. [Decision: Jika form tidak lengkap / file $> 2$ MB] Tampilkan alert validasi dan kembali ke form.
7. [Decision: Jika valid] Simpan permohonan ke database (status: DIAJUKAN) dan terbitkan nomor resi tiket unik.
8. Sistem meneruskan berkas ke meja antrean TU.
9. Petugas TU login ke panel TU, membuka antrean, dan meninjau berkas dokumen siswa.
10. [Decision: Jika berkas kurang/buram] Input alasan koreksi, klik 'Tolak & Minta Revisi', update status ke DITOLAK_PERLU_REVISI, dan kirim notifikasi ke siswa.
11. [Decision: Jika berkas lengkap & sah] Input nomor agenda TU dan teruskan ke antrean Kepala Sekolah.
12. Kepala Sekolah menyetujui, sistem generate nomor surat resmi dan bubuhkan kode QR TTE.
13. Sistem mengompilasi kop sekolah, data siswa, dan kode QR ke file PDF resmi (status: SELESAI).
14. Siswa menerima notifikasi selesai dan mengunduh berkas PDF surat resmi.

#pagebreak()

= BAB III: PERANCANGAN SEQUENCE DIAGRAM (POLA BCE UNINDRA)
== 3.1 Diagram Sequence: Pengajuan Siswa & Verifikasi TU (Draw.io Native)

#align(center)[
  #image("assets/diagram_sequence.png", width: 100%)
  #v(4pt)
  #text(size: 9.5pt, style: "italic")[Gambar 3.1: Sequence Diagram Pengajuan & Verifikasi Dokumen Pola BCE (100% Bebas Tabrakan)]
]

#v(0.4cm)
== 3.2 Uraian Komponen Boundary-Control-Entity (BCE)
#table(
  columns: (3.0cm, 2.5cm, 9.0cm),
  align: (center, center, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[Komponen BCE]*], [*#text(fill: white)[Simbol]*], [*#text(fill: white)[Peran & Implementasi di SIPESAT]*]),
  [Boundary Class], [|O], [Komponen antarmuka pengguna: `FormPengajuanUI`, `VerifikasiTUUI`. Menangkap input dan menyajikan feedback visual.],
  [Control Class], [↺O], [Pengendali logika bisnis: `SuratController`, `VerifikasiController`. Menjalankan aturan validasi payload dan kalkulasi.],
  [Entity Class], [_O_], [Struktur persistensi database: `tb_pengajuan_surat`. Menyimpan record permohonan, nomor resi, dan status dokumen.]
)

#v(0.8cm)
= BAB IV: KESIMPULAN & BERKAS DIAGRAM DRAW.IO
Seluruh diagram visual interaktif tersimpan pada berkas Draw.io master:
- *`tugas-4-activity-sequence.drawio`* *(2 Tab Bersih: Tab 1 Activity Terpadu, Tab 2 Sequence Diagrams BCE)*.
