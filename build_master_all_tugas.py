import os
import subprocess
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"
ASSETS_DIR = os.path.join(RPL_DIR, "assets")

IMG_USECASE = os.path.join(ASSETS_DIR, "diagram_usecase.png")
IMG_SEQUENCE = os.path.join(ASSETS_DIR, "diagram_sequence.png")
IMG_ACTIVITY = os.path.join(ASSETS_DIR, "diagram_activity.png")
IMG_STATEMACHINE = os.path.join(ASSETS_DIR, "diagram_statemachine.png")

# Verify all images exist
for img in [IMG_USECASE, IMG_SEQUENCE, IMG_ACTIVITY, IMG_STATEMACHINE]:
    if not os.path.exists(img):
        raise FileNotFoundError(f"Missing diagram asset: {img}")

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="D1D5DB", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_docx_base(title_tugas, subtitle_tugas):
    doc = docx.Document()
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(4.0)
    section.bottom_margin = Cm(3.0)
    section.left_margin = Cm(4.0)
    section.right_margin = Cm(3.0)

    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Times New Roman'
    style_normal.font.size = Pt(12)
    style_normal.font.color.rgb = RGBColor(0, 0, 0)
    style_normal.paragraph_format.line_spacing = 1.5
    style_normal.paragraph_format.space_after = Pt(0)
    style_normal.paragraph_format.space_before = Pt(0)

    # COVER
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("TUGAS REKAYASA PERANGKAT LUNAK (RPL)\n" + title_tugas.upper())
    r.bold = True
    r.font.size = Pt(14)
    p.paragraph_format.space_after = Pt(16)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run(subtitle_tugas + "\nStudi Kasus: Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)")
    r_sub.italic = True
    r_sub.font.size = Pt(11.5)
    p_sub.paragraph_format.space_after = Pt(24)

    # Box Identitas Kampus
    p_kampus = doc.add_paragraph()
    p_kampus.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_k = p_kampus.add_run("UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)\nFAKULTAS TEKNIK DAN ILMU KOMPUTER\nPROGRAM STUDI TEKNIK INFORMATIKA\n2026/2027")
    r_k.bold = True
    r_k.font.size = Pt(11)
    p_kampus.paragraph_format.space_after = Pt(22)

    # Kelompok Table
    table_kel = doc.add_table(rows=1, cols=3)
    table_kel.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table_kel.rows[0].cells
    hdr[0].text = "No."
    hdr[1].text = "Nama Anggota"
    hdr[2].text = "NPM"
    for c in hdr:
        set_cell_background(c, "1E293B")
        for p_c in c.paragraphs:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r_c in p_c.runs:
                r_c.font.color.rgb = RGBColor(255, 255, 255)
                r_c.bold = True
                r_c.font.size = Pt(10)

    members = [
        ("1", "Adam Wahyu Kurniawan (Lead Architect & SWE)", "202343500510"),
        ("2", "Fathu Rahman (Business Analyst)", "202343500467"),
        ("3", "Surya Edi Saputra (QA & Technical Writer)", "202343500468"),
        ("4", "Rizqi Muh. Al Hakimi (Database Specialist)", "202343500449"),
    ]
    for m in members:
        row = table_kel.add_row().cells
        row[0].text = m[0]
        row[1].text = m[1]
        row[2].text = m[2]
        row[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for idx, c in enumerate(row):
            set_cell_margins(c, 80, 80, 100, 100)
            c.paragraphs[0].runs[0].font.size = Pt(10)

    set_table_borders(table_kel)
    doc.add_page_break()
    return doc

def add_p(doc, text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, bold=False, italic=False, size=12, indent=True, space_after=6):
    p = doc.add_paragraph()
    p.alignment = align
    if indent and align == WD_ALIGN_PARAGRAPH.JUSTIFY:
        p.paragraph_format.first_line_indent = Cm(1.25)
    else:
        p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.5
    if text:
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.name = 'Times New Roman'
        r.font.size = Pt(size)
    return p

def add_h1(doc, title):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(title)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    return p

def add_h2(doc, title):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.5
    r = p.add_run(title)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    return p

def add_diagram_image(doc, img_path, caption):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(10)
    p_img.paragraph_format.space_after = Pt(4)
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Cm(14.0))

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_after = Pt(12)
    r_cap = p_cap.add_run(caption)
    r_cap.italic = True
    r_cap.font.size = Pt(10)
    r_cap.font.name = 'Times New Roman'

# =========================================================================
# 1. BUILD TUGAS 2 DOCX & TYPST (SRS WIEGERS)
# =========================================================================
print("--- [1/4] Building Tugas 2 (SRS IEEE / Karl Wiegers) ---")
doc2 = build_docx_base("TUGAS 2: SPESIFIKASI KEBUTUHAN PERANGKAT LUNAK (SRS)", "Standar IEEE Std 830-1998 / Karl Wiegers SRS Template")
add_h1(doc2, "BAB I: PENDAHULUAN")
add_h2(doc2, "1.1 Tujuan Dokumen")
add_p(doc2, "Dokumen Spesifikasi Kebutuhan Perangkat Lunak (Software Requirements Specification - SRS) ini disusun untuk mendefinisikan secara menyeluruh kebutuhan fungsional dan nonfungsional dari Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT). Dokumen ini berfungsi sebagai acuan tunggal (single source of truth) antara mahasiswa, tim pengembang, dosen pembimbing, dan pihak sekolah.")

add_h2(doc2, "1.2 Ruang Lingkup Produk")
add_p(doc2, "SIPESAT adalah portal layanan mandiri daring yang mendigitalkan seluruh siklus hidup surat keterangan siswa, mulai dari pengajuan berkas (maksimal 2 MB), verifikasi dan disposisi berkas oleh staf Tata Usaha, penerbitan nomor agenda masuk, hingga pengesahan dan penerbitan surat resmi berkop sekolah dengan tanda tangan digital QR Code.")

