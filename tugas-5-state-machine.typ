#set document(
  title: "Tugas 5 RPL: Perancangan State Machine Diagram - SIPESAT",
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
    TUGAS 5: PERANCANGAN STATE MACHINE DIAGRAM
  ]
  #v(1.0cm)
  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\
    #text(size: 11pt, weight: "regular")[_Pemodelan Siklus Hidup Entitas Dokumen Permohonan Surat Siswa (tb_pengajuan_surat)_]
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

= BAB I: PENDAHULUAN & LANDASAN TEORI
== 1.1 Gambaran Umum Proyek SIPESAT
Sistem Informasi Pengajuan Surat Siswa Berbasis Web (*SIPESAT*) mengotomatisasi proses birokrasi pengajuan surat keterangan siswa, rekomendasi beasiswa, dan dispensasi sekolah.

== 1.2 Konsep Dasar State Machine Diagram (UML 2.5)
State Machine Diagram memodelkan siklus hidup diskret dari suatu objek tunggal, mulai dari inisialisasi awal hingga terminasi akhir, mencakup keadaan (*state*), stimulus pemicu (*trigger*), *guard condition*, dan aksi komputasi otomatis (*actions*).

#pagebreak()

= BAB II: PERANCANGAN STATE MACHINE DIAGRAM SIPESAT
== 2.1 Diagram Siklus Hidup Permohonan Surat Siswa (Draw.io Native)

#align(center)[
  #image("assets/diagram_statemachine.png", width: 100%)
  #v(4pt)
  #text(size: 9.5pt, style: "italic")[Gambar 2.1: State Machine Diagram Siklus Hidup Permohonan Surat Siswa (100% Bebas Tabrakan)]
]

#v(0.5cm)
== 2.2 Uraian Status Keadaan (State) Surat
1. *DRAFT*: Keadaan saat siswa membuka form pengajuan, mengisi keperluan, dan mengunggah dokumen prasyarat (file $<= 2$ MB).
2. *MENUNGGU_VERIFIKASI*: Setelah siswa submit permohonan. Sistem menerbitkan kode tiket resi unik dan berkas masuk antrean verifikasi TU.
3. *DITOLAK_PERLU_REVISI*: Keadaan jika berkas ditolak TU karena buram/kurang. Siswa diizinkan mengunggah ulang perbaikan berkas.
4. *DIVERIFIKASI_TU*: Keadaan saat TU menyetujui berkas, menetapkan nomor agenda masuk, dan meneruskan berkas ke antrean Kepala Sekolah.
5. *DISETUJUI_KEPSEK*: Keadaan saat Kepala Sekolah menyetujui penerbitan surat, sistem generate nomor surat keluar resmi dan kode QR TTE.
6. *SELESAI_SIAP_UNDUH*: Mesin kompilasi PDF menyatukan kop sekolah, data siswa, dan stempel QR menjadi file PDF resmi siap diunduh.
7. *DIARSIPKAN*: Surat telah diunduh siswa atau masa retensi aktif berakhir, lalu dibekukan permanen ke arsip statis sekolah.

#pagebreak()

= BAB III: TABEL TRANSISI KEADAAN (STATE TRANSITION TABLE)
#table(
  columns: (2.8cm, 3.2cm, 3.8cm, 3.5cm, 2.7cm),
  align: (center, left, left, left, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[State Asal]*], [*#text(fill: white)[Trigger]*], [*#text(fill: white)[Guard]*], [*#text(fill: white)[Action]*], [*#text(fill: white)[State Tujuan]*]),
  [INITIAL (●)], [openMenuPengajuan()], [user_authenticated == true], [initFormPayload()], [DRAFT],
  [DRAFT], [submitPermohonan()], [form_valid && file <= 2MB], [generateTicketCode(), notifyTU()], [MENUNGGU_VERIFIKASI],
  [MENUNGGU_VERIFIKASI], [rejectTU()], [berkas_kurang || buram], [setCatatanRevisi(), alertSiswa()], [DITOLAK_PERLU_REVISI],
  [DITOLAK_PERLU_REVISI], [reuploadBerkas()], [file_revisi_valid == true], [updateLampiran(), notifyTU()], [MENUNGGU_VERIFIKASI],
  [MENUNGGU_VERIFIKASI], [approveTU()], [berkas_lengkap & absah], [setNoAgenda(), forwardToKepsek()], [DIVERIFIKASI_TU],
  [DIVERIFIKASI_TU], [approveKepsek()], [validasi_disetujui == true], [generateNoSurat(), createQR_TTE()], [DISETUJUI_KEPSEK],
  [DISETUJUI_KEPSEK], [autoGeneratePDF()], [pdf_compiled == true], [saveToStorage(), notifySiswa()], [SELESAI_SIAP_UNDUH],
  [SELESAI_SIAP_UNDUH], [unduhSurat()], [retention_expired], [freezeToAgendaArsip()], [DIARSIPKAN],
)

#v(0.8cm)
= BAB IV: PENUTUP
Seluruh diagram visual interaktif State Machine tersimpan pada berkas Draw.io master:
- *`tugas-5-state-machine.drawio`* *(1 Tab Tunggal Bersih, 0 Tabrakan Garis)*.
