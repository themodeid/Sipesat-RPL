# SPESIFIKASI KEBUTUHAN PERANGKAT LUNAK
## (SOFTWARE REQUIREMENTS SPECIFICATION - SRS)

---

### **Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)**
**Standar Dokumen: IEEE Std 830-1998 / Karl Wiegers SRS Template**

```
========================================================================================
Mata Kuliah       : Rekayasa Perangkat Lunak (RPL)
Tugas             : Tugas 2 - Penyusunan Dokumen Spesifikasi Kebutuhan Perangkat Lunak (SRS)
Program Studi     : Teknik Informatika
Fakultas          : Teknik dan Ilmu Komputer (FTIK)
Universitas       : Universitas Indraprasta PGRI (UNINDRA) Jakarta
Tahun Akademik    : 2026/2027
Batas Pengumpulan : 25 September 2026, 23.59 WIB
========================================================================================
```

---

### **TIM PENYUSUN (KELOMPOK RPL 7)**

| No. | Nama Mahasiswa | Nomor Pokok Mahasiswa (NPM) | Peran / Kontribusi |
|:---:|:---|:---:|:---|
| 1. | **Adam Wahyu Kurnia** | **202343500510** | *Lead System Architect & Software Engineer* |
| 2. | **Fathu Rahman** | **202343500467** | *Business Analyst & Requirements Engineer* |
| 3. | **Surya Edi Saputra** | **202343500468** | *Quality Assurance & Technical Writer* |
| 4. | **Rizqi Muh. Al Hakimi** | **202343500449** | *Database & UI/UX Specialist* |

---

### **RIWAYAT REVISI DOKUMEN**

| Versi | Tanggal | Penulis | Deskripsi Perubahan |
|:---:|:---:|:---|:---|
| **1.0** | 15 September 2026 | Kelompok 7 | Pengajuan Ide Proyek & Gambaran Umum (Tugas 1). |
| **2.0** | 24 September 2026 | Kelompok 7 | Penyusunan Lengkap Dokumen SRS Standar IEEE / Karl Wiegers (Tugas 2). |

---

## DAFTAR ISI

