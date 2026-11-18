import os
import docx
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_docx_tugas11():
    doc = docx.Document()
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(4.0)
    section.bottom_margin = Cm(3.0)
    section.left_margin = Cm(4.0)
    section.right_margin = Cm(3.0)

    # Base Normal Style
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Times New Roman'
    style_normal.font.size = Pt(11)
    style_normal.font.color.rgb = RGBColor(0, 0, 0)
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(4)

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(13)
        r.font.color.rgb = RGBColor(15, 23, 42) # Slate 900
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(11.5)
        r.font.color.rgb = RGBColor(30, 41, 59)
        return p

    def add_p(text, italic=False, bold=False):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        r.italic = italic
        r.bold = bold
        return p

    def add_bullet(text, bold_prefix=""):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(2)
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.bold = True
        p.add_run(text)
        return p

    def create_testing_table(headers, data, col_widths, pink_header=True):
        t = doc.add_table(rows=len(data) + 1, cols=len(headers))
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(t, color="94A3B8", sz="4", val="single")

        hdr_row = t.rows[0]
        hdr_row._tr.get_or_add_trPr().append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        hdr_fill = "F472B6" if pink_header else "1E293B" # Pink header like the image!

        for i, h in enumerate(headers):
            cell = hdr_row.cells[i]
            cell.width = Cm(col_widths[i])
            cell.text = h
            set_cell_background(cell, hdr_fill)
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10)
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(0, 0, 0) if pink_header else RGBColor(255, 255, 255)

        for row_idx, row_data in enumerate(data):
            row = t.rows[row_idx + 1]
            bg_color = "FDF2F8" if (pink_header and row_idx % 2 == 1) else ("FFFFFF")
            for col_idx, text_val in enumerate(row_data):
                cell = row.cells[col_idx]
                cell.width = Cm(col_widths[col_idx])
                cell.text = text_val
                if bg_color != "FFFFFF":
                    set_cell_background(cell, bg_color)
                set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
                p = cell.paragraphs[0]
                # Center align for No and Kesimpulan
                if col_idx in [0, 4, 5]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.runs[0].font.name = 'Times New Roman'
                p.runs[0].font.size = Pt(9.5)
                if col_idx == 5:
                    p.runs[0].font.bold = True
                    p.runs[0].font.color.rgb = RGBColor(22, 101, 52) # Dark Green

        doc.add_paragraph().paragraph_format.space_after = Pt(6)
        return t

    # ================= COVER =================
    p_cov = doc.add_paragraph()
    p_cov.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_cov.add_run("TUGAS REKAYASA PERANGKAT LUNAK (RPL)\nTUGAS 11: PENGUJIAN PERANGKAT LUNAK (BLACK BOX TESTING)")
    r.bold = True
    r.font.size = Pt(14)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\nPengujian Fungsionalitas Kotak Hitam (Black Box) Berbasis Skenario Nyata")
    r_sub.bold = True
    r_sub.font.size = Pt(12)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Box UNINDRA
    p_box = doc.add_paragraph()
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_box = p_box.add_run("UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)\nFAKULTAS TEKNIK & ILMU KOMPUTER — TEKNIK INFORMATIKA\nTAHUN AKADEMIK 2026/2027")
    r_box.bold = True
    r_box.font.size = Pt(11)

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    p_kel = doc.add_paragraph()
    p_kel.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_kel = p_kel.add_run("Disusun Oleh (Kelompok 7 / Kelas RPL_XD):")
    r_kel.bold = True

    tbl_kel = doc.add_table(rows=5, cols=3)
    tbl_kel.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_kel, color="CBD5E1", sz="4", val="single")

    kel_data = [
        ("No", "Nama Anggota Kelompok", "NPM"),
        ("1", "Adam Wahyu Kurniawan (Lead Architect & SWE)", "202343500510"),
        ("2", "Fathu Rahman (Business Analyst)", "202343500467"),
        ("3", "Surya Edi Saputra (QA & Testing Specialist)", "202343500468"),
        ("4", "Rizqi Muh. Al Hakimi (Database Specialist & UI/UX)", "202343500449"),
    ]
    for r_i, row in enumerate(tbl_kel.rows):
        for c_i, cell in enumerate(row.cells):
            cell.text = kel_data[r_i][c_i]
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_i in [0, 2] else WD_ALIGN_PARAGRAPH.LEFT
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10)
            if r_i == 0:
                set_cell_background(cell, "1E293B")
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

    doc.add_page_break()

    # ================= BAB I =================
    add_h1("BAB I: PENDAHULUAN & METODOLOGI PENGUJIAN")
    add_h2("1.1 Latar Belakang Pengujian")
    add_p(
        "Pengujian perangkat lunak (Software Testing) merupakan tahapan fundamental dalam siklus rekayasa perangkat lunak "
        "yang bertujuan memverifikasi apakah keluaran sistem telah sesuai dengan rancangan spesifikasi kebutuhan pada SRS (Tugas 2) "
        "dan pemodelan desain UML (Tugas 3 s.d. 6). Pada sistem SIPESAT (Sistem Informasi Pengajuan Surat Siswa Berbasis Web), "
        "pengujian difokuskan pada kehandalan proses administrasi persuratan siswa, validasi berkas unggahan, otomatisasi penomoran, "
        "dan ketahanan autentikasi RBAC (Role-Based Access Control)."
    )

    add_h2("1.2 Metodologi Black Box Testing")
    add_p(
        "Metodologi yang digunakan adalah Black Box Testing (Pengujian Kotak Hitam). Pengujian dilakukan dari perspektif pengguna "
        "eksternal tanpa memeriksa struktur internal kode sumber. Teknik pengujian mencakup:"
    )
    add_bullet("Memvalidasi masukan valid dan masukan tidak valid pada formulir web.", "Equivalence Partitioning: ")
    add_bullet("Menguji nilai batas maksimum ukuran file (2 MB) dan kelengkapan kolom wajib.", "Boundary Value Analysis: ")
    add_bullet("Menguji pemisahan otorisasi ketat antara peran Siswa dan Petugas TU.", "Role-Based Access Control: ")

    add_h2("1.3 Lingkungan Pengujian (Testing Environment)")
    add_bullet("Intel Core i5 / AMD Ryzen 5, RAM 16 GB, SSD NVMe 512 GB.", "Perangkat Keras: ")
    add_bullet("Windows 11 Pro 64-bit / Linux Ubuntu 22.04 LTS.", "Sistem Operasi: ")
    add_bullet("Google Chrome v128+ & Microsoft Edge.", "Peramban Web: ")
    add_bullet("Next.js 14 Frontend (Port 3000), Express.js Backend (Port 5000), PostgreSQL 16 via Docker (Port 5432).", "Stack Server: ")
    add_bullet("Siswa (siswa_adam / siswa123) dan Petugas TU (admin / admin).", "Kredensial Akun Uji: ")

    # ================= BAB II =================
    add_h1("BAB II: TABEL MATRIKS PENGUJIAN BLACK BOX SISTEM SIPESAT")
    add_p(
        "Seluruh skenario pengujian di bawah ini mengadopsi format matriks resmi UNINDRA dengan kolom: "
        "No, Skenario Pengujian, Test Case, Hasil yang Diharapkan, Hasil Pengujian, dan Kesimpulan."
    )

    headers_table = ["No", "Skenario Pengujian", "Test Case", "Hasil yang Diharapkan", "Hasil Pengujian", "Kesimpulan"]
    col_widths = [1.0, 3.8, 3.2, 4.0, 2.0, 1.8]

    # Modul 1
    add_h2("2.1 Modul 1: Autentikasi, Login, & Hak Akses Multi-Role")
    m1_data = [
        ("1", "Username dan Password tidak diisi kemudian klik tombol Login", "Username: (kosong)\nPassword: (kosong)", "Sistem menolak dan menampilkan pesan \"Harap isi username dan password\"", "Sesuai harapan", "Valid"),
        ("2", "Mengetikkan Username, dan password tidak diisi atau kosong kemudian klik tombol Login", "Username: admin\nPassword: (kosong)", "Sistem menolak dan menampilkan pesan \"Password belum diisi\"", "Sesuai harapan", "Valid"),
        ("3", "Mengetikkan Password, dan username tidak diisi atau kosong kemudian klik tombol Login", "Username: (kosong)\nPassword: admin", "Sistem menolak dan menampilkan pesan \"Username belum diisi\"", "Sesuai harapan", "Valid"),
        ("4", "Mengetikkan Username dan/atau password tidak sesuai, kemudian klik tombol Login", "Username: adm\nPassword: adm123", "Sistem menolak dan menampilkan pesan \"Username atau Password yang anda masukan salah\"", "Sesuai harapan", "Valid"),
        ("5", "Mengetikkan Username dan password benar akun Petugas TU, kemudian klik tombol Login", "Username: admin\nPassword: admin", "Sistem menerima akses login dan menampilkan halaman utama Admin (/admin/dashboard)", "Sesuai harapan", "Valid"),
        ("6", "Mengetikkan Username dan password benar akun Siswa, kemudian klik tombol Login", "Username: siswa_adam\nPassword: siswa123", "Sistem menerima akses login dan menampilkan portal permohonan siswa (/siswa/pengajuan)", "Sesuai harapan", "Valid"),
        ("7", "Mengklik tombol Logout saat sesi pengguna aktif", "Sesi: Siswa / TU aktif\nAksi: Klik Logout", "Sistem memusnahkan sesi token JWT dan mengalihkan halaman kembali ke /login", "Sesuai harapan", "Valid"),
    ]
    create_testing_table(headers_table, m1_data, col_widths)

    # Modul 2
    add_h2("2.2 Modul 2: Formulir Pengajuan Surat Mandiri Siswa")
    m2_data = [
        ("8", "Mengirim formulir pengajuan tanpa memilih jenis surat", "Jenis Surat: (Belum dipilih)\nKeperluan: Beasiswa\nFile: berkas.pdf", "Sistem menolak submit dan memunculkan peringatan \"Pilih jenis surat yang diajukan\"", "Sesuai harapan", "Valid"),
        ("9", "Mengisi formulir dengan kolom keperluan kosong", "Jenis Surat: Surat Siswa Aktif\nKeperluan: (kosong)\nFile: berkas.pdf", "Sistem menolak submit dan memunculkan peringatan \"Keperluan pengajuan wajib diisi\"", "Sesuai harapan", "Valid"),
        ("10", "Mengunggah berkas persyaratan dengan ukuran melebihi batas (> 2 MB)", "File: scan_rapor_besar.pdf (Ukuran 4,5 MB)", "Sistem menolak file dan menampilkan notifikasi \"Ukuran file maksimal 2 MB\"", "Sesuai harapan", "Valid"),
        ("11", "Mengunggah berkas persyaratan dengan format terlarang (.exe, .php)", "File: malware_script.exe (Ukuran 300 KB)", "Sistem memblokir berkas dengan pesan \"Format tidak diizinkan. Hanya menerima PDF, JPG, PNG\"", "Sesuai harapan", "Valid"),
        ("12", "Mengisi seluruh formulir dengan data lengkap dan berkas sah (< 2 MB)", "Jenis: Surat Keterangan Aktif\nKeperluan: Tunjangan Gaji\nFile: kartu_pelajar.pdf (800 KB)", "Sistem menyimpan data, menerbitkan ID Registrasi unik, dan status awal \"Menunggu Verifikasi\"", "Sesuai harapan", "Valid"),
    ]
    create_testing_table(headers_table, m2_data, col_widths)

    # Modul 3
    add_h2("2.3 Modul 3: Pelacakan Status Surat (Tracking & Timeline Stepper)")
    m3_data = [
        ("13", "Mengecek status permohonan dengan nomor tiket kosong", "Nomor Registrasi: (kosong)\nAksi: Klik Lacak", "Sistem menampilkan pesan \"Harap masukkan nomor registrasi pengajuan surat\"", "Sesuai harapan", "Valid"),
        ("14", "Melacak status dengan nomor registrasi yang tidak terdaftar", "Nomor Registrasi: REG-9999-XXXX (Fiktif)", "Sistem menampilkan notifikasi \"Nomor registrasi tidak ditemukan. Periksa kembali tiket Anda\"", "Sesuai harapan", "Valid"),
        ("15", "Melacak surat valid yang berstatus \"Menunggu Verifikasi\"", "Nomor Registrasi: REG-2026-0001\nStatus: Menunggu", "Sistem menampilkan detail pemohon dan indikator stepper aktif pada tahap \"Menunggu Verifikasi TU\"", "Sesuai harapan", "Valid"),
        ("16", "Melacak surat yang berstatus \"Ditolak\" beserta catatan revisi", "Nomor Registrasi: REG-2026-0002\nStatus: Ditolak", "Sistem menampilkan alert merah \"Pengajuan Ditolak\" lengkap dengan catatan alasan perbaikan", "Sesuai harapan", "Valid"),
        ("17", "Melacak surat yang berstatus \"Selesai / Disetujui\"", "Nomor Registrasi: REG-2026-0003\nStatus: Selesai", "Sistem menampilkan stepper hijau lengkap dan mengaktifkan tombol \"Unduh Surat PDF Resmi\"", "Sesuai harapan", "Valid"),
    ]
    create_testing_table(headers_table, m3_data, col_widths)

    # Modul 4
    add_h2("2.4 Modul 4: Verifikasi & Disposisi Berkas oleh Petugas TU")
    m4_data = [
        ("18", "Petugas TU membuka inbox permohonan surat masuk", "Akun: Petugas TU\nMenu: Inbox Surat Masuk", "Sistem memuat daftar permohonan masuk secara real-time dengan status dan badge tanggal", "Sesuai harapan", "Valid"),
        ("19", "Petugas TU melakukan pratinjau berkas persyaratan siswa", "Aksi: Klik tombol \"Lihat Dokumen\" pada baris siswa", "Sistem membuka modal pratinjau PDF/gambar secara aman tanpa keluar dari halaman utama", "Sesuai harapan", "Valid"),
        ("20", "Petugas TU menolak permohonan tanpa mengisi catatan alasan", "Aksi: Tolak Pengajuan\nCatatan: (kosong)", "Sistem memblokir aksi penolakan dan mewajibkan catatan: \"Alasan penolakan wajib diisi\"", "Sesuai harapan", "Valid"),
        ("21", "Petugas TU menolak permohonan dengan mengisi catatan revisi", "Aksi: Tolak Pengajuan\nCatatan: \"Scan KK buram, upload ulang\"", "Sistem memperbarui status menjadi \"Ditolak\", menyimpan log audit, dan mengirim pesan ke siswa", "Sesuai harapan", "Valid"),
        ("22", "Petugas TU menyetujui permohonan surat yang memenuhi syarat", "Aksi: Klik \"Setujui & Terbitkan Surat\"", "Sistem memperbarui status menjadi \"Disetujui\", memicu engine nomor surat, dan siap cetak", "Sesuai harapan", "Valid"),
    ]
    create_testing_table(headers_table, m4_data, col_widths)

    # Modul 5
    add_h2("2.5 Modul 5: Penomoran Otomatis & Penerbitan Surat Digital PDF ber-QR Code")
    m5_data = [
        ("23", "Pengujian otomasi penomoran surat resmi sekolah", "Trigger: Surat disetujui pada November 2026 urutan ke-5", "Sistem menghasilkan nomor surat terformat: 005/SMK-PSKD/XI/2026 secara otomatis", "Sesuai harapan", "Valid"),
        ("24", "Pengujian konversi bulan kalender ke angka romawi", "Bulan: November (Bulan ke-11)", "Sistem mengonversi bulan 11 menjadi romawi \"XI\" secara presisi tanpa offset", "Sesuai harapan", "Valid"),
        ("25", "Pengujian pembuatan QR Code tanda tangan digital", "Input: ID Pengajuan SURAT-2026-005", "Sistem meng-generate QR Code dinamis yang memuat URL verifikasi otentikasi dokumen", "Sesuai harapan", "Valid"),
        ("26", "Pengunduhan dokumen PDF surat resmi oleh pengguna", "Aksi: Klik tombol \"Unduh PDF\" pada surat terbit", "Sistem mengunduh berkas PDF A4 resmi lengkap dengan kop sekolah, nomor resmi, dan QR Code", "Sesuai harapan", "Valid"),
        ("27", "Pemindaian QR Code pada surat PDF menggunakan kamera HP", "Aksi: Pindai QR Code di lembar surat fisik/PDF", "Peramban membuka portal verifikasi resmi SIPESAT dan menyatakan \"Dokumen Asli Terverifikasi\"", "Sesuai harapan", "Valid"),
    ]
    create_testing_table(headers_table, m5_data, col_widths)

    # Modul 6
    add_h2("2.6 Modul 6: Manajemen Data Master Persuratan & Rekapitulasi Laporan")
    m6_data = [
        ("28", "Petugas TU menambahkan jenis layanan surat baru", "Nama: Surat Keterangan Pindah\nFormat: {NOMOR}/PINDAH/{BULAN_ROMAWI}/{TAHUN}", "Sistem menyimpan jenis surat baru ke database dan langsung aktif di portal pengajuan siswa", "Sesuai harapan", "Valid"),
        ("29", "Petugas TU menonaktifkan jenis surat lama (Soft Deactivation)", "Aksi: Ubah status jenis surat menjadi \"Nonaktif\"", "Siswa tidak dapat memilih jenis surat tersebut, namun arsip riwayat lama tetap terpelihara utuh", "Sesuai harapan", "Valid"),
        ("30", "Penyaringan laporan persuratan berdasarkan rentang tanggal", "Filter: Tanggal 01 Nov 2026 s.d. 30 Nov 2026", "Sistem menyaring tabel dan hanya menampilkan permohonan surat dalam periode November 2026", "Sesuai harapan", "Valid"),
        ("31", "Ekspor laporan rekapitulasi persuratan ke format spreadsheet", "Aksi: Klik tombol \"Ekspor Data (Excel/CSV)\"", "Sistem mengunduh berkas spreadsheet rekapitulasi berisi data pemohon, jenis surat, dan status", "Sesuai harapan", "Valid"),
    ]
    create_testing_table(headers_table, m6_data, col_widths)

    # Modul 7
    add_h2("2.7 Modul 7: Pengujian Keamanan & Hak Akses (Route Guard & Security)")
    m7_data = [
        ("32", "Siswa mencoba mengakses paksa halaman admin lewat URL", "Role: Siswa\nAksi: Buka URL /admin/dashboard di address bar", "Sistem memblokir akses (HTTP 403 Forbidden) dan mengalihkan siswa kembali ke /siswa/pengajuan", "Sesuai harapan", "Valid"),
        ("33", "Akses endpoint API private tanpa menyertakan token JWT", "Request: GET /api/admin/pengajuan\nHeader: Tanpa Authorization", "Backend Express menolak request dengan status HTTP 401 Unauthorized (\"Token tidak ditemukan\")", "Sesuai harapan", "Valid"),
        ("34", "Siswa mencoba mengunduh surat milik siswa lain via ganti ID", "Akun: Siswa A\nAksi: Akses URL unduh file milik Siswa B", "Sistem memverifikasi kepemilikan data (Data Isolation) dan menolak akses dengan HTTP 403", "Sesuai harapan", "Valid"),
        ("35", "Uji serangan Cross-Site Scripting (XSS) pada form alasan", "Input: <script>alert('XSS_ATTACK')</script>", "Sistem mensterilkan tag HTML/JS sehingga tersimpan sebagai string aman tanpa dieksekusi browser", "Sesuai harapan", "Valid"),
    ]
    create_testing_table(headers_table, m7_data, col_widths)

    # ================= BAB III =================
    add_h1("BAB III: ANALISIS HASIL PENGUJIAN & METRIK KUALITAS")
    add_h2("3.1 Rekapitulasi Metrik Pengujian")
    
    headers_rekap = ["Kategori Modul Pengujian", "Total Test Case", "Pass (Sesuai)", "Fail (Gagal)", "Persentase Kelulusan"]
    col_rekap = [6.5, 2.5, 2.5, 2.5, 3.0]
    rekap_data = [
        ("Modul 1: Autentikasi & Hak Akses Multi-Role", "7", "7", "0", "100%"),
        ("Modul 2: Formulir Pengajuan Surat Mandiri Siswa", "5", "5", "0", "100%"),
        ("Modul 3: Pelacakan Status Surat (Tracking Stepper)", "5", "5", "0", "100%"),
        ("Modul 4: Verifikasi & Disposisi Petugas TU", "5", "5", "0", "100%"),
        ("Modul 5: Penomoran Otomatis & Cetak PDF QR Code", "5", "5", "0", "100%"),
        ("Modul 6: Manajemen Data Master & Laporan", "4", "4", "0", "100%"),
        ("Modul 7: Keamanan & Hak Akses (Route Guard)", "4", "4", "0", "100%"),
        ("TOTAL KESELURUHAN PENGUJIAN", "35", "35", "0", "100% (SEMPURNA)"),
    ]
    create_testing_table(headers_rekap, rekap_data, col_rekap, pink_header=False)

    add_h2("3.2 Analisis Kesiapan Sistem")
    add_p(
        "Berdasarkan 35 test case yang telah dieksekusi, sistem SIPESAT memperoleh tingkat kelulusan 100% Valid "
        "tanpa ditemukan cacat kritis (Zero Critical Defect). Seluruh penanganan validasi batas form input, "
        "keamanan token JWT, dan isolasi data multi-role berfungsi stabil sesuai spesifikasi SRS."
    )

    # ================= BAB IV =================
    add_h1("BAB IV: KESIMPULAN & TAUTAN KODE SUMBER")
    add_h2("4.1 Kesimpulan")
    add_p(
        "Pengujian kotak hitam (Black Box Testing) pada sistem SIPESAT membuktikan bahwa aplikasi telah memenuhi seluruh kriteria "
        "keberhasilan fungsional yang ditetapkan pada mata kuliah Rekayasa Perangkat Lunak. Sistem siap digunakan secara operasional "
        "untuk digitalisasi persuratan sekolah."
    )

    add_h2("4.2 Tautan Repositori GitHub Resmi")
    add_p(
        "Sesuai instruksi dosen pengampu mata kuliah RPL, seluruh kode program frontend, backend, skema database Prisma, "
        "dan dokumen tugas dapat diakses secara publik pada repositori GitHub:"
    )
    add_bullet("https://github.com/themodeid/Sipesat-RPL", "URL Repositori: ")

    output_path = os.path.join(RPL_DIR, "tugas-11-pengujian-black-box.docx")
    doc.save(output_path)
    print(f"SUCCESS GENERATING DOCX: {output_path}")

if __name__ == "__main__":
    build_docx_tugas11()
