#set document(
  title: "Tugas 4 RPL: Activity Diagram & Sequence Diagram - SIPESAT",
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
    TUGAS 4: ACTIVITY DIAGRAM & SEQUENCE DIAGRAM
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
Sistem Informasi Pengajuan Surat Siswa Berbasis Web (*SIPESAT*) adalah sistem perangkat lunak yang dirancang untuk memodernisasi pelayanan administrasi persuratan bagi siswa di lingkungan sekolah menengah. Sistem memotong rantai birokrasi manual tatap muka menjadi proses digital mandiri, terukur, dan transparan.

Sistem membagi hak akses ke dalam 3 peran pengguna utama:
1. *Siswa*: Mengajukan permohonan surat secara mandiri, melampirkan berkas persyaratan (maksimal 2 MB), memantau perkembangan status surat, serta mengunduh surat PDF yang telah disahkan.
2. *Staf Tata Usaha (TU)*: Memeriksa dan memverifikasi kelengkapan berkas yang diajukan siswa, memberikan nomor agenda surat masuk, dan meneruskan berkas yang valid ke Kepala Sekolah (atau menolaknya dengan catatan revisi).
3. *Kepala Sekolah*: Memeriksa draf surat yang sudah diverifikasi TU, memberikan persetujuan (_approval_), dan mengesahkan surat dengan tanda tangan elektronik berbasis kode QR.

== 1.2 Standar Kaidah Modul UNINDRA (Pertemuan 04)
Berdasarkan modul resmi yang dikembangkan oleh Koordinator Bu Millati Izzatillah, S.Kom., MMSI dan tim pengembang bahan ajar RPL UNINDRA:
1. *Activity Diagram*: Wajib menerapkan format *Swimlane 2 Kolom* (Aktor di kiri vs Sistem di kanan), menggunakan simbol standar (Start Node, Activity State berawalan kata kerja, Decision diamond dengan cabang Ya/Tidak, dan End Node bullseye), serta *wajib disertai teks uraian langkah proses bernomor* (1, 2, 3, dst).
2. *Sequence Diagram*: Wajib menerapkan pola arsitektur *Boundary-Control-Entity (BCE)*:
   - *Boundary Class* (`|O`): Komponen antarmuka pengguna / UI (misal `FormPengajuanUI`, `VerifikasiTUUI`).
   - *Control Class* (`↺O`): Komponen pengendali logika bisnis (misal `AuthController`, `SuratController`).
   - *Entity Class* (`_O_`): Komponen tabel data / persistensi database (misal `User`, `SuratPengajuan`).
   - Wajib menyertakan kotak pembatas *`alt` (alternative frame)* dengan garis putus-putus untuk memisahkan skenario sukses `[Valid]` dan gagal `[Tidak Valid]`.

#pagebreak()

// BAB II
#heading(level: 1)[BAB II: PERANCANGAN ACTIVITY DIAGRAM (SWIMLANE UNINDRA)]

== 2.1 Activity Diagram 1: Alur Pengajuan Surat oleh Siswa
Memodelkan alur interaksi 2 kolom antara Siswa di sisi kiri dan Aplikasi Web SIPESAT di sisi kanan:
1. Siswa membuka web SIPESAT dan melakukan login menggunakan NISN dan kata sandi.
2. Sistem memvalidasi kredensial dan menampilkan dashboard siswa.
3. Siswa memilih menu 'Pengajuan Surat' dan menentukan jenis surat yang dibutuhkan.
4. Siswa mengisi keperluan surat serta mengunggah file berkas persyaratan (PDF/JPG maksimal 2 MB).
5. Siswa menekan tombol 'Kirim Permohonan'.
6. Sistem memeriksa kelengkapan form dan ukuran file. Jika ukuran $> 2$ MB atau form kosong, sistem memunculkan pesan kesalahan agar diperbaiki. Jika valid, sistem menyimpan lampiran, membuat kode tiket unik, dan mencatat permohonan dengan status `MENUNGGU_VERIFIKASI`.
7. Sistem menyajikan resi nomor tiket ke antarmuka siswa untuk pelacakan.

