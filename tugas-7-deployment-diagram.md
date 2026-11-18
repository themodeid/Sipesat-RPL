# TUGAS REKAYASA PERANGKAT LUNAK (RPL)
**PERANCANGAN DEPLOYMENT DIAGRAM ARSITEKTUR FISIK DAN INFRASTRUKTUR SISTEM**  
**PROGRAM STUDI TEKNIK INFORMATIKA - FTIK UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)**  
**TAHUN AKADEMIK 2026/2027**

---

### IDENTITAS KELOMPOK (KELOMPOK RPL 7 / KELAS RPL_XD)
1. **Adam Wahyu Kurniawan** (NPM: `202343500510`) - *Lead System Architect & Software Engineer*
2. **Fathu Rahman** (NPM: `202343500467`) - *Business Analyst & Requirements Engineer*
3. **Surya Edi Saputra** (NPM: `202343500468`) - *Quality Assurance & Technical Writer*
4. **Rizqi Muh. Al Hakimi** (NPM: `202343500449`) - *Database Specialist & UI/UX*

* **Nama Proyek Perangkat Lunak:**  
  *Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)*
* **Studi Kasus:**  
  Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah Menengah
* **Landasan Acuan Desain Sebelumnya:**  
  * Dokumen Spesifikasi Kebutuhan Perangkat Lunak (SRS) Standar IEEE Std 830-1998 (Tugas 2)
  * Pemodelan Use Case Diagram & Matriks Hak Akses RBAC (Tugas 3)
  * Pemodelan Activity Diagram & Sequence Diagram Standar UML 2.5 (Tugas 4)
  * Pemodelan State Machine Diagram Siklus Hidup Permohonan Surat (Tugas 5)
  * Pemodelan Class Diagram & Object Diagram (Tugas 6)
  * Konstruksi & Implementasi Fullstack Decoupled (Tugas 10)
  * Pengujian Perangkat Lunak Black Box Testing 35 Test Cases (Tugas 11)

---

## BAB I: PENDAHULUAN & LANDASAN TEORI

### 1.1 Gambaran Umum Proyek SIPESAT
Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) adalah platform layanan digital mandiri yang dirancang untuk mengotomatisasi birokrasi persuratan siswa di sekolah menengah (Surat Keterangan Siswa Aktif, Rekomendasi Beasiswa, Legalisir Ijazah, dan Dispensasi). Sistem ini mengadopsi arsitektur terpisah (*Decoupled Architecture*) antara antarmuka web (Frontend), layanan logika bisnis (Backend REST API), dan penyimpanan data terisolasi (PostgreSQL Database).

Untuk memastikan sistem dapat dioperasikan secara stabil, aman, dan berkesinambungan di lingkungan produksi nyata, diperlukan pemodelan arsitektur infrastruktur fisik dan virtual melalui **Deployment Diagram**.

### 1.2 Konsep Dasar Deployment Diagram (UML 2.5)
Deployment Diagram adalah salah satu diagram struktural dalam Unified Modeling Language (UML) 2.5 yang memetakan bagaimana artefak-artefak perangkat lunak (*software artifacts*) didistribusikan dan dieksekusi di atas simpul-simpul komputasi fisik maupun lingkungan eksekusi virtual (*hardware nodes and execution environments*).

Elemen-elemen formal penyusun Deployment Diagram:
1. **Node (`<<device>>`)**: Representasi perangkat keras komputasi fisik (seperti PC Klien, Server Fisik, atau Virtual Machine) yang memiliki memori dan kapasitas pemrosesan.
2. **Execution Environment (`<<executionEnvironment>>`)**: Lingkungan perangkat lunak sistem yang berjalan di dalam simpul fisik dan menyediakan konteks eksekusi langsung bagi aplikasi (contoh: Node.js Runtime, Web Browser Engine, Docker Engine).
3. **Artifact (`<<artifact>>`)**: Berkas fisik konkret hasil kompilasi atau pengembangan perangkat lunak (seperti file biner executable, bundle JavaScript, skema database, atau direktori penyimpanan) yang dideploy ke dalam simpul.
4. **Component (`<<component>>`)**: Unit modular perangkat lunak yang membungkus logika fungsional tertentu di dalam runtime.
5. **Communication Path (`<<protocol>>`)**: Jalur komunikasi jaringan yang menghubungkan dua simpul fisik menggunakan protokol tertentu (misal: HTTP/HTTPS, TCP/IP, WebSocket) lengkap dengan nomor port jaringan.

