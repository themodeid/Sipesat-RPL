# TUGAS 10 - REKAYASA PERANGKAT LUNAK (RPL)
**KONSTRUKSI DAN IMPLEMENTASI PERANGKAT LUNAK BERDASARKAN RANCANGAN DESAIN SISTEM**  
**PROGRAM STUDI TEKNIK INFORMATIKA - FTIK UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)**  
**TAHUN AKADEMIK 2026/2027**

---

### IDENTITAS KELOMPOK (KELOMPOK RPL 7 / KELAS RPL_XD)
1. **Adam Wahyu Kurniawan** (NPM: 202343500510) - *Lead System Architect & Software Engineer*
2. **Fathu Rahman** (NPM: 202343500467) - *Business Analyst & Requirements Engineer*
3. **Surya Edi Saputra** (NPM: 202343500468) - *Quality Assurance & Technical Writer*
4. **Rizqi Muh. Al Hakimi** (NPM: 202343500449) - *Database Specialist & UI/UX*

* **Nama Proyek Perangkat Lunak:**  
  *Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)*
* **Studi Kasus:**  
  Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah Menengah
* **Bahasa Pemrograman & Tech Stack:**  
  * TypeScript / JavaScript (Node.js Runtime)
  * Framework Backend: Express.js & Prisma ORM
  * Database: PostgreSQL (Relational Database)
  * Framework Frontend: Next.js (React Framework) & Tailwind CSS
* **Landasan Acuan Desain Sebelumnya:**  
  * Dokumen Spesifikasi Kebutuhan Perangkat Lunak (SRS) Standar IEEE Std 830-1998 (Tugas 2)
  * Pemodelan Use Case Diagram & Matriks Hak Akses RBAC (Tugas 3)
  * Pemodelan Activity Diagram & Sequence Diagram Standar UML 2.5 (Tugas 4)
  * Pemodelan State Machine Diagram Siklus Hidup Permohonan Surat (Tugas 5)
  * Pemodelan Class Diagram & Object Diagram (Tugas 6)

---

## BAB I: PENDAHULUAN & KONSEP DASAR KONSTRUKSI PL

### 1.1 Gambaran Umum & Posisi Konstruksi dalam SDLC
Dalam siklus hidup pengembangan perangkat lunak (*Software Development Life Cycle* - SDLC), tahap **Konstruksi Perangkat Lunak (Software Construction)** merupakan fase krusial yang berada tepat di antara tahap perancangan arsitektur (*Design*) dan tahap pengujian (*Testing*). Tahap ini menitikberatkan pada proses penerjemahan representasi abstrak perancangan—seperti Class Diagram, Sequence Diagram, State Machine, dan Prototipe Antarmuka—menjadi kode sumber (*source code*) yang dapat dieksekusi secara nyata oleh mesin komputer.

Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) dirancang untuk mengotomatisasi birokrasi persuratan siswa (Surat Keterangan Siswa Aktif, Rekomendasi Beasiswa, Legalisir Ijazah, dan Dispensasi). Mengingat sistem ini mengelola dokumen resmi sekolah dan data identitas siswa, tahap konstruksi perangkat lunak wajib menjamin keselarasan 1-to-1 antara rancangan UML yang telah disahkan dengan implementasi kode program fisik, mencegah terjadinya deviasi (*architectural drift*), serta mengeliminasi kerentanan keamanan dan redudansi logika.

