import os
import subprocess
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

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

    # Style
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
    p.paragraph_format.space_after = Pt(18)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run(subtitle_tugas + "\nStudi Kasus: Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)")
    r_sub.italic = True
    r_sub.font.size = Pt(12)
    p_sub.paragraph_format.space_after = Pt(28)

    # Box Identitas Kampus
    p_kampus = doc.add_paragraph()
    p_kampus.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_k = p_kampus.add_run("UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)\nFAKULTAS TEKNIK DAN ILMU KOMPUTER\nPROGRAM STUDI TEKNIK INFORMATIKA\n2026/2027")
    r_k.bold = True
    r_k.font.size = Pt(11)
    p_kampus.paragraph_format.space_after = Pt(24)

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
            if idx == 0 or idx == 2:
                c.paragraphs[0].runs[0].font.size = Pt(10)
            else:
                c.paragraphs[0].runs[0].font.size = Pt(10)

    set_table_borders(table_kel)
    doc.add_page_break()
    return doc

# =========================================================================
# 1. BUILD TUGAS 3 DOCX
# =========================================================================
print("Building Tugas 3 DOCX...")
doc3 = build_docx_base("TUGAS 3: PERANCANGAN USE CASE DIAGRAM & MATRIKS RBAC", "Pemodelan Batasan Sistem, Aktor Pengguna, dan Matriks Hak Akses")

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

# Content Tugas 3
add_h1(doc3, "BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM")
add_h2(doc3, "1.1 Deskripsi Proyek SIPESAT")
add_p(doc3, "Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) adalah sistem perangkat lunak yang dirancang untuk memodernisasi dan mengotomatisasi rantai birokrasi pengajuan surat keterangan di lingkungan sekolah menengah. Sebelum adanya sistem ini, siswa harus datang langsung ke ruang Tata Usaha (TU), mengisi formulir kertas manual, dan menunggu proses verifikasi berhari-hari tanpa kejelasan status.")
add_p(doc3, "SIPESAT memotong hambatan tersebut dengan menyediakan portal mandiri daring bagi siswa untuk mengajukan surat, mengunggah berkas persyaratan secara digital, memantau posisi surat secara transparan (real-time status tracking), dan mengunduh berkas surat resmi berformat PDF yang telah dilengkapi nomor register resmi serta kode QR tanda tangan elektronik.")

add_h2(doc3, "1.2 Tujuan Pemodelan Use Case Diagram")
add_p(doc3, "Use Case Diagram dalam metodologi Unified Modeling Language (UML) berfungsi memetakan fungsi-fungsi sistem dari perspektif pengguna eksternal (actor). Tujuan utama dari pemodelan Use Case pada sistem SIPESAT adalah:")
add_p(doc3, "1. Mendefinisikan batasan sistem (system boundary) secara tegas.\n2. Mengidentifikasi seluruh aktor yang berinteraksi langsung dengan sistem.\n3. Memetakan kebutuhan fungsional perangkat lunak ke dalam unit-unit fungsionalitas diskret (use cases).\n4. Menjelaskan relasi dependensi antarfungsi menggunakan stereotype <<include>> (keharusan) dan <<extend>> (perluasan opsional).", indent=False)

