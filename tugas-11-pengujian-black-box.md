# TUGAS 11 - REKAYASA PERANGKAT LUNAK (RPL)
**PENGUJIAN PERANGKAT LUNAK (BLACK BOX TESTING) PADA SISTEM INFORMASI PENGAJUAN SURAT SISWA BERBASIS WEB (SIPESAT)**  
**PROGRAM STUDI TEKNIK INFORMATIKA - FTIK UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)**  
**TAHUN AKADEMIK 2026/2027**

---

### IDENTITAS KELOMPOK (KELOMPOK RPL 7 / KELAS RPL_XD)
1. **Adam Wahyu Kurniawan** (NPM: 202343500510) - *Lead System Architect & Software Engineer*
2. **Fathu Rahman** (NPM: 202343500467) - *Business Analyst & Requirements Engineer*
3. **Surya Edi Saputra** (NPM: 202343500468) - *Quality Assurance & Testing Specialist*
4. **Rizqi Muh. Al Hakimi** (NPM: 202343500449) - *Database Specialist & UI/UX*

* **Nama Proyek Perangkat Lunak:**  
  *Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)*
* **Studi Kasus:**  
  Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah Menengah
* **Tech Stack:**  
  Next.js 14 (App Router), TypeScript, Tailwind CSS, Express.js REST API, Prisma ORM, PostgreSQL (Docker).
