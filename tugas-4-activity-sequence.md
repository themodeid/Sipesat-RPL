# TUGAS 4 - REKAYASA PERANGKAT LUNAK (RPL)
**PERANCANGAN ACTIVITY DIAGRAM DAN SEQUENCE DIAGRAM**
**PROGRAM STUDI TEKNIK INFORMATIKA - FTIK UNIVERSITAS INDRAPRASTA PGRI (UNINDRA)**
**TAHUN AKADEMIK 2026/2027**

---

### IDENTITAS KELOMPOK (KELOMPOK RPL 7)
1. **Adam Wahyu Kurniawan** - 202343500510
2. **Fathu Rahman** - 202343500467
3. **Surya Edi Saputra** - 202343500468
4. **Rizqi Muh. Al Hakimi** - 202343500449

* **Nama Proyek Perangkat Lunak:**  
  *Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT)*
* **Studi Kasus:**  
  Pelayanan Administrasi Persuratan Siswa & Tata Usaha Sekolah
* **Landasan Acuan:**  
  Dokumen Spesifikasi Kebutuhan Perangkat Lunak (SRS) Standar IEEE Std 830-1998 / Karl Wiegers (Tugas 2)

---

## BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM

### 1.1 Deskripsi Proyek SIPESAT
Sistem Informasi Pengajuan Surat Siswa Berbasis Web (SIPESAT) adalah sistem yang kami kembangkan untuk mempermudah proses pelayanan administrasi persuratan bagi siswa di lingkungan sekolah. Pada sistem sebelumnya, siswa harus datang langsung ke ruang Tata Usaha (TU) untuk meminta form kertas dan menunggu proses pembuatan surat yang memakan waktu cukup lama. Melalui SIPESAT, siswa dapat mengajukan surat kapan saja secara online, memantau posisi suratnya, dan mengunduh surat resmi yang sudah disetujui.

Sistem ini membagi hak akses ke dalam 3 (tiga) peran pengguna (aktor) utama:
1. **Siswa**: Mengajukan permohonan surat secara mandiri, melampirkan berkas persyaratan (maksimal 2 MB), memantau perkembangan status surat, serta mengunduh surat PDF yang telah disahkan.
2. **Staf Tata Usaha (TU)**: Memeriksa dan memverifikasi kelengkapan berkas yang diajukan siswa, memberikan nomor agenda surat masuk, dan meneruskan berkas yang valid ke Kepala Sekolah (atau menolaknya dengan catatan revisi jika berkas belum lengkap).
3. **Kepala Sekolah**: Memeriksa draf surat yang sudah diverifikasi TU, memberikan persetujuan (approval), dan mengesahkan surat dengan tanda tangan elektronik berbasis kode QR.

### 1.2 Tujuan Pemodelan UML
Pemodelan UML (Unified Modeling Language) pada dokumen ini disusun untuk menjelaskan alur sistem dari dua sudut pandang:
1. **Activity Diagram**: Digunakan untuk memetakan alur aktivitas kerja (workflow) pada sistem, baik yang dilakukan oleh pengguna maupun proses internal yang dilakukan oleh sistem.
2. **Sequence Diagram**: Digunakan untuk menggambarkan interaksi antarkomponen program berdasarkan urutan waktu pemanggilan fungsi, dengan membagi komponen ke dalam pola *Boundary-Control-Entity (BCE)* agar struktur kode lebih rapi.

---

## BAB II: PERANCANGAN ACTIVITY DIAGRAM

Activity Diagram menggambarkan urutan alur kerja dari suatu aktivitas pada sistem SIPESAT, mulai dari titik awal (start), aksi pengguna, percabangan keputusan (decision), hingga selesai.

Berikut adalah diagram alur kerja terpadu (Swimlane Terpadu Siswa, Sistem SIPESAT, dan Petugas TU / Kepala Sekolah) standar modul RPL UNINDRA Pertemuan 04:

![Activity Diagram Alur Terpadu SIPESAT](assets/diagram_activity.png)
*Gambar 2.1: Activity Diagram Alur Terpadu SIPESAT Standar UNINDRA (100% Bebas Tabrakan)*

---

### 2.1 Activity Diagram 1: Alur Pengajuan Surat oleh Siswa
Diagram ini menggambarkan alur saat siswa masuk ke sistem, memilih jenis surat, mengisi keperluan, mengunggah dokumen persyaratan, hingga mendapatkan bukti resi nomor tiket.