add_h1(doc2, "BAB II: DESKRIPSI KESELURUHAN & RANCANGAN ARSITEKTUR")
add_h2(doc2, "2.1 Perspektif Produk & Peran Pengguna")
add_p(doc2, "Sistem menerapkan pembatasan hak akses berbasis peran (RBAC) yang membagi kewenangan pengguna secara tegas:")
add_p(doc2, "1. Siswa: Mengisi formulir keperluan, melampirkan berkas persyaratan digital, memantau posisi berkas secara real-time, dan mengunduh berkas PDF resmi.")
add_p(doc2, "2. Petugas Tata Usaha (TU): Memeriksa kelayakan dan keabsahan berkas, memberikan catatan penolakan jika buram, menerbitkan nomor surat resmi, dan mencetak laporan rekapitulasi bulanan.")

add_h1(doc2, "BAB III: LAMPIRAN RANCANGAN DIAGRAM SISTEM")
add_h2(doc2, "3.1 Lampiran Rancangan: Use Case Diagram SIPESAT (Draw.io Native)")
add_p(doc2, "Berdasarkan spesifikasi kebutuhan fungsional yang telah dipetakan, berikut adalah rancangan Use Case Diagram terpadu sistem SIPESAT yang memodelkan interaksi antara Siswa dan Petugas TU:")
add_diagram_image(doc2, IMG_USECASE, "Gambar 3.1: Rancangan Use Case Diagram Sistem SIPESAT (Draw.io Native - 100% Bebas Tabrakan)")

add_p(doc2, "Seluruh diagram visual interaktif yang menjadi dasar perancangan SRS ini tersimpan pada berkas Draw.io master:")
add_p(doc2, "- tugas-2-srs-wiegers.drawio (Format XML Native Draw.io: Tab 1 Diagram Konteks Arsitektur Produk & Tab 2 Use Case SRS Lampiran B)", indent=False, bold=True)

doc2_path = os.path.join(RPL_DIR, "tugas-2-srs-wiegers.docx")
doc2.save(doc2_path)
print(f"[OK] Saved {doc2_path}")

# Build Tugas 2 Typst
typst_tugas2 = f"""#set document(
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
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\\
    TUGAS 2: SPESIFIKASI KEBUTUHAN PERANGKAT LUNAK (SRS)
  ]
  #v(1.0cm)
  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\\
    #text(size: 10.5pt, weight: "regular")[_Standar Dokumentasi: IEEE Std 830-1998 / Karl Wiegers SRS Template_]
  ]
  #v(1.8cm)
  #rect(width: 5cm, height: 4.2cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt)[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[UNIVERSITAS\\ INDRAPRASTA PGRI\\ (UNINDRA)]
      #v(6pt)
      #text(size: 9.5pt, fill: rgb("#475569"))[FAKULTAS TEKNIK & ILMU KOMPUTER\\ TEKNIK INFORMATIKA]
    ]
  ]
  #v(1.8cm)
  #text(size: 11pt, weight: "bold")[Disusun Oleh (Kelompok 7 / Kelas RPL_XD):]
  #v(0.3cm)
  #table(
    columns: (0.8cm, 8.5cm, 3.5cm),
    align: (center, left, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 {{ rgb("#1e293b") }} else {{ none }},
    table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Anggota]*], [*#text(fill: white)[NPM]*]),
    [1], [Adam Wahyu Kurniawan (Lead Architect & SWE)], [202343500510],
    [2], [Fathu Rahman (Business Analyst)], [202343500467],
    [3], [Surya Edi Saputra (QA & Technical Writer)], [202343500468],
    [4], [Rizqi Muh. Al Hakimi (Database Specialist)], [202343500449],
  )
  #v(1.2cm)
  #text(size: 11pt, weight: "bold")[JAKARTA\\ 2026/2027]
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
"""

with open(os.path.join(RPL_DIR, "tugas-2-srs-wiegers.typ"), "w", encoding="utf-8") as f:
    f.write(typst_tugas2)
print("[OK] Saved tugas-2-srs-wiegers.typ")


# =========================================================================
# 2. BUILD TUGAS 3 DOCX & TYPST (USE CASE & RBAC)
# =========================================================================
print("--- [2/4] Building Tugas 3 (Use Case & RBAC) ---")
doc3 = build_docx_base("TUGAS 3: PERANCANGAN USE CASE DIAGRAM & MATRIKS RBAC", "Pemodelan Batasan Sistem, Aktor Pengguna, dan Matriks Hak Akses")

add_h1(doc3, "BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM")
add_h2(doc3, "1.1 Deskripsi Proyek SIPESAT")
add_p(doc3, "Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) adalah sistem perangkat lunak yang dirancang untuk memodernisasi dan mengotomatisasi rantai birokrasi pengajuan surat keterangan di lingkungan sekolah menengah. Melalui SIPESAT, siswa dapat mengajukan surat kapan saja secara daring, mengunggah dokumen prasyarat, dan memantau status secara transparan.")

add_h1(doc3, "BAB II: PERANCANGAN USE CASE DIAGRAM SIPESAT")
add_h2(doc3, "2.1 Diagram Use Case Terpadu SIPESAT (Draw.io Native)")
add_p(doc3, "Berikut adalah rancangan visual Use Case Diagram SIPESAT yang memetakan batasan sistem, aktor Siswa, aktor Petugas TU, serta relasi stereotype <<include>> dan <<extend>>:")
add_diagram_image(doc3, IMG_USECASE, "Gambar 2.1: Use Case Diagram SIPESAT Standar UML 2.5 (Draw.io Native - 100% Bebas Tabrakan)")

add_h2(doc3, "2.2 Tabel Rincian Use Case Terdefinisi")
t_uc = doc3.add_table(rows=1, cols=4)
t_uc.alignment = WD_TABLE_ALIGNMENT.CENTER
h_uc = t_uc.rows[0].cells
h_uc[0].text = "Kode"
h_uc[1].text = "Nama Use Case"
h_uc[2].text = "Aktor"
h_uc[3].text = "Deskripsi Singkat"
for c in h_uc:
    set_cell_background(c, "1E293B")
    for p_c in c.paragraphs:
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r_c in p_c.runs:
            r_c.font.color.rgb = RGBColor(255, 255, 255)
            r_c.bold = True
            r_c.font.size = Pt(10)

