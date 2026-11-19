#set document(
  title: "Tugas 10 RPL: Konstruksi dan Implementasi Perangkat Lunak - SIPESAT",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)

#set text(font: "Times New Roman", size: 11pt, lang: "id")
#set page(
  paper: "a4",
  margin: (left: 3.5cm, top: 3.5cm, right: 3cm, bottom: 3cm),
  header: none,
  footer: context align(center)[#text(size: 10pt)[#counter(page).display("1")]]
)

#set par(justify: true, leading: 0.75em, first-line-indent: 0pt)
#set heading(numbering: none)
#show heading.where(level: 1): it => block(above: 1.4em, below: 0.7em)[
  #text(size: 13pt, weight: "bold")[#it.body]
]
#show heading.where(level: 2): it => block(above: 1.1em, below: 0.5em)[
  #text(size: 11.5pt, weight: "bold")[#it.body]
]
#show raw.where(block: true): it => block(
  width: 100%,
  fill: rgb("#f8fafc"),
  stroke: 0.5pt + rgb("#cbd5e1"),
  radius: 4pt,
  inset: 8pt,
  breakable: true,
)[#set text(size: 8.8pt); #set par(justify: false, leading: 0.55em); #it]

#align(center)[
  #v(0.3cm)
  #text(size: 14pt, weight: "bold")[
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\
    TUGAS 10: KONSTRUKSI DAN IMPLEMENTASI PL
  ]
  #v(0.5cm)
  #text(size: 12.5pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB\
    (SIPESAT)
  ]
  #v(0.2cm)
  #text(size: 10.5pt, style: "italic")[
    Mengimplementasikan Hasil Rancangan Desain UML ke dalam Kode Program (Versi Revisi)
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

= BAB I: PENDAHULUAN & KONSEP DASAR KONSTRUKSI PL

== 1.1 Gambaran Umum & Posisi Konstruksi dalam SDLC
Dalam siklus hidup pengembangan perangkat lunak (_Software Development Life Cycle_ - SDLC), tahap *Konstruksi Perangkat Lunak (Software Construction)* merupakan fase krusial yang berada tepat di antara tahap perancangan arsitektur (_Design_) dan tahap pengujian (_Testing_). Tahap ini menitikberatkan pada proses penerjemahan representasi abstrak perancangan—seperti Class Diagram, Sequence Diagram, Activity Diagram, dan Prototipe Antarmuka—menjadi kode sumber (_source code_) yang dapat dieksekusi secara nyata oleh komputer.

Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) dirancang untuk mengotomatisasi birokrasi persuratan siswa (Surat Keterangan Siswa Aktif, Rekomendasi Beasiswa, dan Dispensasi Kegiatan) dengan dua peran pengguna eksklusif: Siswa dan Petugas TU (Admin). Tahap konstruksi wajib menjamin keselarasan 1-to-1 antara rancangan UML yang telah disahkan dengan implementasi kode program fisik.