== 2.2 Activity Diagram 2: Alur Verifikasi Berkas oleh Staf Tata Usaha
Memodelkan alur kerja Staf TU dalam meninjau kelayakan berkas masuk:
1. Staf TU login ke panel admin TU dan membuka menu 'Verifikasi Berkas Masuk'.
2. Staf TU memilih salah satu permohonan dari antrean dan meninjau pratinjau (_preview_) berkas lampiran.
3. Staf TU memeriksa kelayakan berkas. Jika tidak lengkap atau buram, Staf TU menuliskan catatan revisi dan menekan tombol 'Tolak & Minta Revisi' (status menjadi `DITOLAK_PERLU_REVISI`).
4. Jika berkas sah dan lengkap, Staf TU menginput nomor agenda masuk TU lalu menekan tombol 'Verifikasi & Teruskan' (status menjadi `DIVERIFIKASI_TU_MENUNGGU_KEPSEK`).

== 2.3 Activity Diagram 3: Alur Persetujuan oleh Kepala Sekolah
Memodelkan alur persetujuan akhir dan penerbitan dokumen resmi:
1. Kepala Sekolah login dan membuka menu 'Persetujuan Surat'.
2. Kepala Sekolah meninjau draf permohonan yang telah diverifikasi TU.
3. Jika tidak disetujui, input catatan evaluasi dan kembalikan ke meja TU (`DITOLAK_KEPSEK`).
4. Jika disetujui, Kepala Sekolah mengklik 'Setujui & Tanda Tangani'.
5. Sistem mengambil format penomoran resmi sekolah, membuat kode QR tanda tangan elektronik terenkripsi, menyatukan kop sekolah dengan draf PDF, dan mengubah status menjadi `SELESAI_SIAP_UNDUH`.

#pagebreak()

// BAB III
#heading(level: 1)[BAB III: PERANCANGAN SEQUENCE DIAGRAM (POLA BCE UNINDRA)]

Sequence Diagram disusun mengadopsi pola formal *Boundary-Control-Entity (BCE)* sesuai modul Pertemuan 04:

#table(
  columns: (3.0cm, 2.5cm, 9.0cm),
  align: (center, center, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header(
    [*#text(fill: white)[Komponen BCE]*],
    [*#text(fill: white)[Simbol]*],
    [*#text(fill: white)[Peran & Implementasi di SIPESAT]*]
  ),
  [Boundary Class], [|O], [Komponen antarmuka pengguna: `LoginUI`, `FormPengajuanUI`, `VerifikasiTUUI`, `ApprovalKepsekUI`. Menangkap input dan menyajikan feedback visual.],
  [Control Class], [↺O], [Pengendali logika bisnis: `AuthController`, `SuratController`, `VerifikasiController`, `ApprovalController`. Menjalankan aturan validasi dan kalkulasi.],
  [Entity Class], [_O_], [Struktur persistensi data: `User`, `SuratPengajuan`, `MasterJenisSurat`, `AuditLog`. Menyimpan dan memperbarui status pada basis data PostgreSQL/MySQL.]
)

#v(0.4cm)
== 3.1 Ringkasan Interaksi Skenario Utama
1. *Skenario Pengajuan Surat*: `Siswa` $arrow.r$ `FormPengajuanUI` $arrow.r$ `SuratController` $arrow.r$ `StorageService` $arrow.r$ `SuratPengajuan (Entity)` $arrow.r$ Balasan kode tiket diteruskan kembali ke UI siswa. Frame `alt` membedakan respon validasi berkas valid vs file melebihi 2 MB.
2. *Skenario Verifikasi Dokumen*: `Staf TU` $arrow.r$ `VerifikasiTUUI` $arrow.r$ `VerifikasiController` $arrow.r$ `SuratPengajuan (Entity)` $arrow.r$ Eksekusi perubahan status dan pengiriman notifikasi pembaruan status.
3. *Skenario Persetujuan Kepsek*: `Kepala Sekolah` $arrow.r$ `ApprovalKepsekUI` $arrow.r$ `ApprovalController` $arrow.r$ `DocumentEngine` (Generate No. Surat & QR Code) $arrow.r$ `SuratPengajuan (Entity)` update status `SELESAI_SIAP_UNDUH`.

#v(0.8cm)
// BAB IV
#heading(level: 1)[BAB IV: KESIMPULAN & BERKAS DIAGRAM DRAW.IO]

Pemodelan Activity Diagram dan Sequence Diagram pada sistem SIPESAT telah memenuhi 100% kaidah materi bahan ajar RPL UNINDRA Pertemuan 04. Seluruh diagram visual interaktif lengkap dengan simbol resmi tersimpan pada berkas:
- *`tugas-4-activity-sequence.drawio`* *(5 Tab Lengkap: Simbol Resmi, Activity Siswa, Activity Petugas, Activity Terpadu, Sequence Diagrams BCE)*.