---

## BAB II: PERANCANGAN ARSITEKTUR FISIK 3-TIER SIPESAT

Arsitektur deployment sistem SIPESAT dibagi ke dalam 3 Tingkatan Komputasi (*Three-Tier Architecture*):

```text
+-----------------------+         HTTP/HTTPS (Port 3000)         +---------------------------------------+
|      CLIENT TIER      | <====================================> |       APPLICATION & WEB SERVER        |
|  (PC / Laptop / HP)   |                                        |  - Next.js 14 Web Server (Port 3000)  |
|  - Web Browser Engine |         REST API JSON (Port 5000)      |  - Express REST API (Port 5000)       |
+-----------------------+ <====================================> +---------------------------------------+
                                                                                     ||
                                                                                     || TCP/IP (Port 5432)
                                                                                     \/
                                                                 +---------------------------------------+
                                                                 |         DATA & STORAGE TIER           |
                                                                 |  - Docker Container Engine            |
                                                                 |  - PostgreSQL 16 Alpine (Port 5432)   |
                                                                 |  - Persistent Named Volume Storage    |
                                                                 +---------------------------------------+
```

1. **Client Tier (Presentation Client)**:
   * Menampung perangkat fisik pengguna (komputer desktop, laptop TU, atau smartphone siswa).
   * Menjalankan browser web modern (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari) yang merender kode HTML5, CSS3, dan mengeksekusi JavaScript React Client Components.
2. **Application & Service Tier (Logic & Server-Side Rendering)**:
   * **Web Server Next.js 14 (Port 3000)**: Menangani perutean sisi server (*Server-Side Rendering & App Router*), optimasi gambar, dan rendering antarmuka pengguna berbasis Tailwind CSS.
   * **API Gateway & Controller Express.js (Port 5000)**: Menjalankan logika bisnis inti, verifikasi otorisasi Role-Based Access Control (RBAC) via JSON Web Token (JWT), penanganan unggah berkas fisik via Multer (maksimal 2 MB), engine penomoran surat otomatis, serta pembuatan tanda tangan digital QR Code dan file PDF resmi via PDFKit.
3. **Data & Storage Tier (Database & File System)**:
   * Menggunakan containerisasi **Docker Engine** untuk menjalankan **PostgreSQL 16 Alpine** pada port 5432.
   * Dilengkapi dua volume penyimpanan terpisah:
     * `sipesat_postgres_data`: Volume persisten Docker untuk menyimpan basis data relasional (tabel pengguna, siswa, pengajuan, riwayat status).
     * `be/uploads/`: Direktori file lokal server untuk menyimpan berkas persyaratan siswa (PDF, JPG, PNG) dan arsip surat resmi digital yang diterbitkan.

---

## BAB III: VISUALISASI UML DEPLOYMENT DIAGRAM (UML 2.5)

Berikut adalah pemodelan visual Deployment Diagram lengkap sistem SIPESAT menggunakan notasi standar UML 2.5:

```mermaid
flowchart TB
    subgraph ClientDevice ["«device» Client Tier: User Device (PC / Smartphone)"]
        subgraph BrowserEnv ["«executionEnvironment» Web Browser Engine"]
            ClientArtifact["«artifact» SIPESAT Web Application<br/>(HTML5 / CSS3 / React Virtual DOM)<br/>• Client JWT Token Storage<br/>• File Upload Input (Limit 2MB)<br/>• Real-Time Stepper UI Tracking<br/>• PDF Download & Viewer Component"]
            UserActors["«actor / role»<br/>1. Siswa (Pemohon Surat)<br/>2. Petugas TU (Verifikator & Pengesah)"]
        end
    end

    subgraph AppServer ["«device / executionServer» Application & Service Host"]
        subgraph NextJSRuntime ["«executionEnvironment» Next.js 14 Web Server (Port: 3000)"]
            NextArtifact["«artifact» fe/.next (Compiled App Router)<br/>• Server-Side Rendering (SSR)<br/>• API Client Proxy Helper (/lib/api.ts)<br/>• Role Guard Protected Routes"]
        end

        subgraph ExpressRuntime ["«executionEnvironment» Express REST API Server (Port: 5000)"]
            AuthCmp["«component» AuthMiddleware (JWT Guard)"]
            PengajuanCmp["«component» PengajuanController (CRUD & State)"]
            SuratCmp["«component» SuratGenerator (Auto-Number & QR TTE)"]
            MulterCmp["«component» Multer FileHandler (MIME & 2MB Check)"]
            PrismaCmp["«component» Prisma Client ORM (Pool & Transactions)"]
        end
    end

    subgraph DataServer ["«device / virtualizationHost» Data & Storage Tier (Docker Engine)"]
        subgraph PostgresContainer ["«container» sipesat-postgres-1"]
            subgraph PostgresDBMS ["«database» PostgreSQL 16 Alpine (Port: 5432)"]
                DBTables["«database schema» sipesat_db (3NF)<br/>• tb_user (Akun & Role RBAC)<br/>• tb_siswa (Profil & Kelas)<br/>• tb_petugas (Staf Tata Usaha)<br/>• tb_jenis_surat (Katalog Layanan)<br/>• tb_pengajuan_surat (Transaksi & Nomor)<br/>• tb_berkas_persyaratan (Path & Ukuran)<br/>• tb_riwayat_status (Audit Trail)"]
            end
        end
        
        DBVolume[("«file system volume»<br/>sipesat_postgres_data<br/>(/var/lib/postgresql/data)")]
        UploadsVolume[("«file system volume»<br/>Local Uploads Directory<br/>(be/uploads/)")]
    end

    %% Communication Paths
    ClientArtifact <-->|«protocol» HTTP / HTTPS (Port 3000)<br/>UI Bundles & HTML SSR| NextArtifact
    ClientArtifact <-->|«protocol» REST API JSON (Port 5000)<br/>Bearer Token & Multipart Form| ExpressRuntime
    NextArtifact -.->|Internal Fetch / SSR Proxy (Port 5000)| ExpressRuntime
    PrismaCmp <-->|«protocol» TCP/IP Connection Pool<br/>Port 5432 (PostgreSQL Driver)| PostgresDBMS
    MulterCmp -.->|Write Uploaded Files| UploadsVolume
    SuratCmp -.->|Generate & Save PDF Surat| UploadsVolume
    PostgresDBMS -.->|Docker Volume Mount| DBVolume
```

---

## BAB IV: SPESIFIKASI NODE DAN ARTEFAK SISTEM

### 4.1 Tabel Spesifikasi Simpul Perangkat Keras & Lingkungan Eksekusi

| Simpul (Node) | Tipe Simpul | Lingkungan Eksekusi | Peran & Tanggung Jawab Komputasi |
| :--- | :---: | :--- | :--- |
| **Client Device** | `<<device>>` | Google Chrome $\ge$ 110, Edge, Safari | Menjalankan antarmuka grafis, menangani interaksi pengguna, validasi input sisi klien, dan penyimpanan token sesi JWT. |
| **Web Server Host** | `<<device>>` | Node.js Runtime v18/v20 (Next.js 14) | Menyajikan aset web statis dan dinamis, Server-Side Rendering (SSR), dan perutean halaman klien. |
| **API Server Host** | `<<device>>` | Node.js Runtime v18/v20 (Express + TS) | Mengeksekusi logika bisnis, otorisasi RBAC, sanitasi payload, generator dokumen PDF resmi ber-QR Code, dan penomoran otomatis. |
| **Container Engine** | `<<device>>` | Docker Desktop / Docker Engine 24+ | Mengisolasi runtime basis data PostgreSQL di dalam container terdedikasi anti-konflik dependensi OS. |
| **Database Server** | `<<container>>` | PostgreSQL 16 Alpine Linux | Menyimpan seluruh entitas data transaksional, menjamin integritas Foreign Key, dan eksekusi transaksi ACID. |

### 4.2 Tabel Spesifikasi Artefak & Komponen Perangkat Lunak

