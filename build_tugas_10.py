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
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_docx_tugas10():
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
    style_normal.font.size = Pt(12)
    style_normal.font.color.rgb = RGBColor(0, 0, 0)
    style_normal.paragraph_format.line_spacing = 1.5

    def add_p(text, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.5
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
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

    def add_code_block(code_text, title=None):
        if title:
            p_lbl = doc.add_paragraph()
            p_lbl.paragraph_format.space_before = Pt(6)
            p_lbl.paragraph_format.space_after = Pt(2)
            r_lbl = p_lbl.add_run(title)
            r_lbl.bold = True
            r_lbl.italic = True
            r_lbl.font.size = Pt(10)
            r_lbl.font.name = 'Times New Roman'

        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        c = tbl.rows[0].cells[0]
        set_cell_background(c, "F8FAFC")
        set_cell_margins(c, top=80, bottom=80, left=120, right=120)

        # Single border box
        tcPr = c._tc.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
            f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
            f'  <w:left w:val="single" w:sz="12" w:space="0" w:color="3B82F6"/>'
            f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)

        p = c.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        r = p.add_run(code_text)
        r.font.name = 'Consolas'
        r.font.size = Pt(9.0)
        r.font.color.rgb = RGBColor(30, 41, 59)

        p_spc = doc.add_paragraph()
        p_spc.paragraph_format.space_after = Pt(6)

    # ================= COVER =================
    p_cov = doc.add_paragraph()
    p_cov.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_cov = p_cov.add_run("TUGAS 10 - REKAYASA PERANGKAT LUNAK (RPL)\nKONSTRUKSI DAN IMPLEMENTASI PERANGKAT LUNAK")
    r_cov.bold = True
    r_cov.font.size = Pt(14)
    p_cov.paragraph_format.space_after = Pt(14)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Mengimplementasikan Hasil Rancangan Desain UML ke dalam Kode Program Fisik\nStudi Kasus: Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)")
    r_sub.italic = True
    r_sub.font.size = Pt(12)
    p_sub.paragraph_format.space_after = Pt(24)

    p_kampus = doc.add_paragraph()
    p_kampus.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_k = p_kampus.add_run("UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)\nFAKULTAS TEKNIK DAN ILMU KOMPUTER\nPROGRAM STUDI TEKNIK INFORMATIKA\n2026/2027")
    r_k.bold = True
    r_k.font.size = Pt(11)
    p_kampus.paragraph_format.space_after = Pt(20)

    # Identitas Kelompok Table
    table_kel = doc.add_table(rows=1, cols=3)
    table_kel.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table_kel.rows[0].cells
    hdr[0].text = "No."
    hdr[1].text = "Nama Anggota Kelompok 7 (RPL_XD)"
    hdr[2].text = "NPM"
    for cell in hdr:
        set_cell_background(cell, "1E293B")
        for p_c in cell.paragraphs:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r_c in p_c.runs:
                r_c.font.color.rgb = RGBColor(255, 255, 255)
                r_c.bold = True
                r_c.font.size = Pt(10)

    members = [
        ("1", "Adam Wahyu Kurniawan (Lead System Architect & SWE)", "202343500510"),
        ("2", "Fathu Rahman (Business Analyst & Req. Engineer)", "202343500467"),
        ("3", "Surya Edi Saputra (QA & Technical Writer)", "202343500468"),
        ("4", "Rizqi Muh. Al Hakimi (Database Specialist & UI/UX)", "202343500449"),
    ]
    for m in members:
        row = table_kel.add_row().cells
        row[0].text = m[0]
        row[1].text = m[1]
        row[2].text = m[2]
        row[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for i in range(3):
            set_cell_margins(row[i], 60, 60, 80, 80)
            row[i].paragraphs[0].runs[0].font.size = Pt(9.5)
            row[i].paragraphs[0].runs[0].font.name = 'Times New Roman'

    set_table_borders(table_kel)
    doc.add_page_break()

    # ================= BAB I =================
    add_h1("BAB I: PENDAHULUAN & KONSEP DASAR KONSTRUKSI PL")
    add_h2("1.1 Gambaran Umum & Posisi Konstruksi dalam SDLC")
    add_p(
        "Dalam siklus hidup pengembangan perangkat lunak (Software Development Life Cycle - SDLC), tahap Konstruksi "
        "Perangkat Lunak (Software Construction) merupakan fase fundamental yang berada di antara tahap perancangan arsitektur (Design) "
        "dan tahap pengujian (Testing). Tahap ini menitikberatkan pada proses penerjemahan representasi abstrak perancangan—seperti "
        "Class Diagram, Sequence Diagram, State Machine Diagram, dan Prototipe Wireframe—menjadi baris kode program fisik yang dapat "
        "dieksekusi secara deterministik oleh mesin komputer."
    )
    add_p(
        "Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) dirancang untuk mengotomatisasi birokrasi persuratan siswa "
        "(Surat Keterangan Siswa Aktif, Rekomendasi Beasiswa, Legalisir Ijazah, dan Dispensasi). Mengingat sistem ini mengelola "
        "dokumen resmi sekolah dan data identitas siswa, tahap konstruksi perangkat lunak wajib menjamin keselarasan 1-to-1 antara "
        "rancangan UML yang telah disahkan dengan implementasi kode program fisik, mencegah terjadinya deviasi (architectural drift), "
        "serta mengeliminasi kerentanan keamanan dan redundansi logika."
    )

    add_h2("1.2 Prinsip Kode Berkualitas Tinggi (Clean Code Principles)")
    add_p("Pembangunan kode program SIPESAT berlandaskan pada 6 pilar rekayasa kode standar industri:")
    p_b1 = doc.add_paragraph()
    p_b1.paragraph_format.line_spacing = 1.5
    p_b1.paragraph_format.space_after = Pt(6)
    p_b1.add_run(
        "1. Readability (Keterbacaan): Kode ditulis bersih dengan indentasi konsisten dan penamaan deskriptif sehingga mudah dipahami tim.\n"
        "2. Maintainability (Kemudahan Pemeliharaan): Modul dipisahkan secara modular antara Routing, Controller, Prisma ORM, dan UI.\n"
        "3. Reusability (Dapat Digunakan Kembali): Logika pemformatan nomor surat dan middleware diisolasi menjadi modul bersama.\n"
        "4. Efficiency (Efisiensi): Kueri database dioptimalkan via projection select untuk mencegah beban I/O memori berlebih.\n"
        "5. Prinsip DRY (Don't Repeat Yourself): Menolak keras duplikasi kode; setiap aturan bisnis didefinisikan satu kali.\n"
        "6. Prinsip KISS (Keep It Simple, Stupid): Memilih solusi yang paling sederhana, deterministik, dan anti-overengineering."
    )

    add_h2("1.3 Standar Penamaan (Coding Standards & Naming Conventions)")
    add_p(
        "Implementasi kode SIPESAT menggunakan ekosistem TypeScript/Node.js modern dengan konvensi: (1) PascalCase untuk nama Class, "
        "Model Prisma, dan Komponen React; (2) camelCase untuk nama fungsi, variabel, method, dan endpoint parameter; (3) SCREAMING_SNAKE_CASE "
        "untuk konstanta global dan nilai enumerasi database; serta (4) Single Responsibility Principle di mana setiap fungsi hanya bertugas "
        "menjalankan satu tujuan spesifik."
    )

    # ================= BAB II =================
    add_h1("BAB II: TRANSFORMASI CLASS DIAGRAM KE KODE PROGRAM (MODEL & DATABASE)")
    add_h2("2.1 Konsep Transformasi Desain Struktural ke Kode")
    add_p(
        "Class Diagram (Tugas 6) mendefinisikan struktur statis sistem berupa kelas, atribut, tipe data, dan relasi. "
        "Pada tahap konstruksi SIPESAT, transformasi dilakukan secara langsung menuju skema basis data relasional PostgreSQL melalui "
        "Prisma ORM dan interface TypeScript. Nama kelas menjadi nama tabel model, visibilitas private ditegakkan melalui seleksi kolom "
        "controller, dan relasi multiplisitas diterjemahkan menjadi relasi Foreign Key relasional."
    )

    add_h2("2.2 Implementasi Entitas Pengguna & RBAC (User Model)")
    add_p("Berikut adalah kode skema Prisma ORM hasil transformasi kelas Pengguna, Siswa, dan Petugas TU:")
    add_code_block(
        "enum Role {\n"
        "  ADMIN\n"
        "  PETUGAS\n"
        "  SISWA\n"
        "}\n\n"
        "model User {\n"
        "  id              String           @id @default(cuid())\n"
        "  username        String?          @unique\n"
        "  nisn            String?          @unique\n"
        "  nama            String\n"
        "  email           String?\n"
        "  password        String\n"
        "  role            Role             @default(SISWA)\n"
        "  kelas           String?\n"
        "  jurusan         String?\n"
        "  noTelepon       String?\n"
        "  alamat          String?\n"
        "  createdAt       DateTime         @default(now())\n"
        "  updatedAt       DateTime         @updatedAt\n\n"
        "  pengajuan       PengajuanSurat[] @relation(\"SiswaPengajuan\")\n"
        "  prosesPengajuan PengajuanSurat[] @relation(\"PetugasPemroses\")\n"
        "  logs            LogAktivitas[]\n"
        "}",
        "Kode 2.1: Model User dan Role Enumerasi pada Skema Prisma ORM (be/prisma/schema.prisma)"
    )

    add_h2("2.3 Implementasi Entitas Transaksional Surat (PengajuanSurat & JenisSurat)")
    add_p("Transformasi kelas JenisSurat dan PengajuanSurat menghasilkan model transaksional dengan integritas foreign key kuat:")
    add_code_block(
        "enum StatusPengajuan {\n"
        "  MENUNGGU\n"
        "  DIPROSES\n"
        "  DISETUJUI\n"
        "  DITOLAK\n"
        "}\n\n"
        "model JenisSurat {\n"
        "  id           String           @id @default(cuid())\n"
        "  kodeSurat    String           @unique\n"
        "  namaSurat    String\n"
        "  deskripsi    String\n"
        "  persyaratan  String?\n"
        "  formatNomor  String           @default(\"421.3/{NOMOR}/SMKN1/{BULAN_ROMAWI}/{TAHUN}\")\n"
        "  templateIsi  String?\n"
        "  isActive     Boolean          @default(true)\n"
        "  createdAt    DateTime         @default(now())\n"
        "  updatedAt    DateTime         @updatedAt\n\n"
        "  pengajuan    PengajuanSurat[]\n"
        "}\n\n"
        "model PengajuanSurat {\n"
        "  id               String          @id @default(cuid())\n"
        "  nomorPengajuan   String          @unique\n"
        "  siswaId          String\n"
        "  siswa            User            @relation(\"SiswaPengajuan\", fields: [siswaId], references: [id], onDelete: Cascade)\n"
        "  jenisSuratId     String\n"
        "  jenisSurat       JenisSurat      @relation(fields: [jenisSuratId], references: [id])\n"
        "  keperluan        String\n"
        "  keterangan       String?\n"
        "  lampiran         String?\n"
        "  status           StatusPengajuan @default(MENUNGGU)\n"
        "  nomorSuratResmi  String?\n"
        "  petugasId        String?\n"
        "  petugas          User?           @relation(\"PetugasPemroses\", fields: [petugasId], references: [id])\n"
        "  catatanPetugas   String?\n"
        "  tanggalPengajuan DateTime        @default(now())\n"
        "  tanggalSelesai   DateTime?\n"
        "  updatedAt        DateTime        @updatedAt\n\n"
        "  logs             LogAktivitas[]\n"
        "}",
        "Kode 2.2: Model Transaksional PengajuanSurat dan JenisSurat (be/prisma/schema.prisma)"
    )

    add_h2("2.4 Tabel Komparasi Pemetaan Class Diagram vs Kode Fisik")
    table_map = doc.add_table(rows=1, cols=3)
    table_map.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_m = table_map.rows[0].cells
    hdr_m[0].text = "Elemen Class Diagram (UML 2.5)"
    hdr_m[1].text = "Implementasi Kode Fisik (Prisma/TS)"
    hdr_m[2].text = "Keterangan Pemetaan Arsitektur"
    for cell in hdr_m:
        set_cell_background(cell, "1E293B")
        for p_c in cell.paragraphs:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r_c in p_c.runs:
                r_c.font.color.rgb = RGBColor(255, 255, 255)
                r_c.bold = True
                r_c.font.size = Pt(9.5)

    mapping_data = [
        ("Kelas Pengguna (Abstract)", "Model User (Prisma ORM)", "Single Table Inheritance terpadu dengan kolom diskriminator role."),
        ("Atribut role: RoleEnum", "Enum Role { ADMIN, PETUGAS, SISWA }", "Native PostgreSQL Enum untuk integritas data level database."),
        ("Kelas JenisSurat", "Model JenisSurat", "Konfigurasi format penomoran surat resmi (formatNomor)."),
        ("Kelas PengajuanSurat", "Model PengajuanSurat", "Entitas transaksional utama siklus permohonan surat siswa."),
        ("Relasi Asosiasi 1..*", "fields: [siswaId], references: [id]", "Foreign Key constraint dengan onDelete: Cascade untuk integritas referensial."),
        ("Kelas LogVerifikasi", "Model LogAktivitas", "Menyimpan rekaman audit log setiap perubahan status surat.")
    ]
    for row_data in mapping_data:
        r_cells = table_map.add_row().cells
        for idx in range(3):
            r_cells[idx].text = row_data[idx]
            set_cell_margins(r_cells[idx], 60, 60, 80, 80)
            r_cells[idx].paragraphs[0].runs[0].font.size = Pt(8.5)
            r_cells[idx].paragraphs[0].runs[0].font.name = 'Times New Roman'
        set_cell_background(r_cells[0], "F1F5F9")
        r_cells[0].paragraphs[0].runs[0].font.bold = True

    set_table_borders(table_map)

    # ================= BAB III =================
    add_h1("BAB III: TRANSFORMASI SEQUENCE DIAGRAM KE LOGIKA CONTROLLER")
    add_h2("3.1 Pemetaan Alur Pesan ke Pemanggilan Fungsi")
    add_p(
        "Sequence Diagram (Tugas 4) memodelkan alur pengiriman pesan antarkomponen: Aktor -> Boundary -> Control -> Entity. "
        "Pada konstruksi backend Express.js, urutan pesan ini diterjemahkan menjadi urutan pemanggilan metode controller asinkron, "
        "validasi token autentikasi, kalkulasi aturan bisnis, penulisan ke database, dan pengembalian kode status HTTP."
    )

    add_h2("3.2 Skenario Pengajuan Surat Baru oleh Siswa (POST /api/pengajuan)")
    add_p("Berikut adalah implementasi kode controller yang mencerminkan alur Sequence Diagram Tambah Pengajuan:")
    add_code_block(
        "// File: be/src/routes/pengajuan.routes.ts\n\n"
        "router.post('/', authMiddleware, async (req: AuthenticatedRequest, res) => {\n"
        "  try {\n"
        "    const user = req.user!;\n"
        "    const { jenisSuratId, keperluan, keterangan, lampiran } = req.body;\n\n"
        "    // 1. Validasi Input Boundary\n"
        "    if (!jenisSuratId || !keperluan) {\n"
        "      return res.status(400).json({ error: 'Jenis surat dan keperluan wajib diisi!' });\n"
        "    }\n\n"
        "    // 2. Logika Penomoran Tiket Deterministik\n"
        "    const now = new Date();\n"
        "    const yearMonth = `${now.getFullYear()}${String(now.getMonth() + 1).padStart(2, '0')}`;\n"
        "    const todayCount = await prisma.pengajuanSurat.count();\n"
        "    const nomorPengajuan = `REQ-${yearMonth}-${String(todayCount + 1).padStart(4, '0')}`;\n\n"
        "    // 3. Eksekusi Penyimpanan ke Layer Entity (Database)\n"
        "    const newPengajuan = await prisma.pengajuanSurat.create({\n"
        "      data: {\n"
        "        nomorPengajuan,\n"
        "        siswaId: user.id,\n"
        "        jenisSuratId,\n"
        "        keperluan,\n"
        "        keterangan: keterangan || null,\n"
        "        lampiran: lampiran || null,\n"
        "        status: StatusPengajuan.MENUNGGU,\n"
        "      },\n"
        "    });\n\n"
        "    // 4. Pencatatan Jejak Audit (Log Aktivitas)\n"
        "    await prisma.logAktivitas.create({\n"
        "      data: {\n"
        "        pengajuanId: newPengajuan.id,\n"
        "        userId: user.id,\n"
        "        statusSesudah: StatusPengajuan.MENUNGGU,\n"
        "        catatan: `Pengajuan surat baru dibuat oleh ${user.nama}`,\n"
        "      },\n"
        "    });\n\n"
        "    return res.status(201).json({ success: true, data: newPengajuan });\n"
        "  } catch (error) {\n"
        "    return res.status(500).json({ error: 'Gagal membuat pengajuan surat.' });\n"
        "  }\n"
        "});",
        "Kode 3.1: Transformasi Alur Sequence Diagram Pengajuan Surat Baru (be/src/routes/pengajuan.routes.ts)"
    )

    add_h2("3.3 Skenario Verifikasi & Penomoran Resmi oleh Petugas TU (PATCH /api/pengajuan/:id)")
    add_p("Berikut adalah kode proses verifikasi berkas dan penomoran otomatis saat status diubah menjadi DISETUJUI:")
    add_code_block(
        "// File: be/src/routes/pengajuan.routes.ts\n\n"
        "router.patch('/:id', authMiddleware, async (req: AuthenticatedRequest, res) => {\n"
        "  try {\n"
        "    const user = req.user!;\n"
        "    if (user.role === 'SISWA') {\n"
        "      return res.status(403).json({ error: 'Hanya petugas tata usaha yang berwenang.' });\n"
        "    }\n\n"
        "    const { id } = req.params;\n"
        "    const { status, catatanPetugas } = req.body;\n"
        "    const existing = await prisma.pengajuanSurat.findUnique({\n"
        "      where: { id },\n"
        "      include: { jenisSurat: true },\n"
        "    });\n\n"
        "    let finalNomorSurat = existing.nomorSuratResmi;\n"
        "    let tanggalSelesai = existing.tanggalSelesai;\n\n"
        "    // Panggilan Helper Reusable DRY saat Status DISETUJUI\n"
        "    if (status === StatusPengajuan.DISETUJUI) {\n"
        "      tanggalSelesai = new Date();\n"
        "      const count = await prisma.pengajuanSurat.count({ where: { status: 'DISETUJUI' } });\n"
        "      finalNomorSurat = generateNomorSuratResmi(existing.jenisSurat.formatNomor, count + 1);\n"
        "    }\n\n"
        "    const updated = await prisma.pengajuanSurat.update({\n"
        "      where: { id },\n"
        "      data: {\n"
        "        status: status as StatusPengajuan,\n"
        "        petugasId: user.id,\n"
        "        catatanPetugas,\n"
        "        nomorSuratResmi: finalNomorSurat,\n"
        "        tanggalSelesai,\n"
        "      },\n"
        "    });\n\n"
        "    return res.json({ success: true, data: updated });\n"
        "  } catch (error) {\n"
        "    return res.status(500).json({ error: 'Gagal memperbarui status.' });\n"
        "  }\n"
        "});",
        "Kode 3.2: Transformasi Sequence Diagram Verifikasi & Penomoran Resmi TU (be/src/routes/pengajuan.routes.ts)"
    )

    # ================= BAB IV =================
    add_h1("BAB IV: TRANSFORMASI WIREFRAME KE KODE ANTARMUKA (FRONTEND)")
    add_h2("4.1 Pemetaan Desain Komponen Wireframe ke React/Next.js")
    add_p(
        "Wireframe antarmuka pengguna ditransformasikan menjadi komponen fungsional React (Next.js App Router) dengan "
        "styling utilitas Tailwind CSS. Formulir dilengkapi penanganan event reaktif, validasi client-side, serta umpan balik visual "
        "berupa warna semantik badge status (Kuning untuk Menunggu, Biru untuk Diproses, Hijau untuk Disetujui, dan Merah untuk Ditolak)."
    )

    add_h2("4.2 Implementasi Komponen Formulir Pengajuan Surat")
    add_code_block(
        "// File: fe/src/components/FormPengajuanSurat.tsx\n\n"
        "'use client';\n"
        "import { useState } from 'react';\n\n"
        "export default function FormPengajuanSurat({ daftarJenis }: { daftarJenis: any[] }) {\n"
        "  const [jenisSuratId, setJenisSuratId] = useState('');\n"
        "  const [keperluan, setKeperluan] = useState('');\n"
        "  const [submitting, setSubmitting] = useState(false);\n\n"
        "  const handleSubmit = async (e: React.FormEvent) => {\n"
        "    e.preventDefault();\n"
        "    setSubmitting(true);\n"
        "    await fetch('/api/pengajuan', {\n"
        "      method: 'POST',\n"
        "      headers: { 'Content-Type': 'application/json' },\n"
        "      body: JSON.stringify({ jenisSuratId, keperluan }),\n"
        "    });\n"
        "    setSubmitting(false);\n"
        "  };\n\n"
        "  return (\n"
        "    <form onSubmit={handleSubmit} className=\"p-6 bg-white dark:bg-zinc-900 rounded-xl border border-zinc-200 space-y-4\">\n"
        "      <h2 className=\"text-xl font-bold\">Buat Permohonan Surat Baru</h2>\n"
        "      <select value={jenisSuratId} onChange={(e) => setJenisSuratId(e.target.value)} className=\"w-full p-2 border rounded\">\n"
        "        <option value=\"\">-- Pilih Jenis Surat --</option>\n"
        "        {daftarJenis.map(j => <option key={j.id} value={j.id}>{j.namaSurat}</option>)}\n"
        "      </select>\n"
        "      <textarea value={keperluan} onChange={(e) => setKeperluan(e.target.value)} placeholder=\"Keperluan surat...\" className=\"w-full p-2 border rounded\" />\n"
        "      <button type=\"submit\" disabled={submitting} className=\"w-full py-2 bg-blue-600 text-white rounded font-medium\">\n"
        "        {submitting ? 'Mengirim...' : 'Kirim Permohonan'}\n"
        "      </button>\n"
        "    </form>\n"
        "  );\n"
        "}",
        "Kode 4.1: Implementasi Komponen Formulir Pengajuan Surat Siswa (fe/src/components/FormPengajuanSurat.tsx)"
    )

    # ================= BAB V =================
    add_h1("BAB V: STANDAR KODING & PENERAPAN PRINSIP DRY (BEFORE VS AFTER)")
    add_h2("5.1 Studi Kasus Keterbacaan Penamaan Kode (Before vs After)")
    add_p(
        "Sesuai arahan slide ajar Pertemuan 10, kode program wajib mengeliminasi variabel abstrak satu huruf yang membingungkan. "
        "Berikut studi kasus Before vs After pada fungsi validasi berkas persyaratan surat:"
    )

    table_bva = doc.add_table(rows=1, cols=2)
    table_bva.alignment = WD_TABLE_ALIGNMENT.CENTER
    h_bva = table_bva.rows[0].cells
    h_bva[0].text = "BEFORE (Kurang Baik / Kualitas Rendah)"
    h_bva[1].text = "AFTER (Sangat Baik / Standar SIPESAT)"
    set_cell_background(h_bva[0], "FEE2E2")
    set_cell_background(h_bva[1], "DCFCE7")
    for idx in range(2):
        for p_c in h_bva[idx].paragraphs:
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r_c in p_c.runs:
                r_c.bold = True
                r_c.font.size = Pt(10)

    row_bva = table_bva.add_row().cells
    row_bva[0].text = (
        "// ❌ Nama variabel satu huruf (b, t, d)\n"
        "// ❌ Tidak ada tipe data TypeScript\n"
        "// ❌ Makna logika sulit dipahami\n\n"
        "function cek(b: any, t: any) {\n"
        "  let d = new Date();\n"
        "  if (b.exp < d.getTime()) {\n"
        "    return false;\n"
        "  }\n"
        "  return true;\n"
        "}"
    )
    row_bva[1].text = (
        "// ✅ Penamaan deskriptif (isBerkasValid)\n"
        "// ✅ Interface tipe data eksplisit\n"
        "// ✅ Self-documenting clean code\n\n"
        "interface BerkasPersyaratan {\n"
        "  id: string;\n"
        "  tanggalKedaluwarsa: Date;\n"
        "}\n\n"
        "export function isBerkasPersyaratanValid(\n"
        "  berkas: BerkasPersyaratan\n"
        "): boolean {\n"
        "  const waktuSekarang = new Date();\n"
        "  return berkas.tanggalKedaluwarsa > waktuSekarang;\n"
        "}"
    )
    for idx in range(2):
        set_cell_margins(row_bva[idx], 80, 80, 100, 100)
        row_bva[idx].paragraphs[0].runs[0].font.name = 'Consolas'
        row_bva[idx].paragraphs[0].runs[0].font.size = Pt(8.5)

    set_table_borders(table_bva)

    add_h2("5.2 Penerapan Prinsip DRY: Reusable Helper Generator Nomor Surat")
    add_p(
        "Prinsip Don't Repeat Yourself (DRY) diwujudkan dengan membuat fungsi terpusat untuk men-generate nomor surat resmi sekolah. "
        "Dengan fungsi ini, rumus konversi bulan romawi dan penyusunan nomor urut tidak pernah ditulis berulang di berbagai controller:"
    )
    add_code_block(
        "// File: be/src/utils/format.ts\n\n"
        "export function getMonthRomawi(monthIndex: number): string {\n"
        "  const romawi = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII'];\n"
        "  return romawi[monthIndex] || 'I';\n"
        "}\n\n"
        "export function generateNomorSuratResmi(formatTemplate: string, sequence: number): string {\n"
        "  const now = new Date();\n"
        "  const year = now.getFullYear().toString();\n"
        "  const monthRomawi = getMonthRomawi(now.getMonth());\n"
        "  const seqFormatted = String(sequence).padStart(3, '0');\n\n"
        "  return formatTemplate\n"
        "    .replace('{NOMOR}', seqFormatted)\n"
        "    .replace('{BULAN_ROMAWI}', monthRomawi)\n"
        "    .replace('{TAHUN}', year);\n"
        "}",
        "Kode 5.1: Implementasi Reusable Function DRY untuk Nomor Surat (be/src/utils/format.ts)"
    )

    add_h2("5.3 Penerapan Prinsip DRY: Reusable Middleware Autentikasi JWT RBAC")
    add_p(
        "Verifikasi token JWT dan ekstraksi sesi pengguna diisolasi ke dalam satu middleware terpusat sehingga seluruh rute "
        "cukup menyisipkan authMiddleware tanpa menduplikasi logika dekripsi token:"
    )
    add_code_block(
        "// File: be/src/middlewares/auth.middleware.ts\n\n"
        "export function authMiddleware(req: AuthenticatedRequest, res: Response, next: NextFunction) {\n"
        "  const authHeader = req.headers.authorization;\n"
        "  if (!authHeader || !authHeader.startsWith('Bearer ')) {\n"
        "    return res.status(401).json({ error: 'Token autentikasi tidak valid.' });\n"
        "  }\n"
        "  const token = authHeader.split(' ')[1];\n"
        "  const decoded = verifyToken(token);\n"
        "  if (!decoded) return res.status(401).json({ error: 'Sesi login kedaluwarsa.' });\n"
        "  req.user = decoded;\n"
        "  return next();\n"
        "}",
        "Kode 5.2: Reusable Middleware Autentikasi Terpadu (be/src/middlewares/auth.middleware.ts)"
    )

    # ================= BAB VI =================
    add_h1("BAB VI: KESIMPULAN & PENUTUP")
    add_p(
        "Berdasarkan tahap konstruksi dan implementasi perangkat lunak yang telah diselesaikan pada proyek Sistem Informasi "
        "Pengajuan Surat Siswa Berbasis Web (SIPESAT), dapat disimpulkan bahwa:\n"
        "1. Transformasi Rancangan ke Kode Program Berhasil 100%: Seluruh elemen struktural pada Class Diagram (Model User, "
        "PengajuanSurat, JenisSurat, dan LogAktivitas) serta alur interaksi Sequence Diagram telah diterjemahkan secara akurat ke dalam "
        "kode backend TypeScript dan Prisma ORM tanpa deviasi arsitektural.\n"
        "2. Kepatuhan Standar Clean Code & Prinsip DRY: Kode program menerapkan konvensi penamaan standar industri, modularitas tinggi, "
        "fungsi-fungsi pembantu terpusat (generator nomor surat romawi dan middleware autentikasi), serta penghindaran duplikasi logika.\n"
        "3. Kesiapan Sistem Menuju Tahap Pengujian: Kode sumber sistem telah berada dalam kondisi terstruktur, aman, dan siap untuk melangkah "
        "ke tahap selanjutnya dalam SDLC, yaitu Tahap Pengujian Perangkat Lunak (Software Testing & QA)."
    )

    output_path = os.path.join(RPL_DIR, "tugas-10-konstruksi-implementasi.docx")
    doc.save(output_path)
    print(f"SUCCESS: {output_path}")

if __name__ == "__main__":
    build_docx_tugas10()