```mermaid
flowchart TD
    subgraph Siswa["Aktor: Siswa"]
        A1([Mulai]) --> A2[Buka Halaman Web SIPESAT]
        A2 --> A3[Input NISN & Password]
        A3 --> A4[Pilih Menu 'Pengajuan Surat']
        A4 --> A5[Pilih Jenis Surat]
        A5 --> A6[Isi Form Keperluan & Unggah Berkas]
        A6 --> A7[Klik Tombol 'Kirim Permohonan']
        A13[Menerima Resi Pengajuan & Kode Tiket] --> A14([Selesai])
    end

    subgraph Web["Boundary: Antarmuka Web SIPESAT"]
        A7 --> B1[Validasi Kelengkapan Form & Ukuran File]
        B1 --> B2{Apakah Data Lengkap & Valid?}
        B2 -- Tidak --> B3[Tampilkan Pesan Peringatan Validasi]
        B3 --> A6
        B2 -- Ya --> B4[Kirim Payload Pengajuan ke Server]
        B5[Tampilkan Konfirmasi Berhasil] --> A13
    end

    subgraph Server["Sistem Backend & Database"]
        B4 --> C1[Simpan Dokumen Lampiran ke Storage]
        C1 --> C2[Generate Kode Tiket Unik Pelacakan]
        C2 --> C3[(INSERT Data Pengajuan Status: 'MENUNGGU_VERIFIKASI')]
        C3 --> C4[Trigger Notifikasi ke Antrean TU]
        C4 --> B5
    end

    style A1 fill:#238636,stroke:#2ea043,color:#fff
    style A14 fill:#da3633,stroke:#f85149,color:#fff
    style B2 fill:#d29922,stroke:#bb8009,color:#fff
```

#### Uraian Alur Kerja Activity Diagram 1:
1. Siswa membuka website SIPESAT lalu login menggunakan NISN dan kata sandi.
2. Siswa masuk ke menu "Pengajuan Surat" dan memilih jenis surat yang dibutuhkan (misalnya Surat Keterangan Siswa Aktif, Rekomendasi Beasiswa, dsb).
3. Siswa mengisi keperluan surat serta mengunggah file berkas persyaratan yang diminta (format PDF/JPG dengan ukuran maksimal 2 MB).
4. Siswa menekan tombol "Kirim Permohonan".
5. Sistem memeriksa kelengkapan isian form dan ukuran file. Jika file tidak sesuai atau melebihi 2 MB, sistem memunculkan pesan kesalahan agar siswa memperbaiki unggahannya.
6. Jika data sudah lengkap dan valid, sistem menyimpan berkas lampiran, membuat kode tiket unik (misal: `SPT-202610-0042`), dan menyimpan permohonan ke database dengan status awal `MENUNGGU_VERIFIKASI`.
7. Sistem menampilkan resi tanda terima pengajuan beserta kode tiket yang dapat disimpan oleh siswa untuk melacak progres surat.

---

### 2.2 Activity Diagram 2: Alur Verifikasi Berkas oleh Staf Tata Usaha (TU)
Diagram ini menggambarkan alur kerja staf TU dalam memeriksa kelengkapan berkas yang diajukan oleh siswa, menentukan keputusan apakah permohonan disetujui atau ditolak, dan memberikan nomor agenda surat masuk.

```mermaid
flowchart TD
    subgraph TU["Aktor: Staf Tata Usaha (Admin)"]
        D1([Mulai]) --> D2[Login ke Dashboard Admin TU]
        D2 --> D3[Buka Menu 'Verifikasi Masuk']
        D3 --> D4[Pilih Permohonan Siswa dari Antrean]
        D4 --> D5[Tinjau Data Siswa & Preview Berkas]
        D5 --> D6{Apakah Berkas Lengkap & Sah?}
        D6 -- Tidak --> D7[Tulis Catatan / Alasan Penolakan]
        D7 --> D8[Klik Tombol 'Tolak & Minta Revisi']
        D6 -- Ya --> D9[Input Nomor Agenda Masuk TU]
        D9 --> D10[Klik Tombol 'Verifikasi & Teruskan']
        D13([Selesai])
    end

    subgraph System["Sistem SIPESAT & Database"]
        D8 --> E1[(UPDATE Status: 'DITOLAK_PERLU_REVISI')]
        E1 --> E2[Kirim Notifikasi Catatan Revisi ke Siswa]
        E2 --> D13

        D10 --> E3[(UPDATE Status: 'DIVERIFIKASI_TU_MENUNGGU_KEPSEK')]
        E3 --> E4[Kirim Notifikasi Antrean Validasi ke Kepala Sekolah]
        E4 --> D13
    end

    style D1 fill:#238636,stroke:#2ea043,color:#fff
    style D13 fill:#da3633,stroke:#f85149,color:#fff
    style D6 fill:#d29922,stroke:#bb8009,color:#fff
```

