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


// ==================== KOMPONEN VEKTOR MOCKUP FIGMA SIPESAT ====================
#let figma_artboards = [
  #set par(justify: false, first-line-indent: 0pt, leading: 0.48em)
  #set text(font: "Times New Roman", size: 8pt)

  // BARIS 1: ARTBOARD 1 (LOGIN DUAL-ROLE) & ARTBOARD 2 (FORM PENGAJUAN & STEPPER SISWA)
  #grid(
    columns: (1fr, 1fr),
    gutter: 10pt,

    // -------------------- ARTBOARD 1: LOGIN DUAL-ROLE --------------------
    block(width: 100%, stroke: 0.8pt + rgb("#94a3b8"), radius: 5pt, fill: rgb("#f8fafc"), clip: true)[
      #rect(width: 100%, fill: rgb("#1c2434"), inset: (x: 7pt, y: 4.5pt))[
        #grid(
          columns: (auto, 1fr, auto),
          gutter: 5pt,
          align(left + horizon)[
            #box(circle(radius: 2.5pt, fill: rgb("#ef4444")))
            #h(2pt)
            #box(circle(radius: 2.5pt, fill: rgb("#f59e0b")))
            #h(2pt)
            #box(circle(radius: 2.5pt, fill: rgb("#10b981")))
          ],
          align(center + horizon)[
            #rect(fill: rgb("#334155"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
              #text(fill: rgb("#e2e8f0"), size: 6.2pt, font: "Courier New")[localhost:3000/login]
            ]
          ],
          align(right + horizon)[#text(fill: rgb("#94a3b8"), size: 6.5pt)[Frame 01 • Login]]
        )
      ]
      #pad(x: 10pt, y: 5.5pt)[
        #align(center)[
          #rect(width: 22pt, height: 22pt, radius: 5pt, fill: rgb("#1c2434"))[
            #align(center + horizon)[#text(fill: rgb("#3b82f6"), weight: "bold", size: 10pt)[S]]
          ]
          #v(2pt)
          #text(size: 9.5pt, weight: "bold", fill: rgb("#0f172a"))[SIPESAT WEB]\
          #text(size: 7.2pt, fill: rgb("#64748b"))[Sistem Informasi Pengajuan Surat Siswa]\
          #v(2pt)
          #rect(fill: rgb("#e2e8f0"), radius: 8pt, inset: (x: 7pt, y: 2pt))[
            #text(size: 6.5pt, weight: "bold", fill: rgb("#334155"))[SMK NEGERI 1 CONTOH KOTA]
          ]
        ]
        #v(5pt)
        #rect(width: 100%, fill: white, stroke: 0.6pt + rgb("#cbd5e1"), radius: 5pt, inset: 8pt)[
          #rect(width: 100%, fill: rgb("#f1f5f9"), stroke: 0.4pt + rgb("#cbd5e1"), radius: 4pt, inset: 2pt)[
            #grid(
              columns: (1fr, 1fr),
              rect(width: 100%, fill: white, radius: 3pt, inset: 3pt)[
                #align(center)[#text(size: 7.2pt, weight: "bold", fill: rgb("#1e6eeb"))[Siswa (NISN)]]
              ],
              rect(width: 100%, inset: 3pt)[
                #align(center)[#text(size: 7.2pt, fill: rgb("#64748b"))[Petugas / Admin TU]]
              ]
            )
          ]
          #v(5pt)
          #text(size: 6.8pt, weight: "bold", fill: rgb("#334155"))[NOMOR INDUK SISWA NASIONAL (NISN)]
          #v(2pt)
          #rect(width: 100%, fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#1e6eeb"), radius: 3pt, inset: 4.5pt)[
            #text(size: 7.5pt, font: "Courier New", fill: rgb("#0f172a"))[0061234567]
          ]
          #v(4pt)
          #text(size: 6.8pt, weight: "bold", fill: rgb("#334155"))[KATA SANDI]
          #v(2pt)
          #rect(width: 100%, fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), radius: 3pt, inset: 4.5pt)[
            #grid(
              columns: (1fr, auto),
              text(size: 7.5pt, fill: rgb("#0f172a"))[••••••••],
              text(size: 6.5pt, fill: rgb("#64748b"))[\[Lihat\]]
            )
          ]
          #v(6pt)
          #rect(width: 100%, fill: rgb("#1e6eeb"), radius: 4pt, inset: 5pt)[
            #align(center)[#text(size: 7.8pt, weight: "bold", fill: white)[Masuk ke Sistem →]]
          ]
          #v(4pt)
          #align(center)[
            #text(size: 6.5pt, fill: rgb("#64748b"))[Belum punya akun? #text(fill: rgb("#1e6eeb"), weight: "bold")[Registrasi Akun Mandiri]]
          ]
        ]
      ]
    ],

    // -------------------- ARTBOARD 2: FORM PENGAJUAN & STEPPER SISWA --------------------
    block(width: 100%, stroke: 0.8pt + rgb("#94a3b8"), radius: 5pt, fill: rgb("#f8fafc"), clip: true)[
      #rect(width: 100%, fill: rgb("#1c2434"), inset: (x: 7pt, y: 4.5pt))[
        #grid(
          columns: (auto, 1fr, auto),
          gutter: 5pt,
          align(left + horizon)[
            #box(circle(radius: 2.5pt, fill: rgb("#ef4444")))
            #h(2pt)
            #box(circle(radius: 2.5pt, fill: rgb("#f59e0b")))
            #h(2pt)
            #box(circle(radius: 2.5pt, fill: rgb("#10b981")))
          ],
          align(center + horizon)[
            #rect(fill: rgb("#334155"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
              #text(fill: rgb("#e2e8f0"), size: 6.2pt, font: "Courier New")[localhost:3000/pengajuan/baru]
            ]
          ],
          align(right + horizon)[#text(fill: rgb("#94a3b8"), size: 6.5pt)[Frame 02 • Portal Siswa]]
        )
      ]
      #pad(x: 7pt, y: 5pt)[
        #rect(width: 100%, fill: white, stroke: 0.5pt + rgb("#cbd5e1"), radius: 4pt, inset: 5.5pt)[
          #grid(
            columns: (1fr, auto),
            [#text(size: 7.6pt, weight: "bold", fill: rgb("#0f172a"))[Pelacakan Tiket: `REQ-202609-0001`]],
            rect(fill: rgb("#dcfce7"), radius: 3pt, inset: (x: 5pt, y: 1.5pt))[
              #text(size: 6.3pt, weight: "bold", fill: rgb("#166534"))[DISETUJUI]
            ]
          )
          #v(4pt)
          #grid(
            columns: (1fr, 1fr, 1fr, 1fr),
            gutter: 3pt,
            rect(fill: rgb("#dcfce7"), radius: 2pt, inset: 2.5pt)[#align(center)[#text(size: 5.8pt, weight: "bold", fill: rgb("#166534"))[1. Diajukan ✓]]],
            rect(fill: rgb("#dcfce7"), radius: 2pt, inset: 2.5pt)[#align(center)[#text(size: 5.8pt, weight: "bold", fill: rgb("#166534"))[2. Verifikasi ✓]]],
            rect(fill: rgb("#dcfce7"), radius: 2pt, inset: 2.5pt)[#align(center)[#text(size: 5.8pt, weight: "bold", fill: rgb("#166534"))[3. No. Resmi ✓]]],
            rect(fill: rgb("#1e6eeb"), radius: 2pt, inset: 2.5pt)[#align(center)[#text(size: 5.8pt, weight: "bold", fill: white)[4. Unduh PDF]]],
          )
        ]
        #v(5pt)
        #rect(width: 100%, fill: white, stroke: 0.5pt + rgb("#cbd5e1"), radius: 4pt, inset: 6.5pt)[
          #text(size: 8pt, weight: "bold", fill: rgb("#0f172a"))[Formulir Pengajuan Surat Mandiri Siswa]
          #v(3pt)
          #line(length: 100%, stroke: 0.4pt + rgb("#e2e8f0"))
          #v(4pt)
          #text(size: 6.6pt, weight: "bold", fill: rgb("#334155"))[1. PILIH KATEGORI / JENIS SURAT RESMI]
          #v(2pt)
          #rect(width: 100%, fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), radius: 3pt, inset: 4pt)[
            #grid(
              columns: (1fr, auto),
              text(size: 7.2pt, fill: rgb("#0f172a"))[Surat Keterangan Siswa Aktif (`SK-AKTIF`)],
              text(size: 7pt, fill: rgb("#64748b"))[▼]
            )
          ]
          #v(4pt)
          #text(size: 6.6pt, weight: "bold", fill: rgb("#334155"))[2. MAKSUD & KEPERLUAN PENGAJUAN \*]
          #v(2pt)
          #rect(width: 100%, fill: rgb("#f8fafc"), stroke: 0.5pt + rgb("#cbd5e1"), radius: 3pt, inset: 4pt)[
            #text(size: 7pt, fill: rgb("#334155"))[Persyaratan perpanjangan tunjangan pendidikan orang tua di Dinas Pendidikan Provinsi.]
          ]
          #v(4pt)
          #text(size: 6.6pt, weight: "bold", fill: rgb("#334155"))[3. UNGGAH BERKAS SYARAT (PDF/JPG/PNG ≤ 2 MB)]
          #v(2pt)
          #rect(width: 100%, fill: rgb("#ecfdf5"), stroke: 0.5pt + rgb("#10b981"), radius: 3pt, inset: 4pt)[
            #grid(
              columns: (1fr, auto),
              text(size: 6.8pt, weight: "bold", fill: rgb("#065f46"))[✓ kartu_pelajar_ahmad.pdf (800 KB — Valid)],
              text(size: 6.5pt, fill: rgb("#dc2626"))[\[Hapus\]]
            )
          ]
          #v(5pt)
          #align(right)[
            #box(rect(fill: rgb("#f1f5f9"), stroke: 0.4pt + rgb("#cbd5e1"), radius: 3pt, inset: (x: 7pt, y: 3.5pt))[#text(size: 7pt, fill: rgb("#475569"))[Batal]])
            #h(4pt)
            #box(rect(fill: rgb("#1e6eeb"), radius: 3pt, inset: (x: 8pt, y: 3.5pt))[#text(size: 7pt, weight: "bold", fill: white)[Kirim Pengajuan Surat]])
          ]
        ]
      ]
    ]
  )

  #v(8pt)

  // BARIS 2: ARTBOARD 3 (DASHBOARD ANTREAN & VERIFIKASI TU) & ARTBOARD 4 (CETAK SURAT RESMI BER-QR)
  #grid(
    columns: (1fr, 1fr),
    gutter: 10pt,

    // -------------------- ARTBOARD 3: DASHBOARD ANTREAN & VERIFIKASI TU --------------------
    block(width: 100%, stroke: 0.8pt + rgb("#94a3b8"), radius: 5pt, fill: rgb("#f8fafc"), clip: true)[
      #rect(width: 100%, fill: rgb("#1c2434"), inset: (x: 7pt, y: 4.5pt))[
        #grid(
          columns: (auto, 1fr, auto),
          gutter: 5pt,
          align(left + horizon)[
            #box(circle(radius: 2.5pt, fill: rgb("#ef4444")))
            #h(2pt)
            #box(circle(radius: 2.5pt, fill: rgb("#f59e0b")))
            #h(2pt)
            #box(circle(radius: 2.5pt, fill: rgb("#10b981")))
          ],
          align(center + horizon)[
            #rect(fill: rgb("#334155"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
              #text(fill: rgb("#e2e8f0"), size: 6.2pt, font: "Courier New")[localhost:3000/admin/antrean]
            ]
          ],
          align(right + horizon)[#text(fill: rgb("#94a3b8"), size: 6.5pt)[Frame 03 • Panel Admin TU]]
        )
      ]
      #pad(x: 7pt, y: 5pt)[
        #grid(
          columns: (1fr, 1fr, 1fr, 1fr),
          gutter: 4pt,
          rect(width: 100%, fill: white, stroke: 0.5pt + rgb("#cbd5e1"), radius: 3pt, inset: 4pt)[
            #text(size: 6pt, fill: rgb("#64748b"))[Total Surat]\
            #text(size: 9pt, weight: "bold", fill: rgb("#0f172a"))[24]
          ],
          rect(width: 100%, fill: rgb("#fffbeb"), stroke: 0.5pt + rgb("#f59e0b"), radius: 3pt, inset: 4pt)[
            #text(size: 6pt, fill: rgb("#b45309"))[Menunggu]\
            #text(size: 9pt, weight: "bold", fill: rgb("#b45309"))[3]
          ],
          rect(width: 100%, fill: rgb("#eff6ff"), stroke: 0.5pt + rgb("#3b82f6"), radius: 3pt, inset: 4pt)[
            #text(size: 6pt, fill: rgb("#1d4ed8"))[Diproses]\
            #text(size: 9pt, weight: "bold", fill: rgb("#1d4ed8"))[2]
          ],
          rect(width: 100%, fill: rgb("#ecfdf5"), stroke: 0.5pt + rgb("#10b981"), radius: 3pt, inset: 4pt)[
            #text(size: 6pt, fill: rgb("#047857"))[Disetujui]\
            #text(size: 9pt, weight: "bold", fill: rgb("#047857"))[19]
          ],
        )
        #v(5pt)
        #rect(width: 100%, fill: white, stroke: 0.5pt + rgb("#cbd5e1"), radius: 4pt, inset: 5pt)[
          #text(size: 7.5pt, weight: "bold", fill: rgb("#0f172a"))[Antrean Verifikasi Permohonan Masuk (FIFO)]
          #v(3pt)
          #table(
            columns: (1.35fr, 1.25fr, 1.0fr, 0.9fr),
            align: (left + horizon, left + horizon, left + horizon, center + horizon),
            inset: 3pt,
            stroke: 0.3pt + rgb("#cbd5e1"),
            fill: (c, r) => if r == 0 { rgb("#f1f5f9") } else { none },
            [*#text(size: 6.2pt)[No. Resi]*], [*#text(size: 6.2pt)[Pemohon]*], [*#text(size: 6.2pt)[Jenis]*], [*#text(size: 6.2pt)[Status]*],
            [#text(size: 6pt, font: "Courier New")[REQ-2026-01]], [#text(size: 6.2pt)[Ahmad Fauzi]], [#text(size: 6.2pt)[SK-AKTIF]], [#text(size: 5.8pt, weight: "bold", fill: rgb("#047857"))[DISETUJUI]],
            [#text(size: 6pt, font: "Courier New")[REQ-2026-02]], [#text(size: 6.2pt)[Siti Nurhaliza]], [#text(size: 6.2pt)[BEASISWA]], [#text(size: 5.8pt, weight: "bold", fill: rgb("#1d4ed8"))[DIPROSES]],
            [#text(size: 6pt, font: "Courier New")[REQ-2026-03]], [#text(size: 6.2pt)[Budi Santoso]], [#text(size: 6.2pt)[SI-DISPEN]], [#text(size: 5.8pt, weight: "bold", fill: rgb("#b45309"))[MENUNGGU]],
          )
        ]
        #v(5pt)
        #rect(width: 100%, fill: white, stroke: 0.7pt + rgb("#1e6eeb"), radius: 4pt, inset: 5.5pt)[
          #text(size: 7.3pt, weight: "bold", fill: rgb("#1e3a8a"))[Panel Keputusan Verifikasi TU — `REQ-2026-02`]
          #v(2pt)
          #text(size: 6.4pt, fill: rgb("#475569"))[Berkas Lampiran: `rapor_siti_smt1_4.pdf` (1,2 MB) • #text(fill: rgb("#1e6eeb"), weight: "bold")[\[Pratinjau Dokumen\]]]
          #v(3pt)
          #rect(width: 100%, fill: rgb("#f8fafc"), stroke: 0.4pt + rgb("#cbd5e1"), radius: 2.5pt, inset: 3.5pt)[
            #text(size: 6.4pt, fill: rgb("#64748b"))[Catatan Petugas TU (Wajib diisi bila ditolak): Berkas lengkap dan sesuai data induk.]
          ]
          #v(4pt)
          #grid(
            columns: (1fr, 1fr),
            gutter: 5pt,
            rect(width: 100%, fill: rgb("#ef4444"), radius: 3pt, inset: 3.5pt)[
              #align(center)[#text(size: 6.6pt, weight: "bold", fill: white)[✕ Tolak & Minta Revisi]]
            ],
            rect(width: 100%, fill: rgb("#10b981"), radius: 3pt, inset: 3.5pt)[
              #align(center)[#text(size: 6.6pt, weight: "bold", fill: white)[✓ Setujui & Terbit Surat]]
            ]
          )
        ]
      ]
    ],

    // -------------------- ARTBOARD 4: CETAK SURAT RESMI A4 BER-QR CODE --------------------
    block(width: 100%, stroke: 0.8pt + rgb("#94a3b8"), radius: 5pt, fill: rgb("#e2e8f0"), clip: true)[
      #rect(width: 100%, fill: rgb("#1c2434"), inset: (x: 7pt, y: 4.5pt))[
        #grid(
          columns: (auto, 1fr, auto),
          gutter: 5pt,
          align(left + horizon)[
            #box(circle(radius: 2.5pt, fill: rgb("#ef4444")))
            #h(2pt)
            #box(circle(radius: 2.5pt, fill: rgb("#f59e0b")))
            #h(2pt)
            #box(circle(radius: 2.5pt, fill: rgb("#10b981")))
          ],
          align(center + horizon)[
            #rect(fill: rgb("#334155"), radius: 3pt, inset: (x: 6pt, y: 2pt))[
              #text(fill: rgb("#e2e8f0"), size: 6.2pt, font: "Courier New")[localhost:3000/cetak/req1]
            ]
          ],
          align(right + horizon)[#text(fill: rgb("#94a3b8"), size: 6.5pt)[Frame 04 • Surat Resmi QR]]
        )
      ]
      #pad(x: 8pt, y: 5pt)[
        #rect(width: 100%, fill: white, stroke: 0.6pt + rgb("#94a3b8"), radius: 2pt, inset: 8pt)[
          #align(center)[
            #text(size: 6.4pt, weight: "bold")[PEMERINTAH PROVINSI JAWA BARAT • DINAS PENDIDIKAN]\
            #text(size: 8.5pt, weight: "bold")[SMK NEGERI 1 CONTOH KOTA]\
            #text(size: 5.7pt, fill: rgb("#475569"))[Jalan Pendidikan No. 123 Komplek Sekolah Menengah, Telp. (021) 8876543]
            #v(2pt)
            #line(length: 100%, stroke: 1.2pt + black)
            #v(4pt)
            #text(size: 7.8pt, weight: "bold", underline(offset: 1.5pt)[SURAT KETERANGAN SISWA AKTIF])\
            #text(size: 6.4pt, font: "Courier New")[Nomor: 421.3/088/SMKN1/SK-AKTIF/IX/2026]
          ]
          #v(4pt)
          #text(size: 6.4pt)[Yang bertanda tangan di bawah ini menerangkan bahwa:]
          #v(2pt)
          #pad(left: 6pt)[
            #grid(
              columns: (2.1cm, 0.2cm, 1fr),
              row-gutter: 2pt,
              [#text(size: 6.3pt, weight: "bold")[Nama Lengkap]], [:], [#text(size: 6.3pt, weight: "bold")[AHMAD FAUZI PRATAMA]],
              [#text(size: 6.3pt, weight: "bold")[NISN / Kelas]], [:], [#text(size: 6.3pt)[0061234567 / XII RPL 1]],
              [#text(size: 6.3pt, weight: "bold")[Jurusan]], [:], [#text(size: 6.3pt)[Rekayasa Perangkat Lunak]],
              [#text(size: 6.3pt, weight: "bold")[Keperluan]], [:], [#text(size: 6.3pt)[Perpanjangan tunjangan pendidikan]],
            )
          ]
          #v(3pt)
          #text(size: 6.2pt)[Adalah benar terdaftar sebagai siswa aktif pada SMK Negeri 1 Contoh Kota Tahun Ajaran 2026/2027 dan berkelakuan baik.]
          #v(6pt)
          #grid(
            columns: (1fr, 1.15fr),
            gutter: 6pt,
            align(left + horizon)[
              #rect(stroke: 0.5pt + rgb("#94a3b8"), radius: 3pt, inset: 3.5pt)[
                #grid(
                  columns: (auto, 1fr),
                  gutter: 4pt,
                  rect(width: 20pt, height: 20pt, stroke: 0.8pt + black, inset: 2pt)[
                    #grid(
                      columns: (1fr, 1fr, 1fr),
                      rows: (1fr, 1fr, 1fr),
                      gutter: 1pt,
                      rect(fill: black), rect(fill: white), rect(fill: black),
                      rect(fill: white), rect(fill: black), rect(fill: black),
                      rect(fill: black), rect(fill: white), rect(fill: black),
                    )
                  ],
                  [
                    #text(size: 5.5pt, weight: "bold", fill: rgb("#047857"))[TTE QR RESMI]\
                    #text(size: 5.1pt, font: "Courier New", fill: rgb("#475569"))[REQ-2026-01]\
                    #text(size: 5pt, fill: rgb("#64748b"))[Verifikasi Publik]
                  ]
                )
              ]
            ],
            align(left)[
              #text(size: 6pt)[Ditetapkan di: Kota Contoh]\
              #text(size: 6pt)[Tanggal: 19 November 2026]\
              #text(size: 6.1pt, weight: "bold")[Tata Usaha SMK Negeri 1]
              #v(7pt)
              #text(size: 6.3pt, weight: "bold", underline[Drs. H. Mulyadi, M.Pd.])\
              #text(size: 5.6pt, font: "Courier New")[NIP. 19680512 199403 1 004]
            ]
          )
        ]
      ]
    ]
  )
]

= BAB III: VISUALISASI MOCKUP ANTARMUKA FIGMA & 8 LAYAR UTAMA

Berikut adalah hasil perancangan antarmuka visual (_High-Fidelity Figma Artboards_) untuk layanan Siswa dan Petugas Tata Usaha pada sistem SIPESAT:

#figure(
  figma_artboards,
  kind: image,
  caption: [Hasil Desain Antarmuka Figma SIPESAT (Frame 01 Login, Frame 02 Form & Stepper Siswa, Frame 03 Verifikasi TU, Frame 04 Cetak Surat Resmi Ber-QR Code)]
)

#v(0.2cm)
== 3.1 Rincian 8 Layar Utama pada Prototipe Figma

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
