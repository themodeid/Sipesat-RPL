import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

RPL_DIR = r"c:\A_main_code\all-my-projek\RPL"

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette: Navy & Blue Academic
    NAVY_DARK = RGBColor(15, 23, 42)       # #0f172a
    NAVY_HEADER = RGBColor(30, 41, 59)     # #1e293b
    BLUE_PRIMARY = RGBColor(30, 64, 175)   # #1e40af
    BLUE_ACCENT = RGBColor(37, 99, 235)    # #2563eb
    TEXT_DARK = RGBColor(15, 23, 42)       # #0f172a
    TEXT_MUTED = RGBColor(71, 85, 105)     # #475569
    TEXT_LIGHT = RGBColor(248, 250, 252)   # #f8fafc
    CARD_BG = RGBColor(248, 250, 252)      # #f8fafc
    CARD_BORDER = RGBColor(203, 213, 225)  # #cbd5e1
    WHITE = RGBColor(255, 255, 255)

    def add_header(slide, title, subtitle):
        # Top Header Banner
        header_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        header_box.fill.solid()
        header_box.fill.fore_color.rgb = NAVY_HEADER
        header_box.line.color.rgb = BLUE_ACCENT
        header_box.line.width = Pt(2)

        tf = header_box.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = Inches(0.8)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = TEXT_LIGHT

        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = "Calibri"
        p2.font.size = Pt(12)
        p2.font.color.rgb = RGBColor(148, 163, 184)

    def add_card(slide, left, top, width, height, title, items, badge=""):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)
        tf.margin_bottom = Inches(0.2)

        if badge:
            p_badge = tf.paragraphs[0]
            p_badge.text = badge.upper()
            p_badge.font.name = "Calibri"
            p_badge.font.size = Pt(10)
            p_badge.font.bold = True
            p_badge.font.color.rgb = BLUE_PRIMARY
            p_title = tf.add_paragraph()
        else:
            p_title = tf.paragraphs[0]

        p_title.text = title
        p_title.font.name = "Calibri"
        p_title.font.size = Pt(16)
        p_title.font.bold = True
        p_title.font.color.rgb = NAVY_DARK
        p_title.space_after = Pt(8)

        for it in items:
            p_item = tf.add_paragraph()
            p_item.text = f"• {it}"
            p_item.font.name = "Calibri"
            p_item.font.size = Pt(12)
            p_item.font.color.rgb = TEXT_MUTED
            p_item.space_after = Pt(4)

    # ==================== SLIDE 1: COVER SLIDE ====================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = NAVY_DARK
    bg1.line.fill.background()

    # Title Box
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.3), Inches(11.333), Inches(4.8))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "SISTEM INFORMASI PENGAJUAN SURAT SISWA (SIPESAT)"
    p.font.name = "Calibri"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    p_sub = tf1.add_paragraph()
    p_sub.text = "Digitalisasi Layanan Administrasi Persuratan Sekolah Berbasis Web Decoupled"
    p_sub.font.name = "Calibri"
    p_sub.font.size = Pt(18)
    p_sub.font.color.rgb = RGBColor(147, 197, 253)
    p_sub.space_after = Pt(28)

    p_meta = tf1.add_paragraph()
    p_meta.text = "MATA KULIAH: REKAYASA PERANGKAT LUNAK (RPL) — KELAS RPL_XD\nPROGRAM STUDI TEKNIK INFORMATIKA — FTIK UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)"
    p_meta.font.name = "Calibri"
    p_meta.font.size = Pt(13)
    p_meta.font.bold = True
    p_meta.font.color.rgb = RGBColor(203, 213, 225)
    p_meta.space_after = Pt(20)

    p_team = tf1.add_paragraph()
    p_team.text = "Disusun oleh KELOMPOK 7 RPL:\n1. Adam Wahyu Kurniawan (202343500510) — Lead Developer & Architect\n2. Fathu Rahman (202343500467) — Business Analyst & Requirements\n3. Surya Edi Saputra (202343500468) — Quality Assurance & Testing\n4. Rizqi Muh. Al Hakimi (202343500449) — Database Specialist & UI/UX"
    p_team.font.name = "Calibri"
    p_team.font.size = Pt(12)
    p_team.font.color.rgb = RGBColor(148, 163, 184)

    # ==================== SLIDE 2: LATAR BELAKANG & MASALAH ====================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "1. LATAR BELAKANG & PERMASALAHAN", "Tantangan Birokrasi Persuratan Siswa di Lingkungan Sekolah Menengah")
    add_card(s2, Inches(0.8), Inches(1.5), Inches(3.6), Inches(5.3), "Antrean & Jam Operasional", [
        "Siswa harus datang fisik ke ruang Tata Usaha pada jam istirahat atau pulang sekolah.",
        "Terjadi penumpukan antrean pada musim beasiswa, registrasi PTN, atau pendaftaran kerja.",
        "Mengurangi waktu belajar dan efektivitas jam kerja staf Tata Usaha."
    ], badge="Kendala Aksesibilitas")
    add_card(s2, Inches(4.8), Inches(1.5), Inches(3.6), Inches(5.3), "Penyimpanan Berkas Manual", [
        "Formulir kertas dan fotokopi berkas syarat siswa sering terselip atau rusak.",
        "Pencatatan manual di buku agenda rentan terhadap nomor surat ganda atau terlewat.",
        "Pencarian riwayat surat membutuhkan waktu lama dan memakan ruang arsip fisik."
    ], badge="Resiko Arsip Fisik")
    add_card(s2, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.3), "Status Tidak Transparan", [
        "Siswa tidak mengetahui apakah surat sudah diverifikasi, disetujui, atau ditolak.",
        "Harus bolak-balik menanyakan progres surat ke loket TU.",
        "Tidak ada rekaman audit trail resmi jika terjadi keterlambatan penerbitan surat."
    ], badge="Ketidakpastian Siswa")

    # ==================== SLIDE 3: SOLUSI & TUJUAN SIPESAT ====================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "2. SOLUSI & TUJUAN SISTEM (SIPESAT)", "Transformasi Menuju Pelayanan Administrasi Digital Mandiri")
    add_card(s3, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3), "Tujuan Utama Perancangan SIPESAT", [
        "Menyediakan platform pengajuan surat mandiri (self-service) yang dapat diakses siswa 24/7.",
        "Mendukung 4 jenis surat resmi: Siswa Aktif, Rekomendasi Beasiswa, Legalisir Ijazah, dan Dispensasi.",
        "Otomatisasi validasi unggah berkas persyaratan (Maksimal 2 MB, format PDF/JPG/PNG).",
        "Mengeliminasi ketergantungan kertas (paperless office) dan mempercepat turnaround time layanan."
    ], badge="Value Proposition")
    add_card(s3, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3), "Fitur Unggulan Sistem", [
        "Auto-Numbering Engine: Generator format nomor surat dinamis resmi sekolah.",
        "Tanda Tangan Digital QR Code: Verifikasi keaslian dokumen digital anti-pemalsuan.",
        "Timeline Tracking Stepper: Pemantauan alur status surat secara transparan & real-time.",
        "Decoupled Architecture: Pemisahan Next.js 14 frontend dan Express REST API backend yang cepat dan ringan."
    ], badge="Keunggulan Teknis")

    # ==================== SLIDE 4: RUANG LINGKUP & 2 ROLE ====================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "3. RUANG LINGKUP & PERAN PENGGUNA (RBAC)", "Penyederhanaan Alur Birokrasi: 2 Peran Pengguna Eksklusif")
    add_card(s4, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3), "Peran 1: Siswa (Aktor Pemohon)", [
        "Login akun menggunakan NISN terdaftar dan kata sandi.",
        "Mengakses katalog jenis surat dan persyaratan administratif.",
        "Mengisi formulir permohonan dan mengunggah berkas syarat (≤ 2MB).",
        "Memantau status permohonan via Timeline Stepper (5 status alur hidup).",
        "Mengunduh langsung dokumen surat resmi ber-QR Code setelah disetujui."
    ], badge="End User Interface")
    add_card(s4, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3), "Peran 2: Petugas TU / Admin (Otorisator)", [
        "Login menggunakan akun admin/petugas terdaftar.",
        "Dashboard operasional: ringkasan agregat surat masuk, diproses, selesai.",
        "Verifikasi keabsahan dokumen persyaratan siswa.",
        "Pemberian disposisi: Setujui (Approve) atau Tolak (Reject) disertai alasan perbaikan.",
        "Penetapan nomor surat resmi otomatis dan penerbitan dokumen digital.",
        "Ekspor laporan rekapitulasi persuratan (CSV / PDF) per periode."
    ], badge="Administrative Portal")

    # ==================== SLIDE 5: SPESIFIKASI KEBUTUHAN (SRS) ====================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "4. SPESIFIKASI KEBUTUHAN PERANGKAT LUNAK (SRS)", "Standar IEEE Std 830-1998 / Karl Wiegers (Tugas 2)")
    add_card(s5, Inches(0.8), Inches(1.5), Inches(3.6), Inches(5.3), "Kebutuhan Fungsional (FR)", [
        "FR-01: Autentikasi RBAC multi-role dengan token JWT.",
        "FR-02: Manajemen pengajuan surat mandiri & input dinamis.",
        "FR-03: Validasi unggah berkas persyaratan (MIME & 2MB).",
        "FR-04: Pelacakan status permohonan real-time.",
        "FR-05: Modul verifikasi & disposisi petugas TU.",
        "FR-06: Penomoran otomatis & generator PDF ber-QR Code."
    ], badge="Functional Needs")
    add_card(s5, Inches(4.8), Inches(1.5), Inches(3.6), Inches(5.3), "Kebutuhan Non-Fungsional (NFR)", [
        "Performance: Waktu respon API rata-rata di bawah 300 ms.",
        "Security: Hashing kata sandi Bcrypt & validasi Bearer JWT.",
        "Integrity: Transaksi database ACID via Prisma ORM.",
        "Availability: Sistem dapat diakses 24/7 berbasis web.",
        "Portability: Arsitektur containerized Docker (Postgres 16)."
    ], badge="Quality Attributes")
    add_card(s5, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.3), "Batasan Perancangan Sistem", [
        "Format nomor surat mengikuti standar dinas pendidikan.",
        "Penyimpanan berkas dibatasi maksimal 2 MB per dokumen.",
        "Siswa hanya dapat mengedit permohonan saat berstatus DRAFT.",
        "Dokumen final hanya dapat diunduh jika status telah DISETUJUI."
    ], badge="Design Constraints")

    # ==================== SLIDE 6: USE CASE DIAGRAM ====================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "5. PEMODELAN UML: USE CASE DIAGRAM", "Pemodelan Interaksi Fungsional Sistem dengan Aktor (Tugas 3)")
    add_card(s6, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3), "Struktur Use Case Diagram SIPESAT", [
        "2 Aktor Utama: Siswa dan Petugas TU / Admin.",
        "18 Use Cases teridentifikasi mencakup seluruh siklus hidup surat.",
        "Relasi <<include>>: Setiap aksi pengajuan surat dan verifikasi mewajibkan proses Login Autentikasi terlebih dahulu.",
        "Relasi <<include>>: Proses Cetak Surat Resmi mewajibkan verifikasi dan penomoran surat terlebih dahulu.",
        "Relasi <<extend>>: Pengunggahan berkas persyaratan dan penolakan surat disertai catatan disposisi."
    ], badge="UML 2.5 Use Case")
    add_card(s6, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3), "Paket Fitur Use Case Utama", [
        "Paket 1: Autentikasi & Profil (Login, Logout, Ganti Password).",
        "Paket 2: Layanan Siswa (Lihat Katalog, Isi Form, Upload Syarat, Lacak Stepper, Unduh PDF Surat).",
        "Paket 3: Layanan Petugas TU (Verifikasi Berkas, Beri Disposisi, Terbitkan No. Surat, Tanda Tangan QR, Ekspor Laporan).",
        "Master Diagram: Tersimpan lengkap dalam berkas use-case-siswa-admin.drawio (Tab 3)."
    ], badge="Modular Packages")

    # ==================== SLIDE 7: ACTIVITY DIAGRAM ====================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "6. PEMODELAN UML: ACTIVITY DIAGRAM", "Alur Kerja Aliran Data Multi-Swimlane (Tugas 4)")
    add_card(s7, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3), "Activity Diagram: Alur Pengajuan Siswa", [
        "Swimlane 1: Siswa | Swimlane 2: Sistem SIPESAT.",
        "Langkah: Siswa login -> Sistem validasi kredensial -> Tampilkan dashboard.",
        "Siswa memilih jenis surat -> Mengisi formulir tujuan permohonan.",
        "Siswa mengunggah berkas persyaratan -> Sistem validasi MIME & limit 2MB.",
        "Percabangan Validasi: Jika ukuran > 2MB, sistem tolak & minta unggah ulang.",
        "Jika valid: Simpan ke database, set status DIAJUKAN, terbitkan kode tiket pelacakan."
    ], badge="Siswa Swimlane")
    add_card(s7, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3), "Activity Diagram: Alur Verifikasi Petugas TU", [
        "Swimlane 1: Petugas TU | Swimlane 2: Sistem SIPESAT.",
        "Petugas membuka antrean surat masuk -> Sistem tampilkan daftar pengajuan.",
        "Petugas memeriksa kelengkapan & keabsahan berkas fisik-digital.",
        "Percabangan Keputusan: Jika tidak sesuai -> Status DITOLAK + catatan perbaikan.",
        "Jika sesuai -> Status DISETUJUI -> Sistem men-generate nomor surat resmi dan membuat stempel QR Code TTE.",
        "Sistem memperbarui status menjadi SELESAI dan membuka akses unduh PDF."
    ], badge="Petugas TU Swimlane")

    # ==================== SLIDE 8: SEQUENCE DIAGRAM ====================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "7. PEMODELAN UML: SEQUENCE DIAGRAM", "Pola Interaksi Objek Boundary - Control - Entity (BCE) (Tugas 4)")
    add_card(s8, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3), "Pola Arsitektur BCE Standar UNINDRA", [
        "Boundary (|O): Antarmuka web pengajuan (FormPengajuanUI, DashboardTU_UI).",
        "Control (↺O): Komponen logika bisnis (PengajuanController, SuratController, AuthController).",
        "Entity (_O_): Tabel basis data relasional (tb_pengajuan_surat, tb_user, tb_jenis_surat).",
        "Menjamin pemisahan tegas antara visual pengguna, pemrosesan logika, dan penyimpanan data fisik."
    ], badge="BCE Pattern")
    add_card(s8, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3), "Cakupan 4 Skenario Sequence Diagram", [
        "Sequence 1: Skenario Autentikasi Pengguna & Penyerahan Token JWT.",
        "Sequence 2: Skenario Permohonan Surat Siswa & Penanganan Berkas Multer.",
        "Sequence 3: Skenario Verifikasi Dokumen & Disposisi Petugas TU.",
        "Sequence 4: Skenario Pelacakan Status & Streaming Unduh Dokumen PDF.",
        "Dilengkapi bingkai percabangan kondisi alt (Valid vs Invalid Credentials / Approved vs Rejected)."
    ], badge="Core Scenarios")

    # ==================== SLIDE 9: CLASS DIAGRAM ====================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "8. PEMODELAN UML: CLASS DIAGRAM & BASIS DATA", "Struktur Statis Sistem, Enkapsulasi & Normalisasi 3NF (Tugas 6)")
    add_card(s9, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3), "Hierarki Kelas & Hubungan OOP", [
        "Superclass Abstract: Pengguna (id, username, password_hash, role, status).",
        "Subclass Inheritance: Siswa (nisn, kelas, jurusan) & PetugasTU (nip, nomor_sk, bagian).",
        "Kelas PengajuanSurat: Memiliki relasi asosiasi ke Siswa (1..*), JenisSurat (1..1), dan PetugasTU (0..1).",
        "Komposisi: BerkasPersyaratan dan RiwayatStatus terikat mutlak pada siklus hidup PengajuanSurat.",
        "Enkapsulasi: Atribut private (-) dilindungi oleh getter/setter dan metode operasi public (+)."
    ], badge="UML Class Structure")
    add_card(s9, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3), "Pemetaan ke PostgreSQL Relasional (3NF)", [
        "tb_user: Autentikasi terpusat & hashing Bcrypt.",
        "tb_siswa: Biodata spesifik siswa sekolah menengah.",
        "tb_petugas: Identitas otoritas staf Tata Usaha.",
        "tb_jenis_surat: Master konfigurasi format penomoran & syarat.",
        "tb_pengajuan_surat: Tabel transaksi permohonan surat.",
        "tb_berkas_persyaratan: Path penyimpanan fisik & metadata berkas.",
        "tb_riwayat_status: Rekam jejak audit trail alur disposisi."
    ], badge="Database Schema 3NF")

    # ==================== SLIDE 10: DEPLOYMENT DIAGRAM ====================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "9. ARSITEKTUR FISIK: DEPLOYMENT DIAGRAM", "Topologi Sistem 3-Tier Decoupled & Docker Containerization")
    add_card(s10, Inches(0.8), Inches(1.5), Inches(3.6), Inches(5.3), "Client Tier (Perangkat Pengguna)", [
        "Node: PC Laptop atau Smartphone.",
        "Environment: Browser Modern (Chrome, Edge, Safari).",
        "Artifact: SIPESAT Web App (HTML5, CSS3, React DOM).",
        "Komunikasi: HTTP/HTTPS (Port 3000) & REST API JSON (Port 5000)."
    ], badge="Tier 1: Presentation")
    add_card(s10, Inches(4.8), Inches(1.5), Inches(3.6), Inches(5.3), "Application & Service Tier", [
        "Web Server: Next.js 14 App Router (Port 3000) untuk Server-Side Rendering.",
        "API Server: Express.js + TypeScript (Port 5000).",
        "Components: AuthMiddleware (JWT), PengajuanController, SuratGenerator (PDFKit & QR), Multer FileHandler.",
        "ORM Engine: Prisma Client Connection Pool."
    ], badge="Tier 2: Logic & API")
    add_card(s10, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.3), "Data & Storage Tier (Docker)", [
        "Virtual Host: Docker Engine 24+.",
        "Container: sipesat-postgres-1 (PostgreSQL 16 Alpine, Port 5432).",
        "Volume 1: sipesat_postgres_data (Persistent Relational DB).",
        "Volume 2: be/uploads/ (Local File Storage Berkas Siswa & Dokumen Surat)."
    ], badge="Tier 3: Persistence")

    # ==================== SLIDE 11: IMPLEMENTASI & PENGUJIAN ====================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "10. IMPLEMENTASI SISTEM & HASIL PENGUJIAN", "Konstruksi Fullstack (Tugas 10) & Black Box Testing 35 Test Cases (Tugas 11)")
    add_card(s11, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3), "Hasil Implementasi Sistem (Tugas 10)", [
        "Monorepo Decoupled: be/ (Express REST API) & fe/ (Next.js 14).",
        "Penomoran Surat Dinamis: Format resmi (cth: 421/001/SMK-PSKD/XI/2026).",
        "Tanda Tangan Elektronik QR Code: Terenkripsi dan siap dipindai smartphone.",
        "Stepper Timeline: Visualisasi interaktif status alur permohonan surat.",
        "One-Click Launcher: Skrip start-local.bat dan migrate.bat untuk otomasi eksekusi."
    ], badge="Konstruksi Perangkat Lunak")
    add_card(s11, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3), "Hasil Pengujian Black Box (Tugas 11)", [
        "Metode: Black Box Testing (Equivalence Partitioning & Boundary Value Analysis).",
        "Cakupan: 35 Test Cases pada 7 Modul Inti (Autentikasi, Pengajuan, Stepper, Disposisi TU, Auto-Numbering, Master Data, Security Route Guard).",
        "Hasil: 35 dari 35 skenario pengujian berstatus VALID (100% PASS).",
        "Temuan: 0 Critical Defects, sistem siap dioperasikan di lingkungan sekolah."
    ], badge="Quality Assurance 100% Pass")

    # ==================== SLIDE 12: KESIMPULAN & PENUTUP ====================
    s12 = prs.slides.add_slide(blank_layout)
    bg12 = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg12.fill.solid()
    bg12.fill.fore_color.rgb = NAVY_DARK
    bg12.line.fill.background()

    t_box12 = s12.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(4.5))
    tf12 = t_box12.text_frame
    tf12.word_wrap = True

    p = tf12.paragraphs[0]
    p.text = "KESIMPULAN & PENUTUP"
    p.font.name = "Calibri"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    p_sub = tf12.add_paragraph()
    p_sub.text = "Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)"
    p_sub.font.name = "Calibri"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = RGBColor(147, 197, 253)
    p_sub.space_after = Pt(20)

    p_c1 = tf12.add_paragraph()
    p_c1.text = "1. Efisiensi Birokrasi: SIPESAT memangkas waktu pengajuan surat dari 2-3 hari kerja menjadi hitungan jam dengan alur mandiri yang terstandarisasi."
    p_c1.font.name = "Calibri"
    p_c1.font.size = Pt(13)
    p_c1.font.color.rgb = RGBColor(226, 232, 240)
    p_c1.space_after = Pt(8)

    p_c2 = tf12.add_paragraph()
    p_c2.text = "2. Integritas & Transparansi: Eliminasi risiko berkas fisik hilang, nomor surat ganda, dan ketidakpastian status berkat pelacakan stepper dan TTE QR Code."
    p_c2.font.name = "Calibri"
    p_c2.font.size = Pt(13)
    p_c2.font.color.rgb = RGBColor(226, 232, 240)
    p_c2.space_after = Pt(8)

    p_c3 = tf12.add_paragraph()
    p_c3.text = "3. Kepatuhan Akademik: Seluruh artefak perancangan (SRS, Use Case, Activity, Sequence, Class, Deployment, Konstruksi, dan Black Box Testing) selesai 100%."
    p_c3.font.name = "Calibri"
    p_c3.font.size = Pt(13)
    p_c3.font.color.rgb = RGBColor(226, 232, 240)
    p_c3.space_after = Pt(24)

    p_thx = tf12.add_paragraph()
    p_thx.text = "Terima Kasih atas Perhatian Dosen dan Rekan-Rekan Mahasiswa!\nSESI TANYA JAWAB (Q&A)"
    p_thx.font.name = "Calibri"
    p_thx.font.size = Pt(18)
    p_thx.font.bold = True
    p_thx.font.color.rgb = RGBColor(56, 189, 248)

    out_path = os.path.join(RPL_DIR, "SIPESAT_PRESENTASI_KELOMPOK_7.pptx")
    prs.save(out_path)
    print(f"Presentation generated successfully: {out_path}")

if __name__ == "__main__":
    create_deck()