* **Repositori GitHub Resmi:**  
  [`https://github.com/themodeid/Sipesat-RPL`](https://github.com/themodeid/Sipesat-RPL)

---

## BAB I: PENDAHULUAN & METODOLOGI PENGUJIAN

### 1.1 Latar Belakang & Posisi Pengujian dalam SDLC
Pengujian Perangkat Lunak (*Software Testing*) merupakan tahap verifikasi dan validasi kritis dalam siklus hidup rekayasa perangkat lunak (*Software Development Life Cycle* - SDLC). Tahap ini bertujuan menjamin bahwa sistem yang telah dibangun pada tahap Konstruksi (Tugas 10) benar-benar beroperasi sesuai dengan spesifikasi kebutuhan fungsional yang tertuang dalam dokumen SRS (Tugas 2) serta mematuhi alur bisnis pada diagram UML (Tugas 3 s.d. 6).

Pada sistem **SIPESAT (Sistem Informasi Pengajuan Surat Siswa Berbasis Web)**, pengujian difokuskan untuk memastikan bahwa alur birokrasi persuratan—mulai dari permohonan surat oleh siswa, validasi kelayakan dokumen, verifikasi dan disposisi oleh Petugas Tata Usaha (TU), hingga penomoran otomatis dan penerbitan dokumen digital PDF ber-QR Code—berjalan secara presisi, deterministik, dan kebal dari celah validasi (*input boundary errors*) maupun kebocoran otorisasi (*unauthorized privilege escalation*).

### 1.2 Metodologi Black Box Testing
Metodologi pengujian yang digunakan adalah **Black Box Testing (Pengujian Kotak Hitam)**. Pendekatan ini berfokus pada pengujian fungsionalitas eksternal perangkat lunak tanpa memeriksa struktur kode internal secara langsung. Teknik yang diterapkan mencakup:
1. **Equivalence Partitioning (EP)**: Membagi rentang masukan data menjadi partisi valid dan tidak valid untuk menguji respons sistem terhadap masukan yang sah dan masukan yang menyimpang.
2. **Boundary Value Analysis (BVA)**: Menguji nilai batas ekstrem pada form input (misalnya ukuran berkas unggahan maksimal 2 MB, batas minimal dan maksimal karakter alasan permohonan).
3. **Role-Based Access Control (RBAC) Testing**: Memastikan pemisahan ketat hak akses antara peran Siswa dan peran Petugas TU.

### 1.3 Lingkungan Pengujian (Testing Environment)
* **Perangkat Keras (Hardware)**: Processor Intel Core i5 / AMD Ryzen 5, RAM 16 GB DDR4, SSD NVMe 512 GB.
* **Sistem Operasi**: Windows 11 Pro 64-bit / Linux Ubuntu 22.04 LTS.
* **Peramban Web (Browser)**: Google Chrome Version 128+ & Microsoft Edge.
* **Database & Server**: PostgreSQL 16 (Docker Container Port 5432), Node.js v20 LTS, Express Backend Server (Port 5000), Next.js Frontend Server (Port 3000).
* **Akun Uji (Test Credentials)**:
  * Akun Siswa: Username `siswa_adam` | Password `siswa123` (Hak akses: Pengajuan & Pelacakan).
  * Akun Petugas TU (Admin): Username `admin` | Password `admin` (Hak akses: Verifikasi, Disposisi, Cetak PDF, & Master Data).

---

## BAB II: TABEL MATRIKS PENGUJIAN SISTEM SIPESAT (BLACK BOX TESTING)

Pengujian dilakukan secara menyeluruh terhadap 7 modul fungsional utama sistem SIPESAT dengan format tabel standar akademik resmi UNINDRA:
* **No**: Nomor urut pengujian.
* **Skenario Pengujian**: Tindakan operasional yang dieksekusi pengguna pada antarmuka.
* **Test Case**: Masukan data spesifik (*input payload*) yang diberikan ke sistem.
* **Hasil yang Diharapkan**: Respon semantik dan perilaku sistem yang disyaratkan dalam spesifikasi desain.
* **Hasil Pengujian**: Perilaku faktual sistem saat pengujian berlangsung.
* **Kesimpulan**: Status kelayakan pengujian (**Valid** bila sesuai harapan, **Invalid** bila terjadi deviasi/kegagalan).

---

### 2.1 Modul 1: Autentikasi, Login, & Hak Akses Multi-Role

| No | Skenario Pengujian | Test Case | Hasil yang Diharapkan | Hasil Pengujian | Kesimpulan |
|:---:|:---|:---|:---|:---:|:---:|
| 1 | Username dan Password tidak diisi kemudian klik tombol Login | Username: (kosong)<br>Password: (kosong) | Sistem menolak akses dan menampilkan pesan validasi *"Harap isi username dan password"* | Sesuai harapan | **Valid** |
| 2 | Mengetikkan Username, dan password tidak diisi atau kosong kemudian klik tombol Login | Username: admin<br>Password: (kosong) | Sistem menolak akses dan menampilkan pesan validasi *"Password belum diisi"* | Sesuai harapan | **Valid** |
| 3 | Mengetikkan Password, dan username tidak diisi atau kosong kemudian klik tombol Login | Username: (kosong)<br>Password: admin | Sistem menolak akses dan menampilkan pesan validasi *"Username belum diisi"* | Sesuai harapan | **Valid** |
| 4 | Mengetikkan Username dan/atau password tidak sesuai, kemudian klik tombol Login | Username: adm<br>Password: adm123 | Sistem menolak akses dan menampilkan pesan *"Username atau Password yang anda masukkan salah"* | Sesuai harapan | **Valid** |
| 5 | Mengetikkan Username dan password benar akun Petugas TU, kemudian klik tombol Login | Username: admin<br>Password: admin | Sistem menerima autentikasi dan mengarahkan pengguna ke Dashboard Utama Petugas TU (`/admin/dashboard`) | Sesuai harapan | **Valid** |
| 6 | Mengetikkan Username dan password benar akun Siswa, kemudian klik tombol Login | Username: siswa_adam<br>Password: siswa123 | Sistem menerima autentikasi dan mengarahkan pengguna ke Portal Layanan Mandiri Siswa (`/siswa/pengajuan`) | Sesuai harapan | **Valid** |
| 7 | Mengklik tombol Logout dari sesi aktif pengguna | Sesi aktif: Petugas TU / Siswa<br>Aksi: Klik *"Logout"* | Sistem memusnahkan sesi token JWT di local storage dan mengembalikan pengguna ke halaman Login (`/login`) | Sesuai harapan | **Valid** |

---

### 2.2 Modul 2: Formulir Pengajuan Surat Mandiri Siswa

| No | Skenario Pengujian | Test Case | Hasil yang Diharapkan | Hasil Pengujian | Kesimpulan |
|:---:|:---|:---|:---|:---:|:---:|
| 8 | Mengirim formulir pengajuan surat tanpa memilih jenis surat | Jenis Surat: (Belum dipilih)<br>Keperluan: Lomba Sains<br>File: berkas.pdf | Sistem menolak submit formulir dan menampilkan peringatan *"Pilih jenis surat yang diajukan"* | Sesuai harapan | **Valid** |
| 9 | Mengisi formulir dengan kolom keperluan kosong | Jenis Surat: Surat Keterangan Siswa Aktif<br>Keperluan: (kosong)<br>File: berkas.pdf | Sistem menolak submit formulir dan menampilkan peringatan *"Alasan/keperluan permohonan wajib diisi"* | Sesuai harapan | **Valid** |
| 10 | Mengunggah berkas persyaratan dengan ukuran melebihi batas (Ukuran $> 2\text{ MB}$) | File: scan_rapor_besar.pdf (Ukuran 4,5 MB) | Sistem memblokir unggahan file di sisi frontend & backend dengan notifikasi *"Ukuran file maksimal 2 MB"* | Sesuai harapan | **Valid** |
| 11 | Mengunggah berkas persyaratan dengan format terlarang (.exe, .php, .sh) | File: script_jahat.exe (Ukuran 500 KB) | Sistem menolak file dan menampilkan peringatan *"Format file tidak diizinkan. Hanya menerima PDF, JPG, atau PNG"* | Sesuai harapan | **Valid** |
| 12 | Mengisi seluruh formulir pengajuan dengan data lengkap dan berkas valid (PDF $< 2\text{ MB}$) | Jenis Surat: Surat Keterangan Aktif<br>Keperluan: Pengurusan Beasiswa<br>File: kartu_pelajar.pdf (850 KB) | Sistem berhasil menyimpan permohonan, menerbitkan Nomor Pengajuan unik (`REG-2026-XXXX`), dan status awal disetel ke *"Menunggu Verifikasi"* | Sesuai harapan | **Valid** |

---

### 2.3 Modul 3: Pelacakan Status Pengajuan Surat (Tracking & Timeline Stepper)

| No | Skenario Pengujian | Test Case | Hasil yang Diharapkan | Hasil Pengujian | Kesimpulan |
|:---:|:---|:---|:---|:---:|:---:|
| 13 | Melakukan pencarian status surat dengan kolom nomor pengajuan kosong | Nomor Pengajuan: (kosong)<br>Aksi: Klik *"Lacak"* | Sistem menampilkan peringatan *"Masukkan nomor registrasi pengajuan surat"* | Sesuai harapan | **Valid** |
| 14 | Melacak status dengan nomor pengajuan yang tidak terdaftar di database | Nomor Pengajuan: `REG-9999-XXXX` (Fiktif) | Sistem menampilkan informasi *"Nomor registrasi pengajuan tidak ditemukan. Periksa kembali nomor tiket Anda"* | Sesuai harapan | **Valid** |
| 15 | Melacak status surat yang valid dan berstatus *"Menunggu Verifikasi"* | Nomor Pengajuan: `REG-2026-0001`<br>Status: Menunggu | Sistem menampilkan data pemohon dan indikator stepper aktif pada tahap 1: *"Menunggu Verifikasi Berkas oleh TU"* | Sesuai harapan | **Valid** |
| 16 | Melacak status surat yang berstatus *"Ditolak"* lengkap dengan catatan revisi | Nomor Pengajuan: `REG-2026-0002`<br>Status: Ditolak | Sistem menampilkan banner merah *"Pengajuan Ditolak"* beserta alasan penolakan: *"Kartu Keluarga buram, mohon upload ulang"* | Sesuai harapan | **Valid** |
| 17 | Melacak status surat yang berstatus *"Selesai"* | Nomor Pengajuan: `REG-2026-0003`<br>Status: Selesai | Sistem menampilkan stepper hijau penuh dan memunculkan tombol *"Unduh Surat Resmi (PDF)"* | Sesuai harapan | **Valid** |

---

### 2.4 Modul 4: Verifikasi & Disposisi Berkas oleh Petugas TU

| No | Skenario Pengujian | Test Case | Hasil yang Diharapkan | Hasil Pengujian | Kesimpulan |
|:---:|:---|:---|:---|:---:|:---:|
| 18 | Petugas TU membuka menu inbox permohonan surat masuk | Akun: Petugas TU<br>Menu: Inbox Pengajuan | Sistem memuat tabel daftar permohonan surat masuk secara real-time dengan status terkini dan badge prioritas | Sesuai harapan | **Valid** |
| 19 | Petugas TU mengklik preview berkas persyaratan siswa | Aksi: Klik ikon *"Lihat Berkas"* pada permohonan siswa | Sistem membuka modal pratinjau dokumen PDF/gambar secara aman tanpa merusak halaman antarmuka utama | Sesuai harapan | **Valid** |
| 20 | Petugas TU menolak permohonan tanpa mengisi alasan/catatan penolakan | Status: Tolak Pengajuan<br>Catatan Alasan: (kosong) | Sistem menolak aksi penolakan dan mewajibkan petugas mengisi catatan: *"Catatan penolakan wajib diisi agar siswa dapat memperbaiki berkas"* | Sesuai harapan | **Valid** |
| 21 | Petugas TU menolak permohonan dengan mengisi catatan alasan penolakan sah | Status: Tolak Pengajuan<br>Catatan: *"Foto copy rapor semester ganjil belum dilegalisir"* | Sistem memperbarui status permohonan menjadi *"Ditolak"*, menyimpan log audit, dan mengirimkan catatan ke pelacakan siswa | Sesuai harapan | **Valid** |
| 22 | Petugas TU menyetujui permohonan surat yang berkasnya telah memenuhi syarat | Status: Setujui Pengajuan<br>Aksi: Klik *"Verifikasi & Terbitkan"* | Sistem memperbarui status permohonan menjadi *"Disetujui"*, memicu engine penomoran surat otomatis, dan status siap cetak | Sesuai harapan | **Valid** |

---

### 2.5 Modul 5: Penomoran Otomatis & Penerbitan Surat Digital PDF ber-QR Code

| No | Skenario Pengujian | Test Case | Hasil yang Diharapkan | Hasil Pengujian | Kesimpulan |
|:---:|:---|:---|:---|:---:|:---:|
| 23 | Pengujian pembentukan nomor urut surat resmi otomatis | Input: Pengajuan disetujui bulan November 2026 urutan ke-5 | Sistem membentuk format nomor surat resmi secara dinamis: `005/SMK-PSKD/XI/2026` sesuai template jenis surat | Sesuai harapan | **Valid** |
| 24 | Pengujian konsistensi bulan romawi pada nomor surat | Input: Eksekusi transaksi pada bulan November (Index 10) | Sistem mengonversi indeks bulan secara tepat menjadi angka romawi `"XI"` tanpa kekeliruan offset kalender | Sesuai harapan | **Valid** |
| 25 | Pengujian pembentukan Tanda Tangan Digital QR Code verifikasi | Input: ID Pengajuan `SURAT-2026-005` | Sistem menghasilkan QR Code SVG/PNG yang memuat tautan verifikasi otentikasi dokumen publik sekolah | Sesuai harapan | **Valid** |
| 26 | Siswa atau Petugas TU mengunduh file surat digital resmi (PDF) | Aksi: Klik tombol *"Unduh Surat PDF"* pada pengajuan selesai | Sistem mengunduh berkas PDF A4 resmi lengkap dengan kop surat sekolah, nomor surat, identitas siswa, isi surat, stempel, dan QR Code | Sesuai harapan | **Valid** |
| 27 | Memindai (*scan*) QR Code pada surat PDF menggunakan kamera smartphone | Alat: Kamera HP / Pemindai QR<br>Target: QR Code di surat PDF | Pemindai mengarahkan ke halaman verifikasi resmi web SIPESAT dan menyatakan: *"Dokumen Asli Diterbitkan oleh Tata Usaha Sekolah"* | Sesuai harapan | **Valid** |

---

### 2.6 Modul 6: Manajemen Data Master Persuratan & Laporan Rekapitulasi

| No | Skenario Pengujian | Test Case | Hasil yang Diharapkan | Hasil Pengujian | Kesimpulan |
|:---:|:---|:---|:---|:---:|:---:|
| 28 | Petugas TU menambahkan jenis surat baru ke sistem | Nama Surat: Surat Izin Observasi<br>Format: `{NOMOR}/OBS/SMK/{BULAN_ROMAWI}/{TAHUN}` | Sistem menyimpan jenis surat baru ke database dan langsung muncul pada pilihan formulir permohonan siswa | Sesuai harapan | **Valid** |
| 29 | Petugas TU menonaktifkan jenis surat lama (Soft Deactivation) | Aksi: Ubah status jenis surat menjadi *"Nonaktif"* | Siswa tidak lagi dapat memilih jenis surat tersebut di formulir baru, namun riwayat pengajuan lama tetap terpelihara | Sesuai harapan | **Valid** |
| 30 | Petugas TU menyaring laporan permohonan berdasarkan rentang tanggal | Filter: Tanggal 01 Nov 2026 s.d. 30 Nov 2026 | Sistem menyaring dan hanya menampilkan data transaksi permohonan yang dibuat dalam rentang November 2026 | Sesuai harapan | **Valid** |
| 31 | Petugas TU mengekspor laporan rekapitulasi persuratan | Aksi: Klik tombol *"Ekspor Laporan (Excel / CSV)"* | Sistem mengunduh berkas rekapitulasi berisi data pemohon, jenis surat, tanggal pengajuan, tanggal terbit, dan status akhir | Sesuai harapan | **Valid** |

---

### 2.7 Modul 7: Pengujian Keamanan & Hak Akses (Security & Route Protection)

| No | Skenario Pengujian | Test Case | Hasil yang Diharapkan | Hasil Pengujian | Kesimpulan |
|:---:|:---|:---|:---|:---:|:---:|
| 32 | Siswa mencoba mengakses paksa URL khusus Petugas TU tanpa izin | Role: Siswa<br>Aksi: Buka URL `/admin/dashboard` langsung di address bar | Sistem menolak akses via middleware RBAC, menampilkan peringatan *"Akses Terlarang (403 Forbidden)"*, dan mengembalikan ke `/siswa` | Sesuai harapan | **Valid** |
| 33 | Pengguna anonim mencoba mengakses endpoint API private tanpa token JWT | Request: `GET /api/admin/pengajuan`<br>Header: (Tanpa Authorization Bearer) | Backend Express menolak request dengan respons `HTTP 401 Unauthorized` (*"Token autentikasi tidak ditemukan"*) | Sesuai harapan | **Valid** |
| 34 | Siswa mencoba mengunduh surat milik siswa lain dengan mengubah ID di URL | Akun: Siswa A<br>Aksi: Akses URL unduh surat milik Siswa B | Sistem memvalidasi kepemilikan data (*Data Isolation*) dan menolak aksi dengan respons `HTTP 403 Forbidden` | Sesuai harapan | **Valid** |
| 35 | Pengujian serangan Cross-Site Scripting (XSS) pada kolom teks alasan | Input Keperluan: `<script>alert('hack')</script>` | Sistem menyaring (*sanitasi*) tag HTML/JS sehingga tersimpan sebagai string teks biasa tanpa dieksekusi oleh peramban | Sesuai harapan | **Valid** |

---

## BAB III: ANALISIS HASIL PENGUJIAN & METRIK KUALITAS

### 3.1 Rekapitulasi Metrik Keberhasilan Pengujian
Berdasarkan eksekusi 35 skenario uji coba fungsionalitas kotak hitam (*Black Box Testing*) yang telah dipaparkan pada Bab II, diperoleh rekapitulasi metrik pengujian sistem SIPESAT sebagai berikut:

| Kategori Modul Pengujian | Jumlah Test Case | Sesuai Harapan (Pass) | Tidak Sesuai (Fail) | Persentase Keberhasilan |
|:---|:---:|:---:|:---:|:---:|
| Modul 1: Autentikasi & Hak Akses Multi-Role | 7 | 7 | 0 | 100% |
| Modul 2: Formulir Pengajuan Surat Mandiri Siswa | 5 | 5 | 0 | 100% |
| Modul 3: Pelacakan Status Surat (Tracking Stepper) | 5 | 5 | 0 | 100% |
| Modul 4: Verifikasi & Disposisi Petugas TU | 5 | 5 | 0 | 100% |
| Modul 5: Penomoran Otomatis & Cetak PDF QR Code | 5 | 5 | 0 | 100% |
| Modul 6: Manajemen Data Master & Laporan | 4 | 4 | 0 | 100% |
| Modul 7: Keamanan & Hak Akses (Route Guard) | 4 | 4 | 0 | 100% |
| **TOTAL KESELURUHAN** | **35** | **35** | **0** | **100% (SEMPURNA)** |

### 3.2 Analisis Kesiapan Implementasi & Kualitas Perangkat Lunak
1. **Validasi Batas Beroperasi Sempurna**: Seluruh penanganan kondisi input kosong, format berkas menyimpang, maupun batas ukuran berkas ($> 2\text{ MB}$) berhasil ditolak secara konsisten oleh sistem dengan pesan ramah pengguna.
2. **Integritas Penomoran & Tanda Tangan Digital**: Fungsi pembentukan nomor surat resmi (`generateNomorSuratResmi`) dan generator QR Code terbukti menghasilkan dokumen dinamis yang unik, tertelusur, dan bebas dari duplikasi nomor surat.
3. **Pemisahan Hak Akses Ketat (RBAC)**: Pengujian penetrasi sederhana pada rute administratif (`/admin/*`) dan isolasi kepemilikan data antar-siswa membuktikan bahwa middleware autentikasi JWT berhasil melindungi data sensitif sekolah dari akses tanpa hak.

---

## BAB IV: KESIMPULAN & TAUTAN KODE SUMBER

### 4.1 Kesimpulan
Pelaksanaan pengujian perangkat lunak sistem **SIPESAT (Sistem Informasi Pengajuan Surat Siswa Berbasis Web)** menggunakan metode *Black Box Testing* telah diselesaikan secara tuntas. Dari 35 kasus pengujian yang mencakup seluruh modul operasional siswa dan petugas tata usaha:
* **Tingkat Keberhasilan Pengujian**: **100% Valid (Pass)**.
* **Kepadatan Cacat (*Defect Density*)**: **0 Critical Bugs**.
* Sistem dinyatakan telah memenuhi seluruh spesifikasi kebutuhan perangkat lunak (SRS IEEE 830), aman dari kerentanan input dasar, serta berada dalam status **Siap Produksi (*Production Ready*)** untuk diimplementasikan di lingkungan sekolah.

### 4.2 Tautan Repositori GitHub Resmi
Sesuai arahan dosen pengampu mata kuliah Rekayasa Perangkat Lunak (RPL), seluruh kode sumber (*source code* frontend dan backend), skema database Prisma, serta naskah laporan tugas 1 sampai 11 dapat diakses secara publik dan transparan pada tautan berikut:

🌐 **Tautan Repositori GitHub SIPESAT**:  
👉 [`https://github.com/themodeid/Sipesat-RPL`](https://github.com/themodeid/Sipesat-RPL)

---

*Disusun, diuji secara empiris, dan disahkan oleh Kelompok RPL 7 (Adam Wahyu Kurniawan dkk) untuk memenuhi penilaian resmi Tugas Pertemuan 11 Mata Kuliah Rekayasa Perangkat Lunak - Universitas Indraprasta PGRI (UNINDRA).*