usecases = [
    ("UC-01", "Login ke Sistem", "Siswa, TU", "Otentikasi akun pengguna menggunakan NISN/NIP dan kata sandi terenkripsi."),
    ("UC-01B", "Validasi Kredensial & Hak Akses", "Sistem (Include)", "Pengecekan keabsahan tanda tangan token JWT pada rute terproteksi."),
    ("UC-02", "Registrasi Akun Mandiri", "Siswa", "Pendaftaran akun baru siswa dengan verifikasi NISN ke database induk siswa."),
    ("UC-03", "Kelola Profil & Sandi", "Siswa, TU", "Pembaharuan kontak telepon, email aktif, dan pergantian kata sandi akun."),
    ("UC-04", "Logout Sesi", "Siswa, TU", "Penghapusan cookie sesi HttpOnly dan pencabutan token aktif di server."),
    ("UC-05", "Lihat Katalog & Syarat Surat", "Siswa", "Eksplorasi daftar jenis surat yang tersedia beserta panduan berkas pendukung wajib."),
    ("UC-06", "Mengajukan Permohonan Surat", "Siswa", "Pengisian formulir keperluan, penentuan tujuan pembuatan surat, dan kirim draf."),
    ("UC-07", "Unggah Berkas Syarat (PDF ≤ 2MB)", "Siswa (Include)", "Pengunggahan file bukti pendukung (PDF/JPG, batas maksimum 2 MB)."),
    ("UC-08", "Melacak Status Surat (Real-time)", "Siswa", "Pemantauan posisi proses dokumen secara live via Stepper Status."),
    ("UC-08A", "Melihat Catatan Koreksi / Revisi", "Siswa (Extend)", "Pembacaan feedback alasan penolakan berkas dan instruksi perbaikan."),
    ("UC-09", "Melihat Riwayat Pengajuan", "Siswa", "Peninjauan rekam jejak surat yang pernah diajukan di masa lalu."),
    ("UC-10", "Unduh Surat PDF Ber-QR Code", "Siswa", "Pengunduhan berkas PDF resmi berkop sekolah dengan validasi kode QR."),
    ("UC-11", "Dashboard Antrean TU", "Petugas TU", "Tinjauan metrik operasional: surat masuk, verifikasi, selesai, dan ditolak."),
    ("UC-12", "Kelola Antrean Surat Masuk", "Petugas TU", "Penyaringan dan pengurutan permohonan surat masuk berdasarkan tanggal masuk."),
    ("UC-13", "Verifikasi Berkas Dokumen", "Petugas TU", "Pemeriksaan isi berkas unggahan siswa terhadap data registrasi sekolah."),
    ("UC-14", "Setujui Permohonan (Approve)", "Petugas TU", "Pengesahan administratif surat permohonan yang telah memenuhi seluruh syarat."),
    ("UC-14A", "Terbitkan No. Surat & TTE QR Code", "TU (Include)", "Generate nomor agenda resmi sekolah otomatis dan kode hash QR Code."),
    ("UC-15", "Tolak Permohonan (Reject)", "Petugas TU", "Penolakan permohonan yang tidak memenuhi syarat atau berkas buram."),
    ("UC-15A", "Input Alasan & Catatan Penolakan", "TU (Include)", "Penyusunan catatan tertulis kekurangan berkas untuk ditindaklanjuti siswa."),
    ("UC-16", "Kelola Master Jenis Surat", "Petugas TU", "Manajemen jenis surat, perubahan syarat wajib, dan template isi naskah."),
    ("UC-17", "Kelola Data Siswa & Akun", "Petugas TU", "Pengawasan status akun, reset kata sandi bermasalah, dan aktivasi akun."),
    ("UC-18", "Ekspor Rekapitulasi Laporan", "Petugas TU", "Pembuatan laporan rekapitulasi persuratan ke format Excel atau PDF."),
]