#### Uraian Alur Kerja Activity Diagram 2:
1. Staf TU membuka website SIPESAT dan melakukan login ke panel admin TU.
2. Staf TU membuka menu "Verifikasi Masuk" untuk melihat daftar permohonan surat yang masuk dari siswa.
3. Staf TU memilih salah satu permohonan dan melihat pratinjau (preview) berkas lampiran yang diunggah.
4. Staf TU memeriksa apakah berkas persyaratan sudah lengkap, jelas terbaca, dan sah.
5. Jika berkas tidak lengkap atau buram, staf TU menuliskan catatan alasan penolakan dan menekan tombol "Tolak & Minta Revisi". Status diubah menjadi `DITOLAK_PERLU_REVISI` dan sistem otomatis mengirimkan notifikasi ke siswa.
6. Jika berkas sudah lengkap dan benar, staf TU memasukkan nomor agenda masuk TU lalu menekan tombol "Verifikasi & Teruskan". Status diubah menjadi `DIVERIFIKASI_TU_MENUNGGU_KEPSEK` dan permohonan diteruskan ke antrean Kepala Sekolah.

---

### 2.3 Activity Diagram 3: Alur Persetujuan oleh Kepala Sekolah
Diagram ini menggambarkan alur kerja Kepala Sekolah dalam meninjau draf permohonan surat yang telah diverifikasi TU, memberikan persetujuan, hingga surat resmi ber-QR Code berhasil dibuat oleh sistem.

```mermaid
flowchart TD
    subgraph Kepsek["Aktor: Kepala Sekolah"]
        F1([Mulai]) --> F2[Login ke Panel Kepala Sekolah]
        F2 --> F3[Buka Menu 'Persetujuan Surat']
        F3 --> F4[Pilih Draf Surat Terverifikasi TU]
        F4 --> F5[Review Draf Surat & Lembar Disposisi]
        F5 --> F6{Setujui Penerbitan Surat?}
        F6 -- Tolak/Revisi --> F7[Input Catatan Evaluasi]
        F7 --> F8[Klik 'Kembalikan ke TU']
        F6 -- Setuju --> F9[Klik 'Setujui & Tanda Tangani']
        F14([Selesai])
    end

    subgraph Engine["Sistem & Document Generation Engine"]
        F8 --> G1[(UPDATE Status: 'DITOLAK_KEPSEK')]
        G1 --> G2[Kirim Notifikasi Evaluasi ke Meja TU]
        G2 --> F14

        F9 --> G3[Ambil Format Penomoran Surat Resmi Sekolah]
        G3 --> G4[Generate Nomor Surat Otomatis]
        G4 --> G5[Generate QR Code Tanda Tangan Digital Enkripsi]
        G5 --> G6[Kompilasi Data Siswa, Kop Resmi & QR ke PDF]
        G6 --> G7[Simpan Berkas PDF Resmi ke Cloud Storage]
        G7 --> G8[(UPDATE Status: 'SELESAI_SIAP_UNDUH')]
        G8 --> G9[Kirim Notifikasi Penerbitan Surat ke Siswa]
        G9 --> F14
    end

    style F1 fill:#238636,stroke:#2ea043,color:#fff
    style F14 fill:#da3633,stroke:#f85149,color:#fff
    style F6 fill:#d29922,stroke:#bb8009,color:#fff
```

#### Uraian Alur Kerja Activity Diagram 3:
1. Kepala Sekolah login ke panel Kepala Sekolah dan membuka menu "Persetujuan Surat".
2. Kepala Sekolah memilih draf permohonan surat yang sebelumnya telah diverifikasi oleh staf TU.
3. Kepala Sekolah memeriksa isi permohonan. Jika ada data yang kurang tepat, Kepala Sekolah dapat mengisi catatan evaluasi dan mengembalikannya ke meja TU dengan status `DITOLAK_KEPSEK`.
4. Jika disetujui, Kepala Sekolah menekan tombol "Setujui & Tanda Tangani".
5. Sistem secara otomatis menghitung nomor urut surat keluar resmi sekolah (misal: `421.3/085/SMK-PSKD3/X/2026`).
6. Sistem membuat tanda tangan elektronik berupa kode QR yang berisi identitas pengesahan (nama Kepala Sekolah, NIP, tanggal terbit, dan tautan verifikasi keaslian dokumen).
7. Sistem menyatukan kop resmi sekolah, isi permohonan, nomor surat, dan kode QR ke dalam format PDF resmi, lalu memperbarui status menjadi `SELESAI_SIAP_UNDUH`.

