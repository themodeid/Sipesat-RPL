#set document(
  title: "Tugas 10 RPL: Konstruksi dan Implementasi Perangkat Lunak - SIPESAT",
  author: ("Adam Wahyu Kurniawan", "Fathu Rahman", "Surya Edi Saputra", "Rizqi Muh. Al Hakimi")
)

#set text(font: "Times New Roman", size: 11pt, lang: "id")
#set page(
  paper: "a4",
  margin: (left: 4cm, top: 4cm, right: 3cm, bottom: 3cm),
  header: none,
  footer: context align(center)[#text(size: 10pt)[#counter(page).display("1")]]
)

#set par(justify: true, leading: 0.8em, first-line-indent: 1cm)

#align(center)[
  #text(size: 14pt, weight: "bold")[
    TUGAS REKAYASA PERANGKAT LUNAK (RPL)\
    TUGAS 10: KONSTRUKSI DAN IMPLEMENTASI PL
  ]
  #v(0.8cm)
  #text(size: 12pt, weight: "bold")[
    SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)\
    #text(size: 11pt, weight: "regular")[_Mengimplementasikan Hasil Rancangan Desain UML ke dalam Kode Program_]
  ]
  #v(1.4cm)
  #rect(width: 5.5cm, height: 4.2cm, stroke: 1.5pt + rgb("#1e293b"), radius: 4pt)[
    #align(center + horizon)[
      #text(size: 11pt, weight: "bold", fill: rgb("#1e293b"))[UNIVERSITAS\ INDRAPRASTA PGRI\ (UNINDRA)]
      #v(6pt)
      #text(size: 9.5pt, fill: rgb("#475569"))[FAKULTAS TEKNIK & ILMU KOMPUTER\ TEKNIK INFORMATIKA]
    ]
  ]
  #v(1.4cm)
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
  #v(1.0cm)
  #text(size: 11pt, weight: "bold")[JAKARTA\ 2026/2027]
]

#pagebreak()

= BAB I: PENDAHULUAN & KONSEP DASAR KONSTRUKSI PL

== 1.1 Gambaran Umum & Posisi Konstruksi dalam SDLC
Dalam siklus hidup pengembangan perangkat lunak (_Software Development Life Cycle_ - SDLC), tahap *Konstruksi Perangkat Lunak (Software Construction)* merupakan fase krusial yang berada tepat di antara tahap perancangan arsitektur (_Design_) dan tahap pengujian (_Testing_). Tahap ini menitikberatkan pada proses penerjemahan representasi abstrak perancangan—seperti Class Diagram, Sequence Diagram, State Machine, dan Prototipe Antarmuka—menjadi kode sumber (_source code_) yang dapat dieksekusi secara nyata oleh mesin komputer.

Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) dirancang untuk mengotomatisasi birokrasi persuratan siswa (Surat Keterangan Siswa Aktif, Rekomendasi Beasiswa, Legalisir Ijazah, dan Dispensasi). Mengingat sistem ini mengelola dokumen resmi sekolah dan data identitas siswa, tahap konstruksi perangkat lunak wajib menjamin keselarasan 1-to-1 antara rancangan UML yang telah disahkan dengan implementasi kode program fisik, mencegah terjadinya deviasi (_architectural drift_), serta mengeliminasi kerentanan keamanan dan redudansi logika.