for row_data in usecases:
    row = t_uc.add_row().cells
    for i, val in enumerate(row_data):
        row[i].text = val
        set_cell_margins(row[i], 60, 60, 80, 80)
        row[i].paragraphs[0].runs[0].font.size = Pt(9.5)
        if i == 0 or i == 2:
            row[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

set_table_borders(t_uc)

add_h1(doc3, "BAB III: MATRIKS HAK AKSES (ROLE-BASED ACCESS CONTROL)")
add_p(doc3, "Untuk menjamin keamanan sistem dan integritas data persuratan sekolah, setiap fungsi dipagari otorisasi ketat:")

t_rb = doc3.add_table(rows=1, cols=4)
t_rb.alignment = WD_TABLE_ALIGNMENT.CENTER
h_rb = t_rb.rows[0].cells
h_rb[0].text = "No."
h_rb[1].text = "Nama Use Case / Modul"
h_rb[2].text = "Role Siswa"
h_rb[3].text = "Role Petugas TU"
for c in h_rb:
    set_cell_background(c, "1E293B")
    for p_c in c.paragraphs:
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r_c in p_c.runs:
            r_c.font.color.rgb = RGBColor(255, 255, 255)
            r_c.bold = True
            r_c.font.size = Pt(10)

rbac_data = [
    ("1", "UC-01: Login ke Sistem", "Ya", "Ya"),
    ("2", "UC-02: Registrasi Akun Mandiri", "Ya", "Tidak"),
    ("3", "UC-03: Kelola Profil & Sandi", "Ya", "Ya"),
    ("4", "UC-04: Logout Sesi Pengguna", "Ya", "Ya"),
    ("5", "UC-05: Lihat Katalog & Syarat Surat", "Ya", "Ya (Kelola)"),
    ("6", "UC-06: Mengajukan Permohonan Surat", "Ya", "Tidak"),
    ("7", "UC-07: Unggah Berkas Syarat (PDF ≤ 2MB)", "Ya", "Tidak"),
    ("8", "UC-08: Melacak Status Surat (Real-time)", "Ya", "Tidak"),
    ("9", "UC-09: Melihat Riwayat Pengajuan", "Ya", "Tidak"),
    ("10", "UC-10: Unduh Surat PDF Ber-QR Code", "Ya", "Ya"),
    ("11", "UC-11: Dashboard Antrean TU", "Tidak", "Ya"),
    ("12", "UC-12: Kelola Antrean Surat Masuk", "Tidak", "Ya"),
    ("13", "UC-13: Verifikasi Berkas Dokumen", "Tidak", "Ya"),
    ("14", "UC-14: Setujui Permohonan (Approve)", "Tidak", "Ya"),
    ("15", "UC-15: Tolak Permohonan (Reject)", "Tidak", "Ya"),
    ("16", "UC-16: Kelola Master Jenis Surat", "Tidak", "Ya"),
    ("17", "UC-17: Kelola Data Siswa & Akun", "Tidak", "Ya"),
    ("18", "UC-18: Ekspor Rekapitulasi Laporan", "Tidak", "Ya"),
]

for row_data in rbac_data:
    row = t_rb.add_row().cells
    for i, val in enumerate(row_data):
        row[i].text = val
        set_cell_margins(row[i], 60, 60, 80, 80)
        row[i].paragraphs[0].runs[0].font.size = Pt(9.5)
        if i == 0 or i >= 2:
            row[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

set_table_borders(t_rb)

add_h1(doc3, "BAB IV: PENUTUP")
add_p(doc3, "Perancangan Use Case Diagram dan Matriks Hak Akses (RBAC) pada sistem SIPESAT telah diselaraskan dengan standar akademik UNINDRA. Berkas master visual native tersimpan pada:")
add_p(doc3, "- tugas-3-usecase.drawio (Format XML Native Draw.io - 1 Tab Tunggal)", indent=False, bold=True)

doc3_path = os.path.join(RPL_DIR, "tugas-3-usecase.docx")
doc3.save(doc3_path)
print(f"[OK] Saved {doc3_path}")

# Update Tugas 3 Typst
typst_tugas3 = f"""#set document(
  title: "Tugas 3 RPL: Perancangan Use Case Diagram & Matriks RBAC - SIPESAT",
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
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\\
    TUGAS 3: PERANCANGAN USE CASE DIAGRAM & MATRIKS HAK AKSES (RBAC)
  ]
  #v(1.0cm)
  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\\
    #text(size: 11pt, weight: "regular")[_Studi Kasus: Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah_]
  ]
  #v(1.8cm)
  #rect(width: 5cm, height: 4.2cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt)[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[UNIVERSITAS\\ INDRAPRASTA PGRI\\ (UNINDRA)]
      #v(6pt)
      #text(size: 9.5pt, fill: rgb("#475569"))[FAKULTAS TEKNIK & ILMU KOMPUTER\\ TEKNIK INFORMATIKA]
    ]
  ]
  #v(1.8cm)
  #text(size: 11pt, weight: "bold")[Disusun Oleh (Kelompok 7 / Kelas RPL_XD):]
  #v(0.3cm)
  #table(
    columns: (0.8cm, 8.5cm, 3.5cm),
    align: (center, left, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 {{ rgb("#1e293b") }} else {{ none }},
    table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Anggota]*], [*#text(fill: white)[NPM]*]),
    [1], [Adam Wahyu Kurniawan (Lead Architect & SWE)], [202343500510],
    [2], [Fathu Rahman (Business Analyst)], [202343500467],
    [3], [Surya Edi Saputra (QA & Technical Writer)], [202343500468],
    [4], [Rizqi Muh. Al Hakimi (Database Specialist)], [202343500449],
  )
  #v(1.2cm)
  #text(size: 11pt, weight: "bold")[JAKARTA\\ 2026/2027]
]

#pagebreak()

= BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM
== 1.1 Deskripsi Proyek SIPESAT
Sistem Informasi Pengajuan Surat Siswa Berbasis Web (*SIPESAT*) adalah sistem perangkat lunak yang dirancang untuk memodernisasi dan mengotomatisasi rantai birokrasi pengajuan surat keterangan di lingkungan sekolah menengah.

== 1.2 Tujuan Pemodelan Use Case Diagram
1. Mendefinisikan batasan sistem (*system boundary*) secara tegas.
2. Mengidentifikasi seluruh aktor yang berinteraksi langsung dengan sistem.
3. Menjelaskan relasi dependensi antarfungsi menggunakan stereotype `<<include>>` (keharusan) dan `<<extend>>` (perluasan opsional).

#pagebreak()

= BAB II: PERANCANGAN USE CASE DIAGRAM SIPESAT
== 2.1 Diagram Use Case Terpadu (Draw.io Native)

#align(center)[
  #image("assets/diagram_usecase.png", width: 100%)
  #v(4pt)
  #text(size: 9.5pt, style: "italic")[Gambar 2.1: Use Case Diagram SIPESAT Standar UML 2.5 (100% Bebas Tabrakan)]
]

#v(0.5cm)
== 2.2 Tabel Rincian Use Case Terdefinisi
#table(
  columns: (1.5cm, 4.5cm, 3.0cm, 5.5cm),
  align: (center, left, center, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 {{ rgb("#1e293b") }} else if calc.even(row) {{ rgb("#f8fafc") }} else {{ none }},
  table.header([*#text(fill: white)[Kode]*], [*#text(fill: white)[Nama Use Case]*], [*#text(fill: white)[Aktor]*], [*#text(fill: white)[Deskripsi]*]),
  [UC-01], [Login ke Sistem], [Siswa, TU], [Otentikasi pengguna via NISN/NIP dan kata sandi terenkripsi.],
  [UC-01B], [Validasi Kredensial & Hak Akses], [Sistem (Include)], [Pengecekan keabsahan JWT pada rute terproteksi.],
  [UC-02], [Registrasi Akun Mandiri], [Siswa], [Pendaftaran akun baru siswa dengan validasi NISN ke database.],
  [UC-03], [Kelola Profil & Sandi], [Siswa, TU], [Pembaharuan data profil, email, dan ganti kata sandi.],
  [UC-04], [Logout Sesi], [Siswa, TU], [Penghapusan token JWT dan pembersihan sesi aktif.],
  [UC-05], [Lihat Katalog & Syarat Surat], [Siswa], [Eksplorasi daftar jenis surat beserta panduan syarat wajib.],
  [UC-06], [Mengajukan Permohonan Surat], [Siswa], [Pengisian formulir keperluan dan pemilihan jenis surat.],
  [UC-07], [Unggah Berkas Syarat (PDF ≤ 2MB)], [Siswa (Include)], [Unggah berkas bukti pendukung dengan validasi batas 2 MB.],
  [UC-08], [Melacak Status Surat (Real-time)], [Siswa], [Pemantauan status pengajuan secara live via Stepper Timeline.],
  [UC-08A], [Melihat Catatan Koreksi / Revisi], [Siswa (Extend)], [Peninjauan feedback alasan penolakan dan perbaikan berkas.],
  [UC-09], [Melihat Riwayat Pengajuan], [Siswa], [Arsip rekam jejak surat yang pernah diajukan sebelumnya.],
  [UC-10], [Unduh Surat PDF Ber-QR Code], [Siswa], [Pengunduhan file PDF resmi berkop sekolah dan kode QR.],
  [UC-11], [Dashboard Antrean TU], [Petugas TU], [Tinjauan metrik statistik antrean operasional persuratan.],
  [UC-12], [Kelola Antrean Surat Masuk], [Petugas TU], [Penyaringan dan pengelolaan urutan surat masuk sekolah.],
  [UC-13], [Verifikasi Berkas Dokumen], [Petugas TU], [Pemeriksaan kelayakan berkas fisik/digital unggahan siswa.],
  [UC-14], [Setujui Permohonan (Approve)], [Petugas TU], [Persetujuan berkas yang memenuhi syarat kelengkapan.],
  [UC-14A], [Terbitkan No. Surat & TTE QR], [TU (Include)], [Generate nomor agenda keluar resmi dan kode QR stempel.],
  [UC-15], [Tolak Permohonan (Reject)], [Petugas TU], [Penolakan berkas buram atau tidak memenuhi syarat.],
  [UC-15A], [Input Alasan & Catatan Koreksi], [TU (Include)], [Penyusunan catatan evaluasi tertulis kepada siswa.],
  [UC-16], [Kelola Master Jenis Surat], [Petugas TU], [Pengelolaan katalog jenis surat dan template naskah.],
  [UC-17], [Kelola Data Siswa & Akun], [Petugas TU], [Manajemen akun siswa dan reset kata sandi bermasalah.],
  [UC-18], [Ekspor Rekapitulasi Laporan], [Petugas TU], [Penerbitan rekap laporan bulanan ke format Excel/PDF.],
)

#pagebreak()

= BAB III: MATRIKS HAK AKSES (ROLE-BASED ACCESS CONTROL)
#table(
  columns: (1.2cm, 7.5cm, 3.0cm, 3.0cm),
  align: (center, left, center, center),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 {{ rgb("#1e293b") }} else if calc.even(row) {{ rgb("#f8fafc") }} else {{ none }},
  table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Use Case / Modul]*], [*#text(fill: white)[Role Siswa]*], [*#text(fill: white)[Role Petugas TU]*]),
  [1], [UC-01: Login ke Sistem], [✅ Ya], [✅ Ya],
  [2], [UC-02: Registrasi Akun Mandiri], [✅ Ya], [❌ Tidak],
  [3], [UC-03: Kelola Profil & Sandi], [✅ Ya], [✅ Ya],
  [4], [UC-04: Logout Sesi Pengguna], [✅ Ya], [✅ Ya],
  [5], [UC-05: Lihat Katalog & Syarat Surat], [✅ Ya], [✅ Ya (Kelola)],
  [6], [UC-06: Mengajukan Permohonan Surat], [✅ Ya], [❌ Tidak],
  [7], [UC-07: Unggah Berkas Syarat (PDF ≤ 2MB)], [✅ Ya], [❌ Tidak],
  [8], [UC-08: Melacak Status Surat (Real-time)], [✅ Ya], [❌ Tidak],
  [9], [UC-09: Melihat Riwayat Pengajuan], [✅ Ya], [❌ Tidak],
  [10], [UC-10: Unduh Surat PDF Ber-QR Code], [✅ Ya], [✅ Ya],
  [11], [UC-11: Dashboard Antrean TU], [❌ Tidak], [✅ Ya],
  [12], [UC-12: Kelola Antrean Surat Masuk], [❌ Tidak], [✅ Ya],
  [13], [UC-13: Verifikasi Berkas Dokumen], [❌ Tidak], [✅ Ya],
  [14], [UC-14: Setujui Permohonan (Approve)], [❌ Tidak], [✅ Ya],
  [15], [UC-15: Tolak Permohonan (Reject)], [❌ Tidak], [✅ Ya],
  [16], [UC-16: Kelola Master Jenis Surat], [❌ Tidak], [✅ Ya],
  [17], [UC-17: Kelola Data Siswa & Akun], [❌ Tidak], [✅ Ya],
  [18], [UC-18: Ekspor Rekapitulasi Laporan], [❌ Tidak], [✅ Ya],
)

#v(0.8cm)
= BAB IV: PENUTUP
Seluruh diagram visual interaktif use case dapat diakses dan disunting pada berkas master:
- *`tugas-3-usecase.drawio`* (1 Tab Tunggal Bersih, 0 Tabrakan Garis).
"""

with open(os.path.join(RPL_DIR, "tugas-3-usecase.typ"), "w", encoding="utf-8") as f:
    f.write(typst_tugas3)
print("[OK] Saved tugas-3-usecase.typ")


# =========================================================================
# 3. BUILD TUGAS 4 DOCX & TYPST (ACTIVITY & SEQUENCE BCE)
# =========================================================================
print("--- [3/4] Building Tugas 4 (Activity & Sequence BCE) ---")
doc4 = build_docx_base("TUGAS 4: ACTIVITY & SEQUENCE DIAGRAM", "Pemodelan Alur Kerja Swimlane dan Arsitektur Interaksi BCE Sesuai Standar UNINDRA")

add_h1(doc4, "BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM")
add_h2(doc4, "1.1 Deskripsi Proyek SIPESAT")
add_p(doc4, "Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) membagi hak akses ke dalam 3 peran pengguna utama: Siswa (pemohon), Staf Tata Usaha (verifikator & pengelola), dan Kepala Sekolah (pengesah tanda tangan digital QR Code).")

add_h2(doc4, "1.2 Standar Kaidah Modul UNINDRA (Pertemuan 04)")
add_p(doc4, "Berdasarkan modul resmi yang dikembangkan oleh Koordinator Bu Millati Izzatillah, S.Kom., MMSI:")
add_p(doc4, "1. Activity Diagram: Wajib menerapkan format Swimlane (Aktor di kiri vs Sistem di tengah vs TU/Kepsek di kanan) serta teks uraian langkah bernomor.\n2. Sequence Diagram: Wajib menerapkan pola arsitektur Boundary-Control-Entity (BCE) dengan kotak pembatas alt untuk skenario valid vs tidak valid.", indent=False)

add_h1(doc4, "BAB II: PERANCANGAN ACTIVITY DIAGRAM (SWIMLANE UNINDRA)")
add_h2(doc4, "2.1 Diagram Alur Terpadu Pengajuan Surat Siswa (Draw.io Native)")
add_p(doc4, "Diagram berikut memodelkan alur interaksi terpadu antara Siswa, Sistem Web SIPESAT, dan Petugas TU / Kepala Sekolah:")
add_diagram_image(doc4, IMG_ACTIVITY, "Gambar 2.1: Activity Diagram Alur Terpadu SIPESAT Standar UNINDRA (100% Bebas Tabrakan)")

add_h2(doc4, "2.2 Uraian Langkah Bernomor Alur Terpadu")
act_steps = [
    "1. Siswa membuka web SIPESAT dan melakukan login menggunakan NISN dan kata sandi.",
    "2. Masuk menu 'Pengajuan Surat' dan pilih jenis surat yang diperlukan.",
    "3. Isi formulir keperluan dan unggah dokumen syarat (PDF/JPG ≤ 2MB).",
    "4. Klik tombol 'Kirim Permohonan'.",
    "5. Sistem memvalidasi kelengkapan formulir dan ukuran berkas dokumen.",
    "6. [Decision: Jika form tidak lengkap / file > 2MB] Tampilkan alert validasi dan kembali ke form.",
    "7. [Decision: Jika valid] Sistem menyimpan permohonan ke database (status: DIAJUKAN) dan menerbitkan nomor resi tiket unik.",
    "8. Sistem meneruskan berkas ke meja antrean TU.",
    "9. Petugas TU login ke panel TU, membuka antrean, dan meninjau berkas dokumen siswa.",
    "10. [Decision: Jika berkas kurang/buram] Input alasan koreksi, klik 'Tolak & Minta Revisi', update status ke DITOLAK_PERLU_REVISI, dan kirim notifikasi ke siswa.",
    "11. [Decision: Jika berkas lengkap & sah] Input nomor agenda TU dan teruskan ke antrean Kepala Sekolah.",
    "12. Kepala Sekolah menyetujui, sistem generate nomor surat resmi dan bubuhkan kode QR TTE.",
    "13. Sistem mengompilasi kop sekolah, data siswa, dan kode QR ke file PDF resmi (status: SELESAI).",
    "14. Siswa menerima notifikasi selesai dan mengunduh berkas PDF surat resmi."
]
for s in act_steps:
    add_p(doc4, s, indent=False)

add_h1(doc4, "BAB III: PERANCANGAN SEQUENCE DIAGRAM (POLA BCE UNINDRA)")
add_h2(doc4, "3.1 Diagram Sequence: Pengajuan Siswa & Verifikasi TU (Draw.io Native)")
add_p(doc4, "Diagram berikut memodelkan pertukaran pesan interaksi objek berbasis Boundary-Control-Entity (BCE) lengkap dengan frame alt:")
add_diagram_image(doc4, IMG_SEQUENCE, "Gambar 3.1: Sequence Diagram Pengajuan & Verifikasi Dokumen Pola BCE (100% Bebas Tabrakan)")

add_h2(doc4, "3.2 Uraian Pesan & Komponen BCE")
add_p(doc4, "Komponen yang berinteraksi meliputi:")
add_p(doc4, "- Boundary Class (|O): FormPengajuanUI dan VerifikasiTUUI sebagai penangkap aksi input pengguna.")
add_p(doc4, "- Control Class (↺O): SuratController dan VerifikasiController sebagai pengendali aturan bisnis dan validasi berkas.")
add_p(doc4, "- Entity Class (_O_): tb_pengajuan_surat sebagai penyimpan status dan nomor register pada basis data.")

add_h1(doc4, "BAB IV: PENUTUP")
add_p(doc4, "Seluruh rancangan diagram Activity dan Sequence BCE tersimpan pada berkas Draw.io master:")
add_p(doc4, "- tugas-4-activity-sequence.drawio (2 Tab Bersih: Tab 1 Activity Terpadu, Tab 2 Sequence Diagrams BCE)", indent=False, bold=True)

doc4_path = os.path.join(RPL_DIR, "tugas-4-activity-sequence.docx")
doc4.save(doc4_path)
print(f"[OK] Saved {doc4_path}")

# Update Tugas 4 Typst
typst_tugas4 = f"""#set document(
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
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\\
    TUGAS 4: ACTIVITY DIAGRAM & SEQUENCE DIAGRAM
  ]
  #v(1.0cm)
  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\\
    #text(size: 11pt, weight: "regular")[_Studi Kasus: Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah_]
  ]
  #v(1.8cm)
  #rect(width: 5cm, height: 4.2cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt)[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[UNIVERSITAS\\ INDRAPRASTA PGRI\\ (UNINDRA)]
      #v(6pt)
      #text(size: 9.5pt, fill: rgb("#475569"))[FAKULTAS TEKNIK & ILMU KOMPUTER\\ TEKNIK INFORMATIKA]
    ]
  ]
  #v(1.8cm)
  #text(size: 11pt, weight: "bold")[Disusun Oleh (Kelompok 7 / Kelas RPL_XD):]
  #v(0.3cm)
  #table(
    columns: (0.8cm, 8.5cm, 3.5cm),
    align: (center, left, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 {{ rgb("#1e293b") }} else {{ none }},
    table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Anggota]*], [*#text(fill: white)[NPM]*]),
    [1], [Adam Wahyu Kurniawan (Lead Architect & SWE)], [202343500510],
    [2], [Fathu Rahman (Business Analyst)], [202343500467],
    [3], [Surya Edi Saputra (QA & Technical Writer)], [202343500468],
    [4], [Rizqi Muh. Al Hakimi (Database Specialist)], [202343500449],
  )
  #v(1.2cm)
  #text(size: 11pt, weight: "bold")[JAKARTA\\ 2026/2027]
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
  fill: (col, row) => if row == 0 {{ rgb("#1e293b") }} else if calc.even(row) {{ rgb("#f8fafc") }} else {{ none }},
  table.header([*#text(fill: white)[Komponen BCE]*], [*#text(fill: white)[Simbol]*], [*#text(fill: white)[Peran & Implementasi di SIPESAT]*]),
  [Boundary Class], [|O], [Komponen antarmuka pengguna: `FormPengajuanUI`, `VerifikasiTUUI`. Menangkap input dan menyajikan feedback visual.],
  [Control Class], [↺O], [Pengendali logika bisnis: `SuratController`, `VerifikasiController`. Menjalankan aturan validasi payload dan kalkulasi.],
  [Entity Class], [_O_], [Struktur persistensi database: `tb_pengajuan_surat`. Menyimpan record permohonan, nomor resi, dan status dokumen.]
)

#v(0.8cm)
= BAB IV: KESIMPULAN & BERKAS DIAGRAM DRAW.IO
Seluruh diagram visual interaktif tersimpan pada berkas Draw.io master:
- *`tugas-4-activity-sequence.drawio`* *(2 Tab Bersih: Tab 1 Activity Terpadu, Tab 2 Sequence Diagrams BCE)*.
"""

with open(os.path.join(RPL_DIR, "tugas-4-activity-sequence.typ"), "w", encoding="utf-8") as f:
    f.write(typst_tugas4)
print("[OK] Saved tugas-4-activity-sequence.typ")


# =========================================================================
# 4. BUILD TUGAS 5 DOCX & TYPST (STATE MACHINE)
# =========================================================================
print("--- [4/4] Building Tugas 5 (State Machine Diagram) ---")
doc5 = build_docx_base("TUGAS 5: PERANCANGAN STATE MACHINE DIAGRAM", "Pemodelan Siklus Hidup Entitas Dokumen Permohonan Surat Siswa (tb_pengajuan_surat)")

add_h1(doc5, "BAB I: PENDAHULUAN & LANDASAN TEORI")
add_h2(doc5, "1.1 Gambaran Umum Proyek SIPESAT")
add_p(doc5, "Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) adalah platform layanan persuratan digital sekolah yang dirancang untuk mengotomatisasi proses birokrasi pengajuan surat keterangan siswa, rekomendasi beasiswa, dan dispensasi sekolah.")

add_h2(doc5, "1.2 Konsep Dasar State Machine Diagram (UML 2.5)")
add_p(doc5, "State Machine Diagram memodelkan siklus hidup diskret dari suatu objek tunggal, mulai dari inisialisasi awal hingga terminasi akhir, mencakup keadaan (state), stimulus pemicu (event/trigger), guard condition boolean, dan aksi transisi otomatis.")

add_h1(doc5, "BAB II: PERANCANGAN STATE MACHINE DIAGRAM SIPESAT")
add_h2(doc5, "2.1 Diagram Siklus Hidup Permohonan Surat Siswa (Draw.io Native)")
add_p(doc5, "Berikut adalah rancangan visual State Machine Diagram entitas permohonan surat siswa (tb_pengajuan_surat):")
add_diagram_image(doc5, IMG_STATEMACHINE, "Gambar 2.1: State Machine Diagram Siklus Hidup Permohonan Surat Siswa (100% Bebas Tabrakan)")

add_h2(doc5, "2.2 Uraian Status Keadaan (State) Surat")
states_desc = [
    "1. DRAFT: Keadaan saat siswa membuka form pengajuan, mengisi keperluan, dan mengunggah dokumen prasyarat (file ≤ 2MB).",
    "2. MENUNGGU_VERIFIKASI: Setelah siswa menekan kirim permohonan. Sistem menerbitkan kode tiket resi unik dan berkas masuk antrean verifikasi TU.",
    "3. DITOLAK_PERLU_REVISI: Keadaan jika berkas ditolak TU karena buram/kurang. Siswa diizinkan mengunggah ulang perbaikan berkas.",
    "4. DIVERIFIKASI_TU: Keadaan saat TU menyetujui berkas, menetapkan nomor agenda masuk, dan meneruskan berkas ke Kepala Sekolah.",
    "5. DISETUJUI_KEPSEK: Keadaan saat Kepala Sekolah menyetujui penerbitan surat, sistem generate nomor surat keluar resmi dan kode QR TTE.",
    "6. SELESAI_SIAP_UNDUH: Mesin kompilasi PDF menyatukan kop sekolah, data siswa, dan stempel QR menjadi file PDF resmi siap diunduh.",
    "7. DIARSIPKAN: Surat telah diunduh siswa atau masa retensi aktif berakhir, lalu dibekukan permanen ke arsip statis sekolah."
]
for s in states_desc:
    add_p(doc5, s, indent=False)

add_h1(doc5, "BAB III: TABEL TRANSISI KEADAAN (STATE TRANSITION TABLE)")
t_st = doc5.add_table(rows=1, cols=5)
t_st.alignment = WD_TABLE_ALIGNMENT.CENTER
h_st = t_st.rows[0].cells
h_st[0].text = "State Asal"
h_st[1].text = "Event / Trigger"
h_st[2].text = "Guard Condition"
h_st[3].text = "Action / Effect"
h_st[4].text = "State Tujuan"
for c in h_st:
    set_cell_background(c, "1E293B")
    for p_c in c.paragraphs:
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r_c in p_c.runs:
            r_c.font.color.rgb = RGBColor(255, 255, 255)
            r_c.bold = True
            r_c.font.size = Pt(10)

st_data = [
    ("INITIAL (●)", "openMenuPengajuan()", "user_authenticated == true", "initFormPayload()", "DRAFT"),
    ("DRAFT", "submitPermohonan()", "form_valid && file_size <= 2MB", "generateTicketCode(), notifyTU()", "MENUNGGU_VERIFIKASI"),
    ("MENUNGGU_VERIFIKASI", "rejectTU()", "berkas_kurang || buram", "setCatatanRevisi(), alertSiswa()", "DITOLAK_PERLU_REVISI"),
    ("DITOLAK_PERLU_REVISI", "reuploadBerkas()", "file_revisi_valid == true", "updateLampiran(), notifyTU()", "MENUNGGU_VERIFIKASI"),
    ("MENUNGGU_VERIFIKASI", "approveTU()", "berkas_lengkap & absah", "setNoAgenda(), forwardToKepsek()", "DIVERIFIKASI_TU"),
    ("DIVERIFIKASI_TU", "approveKepsek()", "validasi_disetujui == true", "generateNoSurat(), createQR_TTE()", "DISETUJUI_KEPSEK"),
    ("DISETUJUI_KEPSEK", "autoGeneratePDF()", "pdf_binary_compiled == true", "saveToStorage(), notifySiswa()", "SELESAI_SIAP_UNDUH"),
    ("SELESAI_SIAP_UNDUH", "unduhSurat()", "retention_period_expired", "freezeRecordToAgendaArsip()", "DIARSIPKAN"),
]

for row_data in st_data:
    row = t_st.add_row().cells
    for i, val in enumerate(row_data):
        row[i].text = val
        set_cell_margins(row[i], 60, 60, 80, 80)
        row[i].paragraphs[0].runs[0].font.size = Pt(9.5)
        if i == 0 or i == 4:
            row[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

set_table_borders(t_st)

add_h1(doc5, "BAB IV: PENUTUP")
add_p(doc5, "Seluruh diagram visual interaktif State Machine tersimpan pada berkas Draw.io master:")
add_p(doc5, "- tugas-5-state-machine.drawio (1 Tab Tunggal Bersih, 0 Tabrakan Garis)", indent=False, bold=True)

doc5_path = os.path.join(RPL_DIR, "tugas-5-state-machine.docx")
doc5.save(doc5_path)
print(f"[OK] Saved {doc5_path}")

# Build Tugas 5 Typst
typst_tugas5 = f"""#set document(
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
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\\
    TUGAS 5: PERANCANGAN STATE MACHINE DIAGRAM
  ]
  #v(1.0cm)
  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\\
    #text(size: 11pt, weight: "regular")[_Pemodelan Siklus Hidup Entitas Dokumen Permohonan Surat Siswa (tb_pengajuan_surat)_]
  ]
  #v(1.8cm)
  #rect(width: 5cm, height: 4.2cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt)[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[UNIVERSITAS\\ INDRAPRASTA PGRI\\ (UNINDRA)]
      #v(6pt)
      #text(size: 9.5pt, fill: rgb("#475569"))[FAKULTAS TEKNIK & ILMU KOMPUTER\\ TEKNIK INFORMATIKA]
    ]
  ]
  #v(1.8cm)
  #text(size: 11pt, weight: "bold")[Disusun Oleh (Kelompok 7 / Kelas RPL_XD):]
  #v(0.3cm)
  #table(
    columns: (0.8cm, 8.5cm, 3.5cm),
    align: (center, left, center),
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 {{ rgb("#1e293b") }} else {{ none }},
    table.header([*#text(fill: white)[No]*], [*#text(fill: white)[Nama Anggota]*], [*#text(fill: white)[NPM]*]),
    [1], [Adam Wahyu Kurniawan (Lead Architect & SWE)], [202343500510],
    [2], [Fathu Rahman (Business Analyst)], [202343500467],
    [3], [Surya Edi Saputra (QA & Technical Writer)], [202343500468],
    [4], [Rizqi Muh. Al Hakimi (Database Specialist)], [202343500449],
  )
  #v(1.2cm)
  #text(size: 11pt, weight: "bold")[JAKARTA\\ 2026/2027]
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
  fill: (col, row) => if row == 0 {{ rgb("#1e293b") }} else if calc.even(row) {{ rgb("#f8fafc") }} else {{ none }},
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
"""

with open(os.path.join(RPL_DIR, "tugas-5-state-machine.typ"), "w", encoding="utf-8") as f:
    f.write(typst_tugas5)
print("[OK] Saved tugas-5-state-machine.typ")

# =========================================================================
# 5. COMPILE ALL TYPST TO PDF
# =========================================================================
print("--- [5/5] Compiling All Typst Documents to PDF ---")
typst_files = [
    ("tugas-2-srs-wiegers.typ", "tugas-2-srs-wiegers.pdf"),
    ("tugas-3-usecase.typ", "tugas-3-usecase.pdf"),
    ("tugas-4-activity-sequence.typ", "tugas-4-activity-sequence.pdf"),
    ("tugas-5-state-machine.typ", "tugas-5-state-machine.pdf"),
]

for typ_src, pdf_dst in typst_files:
    cmd = ["typst", "compile", os.path.join(RPL_DIR, typ_src), os.path.join(RPL_DIR, pdf_dst)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[PASS 100%] Compiled {pdf_dst}")
    else:
        print(f"[FAIL] {typ_src} -> {res.stderr}")

print("Master Builder Completed Successfully!")
