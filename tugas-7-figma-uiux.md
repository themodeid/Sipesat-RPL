# TUGAS REKAYASA PERANGKAT LUNAK (RPL)
**DOKUMENTASI HASIL DESAIN FIGMA & SISTEM DESAIN ANTARMUKA PENGGUNA (UI/UX)**  
**PROGRAM STUDI TEKNIK INFORMATIKA - FTIK UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)**  
**TAHUN AKADEMIK 2026/2027**

---

### IDENTITAS KELOMPOK (KELOMPOK RPL 7 / KELAS RPL_XD)
1. **Adam Wahyu Kurniawan** (NPM: `202343500510`) - *Lead System Architect & Software Engineer*
2. **Fathu Rahman** (NPM: `202343500467`) - *Business Analyst & Requirements Engineer*
3. **Surya Edi Saputra** (NPM: `202343500468`) - *Quality Assurance & Technical Writer*
4. **Rizqi Muh. Al Hakimi** (NPM: `202343500449`) - *Database Specialist & UI/UX Designer*

* **Nama Proyek Perangkat Lunak:**  
  *Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)*
* **Studi Kasus:**  
  Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah Menengah

---

## BAB I: TAUTAN RESMI PROYEK FIGMA

Tautan proyek desain antarmuka pengguna (UI/UX Mockup & Prototype) sistem SIPESAT pada Figma:

> 🔗 **Tautan Publik Figma SIPESAT Kelompok 7:**  
> [**https://www.figma.com/design/sipesat-unindra-kelompok-7**](https://www.figma.com/)  
> *(Catatan: Teman-teman tim UI/UX dapat memperbarui URL tautan di atas secara langsung dengan tautan live sharing file Figma kelompok)*

---

## BAB II: SISTEM DESAIN (*DESIGN SYSTEM & STYLE GUIDE*)

Perancangan antarmuka pengguna SIPESAT mengadopsi prinsip **Clean Institutional Modernism** dengan palet warna formal institusi pendidikan, kontras tinggi, dan ramah pengguna (*user-friendly*).

### 2.1 Palet Warna Utama (*Color Palette Tokens*)

| Token Warna | Nilai Heksadesimal | Peran & Penggunaan Visual |
| :--- | :---: | :--- |
| **Primary Navy** | `#1C2434` | Warna latar belakang header institusi, sidebar navigasi, dan teks judul utama. |
| **Royal Blue** | `#1E6EEB` | Aksi utama (*Call to Action*), tombol aktif, tautan, dan indikator stepper aktif. |
| **Emerald Green** | `#10B981` | Status positif (Status: `DISETUJUI`, `SELESAI`), tombol sukses, dan badge valid. |
| **Danger Rose** | `#EF4444` | Status penolakan (`DITOLAK`), pesan error validasi berkas > 2MB, dan konfirmasi hapus. |
| **Amber Warning** | `#F59E0B` | Status dalam proses (`DIPROSES`), peringatan berkas belum lengkap. |
| **Slate Neutral** | `#64748B` | Teks pendukung, label sekunder, dan garis border pemisah tabel. |
| **Canvas Background** | `#F8FAFC` | Latar belakang kanvas aplikasi (*Light Mode*) anti-silau mata. |

### 2.2 Tipografi (*Typography Scale*)
* **Font Family Utama**: *Inter / Geist Sans* (Sans-Serif modern berkarakter bersih).
* **Font Family Data**: *JetBrains Mono / Consolas* (Monospaced untuk Nomor Surat resmi dan Kode Tiket).
* **Ukuran & Hirarki**:
  * Heading 1 (Page Title): `24px / Bold` (Navy `#1C2434`)
  * Heading 2 (Section Card): `18px / Semi-Bold`
  * Sub-heading: `14px / Medium`
  * Body Text: `13px / Regular` (Line-height `1.5`)
  * Caption / Helper Text: `11px / Regular` (Slate `#64748B`)

### 2.3 Prinsip Ergonomi & Tata Letak (*Layout & Spacing*)
* **Grid Desktop**: 12 Kolom, Max Width 1280px, Margin Container 24px, Gutter 16px.
* **Border Radius**: Konsisten `rounded-lg (8px)` untuk kartu panel dan `rounded-md (6px)` untuk input formulir dan tombol.
* **Elevasi & Bayangan**: Menggunakan *hairline border* (`1px solid #E2E8F0`) dikombinasikan bayangan lembut (*soft shadow* `0 1px 3px rgba(0,0,0,0.05)`).

---

## BAB III: ARSITEKTUR INFORMASI & ALUR PENGGUNA (*USER FLOW*)

```text
[ SISWA ] 
   │
   ├── Login (NISN & Sandi)
   ├── Dashboard Siswa ───> Ringkasan 4 Status Surat
   ├── Form Pengajuan Surat ───> Pilih Jenis Surat ───> Isi Tujuan ───> Upload Berkas (≤ 2MB) ───> Submit
   ├── Tracking Permohonan ───> Timeline Stepper 5 Titik (Draft -> Diajukan -> Diproses -> Disetujui)
   └── Unduh Dokumen ───> Cetak Surat Resmi PDF ber-QR Code

[ PETUGAS TU / ADMIN ]
   │
   ├── Login (NIP / Username & Sandi)
   ├── Dashboard Petugas TU ───> Statistik Agregasi Surat Masuk
   ├── Antrean Pengajuan Masuk ───> Filter Jenis Surat & Status
   ├── Modal Verifikasi ───> Pratinjau Berkas Siswa ───> Putusan Disposisi
   │                           ├── Tolak: Input Catatan Kekurangan Berkas
   │                           └── Setujui: Generate Nomor Surat Otomatis & Bubuhkan QR Code
   └── Ekspor Laporan ───> Rekapitulasi Periode Bulanan (Format CSV & PDF)
```

---

## BAB IV: KATALOG MOCKUP ANTARMUKA FIGMA (8 LAYAR UTAMA)

### 4.1 Layar 1: Halaman Autentikasi Pengguna (`/login`)
* **Tujuan**: Pintu gerbang masuk pengguna dengan proteksi otorisasi RBAC 2 Peran.
* **Fitur Visual**:
  * Branding resmi institusi sekolah (Logo & Identitas SIPESAT).
  * Form input NISN / NIP dan Kata Sandi dengan proteksi *Show/Hide Password*.
  * Tombol pintas cepat (*Quick Role Switcher*) untuk demonstrasi pengujian (Akun Siswa Demo vs Akun Admin TU Demo).

### 4.2 Layar 2: Dashboard Siswa (`/dashboard/siswa`)
* **Tujuan**: Pusat informasi status dan tindakan cepat permohonan siswa.
* **Fitur Visual**:
  * 4 Kartu Statistik Cepat: Total Diajukan, Sedang Diproses, Surat Selesai, dan Surat Ditolak.
  * Tombol Aksi Utama: *"➕ Buat Pengajuan Surat Baru"*.
  * Tabel Riwayat Terkini: 5 pengajuan terakhir lengkap dengan tanggal dan badge status semantik.

### 4.3 Layar 3: Formulir Pengajuan Surat Mandiri (`/pengajuan/baru`)
* **Tujuan**: Pengisian data permohonan dan pengunggahan berkas digital.
* **Fitur Visual**:
  * Dropdown dinamis 4 jenis surat: Surat Keterangan Siswa Aktif, Rekomendasi Beasiswa, Legalisir Ijazah, dan Dispensasi.
  * Boks informasi persyaratan otomatis muncul sesuai jenis surat yang dipilih.
  * Area *Drag-and-Drop File Uploader* dengan detektor ukuran file real-time (indikator merah jika > 2 MB).
  * Area teks input keperluan permohonan surat.

### 4.4 Layar 4: Pelacakan Status Permohonan (`/pengajuan/track/[id]`)
* **Tujuan**: Memberikan transparansi mutlak alur proses permohonan kepada siswa.
* **Fitur Visual**:
  * Komponen **Timeline Stepper 5 Titik**:
    1. *Draft Permohonan* (Tercatat di sistem)
    2. *Diajukan* (Menunggu antrean verifikasi TU)
    3. *Sedang Diproses* (Pengecekan berkas fisik & data pokok)
    4. *Disetujui* (Pemberian nomor resmi & TTE digital)
    5. *Selesai* (Dokumen siap diunduh)
  * Kartu Rincian Disposisi: Menampilkan nama petugas verifikator, tanggal proses, dan catatan disposisi.
  * Tombol *"Unduh Dokumen PDF Resmi"* yang langsung aktif begitu status mencapai DISETUJUI.

### 4.5 Layar 5: Dashboard Petugas Tata Usaha (`/dashboard/petugas`)
* **Tujuan**: Command center operasional staf Tata Usaha dalam mengelola seluruh lalu lintas surat sekolah.
* **Fitur Visual**:
  * Metrik Telemetri: Jumlah surat masuk hari ini, rata-rata waktu penyelesaian, dan antrean mendesak.
  * Filter multi-kategori: Filter berdasarkan jenis surat, kelas siswa, dan rentang tanggal permohonan.
  * Indikator waktu pengajuan (*Relative Timestamp*, misal: "15 menit yang lalu").

### 4.6 Layar 6: Modal Verifikasi Dokumen & Disposisi TU
* **Tujuan**: Layar pengambilan keputusan verifikasi berkas siswa.
* **Fitur Visual**:
  * Split Panel: Panel kiri menampilkan pratinjau berkas persyaratan siswa (PDF/JPG reader), panel kanan menampilkan formulir disposisi.
  * Tombol Aksi Dualitas:
    * Tombol Merah: *"❌ Tolak Permohonan"* (wajib mengisi alasan penolakan).
    * Tombol Hijau: *"✅ Setujui & Terbitkan Nomor"* (otomatis memicu generator nomor dinamis).

### 4.7 Layar 7: Pratinjau Dokumen Surat Resmi Hasil Cetak
* **Tujuan**: Visualisasi dokumen surat dinas formal yang diterbitkan sistem.
* **Fitur Visual**:
  * Kop surat resmi sekolah lengkap dengan logo dan alamat.
  * Nomor surat resmi terformat rapi: `421/001/SMK-PSKD/XI/2026`.
  * Teks narasi keterangan siswa aktif yang menarik biodata siswa secara otomatis.
  * Blok stempel dan **Tanda Tangan Digital QR Code** di pojok kanan bawah yang dapat dipindai untuk pembuktian keaslian dokumen.

### 4.8 Layar 8: Modul Laporan Rekapitulasi Persuratan (`/laporan`)
* **Tujuan**: Pembukuan arsip digital untuk pelaporan ke pimpinan sekolah.
* **Fitur Visual**:
  * Pemilih periode tanggal (Harian, Mingguan, Bulanan, Semester).
  * Tabel ringkasan statistik per jenis surat.
  * Tombol ekspor instan: *"📥 Ekspor ke CSV"* dan *"🖨️ Cetak Rekapitulasi PDF"*.

---

## BAB V: KESIMPULAN

Dokumentasi desain Figma dan Mockup sistem SIPESAT ini menjamin keselarasan 100% antara kebutuhan pengguna yang tertuang dalam dokumen SRS (Tugas 2) dengan implementasi nyata pada kode program Next.js dan Express (Tugas 10). Melalui antarmuka yang bersih, intuitif, dan responsif, sistem SIPESAT siap memberikan pengalaman pengguna yang unggul bagi seluruh civitas akademika sekolah.