add_h1(doc3, "BAB II: PERANCANGAN USE CASE DIAGRAM SIPESAT")
add_h2(doc3, "2.1 Identifikasi Aktor Sistem")
add_p(doc3, "Sistem SIPESAT menerapkan pemisahan tugas berbasis peran (Role-Based Access Control) yang terdiri dari 2 aktor utama:")
add_p(doc3, "1. Siswa (Aktor Pemohon): Aktor peserta didik yang terdaftar resmi di sekolah. Bertanggung jawab mengajukan permohonan surat secara mandiri, melampirkan berkas persyaratan sah, memantau status persuratan, dan mengunduh dokumen akhir.")
add_p(doc3, "2. Petugas TU / Admin (Aktor Pengelola & Verifikator): Aktor staf administrasi sekolah yang bertugas memverifikasi keabsahan dokumen permohonan, menerbitkan nomor register/agenda surat keluar, mengelola katalog template surat, memelihara master data akun, serta mengekspor rekapitulasi laporan bulanan.")

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
    ("UC-01B", "Validasi Token JWT", "Sistem (Include)", "Pengecekan keabsahan tanda tangan token JSON Web Token pada rute terproteksi."),
    ("UC-02", "Registrasi Akun Siswa", "Siswa", "Pendaftaran akun baru siswa dengan verifikasi NISN ke database induk siswa."),
    ("UC-03", "Kelola Profil & Sandi", "Siswa, TU", "Pembaharuan kontak telepon, email aktif, dan pergantian kata sandi akun."),
    ("UC-04", "Logout Sesi", "Siswa, TU", "Penghapusan cookie sesi HttpOnly dan pencabutan token aktif di server."),
    ("UC-05", "Katalog & Syarat Surat", "Siswa", "Eksplorasi daftar jenis surat yang tersedia beserta panduan berkas pendukung wajib."),
    ("UC-06", "Ajukan Permohonan Surat", "Siswa", "Pengisian formulir keperluan, penentuan tujuan pembuatan surat, dan kirim draf."),
    ("UC-07", "Unggah Berkas Persyaratan", "Siswa (Include)", "Pengunggahan file bukti pendukung (PDF/JPG, batas maksimum 2 MB)."),
    ("UC-08", "Lacak Status Surat (Tracking)", "Siswa", "Pemantauan posisi proses dokumen secara live via Stepper Status."),
    ("UC-08A", "Periksa Catatan Revisi", "Siswa (Extend)", "Pembacaan feedback alasan penolakan berkas dan instruksi perbaikan."),
    ("UC-09", "Riwayat Arsip Pengajuan", "Siswa", "Peninjauan rekam jejak surat yang pernah diajukan di masa lalu."),
    ("UC-10", "Unduh Surat Resmi Ber-QR", "Siswa", "Pengunduhan berkas PDF resmi berkop sekolah dengan validasi kode QR."),
    ("UC-11", "Dashboard Statistik TU", "Petugas TU", "Tinjauan metrik operasional: surat masuk, verifikasi, selesai, dan ditolak."),
    ("UC-12", "Kelola Antrean Surat", "Petugas TU", "Penyaringan dan pengurutan permohonan surat masuk berdasarkan tanggal masuk."),
    ("UC-13", "Verifikasi Kelayakan Berkas", "Petugas TU", "Pemeriksaan isi berkas unggahan siswa terhadap data registrasi sekolah."),
    ("UC-14", "Setujui Permohonan (Approve)", "Petugas TU", "Pengesahan administratif surat permohonan yang telah memenuhi seluruh syarat."),
    ("UC-14A", "Terbitkan No. Surat & QR", "TU (Include)", "Generate nomor agenda resmi sekolah otomatis dan kode hash QR Code."),
    ("UC-15", "Tolak Permohonan (Reject)", "Petugas TU", "Penolakan permohonan yang tidak memenuhi syarat atau berkas buram."),
    ("UC-15A", "Input Catatan Revisi", "TU (Include)", "Penyusunan catatan tertulis kekurangan berkas untuk ditindaklanjuti siswa."),
    ("UC-16", "Kelola Master Jenis Surat", "Petugas TU", "Manajemen jenis surat, perubahan syarat wajib, dan template isi naskah."),
    ("UC-17", "Kelola Master Akun Pengguna", "Petugas TU", "Pengawasan status akun, reset kata sandi bermasalah, dan aktivasi akun."),
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
add_p(doc3, "Untuk menjamin keamanan sistem dan integritas data persuratan sekolah, setiap fungsi sistem dipagari oleh otorisasi berbasis peran:")

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
    ("2", "UC-02: Registrasi Akun Siswa Baru", "Ya", "Tidak"),
    ("3", "UC-03: Kelola Profil & Sandi", "Ya", "Ya"),
    ("4", "UC-04: Logout Sesi Pengguna", "Ya", "Ya"),
    ("5", "UC-05: Katalog & Syarat Surat", "Ya", "Ya (Kelola)"),
    ("6", "UC-06: Pengajuan Surat Baru", "Ya", "Tidak"),
    ("7", "UC-07: Unggah Berkas Persyaratan", "Ya", "Tidak"),
    ("8", "UC-08: Lacak Status Surat (Tracking)", "Ya", "Tidak"),
    ("9", "UC-09: Riwayat Pengajuan Mandiri", "Ya", "Tidak"),
    ("10", "UC-10: Unduh Surat PDF Ber-QR Code", "Ya", "Ya"),
    ("11", "UC-11: Dashboard Statistik TU", "Tidak", "Ya"),
    ("12", "UC-12: Kelola Antrean Surat Masuk", "Tidak", "Ya"),
    ("13", "UC-13: Verifikasi Berkas Siswa", "Tidak", "Ya"),
    ("14", "UC-14: Persetujuan Permohonan (Approve)", "Tidak", "Ya"),
    ("15", "UC-15: Penolakan Permohonan (Reject)", "Tidak", "Ya"),
    ("16", "UC-16: Kelola Master Jenis Surat", "Tidak", "Ya"),
    ("17", "UC-17: Kelola Master Akun Pengguna", "Tidak", "Ya"),
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
add_p(doc3, "Perancangan Use Case Diagram dan Matriks Hak Akses (RBAC) pada sistem SIPESAT telah diselaraskan secara komprehensif dengan kaidah akademik UNINDRA dan dokumen SRS Karl Wiegers (Tugas 2). Diagram visual interaktif multi-tab tersimpan pada berkas Draw.io resmi:")
add_p(doc3, "- tugas-3-usecase.drawio (Format XML Multi-Tab Native Draw.io)", indent=False, bold=True)