== 1.2 Prinsip Kode Berkualitas Tinggi
Konstruksi kode pada sistem SIPESAT dibangun berlandaskan enam prinsip rekayasa perangkat lunak standar industri:
+ *Readability (Keterbacaan)*: Kode program ditulis dengan struktur bersih, indentasi konsisten, serta penamaan variabel dan fungsi yang deskriptif.
+ *Maintainability (Kemudahan Pemeliharaan)*: Modul-modul sistem dipisahkan secara tegas (_decoupled_) antara lapisan rute (Routing), lapisan kendali logika bisnis (Controller), lapisan akses data (Prisma ORM), dan lapisan antarmuka (Frontend Next.js).
+ *Reusability (Dapat Digunakan Kembali)*: Fungsi-fungsi umum (generator format nomor surat resmi, helper bulan romawi, dan middleware verifikasi JWT) diisolasi ke dalam modul utilitas terpusat.
+ *Efficiency (Efisiensi)*: Kueri basis data dioptimalkan dengan memilih kolom yang relevan dan relasi yang dibutuhkan.
+ *Prinsip DRY (Don't Repeat Yourself)*: Menghindari duplikasi logika. Setiap aturan validasi atau format data hanya didefinisikan satu kali sebagai _Single Source of Truth_.
+ *Prinsip KISS (Keep It Simple, Stupid)*: Memilih solusi implementasi yang paling sederhana, deterministik, dan langsung menjawab kebutuhan tanpa lapisan abstraksi berlebih.

== 1.3 Standar Penamaan (_Coding Standards & Naming Conventions_)
- *PascalCase*: Digunakan untuk penamaan Class, Interface, Type Definition, Model Prisma, dan Komponen React (contoh: `PengajuanSurat`, `JenisSurat`, `FormPengajuanSurat`).
- *camelCase*: Digunakan untuk penamaan variabel, properti objek, parameter, method, dan fungsi (contoh: `nomorPengajuan`, `generateNomorSuratResmi`).
- *SCREAMING_SNAKE_CASE*: Digunakan untuk konstanta global dan nilai enumerasi (contoh: `MENUNGGU`, `DISETUJUI`, `ADMIN`, `SISWA`).

= BAB II: TRANSFORMASI DARI CLASS DIAGRAM KE KODE PROGRAM (MODEL & DATABASE)

== 2.1 Pemetaan Konseptual Class Diagram ke Kode Fisik
Pada tahap konstruksi sistem SIPESAT, Class Diagram (Tugas 6) ditransformasikan secara langsung menuju skema basis data relasional via *Prisma ORM* dan deklarasi tipe *TypeScript*:
+ *Nama Kelas UML* → Ditransformasikan menjadi model basis data relasional (`model User`, `model JenisSurat`, `model PengajuanSurat`, `model LogAktivitas`).
+ *Atribut dan Tipe Data UML* → Ditransformasikan menjadi kolom tabel dengan tipe data ekuivalen (`String`, `Boolean`, `DateTime`, dan Enum).
+ *Visibilitas Private (`-`)* → Ditegakkan melalui enkapsulasi controller dan seleksi field agar data sensitif seperti `password` hash tidak terekspos keluar.
+ *Relasi Multiplisitas ($1 .. *$ dan $0..1 .. *$)* → Diterjemahkan menjadi relasi _Foreign Key_ dan _Relation Directives_ Prisma (`@relation`).

== 2.2 Implementasi Skema Prisma ORM (`be/prisma/schema.prisma`)
```prisma
// File: be/prisma/schema.prisma

enum Role {
  ADMIN
  SISWA
}

enum StatusPengajuan {
  MENUNGGU
  DIPROSES
  DISETUJUI
  DITOLAK
}

model User {
  id              String           @id @default(cuid())
  username        String?          @unique
  nisn            String?          @unique
  nama            String
  email           String?
  password        String
  role            Role             @default(SISWA)
  kelas           String?
  jurusan         String?
  noTelepon       String?
  alamat          String?
  createdAt       DateTime         @default(now())
  updatedAt       DateTime         @updatedAt

  pengajuan       PengajuanSurat[] @relation("SiswaPengajuan")
  prosesPengajuan PengajuanSurat[] @relation("PetugasPemroses")
  logs            LogAktivitas[]
}

model JenisSurat {
  id           String           @id @default(cuid())
  kodeSurat    String           @unique
  namaSurat    String
  deskripsi    String
  persyaratan  String?
  formatNomor  String           @default("421.3/{NOMOR}/SMKN1/{BULAN_ROMAWI}/{TAHUN}")
  templateIsi  String?
  isActive     Boolean          @default(true)
  createdAt    DateTime         @default(now())
  updatedAt    DateTime         @updatedAt

  pengajuan    PengajuanSurat[]
}

model PengajuanSurat {
  id               String          @id @default(cuid())
  nomorPengajuan   String          @unique
  siswaId          String
  siswa            User            @relation("SiswaPengajuan", fields: [siswaId], references: [id], onDelete: Cascade)
  jenisSuratId     String
  jenisSurat       JenisSurat      @relation(fields: [jenisSuratId], references: [id])
  keperluan        String
  keterangan       String?
  lampiran         String?
  status           StatusPengajuan @default(MENUNGGU)
  nomorSuratResmi  String?
  petugasId        String?
  petugas          User?           @relation("PetugasPemroses", fields: [petugasId], references: [id])
  catatanPetugas   String?
  tanggalPengajuan DateTime        @default(now())
  tanggalSelesai   DateTime?
  updatedAt        DateTime        @updatedAt

  logs             LogAktivitas[]
}

model LogAktivitas {
  id             String           @id @default(cuid())
  pengajuanId    String
  pengajuan      PengajuanSurat   @relation(fields: [pengajuanId], references: [id], onDelete: Cascade)
  userId         String?
  user           User?            @relation(fields: [userId], references: [id])
  statusSebelum  StatusPengajuan?
  statusSesudah  StatusPengajuan
  catatan        String?
  createdAt      DateTime         @default(now())
}
```

== 2.3 Tabel Komparasi Pemetaan Class Diagram vs Kode Fisik
#{
  set par(justify: false, first-line-indent: 0pt)
  set text(size: 9.5pt)
  table(
    columns: (3.3cm, 4.7cm, 1fr),
    align: (left + top, left + top, left + top),
    inset: 6pt,
    stroke: 0.5pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
    table.header([*#text(fill: white)[Elemen Class Diagram]*], [*#text(fill: white)[Implementasi Kode]*], [*#text(fill: white)[Keterangan Rekayasa]*]),
    [Kelas `User`], [Model `User` (Prisma)], [Menyimpan pengguna dengan pembeda `role` (`ADMIN` / `SISWA`).],
    [Enumerasi `Role`], [`enum Role { ADMIN, SISWA }`], [PostgreSQL Native Enum untuk pembatasan 2 peran login.],
    [Kelas `JenisSurat`], [Model `JenisSurat` (Prisma)], [Menyimpan master jenis surat dan template format nomor resmi.],
    [Kelas `PengajuanSurat`], [Model `PengajuanSurat` (Prisma)], [Entitas transaksional utama permohonan surat siswa.],
    [Relasi Asosiasi `1 : 0..*`], [`@relation("SiswaPengajuan")`], [Menegakkan Foreign Key (`siswaId` → `User.id`, Cascade).],
    [Kelas `LogAktivitas`], [Model `LogAktivitas` (Prisma)], [Komposisi audit trail setiap transisi status permohonan.],
  )
}

= BAB III: TRANSFORMASI DARI SEQUENCE DIAGRAM KE KODE LOGIKA BISNIS (CONTROLLER & ROUTING)

== 3.1 Skenario 1: Transformasi Alur Pengajuan Surat Baru oleh Siswa
Dalam Sequence Diagram 1 (Tugas 4), pengiriman pesan Boundary → Control → Entity diwujudkan pada endpoint `POST /api/pengajuan`:

```typescript
// File: be/src/routes/pengajuan.routes.ts

router.post('/', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    const { jenisSuratId, keperluan, keterangan, lampiran, siswaId: reqSiswaId } = req.body;

    // 1. Validasi Boundary (Pesan Masuk)
    if (!jenisSuratId || !keperluan) {
      return res.status(400).json({ error: 'Jenis surat dan keperluan wajib diisi!' });
    }

    const targetSiswaId = user.role === 'SISWA' ? user.id : (reqSiswaId || user.id);

    // 2. Logika Bisnis: Pembuatan Nomor Tiket Pengajuan Deterministik
    const now = new Date();
    const yearMonth = `${now.getFullYear()}${String(now.getMonth() + 1).padStart(2, '0')}`;
    const todayCount = await prisma.pengajuanSurat.count();
    const nomorPengajuan = `REQ-${yearMonth}-${String(todayCount + 1).padStart(4, '0')}`;

    // 3. Eksekusi Transaksional ke Lapisan Entity (Database)
    const newPengajuan = await prisma.pengajuanSurat.create({
      data: {
        nomorPengajuan,
        siswaId: targetSiswaId,
        jenisSuratId,
        keperluan,
        keterangan: keterangan || null,
        lampiran: lampiran || null,
        status: StatusPengajuan.MENUNGGU,
      },
      include: { jenisSurat: true, siswa: true },
    });

    // 4. Pencatatan Jejak Audit Otomatis (Audit Trail)
    await prisma.logAktivitas.create({
      data: {
        pengajuanId: newPengajuan.id,
        userId: user.id,
        statusSesudah: StatusPengajuan.MENUNGGU,
        catatan: `Pengajuan surat baru dibuat oleh ${user.nama}`,
      },
    });

    return res.status(201).json({
      success: true,
      message: 'Pengajuan surat berhasil dikirim!',
      data: newPengajuan,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal membuat pengajuan surat.' });
  }
});
```

== 3.2 Skenario 2: Transformasi Alur Verifikasi & Penomoran Resmi oleh Petugas TU
Sesuai Sequence Diagram 2 (Tugas 4), Petugas TU menyetujui atau menolak permohonan pada endpoint `PATCH /api/pengajuan/:id`:

```typescript
// File: be/src/routes/pengajuan.routes.ts

router.patch('/:id', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    if (user.role === 'SISWA') {
      return res.status(403).json({
        error: 'Hanya petugas tata usaha atau admin yang berwenang memverifikasi status.'
      });
    }

    const { id } = req.params;
    const { status, catatanPetugas, nomorSuratResmi } = req.body;

    const existing = await prisma.pengajuanSurat.findUnique({
      where: { id },
      include: { jenisSurat: true },
    });
    if (!existing) {
      return res.status(404).json({ error: 'Pengajuan tidak ditemukan' });
    }

    let finalNomorSurat = nomorSuratResmi || existing.nomorSuratResmi;
    let tanggalSelesai = existing.tanggalSelesai;

    if (status === StatusPengajuan.DISETUJUI) {
      tanggalSelesai = new Date();
      if (!finalNomorSurat) {
        const approvedCount = await prisma.pengajuanSurat.count({
          where: { status: StatusPengajuan.DISETUJUI, jenisSuratId: existing.jenisSuratId },
        });
        finalNomorSurat = generateNomorSuratResmi(
          existing.jenisSurat.formatNomor,
          approvedCount + 1
        );
      }
    }

    const updated = await prisma.pengajuanSurat.update({
      where: { id },
      data: {
        status: status as StatusPengajuan,
        petugasId: user.id,
        catatanPetugas: catatanPetugas !== undefined ? catatanPetugas : existing.catatanPetugas,
        nomorSuratResmi: finalNomorSurat,
        tanggalSelesai,
      },
      include: { siswa: true, jenisSurat: true, petugas: true },
    });

    return res.json({
      success: true,
      message: `Status berhasil diperbarui menjadi ${status}`,
      data: updated,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Gagal memperbarui status pengajuan surat.' });
  }
});
```

= BAB IV: TRANSFORMASI WIREFRAME KE KODE ANTARMUKA (FRONTEND)

== 4.1 Implementasi Komponen Formulir Pengajuan Surat Siswa
Struktur desain Figma ditransformasikan ke dalam komponen modular Next.js 14 dan Tailwind CSS:

```tsx
// File: fe/src/components/FormPengajuanSurat.tsx
'use client';
import { useState } from 'react';

interface JenisSurat {
  id: string;
  namaSurat: string;
  deskripsi: string;
  persyaratan: string;
}

export default function FormPengajuanSurat({ daftarJenis }: { daftarJenis: JenisSurat[] }) {
  const [jenisSuratId, setJenisSuratId] = useState('');
  const [keperluan, setKeperluan] = useState('');
  const [keterangan, setKeterangan] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    try {
      const res = await fetch('/api/pengajuan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ jenisSuratId, keperluan, keterangan }),
      });
      if (res.ok) {
        alert('Permohonan surat berhasil dikirim ke Tata Usaha!');
        window.location.href = '/siswa/riwayat';
      }
    } catch (err) {
      alert('Terjadi kendala saat mengirim permohonan.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-6 bg-white rounded-xl border border-zinc-200 space-y-4">
      <h2 className="text-xl font-bold text-zinc-900">Buat Permohonan Surat Baru</h2>
      <div>
        <label className="block text-sm font-medium mb-1">Pilih Jenis Surat Resmi</label>
        <select
          value={jenisSuratId}
          onChange={(e) => setJenisSuratId(e.target.value)}
          className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
          required
        >
          <option value="">-- Pilih Jenis Surat --</option>
          {daftarJenis.map((item) => (
            <option key={item.id} value={item.id}>{item.namaSurat}</option>
          ))}
        </select>
      </div>
      <div>
        <label className="block text-sm font-medium mb-1">Keperluan Pembuatan Surat</label>
        <textarea
          value={keperluan}
          onChange={(e) => setKeperluan(e.target.value)}
          placeholder="Contoh: Pengajuan Beasiswa PIP / Dinas"
          className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
          rows={3}
          required
        />
      </div>
      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full py-2.5 px-4 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg"
      >
        {isSubmitting ? 'Mengirim...' : 'Kirim Permohonan Surat'}
      </button>
    </form>
  );
}
```

= BAB V: STANDAR KODING & PENERAPAN PRINSIP DRY (BEFORE VS AFTER)

== 5.1 Analisis Standar Penamaan & Keterbacaan (_Before vs After_)
*BEFORE (Kurang Baik / Variabel Tidak Deskriptif):*
```typescript
function cek(b: any, t: any) {
  let d = new Date();
  if (b.exp < d.getTime()) return false;
  return true;
}
```

*AFTER (Sangat Baik / Standar TypeScript SIPESAT):*
```typescript
interface BerkasPersyaratan {
  idBerkas: string;
  namaBerkas: string;
  tanggalKedaluwarsa: Date;
}

export function isBerkasPersyaratanValid(berkas: BerkasPersyaratan): boolean {
  const waktuSekarang = new Date();
  return berkas.tanggalKedaluwarsa.getTime() >= waktuSekarang.getTime();
}
```

== 5.2 Penerapan Prinsip DRY: Reusable Helper Generator Nomor Surat Resmi
```typescript
// File: be/src/utils/format.ts

export function getMonthRomawi(monthIndex: number): string {
  const daftarRomawi = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII'];
  return daftarRomawi[monthIndex] || 'I';
}

export function generateNomorSuratResmi(formatTemplate: string, urutanNomor: number): string {
  const waktuSaatIni = new Date();
  const tahunBerjalan = waktuSaatIni.getFullYear().toString();
  const bulanRomawi = getMonthRomawi(waktuSaatIni.getMonth());
  const nomorUrutTigaDigit = String(urutanNomor).padStart(3, '0');

  return formatTemplate
    .replace('{NOMOR}', nomorUrutTigaDigit)
    .replace('{BULAN_ROMAWI}', bulanRomawi)
    .replace('{TAHUN}', tahunBerjalan);
}
```

== 5.3 Penerapan Prinsip DRY: Reusable Middleware Autentikasi & RBAC
```typescript
// File: be/src/middlewares/auth.middleware.ts
import { Request, Response, NextFunction } from 'express';
import { verifyToken, TokenPayload } from '../utils/jwt';

export interface AuthenticatedRequest extends Request {
  user?: TokenPayload;
}

export function authMiddleware(req: AuthenticatedRequest, res: Response, next: NextFunction) {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Token autentikasi tidak ditemukan atau tidak valid.' });
  }
  const token = authHeader.split(' ')[1];
  const decoded = verifyToken(token);
  if (!decoded) {
    return res.status(401).json({ error: 'Sesi login telah kedaluwarsa. Silakan login kembali.' });
  }
  req.user = decoded;
  return next();
}
```

= BAB VI: KESIMPULAN & PENUTUP
+ *Ketepatan Pemetaan Desain ke Kode*: Seluruh entitas pada Class Diagram (UML 2.5) berhasil ditransformasikan secara konsisten ke dalam skema fisik basis data relasional (PostgreSQL 16 via Prisma ORM) dan definisi tipe TypeScript dengan 2 peran eksklusif (`ADMIN` dan `SISWA`).
+ *Kepatuhan Alur Pesan Sequence Diagram*: Alur pengiriman pesan antarkomponen pada Sequence Diagram telah diwujudkan secara utuh ke dalam rantai pemanggilan fungsi controller asinkron (`POST /api/pengajuan` dan `PATCH /api/pengajuan/:id`).
+ *Penerapan Standar Rekayasa Tinggi*: Konstruksi kode mematuhi prinsip *DRY*, *KISS*, dan *Readability* serta siap diuji pada tahap Pengujian Perangkat Lunak (_Black Box Testing_).