---

### 2.4 Activity Diagram 4: Alur Pelacakan Status & Unduh Surat oleh Siswa
Diagram ini menggambarkan alur siswa dalam memantau perkembangan surat yang diajukannya melalui indikator tahapan (stepper) hingga mengunduh dokumen PDF resmi.

```mermaid
flowchart TD
    subgraph Siswa["Aktor: Siswa"]
        H1([Mulai]) --> H2[Akses Menu 'Riwayat / Lacak Surat']
        H2 --> H3[Input Kode Tiket atau Buka List Pengajuan]
        H7{Apakah Status 'SELESAI'?}
        H7 -- Belum Selesai --> H8[Pantau Tahapan Stepper Berjalan]
        H8 --> H9([Selesai])
        H7 -- Selesai --> H10[Klik Tombol 'Unduh Surat PDF']
        H10 --> H11[File PDF Surat Resmi Terunduh di Perangkat]
        H11 --> H12([Selesai])
    end

    subgraph Web["Portal SIPESAT & Server"]
        H3 --> J1[Query Status Pengajuan Berdasarkan Tiket/Siswa]
        J1 --> J2[(Ambil Rekaman Data dari Basis Data)]
        J2 --> J3[Render Visual Timeline Stepper Status]
        J3 --> H7
        H10 --> J4[Stream File PDF Resmi dari Storage]
        J4 --> H11
    end

    style H1 fill:#238636,stroke:#2ea043,color:#fff
    style H9 fill:#64748b,stroke:#475569,color:#fff
    style H12 fill:#238636,stroke:#2ea043,color:#fff
    style H7 fill:#d29922,stroke:#bb8009,color:#fff
```

#### Uraian Alur Kerja Activity Diagram 4:
1. Siswa membuka menu "Riwayat / Lacak Surat" pada portal SIPESAT.
2. Siswa memasukkan kode tiket unik atau langsung memilih dari daftar riwayat surat yang pernah diajukan.
3. Sistem mengambil data dari database dan menampilkan tahapan status secara visual (stepper): Diajukan → Verifikasi TU → Persetujuan Kepsek → Selesai.
4. Jika proses belum selesai, siswa dapat memantau posisi suratnya kapan saja tanpa perlu datang langsung ke sekolah.
5. Jika status sudah `SELESAI_SIAP_UNDUH`, tombol "Unduh Surat PDF" akan aktif dan siswa dapat langsung mendownload surat resmi tersebut ke perangkatnya.

---

## BAB III: PERANCANGAN SEQUENCE DIAGRAM

Sequence Diagram digunakan untuk menggambarkan interaksi antarkomponen objek di dalam sistem berdasarkan urutan waktu. Untuk mempermudah rancangan teknis dan pemisahan logika koding, pemodelan ini dibagi ke dalam 3 jenis komponen sesuai konsep **Boundary-Control-Entity (BCE)**:
* **<<boundary>> (Antarmuka / Form)**: Komponen tampilan web tempat pengguna berinteraksi langsung (seperti form login atau form isian surat).
* **<<control>> (Pengontrol Logika)**: Komponen program yang mengatur jalannya logika bisnis, validasi data, dan proses pemrosesan fungsi.
* **<<entity>> & <<database>> (Model Data & Basis Data)**: Komponen model data dan tabel pada basis data (PostgreSQL) tempat informasi disimpan secara permanen.

Berikut adalah rancangan visual Sequence Diagram Pengajuan Surat Siswa & Verifikasi Berkas TU standar BCE lengkap dengan frame `alt` alternatif:

![Sequence Diagram Pola BCE](assets/diagram_sequence.png)
*Gambar 3.1: Sequence Diagram Pengajuan & Verifikasi Dokumen Pola BCE (100% Bebas Tabrakan)*

---

### 3.1 Sequence Diagram 1: Alur Login Multi-Pengguna (RBAC)
Memodelkan verifikasi identitas pengguna (Siswa, TU, Kepala Sekolah) dan inisiasi sesi terotorisasi.