doc3_path = os.path.join(RPL_DIR, "tugas-3-usecase.docx")
doc3.save(doc3_path)
print(f"[OK] Saved {doc3_path}")

# =========================================================================
# 2. BUILD TUGAS 4 DOCX
# =========================================================================
print("Building Tugas 4 DOCX...")
doc4 = build_docx_base("TUGAS 4: ACTIVITY & SEQUENCE DIAGRAM", "Pemodelan Alur Kerja Swimlane dan Arsitektur Interaksi BCE Sesuai Standar UNINDRA")

add_h1(doc4, "BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM")
add_h2(doc4, "1.1 Deskripsi Proyek SIPESAT")
add_p(doc4, "Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) adalah sistem yang dikembangkan untuk mempermudah proses pelayanan administrasi persuratan bagi siswa di lingkungan sekolah. Pada sistem sebelumnya, siswa harus datang langsung ke ruang Tata Usaha (TU) untuk meminta form kertas dan menunggu proses pembuatan surat yang memakan waktu cukup lama. Melalui SIPESAT, siswa dapat mengajukan surat kapan saja secara online, memantau posisi suratnya, dan mengunduh surat resmi yang sudah disetujui.")
add_p(doc4, "Sistem ini membagi hak akses ke dalam 3 peran pengguna utama: Siswa (pemohon), Staf Tata Usaha (verifikator & pengelola), dan Kepala Sekolah (pengesah tanda tangan digital QR Code).")

add_h2(doc4, "1.2 Standar Pemodelan Berdasarkan Modul UNINDRA (Pertemuan 04)")
add_p(doc4, "Berdasarkan modul resmi bahan ajar RPL UNINDRA yang dikembangkan oleh Koordinator Bu Millati Izzatillah, S.Kom., MMSI:")
add_p(doc4, "1. Activity Diagram harus dibuat berdasarkan use case pada Use Case Diagram dengan pembagian Swimlane 2 Kolom (Aktor di sebelah kiri dan Sistem di sebelah kanan) serta teks uraian langkah bernomor.\n2. Sequence Diagram wajib mengadopsi pola arsitektur Boundary-Control-Entity (BCE) dengan lifeline terurut waktu dan kotak pembatas alt untuk skenario sukses versus gagal.", indent=False)

add_h1(doc4, "BAB II: PERANCANGAN ACTIVITY DIAGRAM (SWIMLANE UNINDRA)")
add_h2(doc4, "2.1 Activity Diagram 1: Alur Pengajuan Surat oleh Siswa")
add_p(doc4, "Diagram ini memetakan interaksi 2 kolom antara Siswa di sisi kiri dan Sistem Web SIPESAT di sisi kanan:")
act1_steps = [
    "1. Siswa membuka web SIPESAT dan melakukan login menggunakan NISN dan kata sandi.",
    "2. Sistem memvalidasi kredensial dan menampilkan dashboard siswa.",
    "3. Siswa memilih menu 'Pengajuan Surat' dan menentukan jenis surat yang diinginkan.",
    "4. Siswa mengisi formulir peruntukan dan mengunggah berkas persyaratan (maksimal 2 MB).",
    "5. Sistem memvalidasi kelengkapan form dan ukuran berkas (Decision: jika tidak valid, tampilkan error dan kembali ke form; jika valid, lanjutkan).",
    "6. Sistem menyimpan draf permohonan ke database, menerbitkan nomor tiket unik, dan mengirimkan konfirmasi tanda terima ke siswa.",
    "7. Siswa menerima resi tiket dan memantau status persuratan."
]
for s in act1_steps:
    add_p(doc4, s, indent=False)