1. [Bab 1: Pendahuluan](#1-pendahuluan)
   - 1.1 [Tujuan Dokumen](#11-tujuan-dokumen)
   - 1.2 [Konvensi Dokumen](#12-konvensi-dokumen)
   - 1.3 [Audiens yang Dituju dan Saran Pembacaan](#13-audiens-yang-dituju-dan-saran-pembacaan)
   - 1.4 [Cakupan Produk](#14-cakupan-produk)
   - 1.5 [Referensi](#15-referensi)
2. [Bab 2: Deskripsi Keseluruhan](#2-deskripsi-keseluruhan)
   - 2.1 [Perspektif Produk](#21-perspektif-produk)
   - 2.2 [Fungsi Produk](#22-fungsi-produk)
   - 2.3 [Kelas Pengguna dan Karakteristik](#23-kelas-pengguna-dan-karakteristik)
   - 2.4 [Lingkungan Operasi](#24-lingkungan-operasi)
   - 2.5 [Batasan Desain dan Implementasi](#25-batasan-desain-dan-implementasi)
   - 2.6 [Dokumentasi Pengguna](#26-dokumentasi-pengguna)
   - 2.7 [Asumsi dan Ketergantungan](#27-asumsi-dan-ketergantungan)
3. [Bab 3: Kebutuhan Antarmuka Eksternal](#3-kebutuhan-antarmuka-eksternal)
   - 3.1 [Antarmuka Pengguna (User Interface)](#31-antarmuka-pengguna-user-interface)
   - 3.2 [Antarmuka Perangkat Keras (Hardware Interface)](#32-antarmuka-perangkat-keras-hardware-interface)
   - 3.3 [Antarmuka Perangkat Lunak (Software Interface)](#33-antarmuka-perangkat-lunak-software-interface)
   - 3.4 [Antarmuka Komunikasi (Communication Interface)](#34-antarmuka-komunikasi-communication-interface)
4. [Bab 4: Fitur Sistem & Kebutuhan Fungsional](#4-fitur-sistem--kebutuhan-fungsional)
   - 4.1 [Fitur Autentikasi dan Manajemen Sesi](#41-fitur-autentikasi-dan-manajemen-sesi)
   - 4.2 [Fitur Manajemen Master Data (Siswa, Kelas, dan Jenis Surat)](#42-fitur-manajemen-master-data)
   - 4.3 [Fitur Pengajuan Surat Mandiri Siswa](#43-fitur-pengajuan-surat-mandiri-siswa)
   - 4.4 [Fitur Verifikasi, Disposisi, dan Validasi Berkas](#44-fitur-verifikasi-disposisi-dan-validasi-berkas)
   - 4.5 [Fitur Penomoran Otomatis dan Penerbitan Dokumen Digital](#45-fitur-penomoran-otomatis-dan-penerbitan-dokumen-digital)
   - 4.6 [Fitur Pelacakan Status Real-Time dan Riwayat Pengajuan](#46-fitur-pelacakan-status-real-time-dan-riwayat-pengajuan)
   - 4.7 [Fitur Laporan Rekapitulasi Administrasi](#47-fitur-laporan-rekapitulasi-administrasi)
5. [Bab 5: Kebutuhan Nonfungsional & Aturan Bisnis](#5-kebutuhan-nonfungsional--aturan-bisnis)
   - 5.1 [Kebutuhan Kinerja (Performance Requirements)](#51-kebutuhan-kinerja-performance-requirements)
   - 5.2 [Kebutuhan Keamanan Fisik dan Data (Safety Requirements)](#52-kebutuhan-keamanan-fisik-dan-data-safety-requirements)
   - 5.3 [Kebutuhan Keamanan Sistem & Hak Akses (Security Requirements)](#53-kebutuhan-keamanan-sistem--hak-akses-security-requirements)
   - 5.4 [Atribut Kualitas Perangkat Lunak (Software Quality Attributes)](#54-atribut-kualitas-perangkat-lunak-software-quality-attributes)
   - 5.5 [Aturan Bisnis (Business Rules)](#55-aturan-bisnis-business-rules)
6. [Bab 6: Lampiran](#6-lampiran)
   - 6.1 [Lampiran A: Glosarium Istilah](#61-lampiran-a-glosarium-istilah)
   - 6.2 [Lampiran B: Diagram Use Case Sistem](#62-lampiran-b-diagram-use-case-sistem)

---

## 1. PENDAHULUAN

### 1.1 Tujuan Dokumen
Dokumen Spesifikasi Kebutuhan Perangkat Lunak (*Software Requirements Specification* - SRS) ini disusun dengan tujuan untuk:
1. Mendefinisikan secara menyeluruh, terperinci, dan sistematis mengenai kebutuhan fungsional dan nonfungsional dari **Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)**.
2. Menjadi kontrak kerja formal serta acuan tunggal (*single source of truth*) bagi seluruh pemangku kepentingan (*stakeholders*), yang meliputi analis sistem, perancang antarmuka (UI/UX), pengembang perangkat lunak (*software engineers*), penguji perangkat lunak (*quality assurance*), dosen pembimbing/pengampu mata kuliah, dan pihak sekolah sebagai pengguna akhir.
3. Memastikan bahwa sistem yang dibangun pada tahap implementasi memiliki kesesuaian 100% dengan ruang lingkup masalah yang telah diidentifikasi pada dokumen Tugas 1.

### 1.2 Konvensi Dokumen
Dokumen ini disusun mengikuti konvensi penulisan standar IEEE 830-1998 dan Karl Wiegers dengan kaidah:
* Setiap kebutuhan fungsional diberikan penomoran unik dengan format:  
  `[REQ-KATEGORI-NOMOR]`, contoh: `REQ-SUB-01` (Kebutuhan Pengajuan Surat nomor 1).
* Setiap aturan bisnis diberikan penomoran unik dengan format:  
  `[BR-NOMOR]`, contoh: `BR-01` (*Business Rule* nomor 1).
* Tingkat prioritas kebutuhan diklasifikasikan menjadi tiga tingkatan:
  * **Tinggi (*High*)**: Kebutuhan mutlak yang wajib ada agar sistem dapat berfungsi (*core requirement*).
  * **Sedang (*Medium*)**: Kebutuhan penting yang mendukung efisiensi operasional tetapi tidak menghentikan fungsi inti sistem jika ditunda.
  * **Rendah (*Low*)**: Kebutuhan pelengkap atau peningkatan kenyamanan pengguna di masa depan (*nice-to-have*).

### 1.3 Audiens yang Dituju dan Saran Pembacaan
Dokumen ini ditujukan kepada beberapa kelompok pembaca:
* **Dosen Pengampu & Penguji Akademik**: Disarankan membaca Bab 1 hingga Bab 5 secara berurutan untuk menilai kedalaman analisis, pemenuhan standar rekayasa perangkat lunak, dan kelayakan arsitektur sistem.
* **Tim Pengembang (*Software Developers*)**: Wajib memusatkan perhatian pada Bab 3, Bab 4, dan Bab 5 sebagai panduan penyusunan basis data, arsitektur *backend API*, dan antarmuka *frontend*.
* **Penguji Sistem (*QA/Testers*)**: Disarankan merujuk pada urutan stimulus/respons di Bab 4 dan kebutuhan nonfungsional di Bab 5 untuk merancang *test case* dan pengujian *Black-box*.
* **Pihak Administrasi Sekolah (Staf TU)**: Cukup membaca Bab 2 dan Bab 4 untuk memahami alur kerja pengajuan surat dan validasi dokumen.

### 1.4 Cakupan Produk
Perangkat lunak yang dikembangkan adalah sistem informasi berbasis web responsif bernama **SIPESAT** (*Sistem Informasi Pengajuan Surat Siswa*).  
* **Manfaat Utama**: Menggantikan proses pengajuan surat administrasi siswa yang selama ini bersifat manual, lambat, dan rentan kehilangan berkas menjadi sistem digital mandiri (*self-service*).
* **Fitur Utama yang Dicakup**:
  * Autentikasi berbasis peran (*Role-Based Access Control* - RBAC) untuk 2 peran utama: Siswa dan Petugas Tata Usaha (Staf TU / Admin).
  * Formulir pengajuan surat mandiri oleh siswa untuk berbagai jenis surat (Surat Keterangan Siswa Aktif, Surat Keterangan Berkelakuan Baik, Surat Rekomendasi Beasiswa, Surat Keterangan Lulus/Pindah, dan Surat Izin Penelitian).
  * Manajemen unggah berkas pendukung (Kartu Pelajar, Kartu Keluarga, Bukti Pembayaran, dll).
  * Panel verifikasi dokumen, validasi berkas, dan persetujuan akhir (*approval*) terpadu oleh Petugas TU.
  * Generator dokumen PDF resmi otomatis dengan penomoran surat kedinasan dan stempel digital ber-QR Code untuk verifikasi keaslian.
  * Modul pelacakan status pengajuan secara *real-time* (*timeline tracking*).
  * Modul ekspor laporan rekapitulasi pengajuan surat bulanan/tahunan bagi administrasi sekolah.

### 1.5 Referensi
1. IEEE Std 830-1998, *IEEE Recommended Practice for Software Requirements Specifications*, IEEE Computer Society.
2. Karl E. Wiegers & Joy Beatty, *Software Requirements (3rd Edition)*, Microsoft Press, 2013.
3. Ian Sommerville, *Software Engineering (10th Edition)*, Pearson Education, 2016.
4. Roger S. Pressman & Bruce R. Maxim, *Software Engineering: A Practitioner's Approach (8th Edition)*, McGraw-Hill, 2015.
5. Panduan Tugas Mata Kuliah Rekayasa Perangkat Lunak, Program Studi Teknik Informatika, FTIK Universitas Indraprasta PGRI (UNINDRA), 2026.
6. Berkas Tugas 1 Kelompok 7 RPL UNINDRA: *Sistem Informasi Pengajuan Surat Siswa Berbasis Web*, September 2026.

---

## 2. DESKRIPSI KESELURUHAN

### 2.1 Perspektif Produk
SIPESAT merupakan sistem mandiri berbasis web (*self-contained web application*) yang dirancang untuk modernisasi operasional sekolah. Sistem ini tidak menggantikan sistem penilaian akademik utama (seperti *Learning Management System* / e-Rapor), melainkan bertindak sebagai modul pelayanan administrasi ketatausahaan mandiri (*student administrative self-service portal*).  

Konteks arsitektur sistem disajikan pada diagram blok berikut:

```
+-------------------------------------------------------------------------+
|                              PENGGUNA                                   |
|        [Siswa (Smartphone/PC)]          [Petugas TU / Admin (PC)]       |
+-------------------------------------------------------------------------+
                                    │ (Protokol HTTPS)
                                    ▼
+-------------------------------------------------------------------------+
|                  APLIKASI SIPESAT (NEXT.JS APP ROUTER)                  |
|  - Presentation Layer: Tailwind CSS, React Server & Client Components   |
|  - Business Logic Layer: Service Layer, Validation Engine (Zod)         |
|  - Security Layer: Session Management (JWT/HttpOnly), RBAC Middleware   |
|  - Document Engine: PDFKit / React-PDF & Dynamic QR Code Generator     |
+-------------------------------------------------------------------------+
                                    │ (Prisma ORM)
                                    ▼
+-------------------------------------------------------------------------+
|                     DATA LAYER (POSTGRESQL 16)                          |
|  - Master Data Siswa, Kelas, Jurusan, Jenis Surat, Template Surat       |
|  - Transaksi Pengajuan Surat, Riwayat Status, Unggahan Dokumen          |
|  - Audit Log & Rekapitulasi Administrasi                                |
+-------------------------------------------------------------------------+
```

### 2.2 Fungsi Produk
Ringkasan kapabilitas fungsional utama dari SIPESAT meliputi:
1. **Fungsi Autentikasi & Akun**: Registrasi akun siswa, verifikasi NISN, login 2-role (Siswa & Petugas TU), dan perubahan kata sandi.
2. **Fungsi Pengajuan Surat**: Pemilihan template surat, pengisian formulir kebutuhan spesifik, pengunggahan berkas prasyarat (format PDF/JPG/PNG), serta penerbitan nomor resi pengajuan.
3. **Fungsi Validasi & Verifikasi Berkas**: Pemeriksaan kelengkapan berkas oleh Petugas TU, penerimaan/penolakan permohonan disertai alasan perbaikan yang jelas.
4. **Fungsi Persetujuan (*Approval*) & Penomoran Resmi**: Otorisasi permohonan surat dinas dan penerbitan nomor surat resmi sekolah oleh Petugas Tata Usaha.
5. **Fungsi Cetak Dokumen Digital Otomatis**: Penyisipan nomor agenda surat dinas otomatis dan pembuatan file PDF ber-kop surat resmi yang dilengkapi QR Code validator.
6. **Fungsi Pelacakan Status (*Tracking Engine*)**: Visualisasi status pengajuan (*Diajukan* $\rightarrow$ *Ditinjau* $\rightarrow$ *Disetujui / Selesai* atau *Ditolak*).
7. **Fungsi Rekapitulasi & Pelaporan**: Penyaringan data pengajuan berdasarkan rentang tanggal, kelas, atau jenis surat untuk kebutuhan arsip dan pelaporan administrasi sekolah.

### 2.3 Kelas Pengguna dan Karakteristik

| Kelas Pengguna | Deskripsi & Karakteristik | Frekuensi Pemakaian | Hak Akses Utama |
|:---|:---|:---:|:---|
| **Siswa** | Siswa aktif sekolah. Terbiasa menggunakan ponsel pintar (*smartphone*), menginginkan antarmuka yang simpel, cepat, dan transparan dalam melihat perkembangan surat. | Berkala (1–3 kali per semester saat memerlukan surat). | Mengajukan surat, mengunggah syarat, melacak status, mengunduh salinan surat digital, memperbarui profil pribadi. |
| **Petugas Tata Usaha (Staf TU / Admin)** | Staf operasional administrasi sekolah. Memiliki literasi komputer standar perkantoran (Word/Excel), bekerja menggunakan PC/Laptop desktop di jam kerja. Bertanggung jawab penuh atas verifikasi dokumen, penomoran resmi, dan persetujuan akhir surat. | Harian (intensif sepanjang jam kerja operasional sekolah). | Verifikasi berkas, validasi pengajuan, persetujuan (*approval*), penolakan/revisi, input nomor surat dinas, mencetak fisik surat, mengubah status proses, mengelola data siswa & jenis surat, serta ekspor rekapitulasi laporan. |

### 2.4 Lingkungan Operasi
1. **Sisi Klien (*Client-Side*)**:
   * Perangkat: Komputer desktop, laptop, tablet, dan smartphone Android/iOS.
   * Peramban Web (*Browser*): Google Chrome (v110+), Mozilla Firefox (v110+), Microsoft Edge (v110+), Apple Safari (v16+).
2. **Sisi Peladen (*Server-Side*)**:
   * Sistem Operasi: Linux (Ubuntu Server 22.04 LTS / Debian 12) atau Windows Server.
   * Runtime: Node.js (LTS v20+).
   * Framework Web: Next.js 15+ (App Router).
   * Web Server / Reverse Proxy: Nginx / Cloudflare.
3. **Sisi Basis Data (*Database-Side*)**:
   * DBMS: PostgreSQL 15+ (berjalan di container Docker).
   * ORM / Driver: Prisma ORM v5+.

### 2.5 Batasan Desain dan Implementasi
1. **Regulasi Perlindungan Data Pendidikan**: Sistem wajib mengamankan Nomor Induk Siswa Nasional (NISN), alamat rumah, dan data kontak siswa dari akses publik.
2. **Arsitektur Antarmuka**: Seluruh antarmuka web dibangun menggunakan prinsip *Mobile-First Responsive Design* dengan palet warna formal institusi (*Pure Neutral Zinc Palette*) agar tidak membingungkan pengguna.
3. **Keterbatasan Format Unggahan**: Ukuran file berkas pendukung dibatasi maksimal **2 MB per file** dengan ekstensi `.pdf`, `.jpg`, `.jpeg`, atau `.png` demi efisiensi kapasitas media penyimpanan peladen.
4. **Keaslian Dokumen**: Surat cetak/digital wajib dilengkapi pengaman berupa kode QR dinamis yang mengarah ke tautan verifikasi keaslian publik di sistem SIPESAT.

### 2.6 Dokumentasi Pengguna
Sistem akan dilengkapi dengan:
1. **Buku Panduan Pengguna (*User Manual*)**: Format PDF interaktif yang membedah alur pengajuan surat untuk siswa dan alur validasi untuk staf TU.
2. **Panduan Kontekstual di Layar (*Inline Help & Tooltip*)**: Penjelasan syarat berkas langsung pada formulir saat siswa memilih jenis surat tertentu.
3. **Dokumentasi Instalasi & *Deployment* Teknis**: Panduan pemeliharaan sistem, migrasi basis data, dan konfigurasi berkas `.env` untuk administrator sistem.

### 2.7 Asumsi dan Ketergantungan
1. Pengguna diasumsikan memiliki perangkat yang terhubung ke jaringan internet yang stabil saat mengakses sistem.
2. Siswa diasumsikan telah memiliki NISN yang terdaftar aktif pada pangkalan data sekolah.
3. Operasional sistem bergantung pada ketersediaan peladen PostgreSQL dan layanan penyimpanan berkas (*storage engine*).

---

## 3. KEBUTUHAN ANTARMUKA EKSTERNAL

### 3.1 Antarmuka Pengguna (User Interface)
* **Konsistensi Desain**: Menggunakan design system modern berbasis Tailwind CSS dengan palet netral kelas enterprise (Neutral Zinc `zinc-900`/`zinc-950`). Menghindari elemen visual norak, animasi berlebihan, dan efek glow neon yang menurunkan kredibilitas instansi akademik.
* **Tipografi Tabular**: Penomoran surat, nomor resi pengajuan, dan tanggal wajib disajikan menggunakan format angka *monospaced tabular figures* agar perataan vertikal pada tabel rapi.
* **Kemudahan Akses (*Accessibility*)**: Kontras teks memenuhi standar WCAG 2.1 Level AA dengan ukuran target sentuh (*touch target*) minimal 44x44 piksel pada perangkat layar sentuh.
* **Indikator Progres (*Stepper Timeline*)**: Pada halaman pelacakan status siswa, visualisasi disajikan dalam bentuk garis waktu interaktif 5 tahap dengan indikator titik warna (Kuning: Menunggu, Biru: Diproses, Hijau: Selesai, Merah: Ditolak).

### 3.2 Antarmuka Perangkat Keras (Hardware Interface)
* **Peladen Aplikasi**:
  * Prosesor: Minimal 2 Core vCPU (Rekomendasi 4 Core).
  * Memori RAM: Minimal 2 GB (Rekomendasi 4 GB untuk konkurensi build Next.js).
  * Media Penyimpanan: SSD minimal 20 GB dengan IOPS memadai.
* **Klien Siswa / Admin**:
  * Resolusi Layar: Minimal 360x640 piksel pada smartphone, minimal 1366x768 piksel pada PC/Laptop.

### 3.3 Antarmuka Perangkat Lunak (Software Interface)
* **Sistem Manajemen Basis Data**: PostgreSQL terhubung via TCP socket menggunakan Prisma Client dengan *connection pooling*.
* **Mesin Pembuat Dokumen PDF**: Mengintegrasikan pustaka generator PDF internal (seperti `@react-pdf/renderer` atau `pdfkit`) untuk mengompilasi data dinamis dari basis data menjadi dokumen surat dinas siap cetak.
* **Pustaka Kode QR**: Menggunakan generator QR Code internal berbasis JavaScript (`qrcode`) untuk menyisipkan tanda tangan digital terenkripsi pada bagian bawah surat.

### 3.4 Antarmuka Komunikasi (Communication Interface)
* Seluruh pertukaran data antara peramban klien dan peladen wajib melalui protokol aman **HTTPS (Port 443)** dengan enkripsi TLS 1.3.
* Pengiriman data formulir menggunakan format standar **JSON** melalui *RESTful API / Next.js Server Actions*.
* Unggah berkas dokumen menggunakan encoding `multipart/form-data`.
* Sesi login diamankan menggunakan token terenkripsi yang disimpan di dalam *Cookie* dengan atribut `HttpOnly`, `Secure`, dan `SameSite=Strict` untuk memitigasi serangan XSS dan CSRF.

---

## 4. FITUR SISTEM & KEBUTUHAN FUNGSIONAL

### 4.1 Fitur Autentikasi dan Manajemen Sesi
* **Deskripsi**: Mengatur pendaftaran akun siswa baru, proses masuk ke sistem, pembatasan hak akses berbasis peran, dan keluar sistem secara aman.
* **Prioritas**: **Tinggi (*High*)**.
* **Urutan Stimulus/Respons**:
  1. Pengguna memasukkan kredensial (NISN/Email/Username dan Password) pada halaman login.
  2. Sistem memvalidasi masukan terhadap basis data dan memverifikasi hash kata sandi (Argon2 / Bcrypt).
  3. Jika valid, sistem menerbitkan sesi terenkripsi (JWT) dan mengarahkan pengguna ke dashboard sesuai perannya (Dashboard Siswa atau Dashboard Petugas TU / Admin).
  4. Jika tidak valid, sistem menampilkan pesan galat spesifik tanpa membocorkan eksistensi data sensitif.

| ID Kebutuhan | Deskripsi Kebutuhan Fungsional | Prioritas |
|:---|:---|:---:|
| `REQ-AUTH-01` | Sistem wajib menyediakan formulir pendaftaran mandiri bagi siswa dengan memvalidasi NISN dan Nama Lengkap. | Tinggi |
| `REQ-AUTH-02` | Sistem wajib mengotentikasi pengguna berdasarkan kombinasi pengenal (NISN/Username) dan kata sandi. | Tinggi |
| `REQ-AUTH-03` | Sistem wajib mengenkripsi kata sandi menggunakan algoritma *one-way cryptographic hash* yang aman (Bcrypt / Argon2id). | Tinggi |
| `REQ-AUTH-04` | Sistem wajib mengimplementasikan *Role-Based Access Control* (RBAC) pada setiap rute halaman dan API endpoint. | Tinggi |
| `REQ-AUTH-05` | Sistem wajib menghentikan sesi (*logout*) dan menghapus token otentikasi saat pengguna menekan tombol keluar. | Tinggi |

---

### 4.2 Fitur Manajemen Master Data
* **Deskripsi**: Memungkinkan Staf TU (Admin) untuk mengelola data siswa, kelas, angkatan, serta jenis-jenis surat yang dapat diajukan beserta persyaratan berkasnya.
* **Prioritas**: **Tinggi (*High*)**.
* **Urutan Stimulus/Respons**:
  1. Admin membuka menu Master Data di dashboard admin.
  2. Admin dapat menambah, mengubah status, atau memperbarui informasi siswa dan jenis surat.
  3. Sistem memvalidasi masukan (misal: kode surat tidak boleh duplikat).
  4. Sistem menyimpan perubahan ke tabel basis data dan memperbarui tampilan tabel secara instan.

| ID Kebutuhan | Deskripsi Kebutuhan Fungsional | Prioritas |
|:---|:---|:---:|
| `REQ-MSTR-01` | Sistem wajib menyediakan fitur CRUD (Create, Read, Update, Delete/Deactivate) untuk Master Data Siswa. | Tinggi |
| `REQ-MSTR-02` | Sistem wajib menyediakan antarmuka untuk menambah dan mengedit Master Jenis Surat (Nama Surat, Kode Surat, Deskripsi, dan Dokumen Syarat Wajib). | Tinggi |
| `REQ-MSTR-03` | Sistem wajib mendukung fitur impor data siswa secara massal menggunakan berkas spreadsheet (Excel/CSV). | Sedang |
| `REQ-MSTR-04` | Sistem wajib memvalidasi keunikan NISN siswa dan Kode Jenis Surat agar tidak terjadi duplikasi data. | Tinggi |

---

### 4.3 Fitur Pengajuan Surat Mandiri Siswa
* **Deskripsi**: Memfasilitasi siswa untuk mengajukan permohonan surat administrasi secara mandiri dari perangkat mereka kapan saja.
* **Prioritas**: **Tinggi (*High*)**.
* **Urutan Stimulus/Respons**:
  1. Siswa masuk ke akun, membuka menu "Pengajuan Baru", dan memilih jenis surat yang dibutuhkan.
  2. Sistem menampilkan daftar persyaratan dan formulir dinamis (keperluan surat, data orang tua jika diperlukan, dsb.).
  3. Siswa mengisi formulir dan mengunggah dokumen prasyarat yang diminta.
  4. Sistem memvalidasi tipe file dan ukuran file (< 2 MB).
  5. Siswa menekan tombol "Kirim Pengajuan".
  6. Sistem menghasilkan Nomor Tiket/Resi Pengajuan unik (contoh: `SRT-202609-0012`) dan menyimpan transaksi dengan status awal: **"Menunggu Verifikasi"**.

| ID Kebutuhan | Deskripsi Kebutuhan Fungsional | Prioritas |
|:---|:---|:---:|
| `REQ-SUB-01` | Sistem wajib menampilkan katalog jenis surat aktif yang dapat dipilih oleh siswa. | Tinggi |
| `REQ-SUB-02` | Sistem wajib menyediakan formulir isian alasan/keperluan pengajuan surat. | Tinggi |
| `REQ-SUB-03` | Sistem wajib menyediakan komponen pengunggah berkas dengan validasi format (`.pdf`, `.jpg`, `.png`) dan batasan ukuran maksimal 2 MB. | Tinggi |
| `REQ-SUB-04` | Sistem wajib menghasilkan Nomor Resi Pengajuan acak-terstruktur secara otomatis untuk setiap pengajuan baru. | Tinggi |
| `REQ-SUB-05` | Sistem wajib mencegah siswa mengajukan surat baru dengan jenis yang sama jika pengajuan sebelumnya masih berstatus "Menunggu Verifikasi" atau "Sedang Diproses". | Sedang |

---

### 4.4 Fitur Verifikasi, Disposisi, dan Validasi Berkas
* **Deskripsi**: Memungkinkan Petugas TU (Admin) untuk memeriksa berkas permohonan siswa, memverifikasi keabsahan dokumen, memberikan persetujuan (*approval*), atau menolak pengajuan.
* **Prioritas**: **Tinggi (*High*)**.
* **Urutan Stimulus/Respons**:
  1. Petugas TU melihat daftar pengajuan berstatus "Menunggu Verifikasi" pada panel antrian admin.
  2. Petugas TU membuka detail pengajuan dan memeriksa berkas yang diunggah siswa via penampil dokumen.
  3. **Jika berkas valid**: Petugas TU menekan tombol "Setujui Permohonan" $\rightarrow$ status berubah menjadi "Disetujui" $\rightarrow$ sistem secara otomatis menerbitkan nomor surat dinas resmi sekolah dan menyematkan QR Code pengesahan digital.
  4. **Jika berkas tidak lengkap / tidak valid**: Petugas TU menekan tombol "Tolak / Minta Revisi", mengetikkan catatan alasan penolakan secara spesifik $\rightarrow$ status berubah menjadi "Perlu Revisi / Ditolak", dan siswa menerima notifikasi beserta catatan perbaikan.

| ID Kebutuhan | Deskripsi Kebutuhan Fungsional | Prioritas |
|:---|:---|:---:|
| `REQ-VERIF-01` | Sistem wajib menampilkan daftar permohonan surat masuk yang tersusun urut dari waktu pengajuan terlama (FIFO). | Tinggi |
| `REQ-VERIF-02` | Sistem wajib menyediakan penampil dokumen (*document previewer*) agar Petugas TU dapat melihat berkas tanpa harus mengunduhnya ke komputer lokal. | Sedang |
| `REQ-VERIF-03` | Sistem wajib mewajibkan Petugas TU mengisi kolom "Catatan Perbaikan / Alasan Penolakan" apabila permohonan surat ditolak. | Tinggi |
| `REQ-VERIF-04` | Sistem wajib menyediakan hak otorisasi persetujuan akhir (*approval*) dan penerbitan nomor surat dinas resmi khusus bagi peran Petugas Tata Usaha (Admin). | Tinggi |

---

### 4.5 Fitur Penomoran Otomatis dan Penerbitan Dokumen Digital
* **Deskripsi**: Mengotomatisasi penyusunan nomor surat dinas resmi sekolah dan mengompilasi surat dinas berformat PDF berstandar format tata naskah dinas.
* **Prioritas**: **Tinggi (*High*)**.
* **Urutan Stimulus/Respons**:
  1. Begitu permohonan disetujui, sistem secara otomatis mengambil nomor urut agenda terakhir pada tahun berjalan dan menyusun nomor surat lengkap (misal: `421.3/089/SMK-PSKD3/IX/2026`).
  2. Sistem men-generate dokumen PDF ber-kop surat resmi, memuat data identitas siswa, isi pernyataan surat, tanda tangan elektronik, stempel sekolah, dan QR Code verifikasi.
  3. Dokumen PDF disimpan di direktori arsip aman dan siap diunduh oleh siswa atau dicetak fisik oleh staf TU.

| ID Kebutuhan | Deskripsi Kebutuhan Fungsional | Prioritas |
|:---|:---|:---:|
| `REQ-DOC-01` | Sistem wajib menghasilkan nomor surat dinas otomatis sesuai aturan format penomoran surat kedinasan sekolah. | Tinggi |
| `REQ-DOC-02` | Sistem wajib menghasilkan berkas surat dinas dalam format Portable Document Format (PDF) standar A4. | Tinggi |
| `REQ-DOC-03` | Sistem wajib menempelkan QR Code dinamis pada berkas PDF yang menunjuk ke tautan verifikasi keaslian dokumen. | Tinggi |
| `REQ-DOC-04` | Sistem wajib menyediakan tombol cetak dokumen langsung (*browser print dialog*) yang telah dioptimasi dengan aturan CSS `@media print`. | Sedang |

---

### 4.6 Fitur Pelacakan Status Real-Time dan Riwayat Pengajuan
* **Deskripsi**: Memberikan transparansi penuh kepada siswa mengenai posisi berkas permohonannya tanpa perlu datang langsung bertanya ke loket TU.
* **Prioritas**: **Tinggi (*High*)**.
* **Urutan Stimulus/Respons**:
  1. Siswa membuka menu "Riwayat Surat" pada dashboard siswa.
  2. Sistem menampilkan daftar seluruh pengajuan yang pernah dilakukan lengkap dengan lencana status warna.
  3. Siswa mengklik tombol "Lacak": sistem menampilkan diagram garis waktu (*stepper*) beserta catatan petugas TU jika ada revisi.
  4. Jika status telah "Selesai", sistem mengaktifkan tombol "Unduh Surat Digital (PDF)".

| ID Kebutuhan | Deskripsi Kebutuhan Fungsional | Prioritas |
|:---|:---|:---:|
| `REQ-TRK-01` | Sistem wajib menampilkan linimasa tahapan status pengajuan secara real-time. | Tinggi |
| `REQ-TRK-02` | Sistem wajib menampilkan catatan alasan penolakan/perbaikan dari staf TU secara transparan kepada siswa. | Tinggi |
| `REQ-TRK-03` | Sistem wajib menyediakan tautan unduh berkas PDF bagi pengajuan yang telah selesai diproses dan disetujui. | Tinggi |

---

### 4.7 Fitur Laporan Rekapitulasi Administrasi
* **Deskripsi**: Menyediakan modul analitik dan pencetakan rekapitulasi data pengajuan surat untuk kebutuhan evaluasi manajemen dan pertanggungjawaban dinas.
* **Prioritas**: **Sedang (*Medium*)**.

| ID Kebutuhan | Deskripsi Kebutuhan Fungsional | Prioritas |
|:---|:---|:---:|
| `REQ-REP-01` | Sistem wajib menyediakan tabel rekapitulasi pengajuan surat dengan filter rentang tanggal, status, dan jenis surat. | Sedang |
| `REQ-REP-02` | Sistem wajib menyediakan fitur ekspor data rekapitulasi ke format spreadsheet (.xlsx / .csv). | Sedang |
| `REQ-REP-03` | Sistem wajib menyajikan ringkasan statistik (total diajukan, total selesai, total ditolak, rata-rata waktu pemrosesan) pada dashboard eksekutif. | Rendah |

---

## 5. KEBUTUHAN NONFUNGSIONAL & ATURAN BISNIS

### 5.1 Kebutuhan Kinerja (Performance Requirements)
* `NFR-PERF-01`: Waktu tanggap (*response time*) peladen untuk permintaan halaman web dan data tabular tidak boleh melebihi **2,0 detik** pada koneksi internet standar (3G/4G atau pita lebar 10 Mbps).
* `NFR-PERF-02`: Proses pengompilasasian dokumen PDF dan pembuatan QR Code dinamis wajib selesai dalam waktu kurang dari **3,0 detik** per dokumen.
* `NFR-PERF-03`: Basis data wajib mampu melayani minimal **100 transaksi pengajuan bersamaan (*concurrent transactions*)** tanpa penurunan performa yang signifikan.

### 5.2 Kebutuhan Keamanan Fisik dan Data (Safety Requirements)
* `NFR-SAFE-01`: Sistem wajib melakukan pencadangan basis data (*database backup*) terjadwal secara otomatis setiap hari pada pukul 02.00 dini hari WIB.
* `NFR-SAFE-02`: Berkas dokumen yang diunggah wajib disimpan di direktori terisolasi di luar *web root* publik untuk mencegah eksekusi skrip berbahaya (*arbitrary code execution*).

### 5.3 Kebutuhan Keamanan Sistem & Hak Akses (Security Requirements)
* `NFR-SEC-01`: Seluruh komunikasi data wajib menggunakan protokol terenkripsi **HTTPS / TLS 1.3**.
* `NFR-SEC-02`: Seluruh masukan formulir (*user input*) wajib divalidasi dan disanitasi secara ketat di sisi peladen (*Server-Side Validation*) menggunakan pustaka seperti Zod untuk mencegah serangan *SQL Injection* dan *Cross-Site Scripting (XSS)*.
* `NFR-SEC-03`: Sistem wajib mengunci akun pengguna untuk sementara waktu (selama 15 menit) apabila terjadi kegagalan otentikasi login sebanyak **5 kali berturut-turut** guna mencegah serangan *brute force*.
* `NFR-SEC-04`: Akses ke dokumen surat dan data pribadi siswa wajib dilindungi oleh otorisasi berbasis sesi; pengguna dilarang mengakses dokumen milik siswa lain hanya dengan mengganti parameter ID di URL (*Insecure Direct Object References - IDOR prevention*).

### 5.4 Atribut Kualitas Perangkat Lunak (Software Quality Attributes)
* **Ketersediaan (*Availability*)**: Sistem memiliki target waktu aktif (*uptime*) minimal **99,0%** selama hari dan jam kerja operasional sekolah.
* **Keandalan (*Reliability*)**: Tingkat kegagalan sistem (*Mean Time Between Failures - MTBF*) minimal 720 jam operasional tanpa gangguan kritis.
* **Kemudahan Penggunaan (*Usability*)**: Antarmuka dirancang intuitif sehingga siswa baru dapat menyelesaikan pengajuan surat dalam waktu kurang dari **5 menit** tanpa memerlukan pelatihan formal sebelumnya.
* **Kemudahan Pemeliharaan (*Maintainability*)**: Kode program disusun dengan arsitektur bersih modular, menggunakan TypeScript untuk *type safety*, dan terdokumentasi rapi agar mudah dikembangkan oleh pengembang lain di masa depan.
* **Portabilitas (*Portability*)**: Sistem dapat diakses dengan tata letak adaptif di semua sistem operasi (Windows, macOS, Linux, Android, iOS) tanpa membutuhkan instalasi aplikasi pihak ketiga selain peramban web standar.

### 5.5 Aturan Bisnis (Business Rules)

| ID Aturan | Nama Aturan Bisnis | Deskripsi Kebijakan |
|:---|:---|:---|
| `BR-01` | **Status Siswa Aktif** | Pengajuan surat hanya dapat diproses apabila siswa pemohon tercatat aktif pada tahun pelajaran berjalan dan tidak sedang dalam masa skorsing administrasi. |
| `BR-02` | **Format Penomoran Surat Dinas** | Nomor surat wajib tersusun berurutan dengan format: `[Klasifikasi_Surat]/[Nomor_Urut]/[Kode_Sekolah]/[Bulan_Romawi]/[Tahun]`, contoh: `421.3/089/SMK-PSKD3/IX/2026`. Nomor urut di-reset setiap pergantian tahun takwim. |
| `BR-03` | **Standar Waktu Layanan (SLA)** | Petugas Tata Usaha wajib memproses (memverifikasi atau menolak dengan alasan) berkas permohonan siswa maksimal dalam rentang waktu **2 x 24 jam kerja** sejak tanggal pengajuan masuk ke sistem. |
| `BR-04` | **Validasi Keaslian Dokumen Digital** | Surat digital dinyatakan sah dan legal oleh pihak sekolah jika kode QR pada dokumen berhasil dipindai dan mengarah ke domain resmi sekolah yang menampilkan metadata verifikasi status surat (Nama Siswa, Tanggal Terbit, Nomor Surat Resmi, dan Nama Petugas TU Pengesah). |
| `BR-05` | **Kebijakan Revisi Berkas** | Siswa yang pengajuannya ditolak diberi kesempatan memperbaiki unggahan berkas maksimal **3 kali per nomor pengajuan**. Jika melewati batas, siswa wajib membuat pengajuan baru. |

---

## 6. LAMPIRAN

### 6.1 Lampiran A: Glosarium Istilah

| Istilah / Singkatan | Definisi Lengkap |
|:---|:---|
| **SRS** | *Software Requirements Specification* — Dokumen spesifikasi formal yang menjelaskan seluruh kebutuhan dan perilaku dari sistem perangkat lunak yang akan dibangun. |
| **IEEE** | *Institute of Electrical and Electronics Engineers* — Organisasi internasional pengembang standar teknologi informasi, termasuk standar IEEE 830 untuk dokumen kebutuhan perangkat lunak. |
| **SIPESAT** | *Sistem Informasi Pengajuan Surat Siswa* — Nama produk perangkat lunak berbasis web yang dikembangkan pada proyek ini. |
| **RBAC** | *Role-Based Access Control* — Mekanisme pembatasan akses sistem berdasarkan peran/jabatan pengguna tertentu (2 Role Eksklusif: Siswa dan Petugas TU / Admin). |
| **NISN** | *Nomor Induk Siswa Nasional* — Kode pengenal identitas siswa yang bersifat unik, standar, dan berlaku sepanjang masa di seluruh sekolah Indonesia. |
| **TU** | *Tata Usaha* — Unit kerja staf kependidikan di sekolah yang bertugas melayani urusan administrasi, korespondensi, verifikasi, dan pengarsipan surat. |
| **SLA** | *Service Level Agreement* — Komitmen standar batas waktu penyelesaian suatu layanan operasional (dalam hal ini pemrosesan surat maksimal 2x24 jam). |
| **QR Code** | *Quick Response Code* — Kode batang matriks dua dimensi yang menyimpan URL verifikasi keaslian dokumen digital secara instan via kamera ponsel. |
| **ORM** | *Object-Relational Mapping* — Teknik pemrograman untuk memetakan struktur tabel basis data relasional ke dalam objek kode program (menggunakan Prisma ORM). |

---

### 6.2 Lampiran B: Diagram Use Case Sistem (2 Role Eksklusif)

Aktor dan hak akses fungsi sistem SIPESAT dipetakan ke dalam 2 peran utama sebagai berikut:

```
                  +----------------------------------------------------+
                  |       SIPESAT (Sistem Pengajuan Surat Siswa)       |
                  +----------------------------------------------------+
                                            │
   ( Siswa ) ─────┬───> [ Melakukan Registrasi & Login Akun ] <───┬─── ( Petugas TU / Admin )
                  │                                               │
                  ├───> [ Melihat Katalog Jenis Surat ]           ├───> [ Mengelola Master Siswa & Surat ]
                  │                                               │
                  ├───> [ Mengisi Form & Mengunggah Syarat ]      ├───> [ Memeriksa Antrean & Berkas Masuk ]
                  │                                               │
                  ├───> [ Memantau Pelacakan Status (Tracking) ]  ├───> [ Menyetujui (Approve) & Generate QR ]
                  │                                               │
                  └───> [ Mengunduh Salinan Surat PDF ]           ├───> [ Menolak (Reject) & Input Revisi ]
                                                                  │
                                                                  ├───> [ Mencetak Fisik Surat & Laporan ]
                                                                  │
                                                                  └───> [ Melihat Dashboard & Statistik ]
```

---
*Dokumen ini disusun dan disahkan oleh Kelompok RPL 7 untuk memenuhi syarat penilaian TUGAS 2 Mata Kuliah Rekayasa Perangkat Lunak, Program Studi Teknik Informatika, FTIK Universitas Indraprasta PGRI (UNINDRA) Tahun Akademik 2026/2027.*