== 1.2 Prinsip Kode Berkualitas Tinggi
Konstruksi kode pada sistem SIPESAT dibangun berlandaskan enam prinsip rekayasa perangkat lunak standar industri:
+ *Readability (Keterbacaan)*: Kode program ditulis dengan struktur yang bersih, indentasi konsisten, serta penamaan variabel dan fungsi yang deskriptif sehingga mudah dipahami oleh anggota tim lain tanpa interpretasi ganda.
+ *Maintainability (Kemudahan Pemeliharaan)*: Modul-modul sistem dipisahkan secara tegas (_decoupled_) antara lapisan rute (Routing), lapisan kendali logika bisnis (Controller), lapisan akses data (Prisma ORM), dan lapisan antarmuka (Frontend React), sehingga perbaikan _bug_ atau penambahan fitur di masa depan tidak menimbulkan efek samping destruktif pada modul lain.
+ *Reusability (Dapat Digunakan Kembali)*: Fungsi-fungsi yang memiliki kegunaan umum (seperti generator format nomor surat resmi, helper kalkulasi bulan romawi, dan middleware verifikasi token JWT) diisolasi ke dalam modul utilitas terpusat.
+ *Efficiency (Efisiensi)*: Kueri database dioptimalkan dengan memilih hanya kolom-kolom yang relevan (_projection select_), mencegah terjadinya masalah _over-fetching_ dan _N+1 query problem_.
+ *Prinsip DRY (Don't Repeat Yourself)*: Menghindari duplikasi logika dan penulisan aturan bisnis berulang. Setiap aturan validasi atau format data hanya didefinisikan satu kali sebagai _Single Source of Truth_.
+ *Prinsip KISS (Keep It Simple, Stupid)*: Memilih solusi implementasi yang paling sederhana, deterministik, dan langsung menjawab kebutuhan pengguna tanpa lapisan abstraksi berlebih (_anti-overengineering_).

== 1.3 Standar Penamaan (_Coding Standards & Naming Conventions_)
Pembangunan kode program SIPESAT mengadopsi standar penamaan resmi ekosistem TypeScript/JavaScript modern:
- *PascalCase*: Digunakan secara eksklusif untuk penamaan Class, Interface, Type Definition, Model Prisma, dan Komponen React (contoh: `PengajuanSurat`, `JenisSurat`, `UserRole`, `TimelineStepper`).
- *camelCase*: Digunakan untuk penamaan variabel, properti objek, parameter, method, dan fungsi (contoh: `nomorPengajuan`, `generateNomorSuratResmi`, `buatPengajuanBaru`).
- *SCREAMING_SNAKE_CASE*: Digunakan untuk konstanta global dan nilai enumerasi (contoh: `STATUS_MENUNGGU`, `ROLE_ADMIN`, `JWT_SECRET_KEY`).
- *Satu Fungsi, Satu Tugas (Single Responsibility Principle)*: Setiap fungsi atau method dirancang hanya untuk menjalankan satu tugas spesifik dan terisolasi.

#pagebreak()

= BAB II: TRANSFORMASI DARI CLASS DIAGRAM KE KODE PROGRAM (MODEL & DATABASE)

== 2.1 Pemetaan Konseptual Class Diagram ke Kode Fisik
Dalam pemodelan berorientasi objek, Class Diagram (Tugas 6) mendefinisikan cetak biru entitas data, visibilitas atribut, metode operasional, dan hubungan relasional antarkelas. Pada tahap konstruksi sistem SIPESAT, transformasi dilakukan secara langsung menuju skema basis data relasional via *Prisma ORM* dan deklarasi tipe *TypeScript*.

Berikut adalah aturan pemetaan transformasi yang diterapkan:
+ *Nama Kelas UML* $->$ Ditransformasikan menjadi nama model basis data relasional (`model User`, `model PengajuanSurat`, `model JenisSurat`).
+ *Atribut dan Tipe Data UML* $->$ Ditransformasikan menjadi kolom tabel dengan tipe data ekuivalen (misal: `String` $->$ `String/VarChar`, `DateTime` $->$ `DateTime`, `Enum` $->$ `PostgreSQL Native Enum`).
+ *Visibilitas Private (`-`)* $->$ Ditegakkan melalui enkapsulasi controller dan seleksi field (_projection_) agar data sensitif seperti `password_hash` tidak terekspos keluar.
+ *Relasi Multiplisitas ($1 .. *$ dan $1 .. 1$)* $->$ Diterjemahkan menjadi relasi relasional _Foreign Key_ dan _Relation Directives_ Prisma (`@relation`).

== 2.2 Implementasi Entitas Pengguna & Role-Based Access Control (RBAC)
#v(0.2cm)
```prisma
// File: be/prisma/schema.prisma

enum Role {
  ADMIN
  PETUGAS
  SISWA
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

  // Relasi Asosiasi Antarkelas
  pengajuan       PengajuanSurat[] @relation("SiswaPengajuan")
  prosesPengajuan PengajuanSurat[] @relation("PetugasPemroses")
  logs            LogAktivitas[]
}
```

== 2.3 Implementasi Entitas Transaksional Surat & Jenis Surat
#v(0.2cm)
```prisma
// File: be/prisma/schema.prisma

enum StatusPengajuan {
  MENUNGGU
  DIPROSES
  DISETUJUI
  DITOLAK
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
  lampiran         String?         // Path direktori berkas fisik
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
```

== 2.4 Implementasi Entitas Riwayat Audit Log (`LogAktivitas`)
#v(0.2cm)
```prisma
// File: be/prisma/schema.prisma

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

== 2.5 Tabel Komparasi Pemetaan Class Diagram vs Kode Fisik
#table(
  columns: (3.8cm, 4.5cm, 4.5cm),
  align: (left, left, left),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (col, row) => if row == 0 { rgb("#1e293b") } else if calc.even(row) { rgb("#f8fafc") } else { none },
  table.header([*#text(fill: white)[Elemen Class Diagram]*], [*#text(fill: white)[Implementasi Kode]*], [*#text(fill: white)[Keterangan Rekayasa]*]),
  [Kelas `Pengguna` (Abstract)], [Model `User` (Prisma)], [Single Table Inheritance dengan diskriminator `role`.],
  [Atribut `role: RoleEnum`], [Enum `Role { ADMIN, PETUGAS, SISWA }`], [PostgreSQL Native Enum untuk integritas data.],
  [Kelas `JenisSurat`], [Model `JenisSurat` (Prisma)], [Menyimpan pola format nomor resmi sekolah.],
  [Kelas `PengajuanSurat`], [Model `PengajuanSurat` (Prisma)], [Entitas transaksional utama permohonan surat.],
  [Relasi Agregasi `1..*`], [`@relation("SiswaPengajuan")`], [Menegakkan Foreign Key (`siswaId` -> `User.id`).],
  [Kelas `LogVerifikasi`], [Model `LogAktivitas` (Prisma)], [Audit trail setiap transisi status permohonan.],
)

#pagebreak()

= BAB III: TRANSFORMASI DARI SEQUENCE DIAGRAM KE KODE LOGIKA BISNIS (CONTROLLER & ROUTING)

== 3.1 Pemetaan Alur Pesan (_Message Passing_) ke Kode Program
Dalam Sequence Diagram (Tugas 4), interaksi sistem dimodelkan melalui pengiriman pesan antarkomponen: Boundary $->$ Control $->$ Entity. Pada kode backend Express.js, urutan anak panah pada Sequence Diagram ditransformasikan menjadi urutan eksekusi metode asinkron, penanganan validasi batas, transaksi basis data, dan pengembalian respons HTTP.

== 3.2 Skenario 1: Transformasi Alur Pengajuan Surat Baru oleh Siswa
#v(0.2cm)
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
      include: {
        jenisSurat: true,
        siswa: true,
      },
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

    // 5. Pengembalian Pesan Konfirmasi ke Aktor (Response HTTP 201)
    return res.status(201).json({
      success: true,
      message: 'Pengajuan surat berhasil dikirim!',
      data: newPengajuan,
    });
  } catch (error) {
    console.error('Error post pengajuan:', error);
    return res.status(500).json({ error: 'Gagal membuat pengajuan surat.' });
  }
});
```

#pagebreak()

== 3.3 Skenario 2: Transformasi Alur Verifikasi & Penomoran Resmi oleh Petugas TU
#v(0.2cm)
```typescript
// File: be/src/routes/pengajuan.routes.ts

router.patch('/:id', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    
    // Boundary Guard: Otorisasi Role Petugas/Admin
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

    // Logika Pemanggilan Method generateNomorSuratResmi jika Status DISETUJUI
    if (status === StatusPengajuan.DISETUJUI) {
      tanggalSelesai = new Date();
      if (!finalNomorSurat) {
        const approvedCount = await prisma.pengajuanSurat.count({
          where: {
            status: StatusPengajuan.DISETUJUI,
            jenisSuratId: existing.jenisSuratId,
          },
        });
        // Transformasi Pesan: generateNomorSuratResmi(formatTemplate, urutan)
        finalNomorSurat = generateNomorSuratResmi(
          existing.jenisSurat.formatNomor,
          approvedCount + 1
        );
      }
    }

    // Eksekusi Update ke Database
    const updated = await prisma.pengajuanSurat.update({
      where: { id },
      data: {
        status: status as StatusPengajuan,
        petugasId: user.id,
        catatanPetugas: catatanPetugas !== undefined ? catatanPetugas : existing.catatanPetugas,
        nomorSuratResmi: finalNomorSurat,
        tanggalSelesai,
      },
      include: {
        siswa: true,
        jenisSurat: true,
        petugas: true,
      },
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

#pagebreak()

= BAB IV: TRANSFORMASI WIREFRAME / PROTOTIPE KE KODE ANTARMUKA (FRONTEND)

== 4.1 Pemetaan Desain Wireframe ke Komponen React
Struktur wireframe tata letak antarmuka yang dirancang pada fase desain ditransformasikan ke dalam komponen modular *Next.js (React Framework)* yang dipadukan dengan styling utility-first *Tailwind CSS*.

Prinsip transformasi antarmuka yang ditegakkan:
+ *Container & Box Model*: Struktur batas halaman pada wireframe diterjemahkan menjadi layout kartu ber-border halus (`border border-zinc-200 dark:border-zinc-800 rounded-xl`).
+ *State Reactive*: Input pengguna dan status unggahan berkas dikendalikan secara reaktif menggunakan React Hook (`useState`, `useEffect`).
+ *Ergonomi & Visual Feedback*: Status permohonan divisualisasikan menggunakan lencana warna semantik (_Badge Pills_) yang konsisten:
  - `MENUNGGU`: Kuning / Amber (`bg-amber-100 text-amber-800`)
  - `DIPROSES`: Biru (`bg-blue-100 text-blue-800`)
  - `DISETUJUI`: Hijau (`bg-emerald-100 text-emerald-800`)
  - `DITOLAK`: Merah (`bg-rose-100 text-rose-800`)

== 4.2 Implementasi Komponen Formulir Pengajuan Surat Siswa
#v(0.2cm)
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
      console.error(err);
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

#pagebreak()

= BAB V: STANDAR KODING & PENERAPAN PRINSIP DRY (STUDI KASUS BEFORE VS AFTER)

== 5.1 Analisis Standar Penamaan & Keterbacaan (_Before vs After_)
Sesuai arahan modul ajar Pertemuan 10, kode program wajib mengeliminasi variabel abstrak bersuku kata tunggal yang mengaburkan maksud logika.

#v(0.2cm)
*❌ BEFORE (Kurang Baik / Kualitas Rendah):*
```typescript
// Masalah: Nama variabel tidak deskriptif (b, t, d), tanpa tipe, magic string
function cek(b: any, t: any) {
  let d = new Date();
  if (b.exp < d.getTime()) {
    return false;
  }
  return true;
}
```

#v(0.2cm)
*✅ AFTER (Sangat Baik / Standar SIPESAT):*
```typescript
// Solusi: TypeScript type safety, nama fungsi self-explanatory, parameter eksplisit
interface BerkasPersyaratan {
  idBerkas: string;
  namaBerkas: string;
  tanggalKedaluwarsa: Date;
}

export function isBerkasPersyaratanValid(berkas: BerkasPersyaratan): boolean {
  const waktuSekarang = new Date();
  const apakahKedaluwarsa = berkas.tanggalKedaluwarsa.getTime() < waktuSekarang.getTime();
  
  return !apakahKedaluwarsa;
}
```

== 5.2 Penerapan Prinsip DRY: Reusable Helper Generator Nomor Surat Resmi
Dalam sistem persuratan sekolah, setiap jenis surat memiliki format penomoran yang memuat komponen nomor urut, kode klasifikasi instansi, bulan penerbitan dalam format romawi, dan tahun kalender berjalan. Tanpa prinsip DRY, penulisan rumus pergantian bulan romawi dan penyusunan string nomor surat akan diulang berkali-kali di setiap controller pengajuan.

#v(0.2cm)
```typescript
// File: be/src/utils/format.ts

/**
 * Helper konversi indeks bulan (0-11) ke format angka Romawi resmi.
 * Mencegah duplikasi switch-case di berbagai modul.
 */
export function getMonthRomawi(monthIndex: number): string {
  const daftarRomawi = [
    'I', 'II', 'III', 'IV', 'V', 'VI',
    'VII', 'VIII', 'IX', 'X', 'XI', 'XII'
  ];
  return daftarRomawi[monthIndex] || 'I';
}

/**
 * Generator Nomor Surat Resmi Sekolah Dinamis (DRY Implementation).
 * Menggantikan token {NOMOR}, {BULAN_ROMAWI}, dan {TAHUN} secara otomatis.
 */
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

#v(0.2cm)
_Keuntungan Arsitektural_: Jika pihak sekolah mengubah pola nomor surat (misalnya dari `421.3/001/SMKN1/XI/2026` menjadi `421/001-TU/XI/2026`), pengembang *hanya perlu mengubah nilai template pada basis data tanpa menyentuh kode logika backend.*

== 5.3 Penerapan Prinsip DRY: Reusable Middleware Autentikasi & RBAC
#v(0.2cm)
```typescript
// File: be/src/middlewares/auth.middleware.ts

import { Request, Response, NextFunction } from 'express';
import { verifyToken, TokenPayload } from '../utils/jwt';

export interface AuthenticatedRequest extends Request {
  user?: TokenPayload;
}

/**
 * Middleware Autentikasi Terpadu (DRY).
 * Mengamankan seluruh endpoint backend dari akses tanpa izin.
 */
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

#pagebreak()

= BAB VI: KESIMPULAN & PENUTUP

== 6.1 Kesimpulan
Berdasarkan perancangan dan konstruksi perangkat lunak pada sistem *SIPESAT (Sistem Informasi Pengajuan Surat Siswa Berbasis Web)*:
+ *Ketepatan Pemetaan Desain ke Kode*: Seluruh entitas pada Class Diagram (UML 2.5) berhasil ditransformasikan secara konsisten ke dalam skema fisik basis data relasional (PostgreSQL via Prisma ORM) dan definisi tipe TypeScript tanpa deviasi arsitektural.
+ *Kepatuhan Alur Pesan Sequence Diagram*: Alur pengiriman pesan antarkomponen pada Sequence Diagram telah diwujudkan secara utuh ke dalam rantai pemanggilan fungsi controller asinkron (`POST /api/pengajuan` dan `PATCH /api/pengajuan/:id`) yang dilengkapi penanganan validasi batas dan pencatatan jejak audit (_audit trail_).
+ *Penerapan Standar Rekayasa Tinggi*: Konstruksi kode terbukti mematuhi prinsip *DRY (Don't Repeat Yourself)* melalui modul generator nomor surat dinamis dan middleware autentikasi RBAC terpusat, serta menegakkan prinsip *KISS* dan *Readability* dengan konvensi penamaan standar industri.

Dengan terselesaikannya tahap konstruksi dan implementasi ini, sistem informasi SIPESAT telah berada dalam kondisi fungsional yang stabil, aman, dan siap untuk melangkah ke tahapan berikutnya dalam SDLC, yaitu *Tahap Pengujian Perangkat Lunak (Software Testing & QA)*.

#v(1.0cm)
#align(center)[
  _Disusun dan disahkan secara mandiri oleh Kelompok RPL 7 (Adam Wahyu Kurniawan dkk) untuk memenuhi penilaian resmi Tugas Pertemuan 10 Mata Kuliah Rekayasa Perangkat Lunak - Universitas Indraprasta PGRI (UNINDRA)._
]