add_h2(doc4, "2.2 Activity Diagram 2: Alur Verifikasi Berkas oleh Staf Tata Usaha")
act2_steps = [
    "1. Staf TU login ke sistem dan membuka menu 'Verifikasi Berkas Masuk'.",
    "2. Staf TU memilih permohonan dari antrean dan meninjau berkas unggahan siswa.",
    "3. Staf TU mengevaluasi keabsahan dokumen (Decision: jika berkas buram/kurang, input catatan revisi dan ubah status ke DITOLAK_PERLU_REVISI; jika berkas lengkap, masukkan nomor agenda masuk dan teruskan ke Kepala Sekolah).",
    "4. Sistem memperbarui status di database dan mengirimkan notifikasi relevan."
]
for s in act2_steps:
    add_p(doc4, s, indent=False)

add_h2(doc4, "2.3 Activity Diagram 3: Alur Persetujuan & Pengesahan oleh Kepala Sekolah")
act3_steps = [
    "1. Kepala Sekolah login dan membuka antrean draf persetujuan surat.",
    "2. Kepala Sekolah meninjau kelayakan draf dan lembar disposisi TU.",
    "3. Decision: Jika tidak disetujui, input catatan evaluasi dan kembalikan ke meja TU; jika disetujui, klik 'Setujui & Tanda Tangani'.",
    "4. Sistem secara otomatis membuat nomor surat resmi sekolah, menghasilkan kode QR tanda tangan elektronik, mengompilasi berkas PDF resmi, dan mengubah status ke SELESAI_SIAP_UNDUH."
]
for s in act3_steps:
    add_p(doc4, s, indent=False)

add_h1(doc4, "BAB III: PERANCANGAN SEQUENCE DIAGRAM (POLA BCE UNINDRA)")
add_p(doc4, "Sequence Diagram disusun mengadopsi 3 kelas arsitektur formal:")
add_p(doc4, "- Boundary Class (|O): Antarmuka UI pengguna (LoginUI, FormPengajuanUI, VerifikasiTUUI, ApprovalKepsekUI).\n- Control Class (↺O): Logika pengendali bisnis (AuthController, SuratController, VerifikasiController, ApprovalController).\n- Entity Class (_O_): Tabel basis data persistensi (User, SuratPengajuan, MasterSurat, RiwayatSurat).", indent=False)

add_h2(doc4, "3.1 Sequence Diagram: Pengajuan Surat Siswa")
add_p(doc4, "Urutan pesan: Siswa memanggil FormPengajuanUI.inputData(), Boundary memanggil SuratController.submit(), Control memeriksa ukuran berkas via StorageService, Control memanggil Entity SuratPengajuan.insert(), Entity mengembalikan status sukses, dan Control mengembalikan nomor resi tiket ke Boundary.")

add_h2(doc4, "3.2 Sequence Diagram: Verifikasi Dokumen TU")
add_p(doc4, "Urutan pesan: Staf TU memilih antrean di VerifikasiTUUI, Boundary memanggil VerifikasiController.getDetail(), Control menarik data dari Entity SuratPengajuan, TU menentukan status, Control memanggil SuratPengajuan.updateStatus(), dan sistem memicu notifikasi pembaruan status.")

add_h1(doc4, "BAB IV: PENUTUP")
add_p(doc4, "Pemodelan Activity Diagram dan Sequence Diagram pada sistem SIPESAT telah mengikuti kaidah baku modul RPL UNINDRA Pertemuan 04 secara presisi. Seluruh diagram visual terpadu telah diintegrasikan ke dalam berkas Draw.io resmi:")
add_p(doc4, "- tugas-4-activity-sequence.drawio (5 Tab Lengkap: Simbol, Act Siswa, Act Petugas, Act Terpadu, Sequence BCE)", indent=False, bold=True)

doc4_path = os.path.join(RPL_DIR, "tugas-4-activity-sequence.docx")
doc4.save(doc4_path)
print(f"[OK] Saved {doc4_path}")

print("All DOCX files successfully built!")