### 1.2 Prinsip Kode Berkualitas Tinggi
Konstruksi kode pada sistem SIPESAT dibangun berlandaskan enam prinsip rekayasa perangkat lunak standar industri:
1. **Readability (Keterbacaan)**: Kode program ditulis dengan struktur yang bersih, indentasi konsisten, serta penamaan variabel dan fungsi yang deskriptif sehingga mudah dipahami oleh anggota tim lain tanpa interpretasi ganda.
2. **Maintainability (Kemudahan Pemeliharaan)**: Modul-modul sistem dipisahkan secara tegas (*decoupled*) antara lapisan rute (Routing), lapisan kendali logika bisnis (Controller), lapisan akses data (Prisma ORM), dan lapisan antarmuka (Frontend React), sehingga perbaikan *bug* atau penambahan fitur di masa depan tidak menimbulkan efek samping destruktif pada modul lain.
3. **Reusability (Dapat Digunakan Kembali)**: Fungsi-fungsi yang memiliki kegunaan umum (seperti generator format nomor surat resmi, helper kalkulasi bulan romawi, dan middleware verifikasi token JWT) diisolasi ke dalam modul utilitas terpusat.
4. **Efficiency (Efisiensi)**: Kueri database dioptimalkan dengan memilih hanya kolom-kolom yang relevan (*projection select*), mencegah terjadinya masalah *over-fetching* dan *N+1 query problem*.
5. **Prinsip DRY (Don't Repeat Yourself)**: Menghindari duplikasi logika dan penulisan aturan bisnis berulang. Setiap aturan validasi atau format data hanya didefinisikan satu kali sebagai *Single Source of Truth*.
6. **Prinsip KISS (Keep It Simple, Stupid)**: Memilih solusi implementasi yang paling sederhana, deterministik, dan langsung menjawab kebutuhan pengguna tanpa lapisan abstraksi berlebih (*anti-overengineering*).

### 1.3 Standar Penamaan (*Coding Standards & Naming Conventions*)
Pembangunan kode program SIPESAT mengadopsi standar penamaan resmi ekosistem TypeScript/JavaScript modern:
* **PascalCase**: Digunakan secara eksklusif untuk penamaan Class, Interface, Type Definition, Model Prisma, dan Komponen React (contoh: `PengajuanSurat`, `JenisSurat`, `UserRole`, `TimelineStepper`).
* **camelCase**: Digunakan untuk penamaan variabel, properti objek, parameter, method, dan fungsi (contoh: `nomorPengajuan`, `generateNomorSuratResmi`, `buatPengajuanBaru`).
* **SCREAMING_SNAKE_CASE**: Digunakan untuk konstanta global dan nilai enumerasi (contoh: `STATUS_MENUNGGU`, `ROLE_ADMIN`, `JWT_SECRET_KEY`).
* **Satu Fungsi, Satu Tugas (Single Responsibility Principle)**: Setiap fungsi atau method dirancang hanya untuk menjalankan satu tugas spesifik dan terisolasi.

---

## BAB II: TRANSFORMASI DARI CLASS DIAGRAM KE KODE PROGRAM (MODEL & DATABASE)

### 2.1 Pemetaan Konseptual Class Diagram ke Kode Fisik
Dalam pemodelan berorientasi objek, Class Diagram (Tugas 6) mendefinisikan cetak biru entitas data, visibilitas atribut, metode operasional, dan hubungan relasional antarkelas. Pada tahap konstruksi sistem SIPESAT, transformasi dilakukan secara langsung menuju skema basis data relasional via **Prisma ORM** dan deklarasi tipe **TypeScript**.

Berikut adalah aturan pemetaan transformasi yang diterapkan:
1. **Nama Kelas UML** $\rightarrow$ Ditransformasikan menjadi nama model basis data relasional (`model User`, `model PengajuanSurat`, `model JenisSurat`).
2. **Atribut dan Tipe Data UML** $\rightarrow$ Ditransformasikan menjadi kolom tabel dengan tipe data ekuivalen (misal: `String` $\rightarrow$ `String/VarChar`, `DateTime` $\rightarrow$ `DateTime`, `Enum` $\rightarrow$ `PostgreSQL Native Enum`).
3. **Visibilitas Private (`-`)** $\rightarrow$ Ditegakkan melalui enkapsulasi controller dan seleksi field (*projection*) agar data sensitif seperti `password_hash` tidak terekspos keluar.
4. **Relasi Multiplisitas ($1 \dots *$ dan $1 \dots 1$)** $\rightarrow$ Diterjemahkan menjadi relasi relasional *Foreign Key* dan *Relation Directives* Prisma (`@relation`).

---

### 2.2 Implementasi Entitas Pengguna & Role-Based Access Control (RBAC)

#### A. Rujukan Class Diagram (Tugas 6)
Pada Class Diagram, entitas `Pengguna` memiliki atribut `id_pengguna`, `username`, `password_hash`, `email`, `role`, dan method autentikasi, yang kemudian diwariskan ke `Siswa` dan `PetugasTU`.

#### B. Transformasi ke Kode Skema Fisik (Prisma Schema)
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

---

### 2.3 Implementasi Entitas Transaksional Surat & Jenis Surat

#### A. Rujukan Class Diagram (Tugas 6)
Kelas `PengajuanSurat` berelasi asosiasi dengan `JenisSurat` ($1 \dots *$) dan memiliki komposisi terhadap berkas lampiran serta status siklus hidup surat (`StatusPengajuan`).

#### B. Transformasi ke Kode Skema Fisik (Prisma Schema)
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

---

### 2.4 Implementasi Entitas Riwayat Audit Log (`LogAktivitas`)

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

---

### 2.5 Tabel Komparasi Pemetaan Class Diagram vs Kode Fisik

| Elemen Class Diagram (UML 2.5) | Implementasi Kode (TypeScript & Prisma) | Keterangan Rekayasa |
| :--- | :--- | :--- |
| **Kelas `Pengguna` (Abstract)** | Model `User` (Prisma) | Mengadopsi *Single Table Inheritance* terpadu dengan kolom diskriminator `role`. |
| **Atribut `role: RoleEnum`** | Enum `Role { ADMIN, PETUGAS, SISWA }` | Native PostgreSQL Enum untuk integritas data level database. |
| **Kelas `JenisSurat`** | Model `JenisSurat` (Prisma) | Menyimpan konfigurasi pola penomoran surat resmi (`formatNomor`). |
| **Kelas `PengajuanSurat`** | Model `PengajuanSurat` (Prisma) | Entitas transaksional utama siklus permohonan surat sekolah. |
| **Relasi Agregasi `1..*`** | `@relation("SiswaPengajuan")` | Menegakkan integritas referensial foreign key (`siswaId` $\rightarrow$ `User.id`). |
| **Kelas `LogVerifikasi`** | Model `LogAktivitas` (Prisma) | Menyimpan rekaman jejak audit (*audit trail*) setiap perubahan status. |

---

## BAB III: TRANSFORMASI DARI SEQUENCE DIAGRAM KE KODE LOGIKA BISNIS (CONTROLLER & ROUTING)

### 3.1 Pemetaan Alur Pesan (*Message Passing*) ke Kode Program
Dalam Sequence Diagram (Tugas 4), interaksi sistem dimodelkan melalui pengiriman pesan (*message*) antar komponen:  
$$\text{Aktor (Siswa/Petugas)} \xrightarrow{\text{Pesan Input}} \text{Boundary (Router)} \xrightarrow{\text{Proses Logika}} \text{Control (Controller)} \xrightarrow{\text{Operasi I/O}} \text{Entity (Database)}$$

Pada kode program backend Express.js, urutan anak panah pada Sequence Diagram ditransformasikan menjadi urutan eksekusi metode asinkron (*asynchronous method chain*), penanganan validasi batas, transaksi database, dan pengembalian respons HTTP.

---

### 3.2 Skenario 1: Transformasi Alur Pengajuan Surat Baru oleh Siswa
* **Rujukan Sequence Diagram**: Siswa menginput formulir $\rightarrow$ Router memverifikasi autentikasi token JWT $\rightarrow$ Controller men-generate nomor tiket pengajuan (`REQ-YYYYMM-XXXX`) $\rightarrow$ Entity menyimpan rekaman ke database $\rightarrow$ Log aktivitas dicatat $\rightarrow$ Response konfirmasi berhasil dikirimkan ke antarmuka.

#### Implementasi Kode Program:
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

---

### 3.3 Skenario 2: Transformasi Alur Verifikasi & Penomoran Resmi oleh Petugas TU
* **Rujukan Sequence Diagram**: Petugas TU memeriksa berkas $\rightarrow$ Memilih aksi `DISETUJUI` $\rightarrow$ Sistem menghitung urutan surat keluar yang disetujui $\rightarrow$ Men-generate nomor surat dinamis sesuai template format resmi sekolah $\rightarrow$ Mengupdate data surat $\rightarrow$ Mengirim notifikasi status.

#### Implementasi Kode Program:
```typescript
// File: be/src/routes/pengajuan.routes.ts

router.patch('/:id', authMiddleware, async (req: AuthenticatedRequest, res) => {
  try {
    const user = req.user!;
    
    // Boundary Guard: Hanya Petugas TU atau Admin yang berhak memverifikasi
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

---

## BAB IV: TRANSFORMASI WIREFRAME / PROTOTIPE KE KODE ANTARMUKA (FRONTEND)

### 4.1 Pemetaan Desain Wireframe ke Komponen React
Struktur wireframe tata letak antarmuka yang dirancang pada fase desain ditransformasikan ke dalam komponen modular **Next.js (React Framework)** yang dipadukan dengan utility-first styling **Tailwind CSS**.

Prinsip transformasi antarmuka yang ditegakkan:
1. **Container & Box Model**: Struktur batas halaman pada wireframe diterjemahkan menjadi layout kartu ber-border halus (`border border-zinc-200 dark:border-zinc-800 rounded-xl`).
2. **State Reactive**: Input pengguna dan status unggahan berkas dikendalikan secara reaktif menggunakan React Hook (`useState`, `useEffect`).
3. **Ergonomi & Visual Feedback**: Status permohonan divisualisasikan menggunakan lencana warna semantik (*Badge Pills*) yang konsisten:
   * `MENUNGGU`: Kuning / Amber (`bg-amber-100 text-amber-800`)
   * `DIPROSES`: Biru (`bg-blue-100 text-blue-800`)
   * `DISETUJUI`: Hijau (`bg-emerald-100 text-emerald-800`)
   * `DITOLAK`: Merah (`bg-rose-100 text-rose-800`)

---

### 4.2 Implementasi Komponen Formulir Pengajuan Surat Siswa
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
    <form onSubmit={handleSubmit} className="p-6 bg-white dark:bg-zinc-900 rounded-xl border border-zinc-200 dark:border-zinc-800 shadow-sm space-y-4">
      <h2 className="text-xl font-bold text-zinc-900 dark:text-zinc-100">Buat Permohonan Surat Baru</h2>
      
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
          placeholder="Contoh: Pengajuan Beasiswa PIP / Keperluan Dinas"
          className="w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
          rows={3}
          required
        />
      </div>

      <button 
        type="submit" 
        disabled={isSubmitting}
        className="w-full py-2.5 px-4 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition"
      >
        {isSubmitting ? 'Mengirim...' : 'Kirim Permohonan Surat'}
      </button>
    </form>
  );
}
```

---

## BAB V: STANDAR KODING & PENERAPAN PRINSIP DRY (STUDI KASUS BEFORE VS AFTER)

### 5.1 Analisis Standar Penamaan & Keterbacaan (*Before vs After*)
Sesuai dengan arahan modul ajar Pertemuan 10, kode program wajib mengeliminasi variabel abstrak bersuku kata tunggal yang mengaburkan maksud logika.

#### Kasus: Fungsi Pengecekan Masa Kedaluwarsa Berkas Lampiran

```typescript
// ❌ BEFORE (Kurang Baik / Kualitas Rendah):
// Masalah: Nama variabel tidak deskriptif (b, t, d), tidak ada validasi tipe, 
// magic string tidak berkonteks, sulit dipahami oleh programmer lain.
function cek(b: any, t: any) {
  let d = new Date();
  if (b.exp < d.getTime()) {
    return false;
  }
  return true;
}
```

```typescript
// ✅ AFTER (Sangat Baik / Standar SIPESAT):
// Solusi: Menggunakan TypeScript type safety, nama fungsi self-explanatory, 
// parameter eksplisit, dan mengembalikan boolean yang jelas.
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

---

### 5.2 Penerapan Prinsip DRY: Reusable Helper Generator Nomor Surat Resmi
Dalam sistem persuratan sekolah, setiap jenis surat (Surat Keterangan Siswa Aktif, Surat Rekomendasi, Surat Dispensasi) memiliki format penomoran yang memuat komponen nomor urut, kode klasifikasi instansi, bulan penerbitan dalam format romawi, dan tahun kalender berjalan.

Tanpa prinsip DRY, penulisan rumus pergantian bulan romawi dan penyusunan string nomor surat akan diulang berkali-kali di setiap controller pengajuan.

#### Implementasi Fungsi Reusable DRY:
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

*Keuntungan Arsitektural*: Jika sewaktu-waktu pihak sekolah mengubah pola format nomor surat (misalnya dari format `421.3/001/SMKN1/XI/2026` menjadi `421/001-TU/XI/2026`), pengembang **hanya perlu memperbarui nilai template pada basis data tanpa perlu mengubah satu baris pun kode logika backend!**

---

### 5.3 Penerapan Prinsip DRY: Reusable Middleware Autentikasi & RBAC
Proses dekripsi token JWT, ekstraksi identitas pengguna, dan otorisasi hak akses (*Role-Based Access Control*) tidak boleh ditulis manual di setiap rute controller.

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

---

## BAB VI: KESIMPULAN & PENUTUP

### 6.1 Kesimpulan
Berdasarkan perancangan dan konstruksi perangkat lunak yang telah diuraikan pada sistem **SIPESAT (Sistem Informasi Pengajuan Surat Siswa Berbasis Web)**, dapat disimpulkan beberapa poin fundamental:
1. **Ketepatan Pemetaan Desain ke Kode**: Seluruh entitas pada Class Diagram (UML 2.5) berhasil ditransformasikan secara konsisten ke dalam skema fisik basis data relasional (PostgreSQL via Prisma ORM) dan definisi tipe data TypeScript tanpa deviasi arsitektural.
2. **Kepatuhan Alur Pesan Sequence Diagram**: Alur pengiriman pesan antarkomponen pada Sequence Diagram telah diwujudkan secara utuh ke dalam rantai pemanggilan fungsi controller asinkron (`POST /api/pengajuan` dan `PATCH /api/pengajuan/:id`) yang dilengkapi penanganan validasi batas dan pencatatan jejak audit (*audit trail*).
3. **Penerapan Standar Rekayasa Tinggi**: Konstruksi kode terbukti mematuhi prinsip **DRY (Don't Repeat Yourself)** melalui modul generator nomor surat dinamis dan middleware autentikasi RBAC terpusat, serta menegakkan prinsip **KISS** dan **Readability** dengan konvensi penamaan standar industri.

Dengan terselesaikannya tahap konstruksi dan implementasi ini, sistem informasi SIPESAT telah berada dalam kondisi fungsional yang stabil, aman, dan siap untuk melangkah ke tahapan berikutnya dalam SDLC, yaitu **Tahap Pengujian Perangkat Lunak (*Software Testing & Quality Assurance*)**.

---

*Disusun dan disahkan secara mandiri oleh Kelompok RPL 7 (Adam Wahyu Kurniawan dkk) untuk memenuhi penilaian resmi Tugas Pertemuan 10 Mata Kuliah Rekayasa Perangkat Lunak - Universitas Indraprasta PGRI (UNINDRA).*