```mermaid
sequenceDiagram
    autonumber
    actor Pengguna as Aktor: Pengguna (Siswa/TU/Kepsek)
    participant LoginView as <<boundary>> LoginFormView
    participant AuthCtrl as <<control>> AuthController
    participant UserModel as <<entity>> UserModel
    participant DB as <<database>> PostgreSQL

    Pengguna->>LoginView: 1. Masukkan identifier (NISN/NIP) & password
    Pengguna->>LoginView: 2. Klik tombol 'Masuk'
    activate LoginView
    LoginView->>AuthCtrl: 3. submitLogin(identifier, password)
    activate AuthCtrl

    AuthCtrl->>AuthCtrl: 4. validateInputSanitization()
    AuthCtrl->>UserModel: 5. findByIdentifier(identifier)
    activate UserModel
    UserModel->>DB: 6. SELECT * FROM users WHERE identifier = $1
    activate DB
    DB-->>UserModel: 7. Record data user & password_hash
    deactivate DB
    UserModel-->>AuthCtrl: 8. return UserEntity
    deactivate UserModel

    alt Pengguna Tidak Ditemukan / Password Salah
        AuthCtrl->>AuthCtrl: 9a. verifyHash(password, hash) => False
        AuthCtrl-->>LoginView: 10a. return Error('Kredensial Tidak Valid')
        LoginView-->>Pengguna: 11a. Tampilkan pesan kesalahan login
    else Kredensial Valid
        AuthCtrl->>AuthCtrl: 9b. verifyHash(password, hash) => True
        AuthCtrl->>AuthCtrl: 10b. generateSessionToken(role, userId)
        AuthCtrl-->>LoginView: 11b. return Success(token, roleDashboardUrl)
        deactivate AuthCtrl
        LoginView-->>Pengguna: 12b. Redirect ke Dasbor (Siswa / TU / Kepsek)
        deactivate LoginView
    end
```

#### Penjelasan Alur Program Sequence Diagram 1:
Pengguna (Siswa, Staf TU, atau Kepala Sekolah) memasukkan NISN/NIP dan kata sandi pada halaman `LoginFormView`. Komponen `AuthController` memeriksa validitas input dan memanggil `UserModel` untuk mencari data pengguna di basis data. Jika kata sandi cocok dengan data yang tersimpan, controller membuatkan token sesi (JWT) yang menentukan hak akses pengguna, lalu mengarahkan pengguna ke halaman dasbor masing-masing.

---

### 3.2 Sequence Diagram 2: Alur Pengajuan Surat & Unggah Berkas oleh Siswa
Memodelkan pengisian formulir permohonan surat oleh siswa, penyimpanan berkas ke media penyimpanan, dan pencatatan tiket ke basis data.

```mermaid
sequenceDiagram
    autonumber
    actor Siswa as Aktor: Siswa
    participant FormView as <<boundary>> FormPengajuanView
    participant SuratCtrl as <<control>> SuratController
    participant FileService as <<control>> StorageService
    participant PengajuanModel as <<entity>> PengajuanModel
    participant DB as <<database>> PostgreSQL

    Siswa->>FormView: 1. Akses form pengajuan & pilih jenis surat
    activate FormView
    FormView->>SuratCtrl: 2. getPrasyaratByJenis(id_jenis)
    activate SuratCtrl
    SuratCtrl-->>FormView: 3. return ListPersyaratan (dokumen prasyarat)
    deactivate SuratCtrl

    Siswa->>FormView: 4. Isi keperluan, lampirkan berkas (PDF/JPG)
    Siswa->>FormView: 5. Klik submit 'Kirim Permohonan'
    FormView->>SuratCtrl: 6. createPengajuan(siswaId, idJenis, keperluan, fileBuffer)
    activate SuratCtrl

    SuratCtrl->>FileService: 7. uploadFile(fileBuffer, mimeType, max2MB)
    activate FileService
    alt File Melebihi Batas / Format Ilegal
        FileService-->>SuratCtrl: 8a. return Error('Format file tidak didukung / >2MB')
        SuratCtrl-->>FormView: 9a. return ValidationFailed(errorMsg)
        FormView-->>Siswa: 10a. Tampilkan dialog error unggah berkas
    else File Sah & Lolos
        FileService-->>SuratCtrl: 8b. return fileUrlPath
        deactivate FileService
        SuratCtrl->>SuratCtrl: 9b. generateTicketCode('SPT-YYYYMM-XXXX')
        SuratCtrl->>PengajuanModel: 10b. insertPengajuan(payloadData, fileUrlPath)
        activate PengajuanModel
        PengajuanModel->>DB: 11b. INSERT INTO tb_pengajuan_surat VALUES (...)
        activate DB
        DB-->>PengajuanModel: 12b. Confirm INSERT ID
        deactivate DB
        PengajuanModel-->>SuratCtrl: 13b. return PengajuanEntity
        deactivate PengajuanModel
        SuratCtrl-->>FormView: 14b. return Success(ticketCode, resiData)
        deactivate SuratCtrl
        FormView-->>Siswa: 15b. Tampilkan Resi Pengajuan & Kode Tiket
        deactivate FormView
    end
```

