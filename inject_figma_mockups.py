import os
import shutil
import subprocess

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

FIGMA_ARTBOARDS_TYPST = r"""
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
"""

# 1. Inject into tugas-7-figma-uiux.typ
with open(os.path.join(RPL_DIR, "tugas-7-figma-uiux.typ"), "r", encoding="utf-8") as f:
    t7 = f.read()

if "figma_artboards" not in t7:
    t7 = t7.replace(
        "= BAB III: KATALOG MOCKUP ANTARMUKA FIGMA (8 LAYAR UTAMA)",
        FIGMA_ARTBOARDS_TYPST
        + "\n= BAB III: VISUALISASI MOCKUP ANTARMUKA FIGMA & 8 LAYAR UTAMA\n\nBerikut adalah hasil perancangan antarmuka visual (_High-Fidelity Figma Artboards_) untuk layanan Siswa dan Petugas Tata Usaha pada sistem SIPESAT:\n\n#figure(\n  figma_artboards,\n  kind: image,\n  caption: [Hasil Desain Antarmuka Figma SIPESAT (Frame 01 Login, Frame 02 Form & Stepper Siswa, Frame 03 Verifikasi TU, Frame 04 Cetak Surat Resmi Ber-QR Code)]\n)\n\n#v(0.2cm)\n== 3.1 Rincian 8 Layar Utama pada Prototipe Figma"
    )
    with open(os.path.join(RPL_DIR, "tugas-7-figma-uiux.typ"), "w", encoding="utf-8") as f:
        f.write(t7)

subprocess.run(["typst", "compile", os.path.join(RPL_DIR, "tugas-7-figma-uiux.typ"), os.path.join(RPL_DIR, "tugas-7-figma-uiux.pdf")], check=True)
print("[OK] Compiled tugas-7-figma-uiux.pdf with visual Figma artboards!")

# 2. Inject into build_unified_master_book.py after Section 7.3 so Page 19 is 100% full and Page 20 shows the 4 Artboards
with open(os.path.join(RPL_DIR, "build_unified_master_book.py"), "r", encoding="utf-8") as f:
    bscript = f.read()

if "figma_artboards" not in bscript:
    target_str = "// =====================================================================\n// BAB VIII — DELIVERABLE 8:"
    replacement_str = (
        FIGMA_ARTBOARDS_TYPST
        + "\n== 7.4 Visualisasi Hasil Desain Antarmuka Figma (4 Artboard Utama)\n"
        + "#figure(\n  figma_artboards,\n  kind: image,\n  caption: [Hasil Desain Antarmuka Figma SIPESAT (Frame 01 Login Dual-Role, Frame 02 Form Pengajuan & Stepper Siswa, Frame 03 Dashboard & Verifikasi TU, Frame 04 Surat Resmi A4 Ber-QR Code)]\n)\n\n#pagebreak()\n\n"
        + target_str
    )
    bscript = bscript.replace(target_str, replacement_str)

# Also update build_unified_master_book.py to compile to LAPORAN_FINAL_10_DELIVERABLES_RPL_SIPESAT_KELOMPOK_7.pdf and copy to LAPORAN_LENGKAP if not locked
bscript = bscript.replace(
    'res = subprocess.run(["typst", "compile", TYP_PATH, PDF_LAPORAN], capture_output=True, text=True)',
    'PDF_FINAL = os.path.join(RPL_DIR, "LAPORAN_FINAL_10_DELIVERABLES_RPL_SIPESAT_KELOMPOK_7.pdf")\nres = subprocess.run(["typst", "compile", TYP_PATH, PDF_FINAL], capture_output=True, text=True)\nif res.returncode == 0:\n    try:\n        shutil.copy2(PDF_FINAL, PDF_LAPORAN)\n        print("[OK] Updated LAPORAN_LENGKAP_PROJEK_RPL_SIPESAT_KELOMPOK_7.pdf")\n    except PermissionError:\n        print("[INFO] LAPORAN_LENGKAP is open in viewer; updated LAPORAN_FINAL_10_DELIVERABLES_RPL_SIPESAT_KELOMPOK_7.pdf")'
)
bscript = bscript.replace(
    'print(f"Size: {os.path.getsize(PDF_LAPORAN) / 1024:.2f} KB")',
    'print(f"Size: {os.path.getsize(PDF_FINAL) / 1024:.2f} KB")'
)
bscript = bscript.replace(
    'shutil.copy2(PDF_LAPORAN, PDF_BUNDEL)',
    'shutil.copy2(PDF_FINAL, PDF_BUNDEL)'
)

with open(os.path.join(RPL_DIR, "build_unified_master_book.py"), "w", encoding="utf-8") as f:
    f.write(bscript)

subprocess.run(["python", os.path.join(RPL_DIR, "build_unified_master_book.py")], check=True)
print("[OK] Recompiled unified master book with visual Figma artboards!")
