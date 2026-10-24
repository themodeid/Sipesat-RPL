import os
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

def build_docx_tugas6():
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

    # Helper text functions
    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, bold=False, italic=False, size=12, indent=True, space_after=6):
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

    def add_h1(title):
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

    def add_h2(title):
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

    # ================= COVER =================
    p_cov = doc.add_paragraph()
    p_cov.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cov = p_cov.add_run("TUGAS 6 - REKAYASA PERANGKAT LUNAK (RPL)\nPERANCANGAN CLASS DIAGRAM DAN OBJECT DIAGRAM")
    r_cov.bold = True
    r_cov.font.size = Pt(14)
    p_cov.paragraph_format.space_after = Pt(16)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Pemodelan Struktur Statis dan Instansiasi Objek Runtime Sistem Berbasis UML 2.5\nStudi Kasus: Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)")
    r_sub.italic = True
    r_sub.font.size = Pt(12)
    p_sub.paragraph_format.space_after = Pt(28)

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
    hdr[1].text = "Nama Anggota Kelompok 7 (RPL_XD)"
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

    # ================= BAB I =================
    add_h1("BAB I: PENDAHULUAN & LANDASAN TEORI")
    
    add_h2("1.1 Gambaran Umum Proyek SIPESAT")
    add_p(
        "Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) merupakan perangkat lunak layanan administrasi "
        "persuratan terpadu yang dirancang untuk mengotomatisasi birokrasi pengajuan surat di lingkungan sekolah menengah. "
        "Sistem ini menangani siklus hidup pengajuan surat keterangan siswa aktif, surat rekomendasi beasiswa, surat izin dispensasi, "
        "dan surat keterangan kelakuan baik. Arsitektur sistem bertumpu pada kontrol akses berbasis peran (Role-Based Access Control / RBAC) "
        "yang melibatkan tiga entitas pengguna utama: Siswa sebagai pemohon surat, Petugas Tata Usaha (TU) sebagai verifikator dan penerbit nomor surat, "
        "serta Kepala Sekolah sebagai pengesah bertanda tangan elektronik digital (TTE)."
    )

    add_h2("1.2 Konsep Dasar Class Diagram (UML 2.5)")
    add_p(
        "Class Diagram adalah diagram struktural statis utama dalam Unified Modeling Language (UML) 2.5 yang memodelkan "
        "struktur perangkat lunak dengan mendefinisikan kelas-kelas, atribut, metode, serta hubungan antar-kelas. "
        "Kelas merepresentasikan abstraksi dari kumpulan objek yang memiliki struktur data dan perilaku fungsional yang seragam. "
        "Tiga kompartemen utama dalam sebuah kelas UML meliputi:"
    )
    add_p("1. Nama Kelas: Identifier unik yang mencerminkan tanggung jawab konseptual kelas.", indent=False)
    add_p("2. Kompartemen Atribut: Karakteristik data yang dimiliki kelas, dilengkapi tingkat visibilitas (+ public, - private, # protected), nama atribut, dan tipe data primitif/objek.", indent=False)
    add_p("3. Kompartemen Operasi/Metode: Fungsi fungsional yang dapat dieksekusi oleh kelas, mencakup parameter masukan dan tipe nilai kembalian (return type).", indent=False)
    add_p(
        "Relasi antarkelas dalam Class Diagram mencakup Asosiasi (keterhubungan logis), Generalisasi/Inheritance (pewarisan sifat dari superclass ke subclass), "
        "Agregasi (hubungan kepemilikan 'has-a' yang longgar), Komposisi (hubungan kepemilikan mutlak di mana bagian tidak dapat hidup tanpa induknya), "
        "serta Multiplisitas (1..1, 1..*, 0..*) yang menegakkan integritas kardinalitas relasi."
    )

    add_h2("1.3 Konsep Dasar Object Diagram (UML 2.5)")
    add_p(
        "Object Diagram adalah diagram struktural yang menggambarkan snapshot instansiasi konkret dari Class Diagram pada "
        "satu titik waktu tertentu (point in time) saat sistem sedang dieksekusi. Jika Class Diagram memodelkan aturan abstrak dan cetak biru (blueprint), "
        "maka Object Diagram memodelkan entitas nyata yang telah diisi data atribut sesungguhnya di memori sistem."
    )
    add_p(
        "Konvensi penulisan elemen pada Object Diagram mencakup:\n"
        "1. Penamaan Objek: Ditulis dengan format namaObjek : NamaKelas dengan garis bawah (underline).\n"
        "2. Nilai Atribut Spesifik: Menyajikan data konkret hasil eksekusi (misalnya nomorTiket = 'TKT-202610-001', status = 'DISETUJUI').\n"
        "3. Link (Instansiasi Asosiasi): Menghubungkan objek konkret yang saling berinteraksi secara riil."
    )

    # ================= BAB II =================
    add_h1("BAB II: PERANCANGAN CLASS DIAGRAM SIPESAT")
    
    add_h2("2.1 Arsitektur Domain Model & Hirarki Kelas")
    add_p(
        "Struktur domain model SIPESAT dirancang berorientasi objek murni (Object-Oriented Architecture) dengan memisahkan "
        "tanggung jawab kelas ke dalam tiga layer utama: (1) Hirarki Pengguna & Otorisasi RBAC, (2) Entitas Bisnis & Master Persuratan, "
        "dan (3) Entitas Transaksional, Validasi, dan Audit Log."
    )

    # Tabel Kamus Data Kelas
    add_h2("2.2 Kamus Data Kelas (Class Dictionary)")
    add_p("Berikut adalah rincian spesifikasi formal kelas-kelas pembentuk sistem SIPESAT:")

    table_cls = doc.add_table(rows=1, cols=4)
    table_cls.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table_cls.rows[0].cells
    hdr[0].text = "Nama Kelas"
    hdr[1].text = "Tipe / Layer"
    hdr[2].text = "Atribut Utama (Visibility & Data Type)"
    hdr[3].text = "Metode / Operasi Utama"
    for c in hdr:
        set_cell_background(c, "1E293B")
        for p_c in c.paragraphs:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r_c in p_c.runs:
                r_c.font.color.rgb = RGBColor(255, 255, 255)
                r_c.bold = True
                r_c.font.size = Pt(9.5)

    class_dict_data = [
        ("Pengguna (Abstract)", "Superclass RBAC", "- id_pengguna: UUID\n- username: String\n- password_hash: String\n- email: String\n- role: RoleEnum\n- status_aktif: Boolean", "+ login(user, pass): Boolean\n+ logout(): Void\n+ updatePassword(newPass): Boolean"),
        ("Siswa", "Subclass Pengguna", "- nisn: String\n- nis: String\n- nama_lengkap: String\n- kelas: String\n- jurusan: String\n- no_telepon: String", "+ buatPengajuanSurat(): PengajuanSurat\n+ uploadBerkasPersyaratan(): Void\n+ lacakStatusSurat(tiket): StatusEnum"),
        ("PetugasTU", "Subclass Pengguna", "- nip: String\n- nama_petugas: String\n- nomor_sk: String\n- bagian: String", "+ verifikasiBerkas(id): Boolean\n+ beriNomorSurat(id): String\n+ cetakDraftSurat(id): FilePDF\n+ forwardKeKepsek(id): Void"),
        ("KepalaSekolah", "Subclass Pengguna", "- nip: String\n- nama_lengkap: String\n- pangkat_gol: String\n- ttd_digital_hash: String", "+ reviewPengajuan(id): PengajuanSurat\n+ approveSurat(id): Boolean\n+ rejectSurat(id, alasan): Boolean\n+ bubuhkanQRCodeTTE(id): String"),
        ("JenisSurat", "Master Data", "- id_jenis: UUID\n- kode_surat: String\n- nama_surat: String\n- masa_berlaku_hari: Integer\n- template_path: String", "+ getSyaratDokumen(): List<String>\n+ generateNomorOtomatis(): String"),
        ("PengajuanSurat", "Core Transaction", "- id_pengajuan: UUID\n- nomor_tiket: String\n- tanggal_pengajuan: DateTime\n- keperluan: String\n- status: StatusSuratEnum\n- nomor_surat_resmi: String\n- qr_code_hash: String\n- file_output_url: String", "+ hitungEstimasiSelesai(): DateTime\n+ updateStatus(newStatus): Void\n+ generateNomorTiket(): String\n+ batalkanPengajuan(): Boolean"),
        ("BerkasPersyaratan", "Entity / Attachment", "- id_berkas: UUID\n- nama_file: String\n- file_url: String\n- file_size_kb: Integer\n- status_valid: Boolean", "+ validasiUkuranBerkas(): Boolean\n+ validasiEkstensi(): Boolean"),
        ("VerifikasiTU", "Transaction Log", "- id_verifikasi: UUID\n- tanggal_verifikasi: DateTime\n- status_berkas: Boolean\n- catatan_revisi: String", "+ simpanCatatanVerifikasi(): Void\n+ kirimNotifikasiRevisi(): Void"),
        ("ApprovalKepsek", "Transaction Log", "- id_approval: UUID\n- tanggal_approval: DateTime\n- keputusan: ApprovalEnum\n- catatan_kepsek: String\n- signature_token: String", "+ generateTTE(): String\n+ auditKeputusan(): Void"),
        ("Notifikasi", "Supporting Entity", "- id_notifikasi: UUID\n- pesan: String\n- is_read: Boolean\n- timestamp: DateTime", "+ kirimNotifikasi(): Void\n+ tandaiDibaca(): Void"),
        ("AuditLog", "Security & Telemetry", "- id_log: UUID\n- aktivitas: String\n- ip_address: String\n- created_at: DateTime", "+ catatAktivitas(act, ip): Void")
    ]

    for c_data in class_dict_data:
        row = table_cls.add_row().cells
        for i in range(4):
            row[i].text = c_data[i]
            row[i].paragraphs[0].runs[0].font.size = Pt(8.5)
            set_cell_margins(row[i], 60, 60, 80, 80)
        set_cell_background(row[0], "F1F5F9")
        row[0].paragraphs[0].runs[0].font.bold = True

    set_table_borders(table_cls)

    # 2.3 Matriks Relasi Antarkelas
    add_h2("2.3 Matriks Relasi dan Kardinalitas Antarkelas")
    add_p("Hubungan antar-kelas dalam sistem SIPESAT didefinisikan secara ketat:")
    add_p("1. Generalisasi (Inheritance): Siswa, PetugasTU, dan KepalaSekolah merupakan turunan dari superclass abstrak Pengguna.", indent=False)
    add_p("2. Asosiasi (1 to Many): 1 Siswa dapat mengajukan 0..* PengajuanSurat. Setiap PengajuanSurat wajib dimiliki tepat 1 Siswa.", indent=False)
    add_p("3. Asosiasi (Many to 1): Banyak PengajuanSurat merujuk ke 1 JenisSurat.", indent=False)
    add_p("4. Komposisi (1 to Many): 1 PengajuanSurat memiliki 1..* BerkasPersyaratan. Jika pengajuan dihapus, berkas fisik terkait ikut terhapus.", indent=False)
    add_p("5. Asosiasi (1 to 1): 1 PengajuanSurat memiliki tepat 1 VerifikasiTU dan 0..1 ApprovalKepsek.", indent=False)
    add_p("6. Asosiasi (1 to Many): 1 Pengguna menerima 0..* Notifikasi dan menghasilkan 0..* AuditLog.", indent=False)

    doc.add_page_break()

    # ================= BAB III =================
    add_h1("BAB III: PERANCANGAN OBJECT DIAGRAM SIPESAT")
    
    add_h2("3.1 Narasi Skenario Instansiasi Konkret (Runtime Snapshot)")
    add_p(
        "Untuk memvalidasi keabsahan Class Diagram, dirancang Object Diagram yang memodelkan satu skenario nyata: "
        "Siswa atas nama 'Adam Wahyu Kurniawan' (NISN: 0051234567) mengajukan 'Surat Keterangan Siswa Aktif' untuk keperluan "
        "'Persyaratan Beasiswa Prestasi 2026'. Berkas Kartu Keluarga diunggah, diverifikasi valid oleh Staf TU 'Budi Santoso, S.Kom', "
        "diteruskan ke Kepala Sekolah 'Drs. H. Hasan Basri, M.Pd', dan secara resmi disahkan dengan pembubuhan TTE QR-Code "
        "bernomor surat resmi '421.3/088/SMK/X/2026'."
    )

    add_h2("3.2 Tabel Pemetaan Objek Konkret dan Nilai Atribut")
    table_obj = doc.add_table(rows=1, cols=3)
    table_obj.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_o = table_obj.rows[0].cells
    hdr_o[0].text = "Nama Objek : Kelas"
    hdr_o[1].text = "Nilai Atribut Konkret (Runtime State)"
    hdr_o[2].text = "Keterangan Peran dalam Skenario"
    for c in hdr_o:
        set_cell_background(c, "1E293B")
        for p_c in c.paragraphs:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r_c in p_c.runs:
                r_c.font.color.rgb = RGBColor(255, 255, 255)
                r_c.bold = True
                r_c.font.size = Pt(9.5)

    obj_dict_data = [
        ("adamSiswa : Siswa", "id_pengguna = 'USR-001'\nusername = 'adam.wahyu'\nnisn = '0051234567'\nnama_lengkap = 'Adam Wahyu Kurniawan'\nkelas = 'XII RPL 1'\njurusan = 'Rekayasa Perangkat Lunak'", "Siswa pemohon surat aktif yang sah terdaftar di sekolah."),
        ("budiTU : PetugasTU", "id_pengguna = 'USR-002'\nusername = 'budi.tu'\nnip = '198503152010011002'\nnama_petugas = 'Budi Santoso, S.Kom'\nbagian = 'Administrasi Kesiswaan'", "Staf TU yang memeriksa berkas dan menerbitkan nomor surat."),
        ("hasanKepsek : KepalaSekolah", "id_pengguna = 'USR-003'\nusername = 'hasan.kepsek'\nnip = '197204121998021001'\nnama_lengkap = 'Drs. H. Hasan Basri, M.Pd'\npangkat_gol = 'Pembina Utama Muda / IV-C'", "Pimpinan sekolah pemegang otorisasi TTE QR-Code."),
        ("suratAktif : JenisSurat", "id_jenis = 'JNS-001'\nkode_surat = 'SK-AKTIF'\nnama_surat = 'Surat Keterangan Siswa Aktif'\nmasa_berlaku_hari = 30", "Master jenis surat yang dimohonkan."),
        ("pengajuan001 : PengajuanSurat", "id_pengajuan = 'REQ-202610-001'\nnomor_tiket = 'TKT-202610-001'\ntanggal_pengajuan = '16-10-2026 09:15'\nkeperluan = 'Persyaratan Beasiswa Prestasi 2026'\nstatus = DISETUJUI\nnomor_surat_resmi = '421.3/088/SMK/X/2026'\nqr_code_hash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'", "Instansiasi permohonan surat yang telah selesai diproses."),
        ("berkasKK : BerkasPersyaratan", "id_berkas = 'DOC-001'\nnama_file = 'kartu_keluarga_adam.pdf'\nfile_url = '/uploads/kk_adam.pdf'\nfile_size_kb = 485\nstatus_valid = true", "Lampiran dokumen persyaratan yang diunggah siswa."),
        ("verif001 : VerifikasiTU", "id_verifikasi = 'VRF-001'\ntanggal_verifikasi = '16-10-2026 10:30'\nstatus_berkas = true\ncatatan_revisi = 'Berkas lengkap dan data absensi valid'", "Log verifikasi kelayakan permohonan oleh TU."),
        ("appr001 : ApprovalKepsek", "id_approval = 'APP-001'\ntanggal_approval = '16-10-2026 11:45'\nkeputusan = DISETUJUI\ncatatan_kepsek = 'Disetujui untuk pengajuan beasiswa'", "Log otorisasi pengesahan akhir oleh Kepala Sekolah."),
        ("notif001 : Notifikasi", "id_notifikasi = 'NTF-001'\npesan = 'Surat Keterangan Aktif Anda telah disahkan dan siap diunduh.'\nis_read = false\ntimestamp = '16-10-2026 11:46'", "Pemberitahuan real-time kepada siswa pemohon.")
    ]

    for o_data in obj_dict_data:
        row = table_obj.add_row().cells
        for i in range(3):
            row[i].text = o_data[i]
            row[i].paragraphs[0].runs[0].font.size = Pt(8.5)
            set_cell_margins(row[i], 60, 60, 80, 80)
        set_cell_background(row[0], "F1F5F9")
        row[0].paragraphs[0].runs[0].font.bold = True

    set_table_borders(table_obj)

    # ================= BAB IV =================
    add_h1("BAB IV: ANALISIS INTEGRASI DAN IMPLEMENTASI ARSITEKTUR")
    add_h2("4.1 Pemetaan Class Diagram ke Skema Database Relasional (PostgreSQL / Prisma ORM)")
    add_p(
        "Model Class Diagram di atas memetakan relasi 1-to-1 ke dalam tabel basis data PostgreSQL pada sistem SIPESAT. "
        "Superclass 'Pengguna' dipetakan menggunakan pola Single Table Inheritance (STI) atau Concrete Table Inheritance "
        "dengan kolom 'role' enum (SISWA, PETUGAS_TU, KEPALA_SEKOLAH). "
        "Atribut nomor_tiket pada PengajuanSurat memiliki constraint UNIQUE INDEX, sedangkan relasi komposisi "
        "ke BerkasPersyaratan ditegakkan melalui deklarasi foreign key ON DELETE CASCADE."
    )

    add_h2("4.2 Konsistensi Hulu-Hilir dengan Diagram UML Terdahulu")
    add_p(
        "Perancangan Class Diagram dan Object Diagram pada Tugas 6 ini menjaga konsistensi hulu-ke-hilir dengan tugas sebelumnya: "
        "(1) Metode dalam kelas Siswa (buatPengajuanSurat) memetakan Use Case Diagram Tugas 3, "
        "(2) Alur method invocation antarkelas (verifikasiBerkas, forwardKeKepsek, approveSurat) merepresentasikan lifeline Sequence Diagram Tugas 4, dan "
        "(3) Nilai atribut status (DRAFT, MENUNGGU_VERIFIKASI, DISETUJUI, DITOLAK) identik 100% dengan State Machine Diagram Tugas 5."
    )

    # ================= BAB V =================
    add_h1("BAB V: KESIMPULAN & SARAN")
    add_h2("5.1 Kesimpulan")
    add_p("Berdasarkan perancangan Class Diagram dan Object Diagram untuk proyek SIPESAT, dapat disimpulkan bahwa:")
    add_p("1. Class Diagram telah berhasil memodelkan 11 kelas komprehensif yang mencakup entitas otorisasi RBAC, master persuratan, dan log audit dengan prinsip enkapsulasi data murni.", indent=False)
    add_p("2. Relasi pewarisan (Generalisasi), Asosiasi, dan Komposisi menjamin integritas data persuratan sekolah secara terstruktur dan anti-redundansi.", indent=False)
    add_p("3. Object Diagram berhasil membuktikan kelayakan operasional sistem pada skenario runtime penerbitan surat ber-QR Code tanpa adanya anomali ketergantungan siklis (circular dependency).", indent=False)

    add_h2("5.2 Daftar Pustaka")
    add_p("1. Object Management Group (OMG). (2017). Unified Modeling Language (OMG UML) Specification Version 2.5.1.", indent=False)
    add_p("2. Pressman, R. S., & Maxim, B. R. (2020). Software Engineering: A Practitioner's Approach (9th ed.). McGraw-Hill Education.", indent=False)
    add_p("3. Sommerville, I. (2016). Software Engineering (10th ed.). Pearson Education.", indent=False)
    add_p("4. Wiegers, K., & Beatty, J. (2013). Software Requirements (3rd ed.). Microsoft Press.", indent=False)

    out_file = os.path.join(RPL_DIR, "tugas-6-class-object.docx")
    doc.save(out_file)
    print(f"Successfully generated DOCX at: {out_file}")

if __name__ == "__main__":
    build_docx_tugas6()