#### Penjelasan Alur Program Sequence Diagram 2:
Siswa membuka form permohonan surat melalui `FormPengajuanView`. Saat jenis surat dipilih, `SuratController` mengambil daftar persyaratan yang dibutuhkan. Ketika form dan berkas di-submit, `StorageService` memeriksa format dan batas ukuran file (maksimal 2 MB). Setelah berkas berhasil disimpan, `SuratController` membuat kode tiket unik dan `PengajuanModel` mencatat permohonan ke basis data dengan status awal `MENUNGGU_VERIFIKASI`, kemudian sistem menampilkan bukti tanda terima beserta kode tiket ke siswa.

---

### 3.3 Sequence Diagram 3: Alur Verifikasi Berkas oleh Staf Tata Usaha (TU)
Memodelkan peninjauan berkas lampiran siswa, disposisi persetujuan atau penolakan administratif, dan pembaruan catatan riwayat.

```mermaid
sequenceDiagram
    autonumber
    actor StafTU as Aktor: Staf TU
    participant AdminView as <<boundary>> VerifikasiAntreanView
    participant VerifCtrl as <<control>> VerifikasiController
    participant PengajuanModel as <<entity>> PengajuanModel
    participant NotifService as <<control>> NotifikasiService
    participant DB as <<database>> PostgreSQL

    StafTU->>AdminView: 1. Buka antrean verifikasi surat
    activate AdminView
    AdminView->>VerifCtrl: 2. getAntreanVerifikasi(status='MENUNGGU_VERIFIKASI')
    activate VerifCtrl
    VerifCtrl->>PengajuanModel: 3. fetchPendingList()
    activate PengajuanModel
    PengajuanModel->>DB: 4. SELECT * FROM tb_pengajuan_surat WHERE status = 'MENUNGGU_VERIFIKASI'
    activate DB
    DB-->>PengajuanModel: 5. return Records
    deactivate DB
    PengajuanModel-->>VerifCtrl: 6. return DataList
    deactivate PengajuanModel
    VerifCtrl-->>AdminView: 7. render antrean permohonan
    deactivate VerifCtrl

    StafTU->>AdminView: 8. Pilih permohonan siswa & review berkas lampiran
    StafTU->>AdminView: 9. Tentukan keputusan (Tolak / Verifikasi)

    alt Keputusan: Ditolak (Berkas Kurang / Buram)
        StafTU->>AdminView: 10a. Input catatan revisi & klik 'Tolak'
        AdminView->>VerifCtrl: 11a. rejectPengajuan(idPengajuan, catatan, tuId)
        activate VerifCtrl
        VerifCtrl->>PengajuanModel: 12a. updateStatus(id, 'DITOLAK_PERLU_REVISI', catatan)
        activate PengajuanModel
        PengajuanModel->>DB: 13a. UPDATE tb_pengajuan_surat SET status = ..., catatan = ...
        activate DB
        DB-->>PengajuanModel: 14a. Confirm UPDATE
        deactivate DB
        PengajuanModel-->>VerifCtrl: 15a. return UpdatedEntity
        deactivate PengajuanModel
        VerifCtrl->>NotifService: 16a. pushNotificationToSiswa(siswaId, catatanRevisi)
        VerifCtrl-->>AdminView: 17a. return SuccessResponse('Pengajuan Ditolak')
        deactivate VerifCtrl
        AdminView-->>StafTU: 18a. Perbarui tabel antrean
    else Keputusan: Lolos Verifikasi
        StafTU->>AdminView: 10b. Input no_agenda & klik 'Teruskan ke Kepsek'
        AdminView->>VerifCtrl: 11b. approveVerifikasi(idPengajuan, noAgenda, tuId)
        activate VerifCtrl
        VerifCtrl->>PengajuanModel: 12b. updateStatus(id, 'DIVERIFIKASI_TU_MENUNGGU_KEPSEK', noAgenda)
        activate PengajuanModel
        PengajuanModel->>DB: 13b. UPDATE tb_pengajuan_surat SET status = ..., no_agenda = ...
        activate DB
        DB-->>PengajuanModel: 14b. Confirm UPDATE
        deactivate DB
        PengajuanModel-->>VerifCtrl: 15b. return UpdatedEntity
        deactivate PengajuanModel
        VerifCtrl->>NotifService: 16b. notifyKepsekNewQueue(idPengajuan)
        VerifCtrl-->>AdminView: 17b. return SuccessResponse('Diteruskan ke Kepala Sekolah')
        deactivate VerifCtrl
        AdminView-->>StafTU: 18b. Perbarui tabel antrean
        deactivate AdminView
    end
```