| Artefak / Komponen | Simpul Penempatan | Format Berkas / Runtime | Deskripsi Fungsi |
| :--- | :--- | :--- | :--- |
| **`sipesat-fe-bundle`** | Client Browser & Web Server | JavaScript / React Virtual DOM | Komponen antarmuka pengguna, form input pengajuan surat, stepper status, dan tabel administrasi TU. |
| **`AuthMiddleware`** | Express API Server | TypeScript (`auth.ts`) | Memverifikasi tanda tangan digital JWT, mengekstraksi identitas pengguna, dan memblokir akses rute ilegal. |
| **`PengajuanController`** | Express API Server | TypeScript (`pengajuan.ts`) | Mengelola alur hidup permohonan surat (DRAFT $\rightarrow$ DIAJUKAN $\rightarrow$ DIPROSES $\rightarrow$ DISETUJUI / DITOLAK). |
| **`SuratGenerator`** | Express API Server | TypeScript (`surat.ts` + PDFKit) | Menghasilkan nomor surat berformat resmi dan menggambar QR Code verifikasi ke dalam dokumen PDF. |
| **`MulterFileHandler`** | Express API Server | Middleware (`multer.ts`) | Menyaring tipe MIME berkas (PDF/JPG/PNG), membatasi ukuran maksimal 2 MB, dan memberi nama unik berbasis UUID. |
| **`PrismaClient`** | Express API Server | ORM Client Engine | Mengelola koneksi database pooling dan menerjemahkan query TypeScript ke dalam native SQL PostgreSQL. |
| **`sipesat_db`** | PostgreSQL Container | Relational Database 3NF | 7 tabel relasional master-detail penyimpan data pengguna, siswa, jenis surat, pengajuan, dan audit status. |

---

## BAB V: PROTOKOL KOMUNIKASI DAN KEAMANAN JARINGAN

1. **Jalur Komunikasi Klien ke Web Server (`HTTP / HTTPS - Port 3000`)**:
   * Menyalurkan kode biner antarmuka (HTML, CSS, chunk JS Next.js) ke browser klien.
   * Komunikasi dienkripsi menggunakan protokol TLS/HTTPS pada lingkungan produksi untuk mencegah serangan *Man-in-the-Middle* (MitM).
2. **Jalur Komunikasi Klien ke API Backend (`REST API JSON - Port 5000`)**:
   * Seluruh pertukaran data fungsional dikirimkan dalam format payload standar `application/json`.
   * Otentikasi stateless ditegakkan melalui header `Authorization: Bearer <JWT_TOKEN>`.
   * Pengiriman berkas persyaratan menggunakan encoding `multipart/form-data` dengan perlindungan kuota maksimal 2 MB per berkas.
3. **Jalur Komunikasi Backend ke Database (`TCP/IP - Port 5432`)**:
   * Komunikasi antara Express API dan container PostgreSQL dilakukan melalui koneksi jaringan internal bridge Docker (*sipesat-network*) atau localhost loopback pada port 5432.
   * Dilindungi oleh kredensial koneksi terenkripsi pada environment variable (`DATABASE_URL=postgresql://user:pass@host:5432/sipesat_db`), menjamin kredensial tidak pernah bocor ke kode sumber publik.

---

## BAB VI: KESIMPULAN

Pemodelan Deployment Diagram pada sistem SIPESAT mendokumentasikan secara presisi pemisahan tanggung jawab antarlapisan (*separation of concerns*). Melalui pendekatan *Decoupled 3-Tier Architecture* yang didukung isolasi container Docker, sistem SIPESAT memiliki keunggulan:
1. **Skalabilitas**: Lapisan antarmuka pengguna (Next.js) dan lapisan layanan API (Express) dapat diskalakan secara independen sesuai beban lalu lintas pengajuan surat.
2. **Keandalan & Isolasi Data**: Basis data PostgreSQL dan volume berkas fisik terisolasi dari gangguan eksternal, memastikan dokumen resmi siswa tersimpan secara aman dan persisten.
3. **Portabilitas**: Seluruh tumpukan teknologi dapat dijalankan dengan mudah pada lingkungan pengembangan lokal (via `docker compose` dan `start-local.bat`) maupun di-deploy ke Virtual Private Server (VPS) produksi tanpa perubahan arsitektur.