#### Penjelasan Alur Program Sequence Diagram 3:
Staf TU membuka `VerifikasiAntreanView` untuk melihat antrean permohonan surat masuk. `VerifikasiController` mengelola dua kemungkinan alur: jika berkas ditolak karena kurang atau buram, controller mencatat alasan penolakan dan memicu `NotifikasiService` agar siswa memperbaiki lampiran; jika berkas sah, staf TU memasukkan nomor agenda masuk dan status permohonan diubah menjadi `DIVERIFIKASI_TU_MENUNGGU_KEPSEK` untuk diteruskan ke antrean Kepala Sekolah.

---

### 3.4 Sequence Diagram 4: Alur Persetujuan Kepala Sekolah & Penerbitan Surat PDF
Memodelkan pengesahan dokumen oleh pimpinan sekolah, pembentukan nomor surat resmi berurutan, pembuatan kode QR enkripsi, dan kompilasi berkas PDF ber-kop resmi.

```mermaid
sequenceDiagram
    autonumber
    actor Kepsek as Aktor: Kepala Sekolah
    participant PortalView as <<boundary>> ApprovalPortalView
    participant ApprCtrl as <<control>> ApprovalController
    participant NoSuratService as <<control>> NomorSuratService
    participant QRService as <<control>> QRCodeGenerator
    participant PDFEngine as <<control>> PDFCompilerService
    participant PengajuanModel as <<entity>> PengajuanModel
    participant DB as <<database>> PostgreSQL

    Kepsek->>PortalView: 1. Buka daftar pengajuan menunggu persetujuan
    activate PortalView
    PortalView->>ApprCtrl: 2. getPendingApprovalList()
    activate ApprCtrl
    ApprCtrl->>PengajuanModel: 3. fetchKepsekQueue()
    activate PengajuanModel
    PengajuanModel->>DB: 4. SELECT * FROM tb_pengajuan_surat WHERE status = 'DIVERIFIKASI_TU_MENUNGGU_KEPSEK'
    activate DB
    DB-->>PengajuanModel: 5. return Records
    deactivate DB
    PengajuanModel-->>ApprCtrl: 6. return DataList
    deactivate PengajuanModel
    ApprCtrl-->>PortalView: 7. Render daftar surat siap tanda tangan
    deactivate ApprCtrl

    Kepsek->>PortalView: 8. Tinjau permohonan & klik 'Setujui & Tanda Tangani'
    PortalView->>ApprCtrl: 9. executeApproval(idPengajuan, kepsekId)
    activate ApprCtrl

    ApprCtrl->>NoSuratService: 10. generateOfficialNumber(idJenis, tahun)
    activate NoSuratService
    NoSuratService->>DB: 11. SELECT MAX(nomor_urut) FROM tb_surat_keluar WHERE tahun = $1
    activate DB
    DB-->>NoSuratService: 12. return lastNumber
    deactivate DB
    NoSuratService-->>ApprCtrl: 13. return formattedNoSurat ('421.3/085/SMK-PSKD3/X/2026')
    deactivate NoSuratService

    ApprCtrl->>QRService: 14. createDigitalSignatureQR(metadataJson, secretKey)
    activate QRService
    QRService-->>ApprCtrl: 15. return qrImageBuffer
    deactivate QRService

    ApprCtrl->>PDFEngine: 16. compileOfficialPDF(dataSiswa, formattedNoSurat, qrImageBuffer)
    activate PDFEngine
    PDFEngine-->>ApprCtrl: 17. return pdfBinaryUrlPath
    deactivate PDFEngine

    ApprCtrl->>PengajuanModel: 18. finalizeSurat(idPengajuan, formattedNoSurat, pdfBinaryUrlPath)
    activate PengajuanModel
    PengajuanModel->>DB: 19. UPDATE tb_pengajuan_surat SET status = 'SELESAI_SIAP_UNDUH', no_surat = ..., pdf_url = ...
    activate DB
    DB-->>PengajuanModel: 20. Confirm UPDATE
    deactivate DB
    PengajuanModel-->>ApprCtrl: 21. return FinalizedEntity
    deactivate PengajuanModel

    ApprCtrl-->>PortalView: 22. return Success('Surat Resmi Berhasil Diterbitkan')
    deactivate ApprCtrl
    PortalView-->>Kepsek: 23. Tampilkan pesan berhasil & perbarui dasbor
    deactivate PortalView
```

#### Penjelasan Alur Program Sequence Diagram 4:
Ketika Kepala Sekolah menyetujui surat melalui `ApprovalPortalView`, `ApprovalController` memanggil tiga fungsi layanan secara berurutan: pertama, `NomorSuratService` mengambil nomor urut surat resmi terbaru; kedua, `QRCodeGenerator` membuat gambar kode QR sebagai tanda tangan digital resmi; ketiga, `PDFCompilerService` menggabungkan kop surat sekolah, data permohonan, dan kode QR menjadi file dokumen PDF resmi. Setelah berkas siap, `PengajuanModel` memperbarui status surat di database menjadi `SELESAI_SIAP_UNDUH`.

---

## BAB IV: MATRIKS PENELUSURAN KEBUTUHAN (TRACEABILITY MATRIX)

Tabel matriks berikut digunakan untuk memastikan bahwa setiap kebutuhan fungsional yang sudah disusun pada Dokumen SRS (Tugas 2) benar-benar sudah digambarkan pada rancangan diagram Tugas 4 ini:

| Kode Kebutuhan (SRS) | Deskripsi Kebutuhan Fungsional | Activity Diagram Terkait | Sequence Diagram Terkait |
|---|---|:---:|:---:|
| **REQ-F-01** | Autentikasi Pengguna & Hak Akses Berbasis Peran (RBAC) | Activity Diagram 1, 2, 3 | **Sequence Diagram 1** |
| **REQ-F-02** | Pengajuan Surat Mandiri & Unggah Berkas Persyaratan | **Activity Diagram 1** | **Sequence Diagram 2** |
| **REQ-F-03** | Verifikasi & Disposisi Kelengkapan Berkas oleh Staf TU | **Activity Diagram 2** | **Sequence Diagram 3** |
| **REQ-F-04** | Validasi Eksekutif & Persetujuan Kepala Sekolah | **Activity Diagram 3** | **Sequence Diagram 4** |
| **REQ-F-05** | Penomoran Surat Otomatis & Generator Dokumen PDF ber-QR | **Activity Diagram 3** | **Sequence Diagram 4** |
| **REQ-F-06** | Pelacakan Status (*Stepper Tracker*) & Unduh Surat Resmi | **Activity Diagram 4** | **Sequence Diagram 2 & 4** |

---

## BAB V: KESIMPULAN

Berdasarkan hasil perancangan Activity Diagram dan Sequence Diagram untuk sistem SIPESAT pada Tugas 4 ini, dapat kami simpulkan bahwa:
1. Seluruh alur pelayanan persuratan siswa pada sistem SIPESAT, mulai dari pengajuan mandiri oleh siswa, verifikasi berkas oleh staf TU, persetujuan dan pengesahan tanda tangan elektronik oleh Kepala Sekolah, hingga pelacakan dan pengunduhan surat telah berhasil dimodelkan dengan runtut.
2. Penggunaan pembagian kolom (swimlane) pada Activity Diagram mempermudah pembagian hak akses dan batasan tanggung jawab antara siswa, staf TU, kepala sekolah, dan sistem.
3. Penerapan konsep Boundary-Control-Entity (BCE) pada Sequence Diagram mempermudah pemahaman mengenai pemisahan antarmuka (view), logika pemrosesan (controller), dan tabel database (model) yang akan diimplementasikan saat koding aplikasi.
4. Rancangan diagram yang dibuat sudah sesuai dan selaras dengan kebutuhan fungsional yang telah diajukan pada dokumen SRS tugas sebelumnya.

---

Jakarta, Oktober 2026  
**Kelompok 7 RPL - Teknik Informatika UNINDRA**
