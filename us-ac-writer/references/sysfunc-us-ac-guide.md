### System Function: Generator User Story & Acceptance Criteria (UPDATED)

#### **Tahap 1: Definisi Konteks dan Persona (Input Utama)**

Sebelum memulai, LLM harus meminta atau diberikan informasi dasar berikut:

1.  **Nama Fitur / Modul**: Apa nama umum dari fungsionalitas yang akan dibuat? (Contoh: "Manajemen Sertifikat", "Pencarian Talent Lanjutan", "Sistem Notifikasi").
2.  **Tujuan Bisnis Utama**: Dalam satu kalimat, mengapa fitur ini penting? Apa masalah yang diselesaikannya? (Contoh: "Untuk melacak sertifikasi talent agar data tetap akurat", "Untuk mempercepat proses pencarian kandidat yang paling sesuai").
3.  **Persona Utama**: Siapa pengguna utama yang akan berinteraksi dengan fitur ini? (Contoh: "Manager", "Recruiter", "Administrator").
4.  **Aksi-Aksi Kunci**: Daftar singkat tindakan utama yang bisa dilakukan pengguna dalam fitur ini. (Contoh: "Menambahkan sertifikat", "Mengedit sertifikat", "Menghapus sertifikat", "Melihat daftar sertifikat di profil talent").

**Evaluasi Ukuran Fitur (Vertical Slicing):**

Sebelum melanjutkan, LLM harus mengevaluasi apakah fitur yang diminta terlalu besar (Epic) dan perlu dipecah menjadi beberapa User Story yang lebih kecil dan independen.

> **Aturan Praktis:** Jika satu User Story mencakup **lebih dari 3 aksi CRUD** atau **membutuhkan lebih dari 1 Sprint** untuk diselesaikan, WAJIB dipecah menjadi beberapa US yang lebih kecil.

**Contoh Pemecahan:**
- ❌ **Terlalu Besar (Epic):** "Sebagai pelanggan, saya ingin bisa membayar belanjaan saya." → Terlalu banyak metode pembayaran, alur, dan validasi.
- ✅ **Ukuran Tepat (US-1):** "Sebagai pelanggan, saya ingin membayar menggunakan Saldo Dompet."
- ✅ **Ukuran Tepat (US-2):** "Sebagai pelanggan, saya ingin membayar menggunakan Kartu Kredit."
- ✅ **Ukuran Tepat (US-3):** "Sebagai pelanggan, saya ingin menyimpan profil metode pembayaran Kartu Kredit agar transaksi selanjutnya lebih cepat."

#### **Tahap 2: Proses Generasi User Story (US)**

LLM harus mengikuti struktur tabel ini dan mengisi setiap kolom berdasarkan input dari Tahap 1.

**Instruksi untuk LLM:**
"Untuk setiap Aksi Kunci yang diidentifikasi, buatlah satu baris User Story dalam format tabel berikut. Pastikan setiap kolom diisi sesuai dengan pedoman ini:"

| Kolom | Pedoman Pengisian | Contoh (Fitur: Manajemen Sertifikat) |
| :--- | :--- | :--- |
| **US-ID** | Gunakan format `US-XX` dengan nomor yang berurutan. | `US-06` |
| **Judul** | Buat judul singkat dan deskriptif yang merangkum aksi. Gunakan format **Kata Kerja + Objek**. | `Menambahkan Sertifikat Talent` |
| **Persona** | Gunakan **Persona Utama** yang telah didefinisikan. | `Manager` |
| **Aksi yang dilakukan** | Jelaskan aksi spesifik yang dilakukan pengguna. JANGAN gunakan kata "bisa" atau "dapat". Langsung jelaskan aksinya. | `menambahkan data sertifikat baru ke profil seorang talent` |
| **Hasil nilai bisnis** | Jelaskan **mengapa** aksi ini penting dari sudut pandang bisnis. JANGAN gunakan kata "agar" atau "untuk". Langsung jelaskan nilai bisnisnya. | `data kualifikasi talent selalu lengkap dan terbaru` |

**Validasi INVEST untuk Setiap User Story:**

Sebelum melanjutkan ke Tahap 3, setiap User Story yang dihasilkan **WAJIB** divalidasi menggunakan kriteria **INVEST**:

| Kriteria | Pertanyaan Validasi | Contoh Pelanggaran |
| :--- | :--- | :--- |
| **I**ndependent | Apakah US ini bisa dikerjakan tanpa bergantung pada US lain? | US yang harus menunggu US lain selesai dulu |
| **N**egotiable | Apakah detail implementasi masih bisa dinegosiasikan? | US yang sudah mendikte solusi teknis spesifik |
| **V**aluable | Apakah US ini memberikan nilai bisnis yang jelas? | US yang hanya berisi pekerjaan teknis tanpa manfaat user |
| **E**stimable | Apakah tim bisa mengestimasi effort untuk US ini? | US yang terlalu abstrak sehingga tidak bisa diestimasi |
| **S**mall | Apakah US ini cukup kecil untuk selesai dalam 1 Sprint? | US yang mencakup seluruh modul sekaligus |
| **T**estable | Apakah ada kriteria jelas untuk menguji US ini? | US dengan hasil yang subjektif dan tidak terukur |

"Setelah menghasilkan User Stories, validasi setiap US terhadap 6 kriteria INVEST di atas. Jika ada US yang gagal di salah satu kriteria, perbaiki sebelum melanjutkan ke pembuatan Acceptance Criteria."

#### **Tahap 3: Proses Generasi Acceptance Criteria (AC)**

LLM harus menghasilkan beberapa skenario AC untuk setiap User Story yang dibuat di Tahap 2.

**PRINSIP PENTING UNTUK TESTABLE AC:**
1.  **Given** harus menjelaskan **precondition yang spesifik dan relevan**:
    - Jelaskan halaman/screen tempat user berada
    - Jelaskan data/kondisi sistem yang sudah ada
    - HINDARI kondisi yang terlalu umum seperti "saya login ke sistem" tanpa konteks
    - Format: **"Saya seorang [role] AND saya berada di halaman [nama halaman] AND [kondisi lain yang relevan]"**

2.  **When** harus menjelaskan **HANYA aksi user, BUKAN kondisi atau hasil sistem**:
    - ⚠️ **PENTING**: WHEN hanya boleh berisi aksi yang dilakukan USER, bukan respons/hasil sistem
    - Jelaskan setiap langkah action secara berurutan
    - Sebutkan nama field, button, dropdown yang spesifik
    - Jelaskan data yang diinput jika ada
    - **DILARANG** menggunakan kalimat seperti:
      - ❌ "...sistem membuka halaman..."
      - ❌ "...modal terbuka..."
      - ❌ "...field menjadi aktif..."
      - ❌ "...cursor berada di dalamnya..."
    - **DIPERBOLEHKAN** menggunakan kata kerja aksi user:
      - ✅ "saya mengklik..."
      - ✅ "saya mengetik..."
      - ✅ "saya memilih..."
      - ✅ "saya drag..."
      - ✅ "saya scroll..."
    - Format: **"Saya [aksi 1 dengan detail] AND saya [aksi 2 dengan detail]"**
    - ⚠️ Jika ada **hasil sistem di antara aksi**, PECAH menjadi **skenario terpisah**

3.  **Then** harus menjelaskan **expected result yang observable dan verifiable**:
    - Hasil harus bisa dilihat/diverifikasi oleh QA
    - Sebutkan elemen UI yang muncul (notifikasi, badge, tabel, dll)
    - Sebutkan teks exact dari message jika ada
    - Jelaskan perubahan state/data yang terjadi
    - Format: **"Sistem menampilkan [sesuatu yang spesifik] AND [perubahan lain yang terjadi]"**

**Instruksi untuk LLM:**
"Untuk setiap User Story (US), buatlah Acceptance Criteria (AC) yang WAJIB mencakup **minimal** skenario dari setiap kategori berikut. Setiap kategori ditulis sebagai AC terpisah (bukan kolom baru). PENTING: Setiap AC harus testable oleh QA dengan langkah-langkah yang jelas dan expected result yang bisa diverifikasi."

**Kategori Skenario AC yang WAJIB Dihasilkan:**

| Kategori | Deskripsi | Minimum | Contoh Skenario |
| :--- | :--- | :--- | :--- |
| ✅ **Happy Path** | Alur utama yang berhasil dengan semua input valid | 1 AC | Menambahkan sertifikat dengan semua data valid |
| ❌ **Negative/Validation Path** | Alur gagal karena input tidak valid, tidak lengkap, atau kondisi tidak terpenuhi | 1 AC | Submit form tanpa mengisi field wajib |
| 🔲 **Boundary/Edge Case** | Pengujian di batas nilai minimum/maksimum, input ekstrem, atau kondisi langka | 1 AC | Input nama dengan 1 karakter (min), 255 karakter (max), atau karakter spesial |
| 🔄 **State Transition** *(jika relevan)* | Perpindahan status yang valid dan invalid | Opsional | Status dari "Active" ke "Expired", bukan langsung "Draft" ke "Revoked" |
| 👥 **Permission/Access** *(jika relevan)* | Akses berdasarkan role atau izin | Opsional | User tanpa role Manager mencoba mengakses fitur tambah sertifikat |

| Kolom | Pedoman Pengisian | Contoh (AC untuk US-06) |
| :--- | :--- | :--- |
| **AC-ID** | Gunakan format `AC-XX.YY`, di mana `XX` adalah nomor US dan `YY` adalah nomor urut AC. | `AC-06.01` |
| **US-ID** | Referensikan ID User Story yang relevan. | `US-06` |
| **Skenario** | Berikan deskripsi singkat dan jelas tentang apa yang diuji dalam skenario ini. Fokus pada **satu perilaku spesifik**. | `Menambahkan sertifikat dengan semua data yang valid` |
| **GIVEN** | Jelaskan **precondition yang spesifik dan relevan** sebelum aksi dilakukan. WAJIB menyebutkan halaman/screen tempat user berada. Gunakan `AND` untuk beberapa kondisi. Format: **"Saya seorang [role]<br>AND saya berada di halaman [nama halaman]<br>AND [kondisi lain yang relevan]"**. | `Saya seorang Manager<br>AND saya berada di halaman "Detail Talent - John Doe"<br>AND saya dapat melihat section "Sertifikasi" yang masih kosong` |
| **WHEN** | Jelaskan **HANYA aksi user** dengan detail yang cukup untuk QA reproduce. **DILARANG menyertakan kondisi/hasil sistem** seperti "modal terbuka", "field aktif", dll. Sebutkan nama field, button, dropdown yang spesifik. Gunakan `AND` untuk beberapa aksi berurutan. **Jika ada hasil sistem di antara aksi, PECAH menjadi skenario terpisah.** Format: **"Saya [aksi 1]<br>AND saya [aksi 2]"**. | `Saya mengklik tombol "Tambah Sertifikat" di section Sertifikasi<br>AND saya mengisi field "Nama Sertifikat" dengan "PMP Certification"<br>AND saya mengisi field "Lembaga Penerbit" dengan "PMI"<br>AND saya memilih tanggal "01/01/2024" di datepicker "Tanggal Terbit"<br>AND saya menekan tombol "Simpan" di modal` |
| **THEN** | Jelaskan **hasil yang dapat diverifikasi** setelah aksi dilakukan dengan detail element UI dan teks yang spesifik. **PENTING: Setiap `THEN` harus berisi hasil yang testable.** Jika ada beberapa hasil yang perlu diverifikasi, jelaskan semuanya. Format: **"Sistem menampilkan [sesuatu yang spesifik]<br>AND [perubahan lain yang observable]"**. | `Modal "Tambah Sertifikat" tertutup<br>AND muncul notifikasi success berwarna hijau di pojok kanan atas dengan teks "Sertifikat berhasil ditambahkan"<br>AND di section "Sertifikasi" muncul card baru dengan informasi:<br>- Nama: "PMP Certification"<br>- Lembaga: "PMI"<br>- Tanggal Terbit: "01 Jan 2024"` |

**Contoh AC Tambahan untuk US-06 (Negative, Boundary, Edge Case):**

| AC-ID | US-ID | Skenario | GIVEN | WHEN | THEN |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AC-06.02** | US-06 | Mencoba menambahkan sertifikat tanpa mengisi nama | Saya seorang Manager<br>AND saya berada di halaman "Detail Talent - John Doe"<br>AND modal "Tambah Sertifikat" sedang terbuka | Saya membiarkan field "Nama Sertifikat" kosong<br>AND saya mengisi field "Lembaga Penerbit" dengan "PMI"<br>AND saya memilih tanggal "01/01/2024" di datepicker "Tanggal Terbit"<br>AND saya menekan tombol "Simpan" | Field "Nama Sertifikat" menampilkan border merah<br>AND dibawah field muncul teks error berwarna merah: "Nama sertifikat wajib diisi"<br>AND tombol "Simpan" tidak melakukan aksi apapun<br>AND modal tetap terbuka |
| **AC-06.03** | US-06 | ❌ Membatalkan proses via tombol Batal | Saya seorang Manager<br>AND saya berada di halaman "Detail Talent - John Doe"<br>AND modal "Tambah Sertifikat" sedang terbuka<br>AND saya telah mengisi beberapa field | Saya mengklik tombol "Batal" di modal | Modal "Tambah Sertifikat" tertutup<br>AND tidak ada perubahan data di section "Sertifikasi"<br>AND tidak muncul notifikasi apapun |
| **AC-06.04** | US-06 | ❌ Membatalkan proses via klik di luar modal | Saya seorang Manager<br>AND saya berada di halaman "Detail Talent - John Doe"<br>AND modal "Tambah Sertifikat" sedang terbuka<br>AND saya telah mengisi beberapa field | Saya mengklik area di luar modal (overlay) | Modal "Tambah Sertifikat" tertutup<br>AND tidak ada perubahan data di section "Sertifikasi"<br>AND tidak muncul notifikasi apapun |
| **AC-06.05** | US-06 | 🔲 Nama sertifikat di batas karakter maksimum (255 char) | Saya seorang Manager<br>AND saya berada di halaman "Detail Talent - John Doe"<br>AND modal "Tambah Sertifikat" sedang terbuka | Saya mengisi field "Nama Sertifikat" dengan teks sepanjang 255 karakter (batas maksimum)<br>AND saya mengisi field "Lembaga Penerbit" dengan "PMI"<br>AND saya memilih tanggal "01/01/2024" di datepicker "Tanggal Terbit"<br>AND saya menekan tombol "Simpan" | Modal "Tambah Sertifikat" tertutup<br>AND muncul notifikasi success dengan teks "Sertifikat berhasil ditambahkan"<br>AND sertifikat baru muncul di section "Sertifikasi" dengan nama yang tidak terpotong |
| **AC-06.06** | US-06 | 🔲 Nama sertifikat melebihi batas karakter | Saya seorang Manager<br>AND saya berada di halaman "Detail Talent - John Doe"<br>AND modal "Tambah Sertifikat" sedang terbuka | Saya mengisi field "Nama Sertifikat" dengan teks sepanjang 256 karakter (melebihi batas)<br>AND saya menekan tombol "Simpan" | Field "Nama Sertifikat" menampilkan border merah<br>AND dibawah field muncul teks error: "Nama sertifikat maksimal 255 karakter"<br>AND modal tetap terbuka |
| **AC-06.07** | US-06 | 🔲 Tanggal terbit di masa depan (edge case) | Saya seorang Manager<br>AND saya berada di halaman "Detail Talent - John Doe"<br>AND modal "Tambah Sertifikat" sedang terbuka | Saya mengisi field "Nama Sertifikat" dengan "PMP Certification"<br>AND saya mengisi field "Lembaga Penerbit" dengan "PMI"<br>AND saya memilih tanggal "01/01/2030" (masa depan) di datepicker "Tanggal Terbit"<br>AND saya menekan tombol "Simpan" | Field "Tanggal Terbit" menampilkan border merah<br>AND dibawah field muncul teks error: "Tanggal terbit tidak boleh melebihi tanggal hari ini"<br>AND modal tetap terbuka |

#### **Tips Membuat AC yang Testable:**

1. **Specific**: Sebutkan nama element UI yang spesifik (nama button, field, dropdown, modal, section, dll)
2. **Sequential**: Jelaskan langkah-langkah action secara berurutan jika ada multiple steps
3. **Observable**: Hasil harus bisa dilihat/diobserve oleh QA (notifikasi, perubahan UI, perubahan data)
4. **Verifiable**: QA harus bisa memverifikasi hasilnya (cek teks, cek warna, cek data yang muncul)
5. **Complete**: Jelaskan semua expected result yang terjadi, tidak hanya satu hasil saja
6. **Exact Text**: Jika ada message/notifikasi, tulis exact text-nya dalam tanda petik
7. **State Changes**: Jelaskan perubahan state/kondisi sistem setelah action (modal tertutup, data bertambah, dll)
8. **Boundary Values**: Untuk setiap field input, pertimbangkan nilai batas (minimum, maksimum, tepat di batas, melewati batas) dan buat AC terpisah untuk setiap boundary
9. **Edge Cases**: Pertimbangkan kondisi langka seperti input kosong, karakter spesial, duplikasi data, tanggal invalid, dan buat AC terpisah untuk setiap edge case yang relevan

#### **Panduan Boundary Value & Edge Case untuk AC:**

Berdasarkan teknik pengujian **ISTQB** (ref: Bab 5 §5.3.5), setiap AC yang melibatkan input data HARUS mempertimbangkan:

**1. Equivalence Partitioning (EP):**
- Definisikan rentang input **valid** dan **invalid** secara jelas
- Contoh: Usia valid = 18-65 tahun → Partisi: valid (25), invalid bawah (15), invalid atas (70)

**2. Boundary Value Analysis (BVA):**
- Sebutkan **nilai batas** secara eksplisit (minimum, maksimum)
- Buat AC terpisah untuk: tepat di batas bawah, tepat di batas atas, di bawah batas, di atas batas
- Contoh: Saldo minimum Rp 50.000 → AC untuk: 49.999 (gagal), 50.000 (berhasil), 50.001 (berhasil)

**3. Edge Cases yang Wajib Dipertimbangkan:**

| Jenis Edge Case | Contoh | Buat AC Jika |
| :--- | :--- | :--- |
| Input kosong / null | Field nama dikosongkan | ✅ Selalu |
| Karakter spesial | Input mengandung `<script>`, `'`, `"`, `&` | ✅ Selalu |
| Input melebihi batas | Teks > 255 karakter | ✅ Selalu |
| Duplikasi data | Menambah sertifikat dengan nama yang sudah ada | ✅ Jika ada constraint unique |
| Tanggal invalid | Tanggal di masa depan untuk "Tanggal Terbit" | ✅ Jika ada validasi tanggal |
| Concurrent access | Dua user mengedit data yang sama | ⚠️ Jika multi-user |

#### **⚠️ Anti-Pattern: Kondisi/Hasil di WHEN (HARUS DIHINDARI)**

Berikut adalah pola yang **SALAH** dan cara memperbaikinya:

**❌ SALAH - Kondisi/hasil sistem di WHEN:**
```
WHEN: saya mengklik field searchable dropdown "Nama Pelanggan"
      AND field pencarian aktif dan cursor berada di dalamnya  ← INI HASIL, BUKAN AKSI!
      AND saya mengetik huruf "PB" di field pencarian
```

**✅ BENAR - Dipecah menjadi 2 skenario:**

**Skenario 1 (AC-XX.01a): Mengaktifkan field pencarian**
```
GIVEN: saya seorang Fieldman AND saya berada di halaman "Buat SPK"
WHEN: saya mengklik field searchable dropdown "Nama Pelanggan"
THEN: field pencarian aktif dan cursor berada di dalamnya
```

**Skenario 2 (AC-XX.01b): Mencari dengan kata kunci**
```
GIVEN: saya seorang Fieldman AND field pencarian "Nama Pelanggan" sudah aktif
WHEN: saya mengetik huruf "PB" di field pencarian
THEN: sistem menampilkan list pelanggan yang mengandung "PB"
```

**Kata Kunci yang DILARANG di WHEN:**
| Kata/Frasa | Alasan | Pindahkan ke |
|------------|--------|-------------|
| "...aktif" | Hasil sistem | THEN |
| "...terbuka" | Hasil sistem | THEN |
| "...muncul" | Hasil sistem | THEN |
| "...berubah" | Hasil sistem | THEN |
| "...menampilkan" | Hasil sistem | THEN |
| "sistem..." | Aksi sistem | THEN |

**Kata Kunci yang DIPERBOLEHKAN di WHEN:**
| Kata Kerja | Contoh |
|------------|--------|
| mengklik | saya mengklik tombol "Submit" |
| mengetik | saya mengetik "PBI" di field pencarian |
| memilih | saya memilih value "Ongoing" di dropdown |
| mencentang | saya mencentang tickbox "Uang Jalan" |
| menekan | saya menekan tombol Enter |
| drag/drop | saya drag item ke posisi baru |
| scroll | saya scroll ke bawah halaman |
| hover | saya hover mouse di atas tombol |

#### **⚠️ Anti-Pattern: Penggunaan OR di WHEN (HARUS DIHINDARI)**

**DILARANG** menggunakan `OR` di kolom WHEN. Jika ada aksi alternatif yang menghasilkan THEN yang sama, **WAJIB** dipecah menjadi AC terpisah.

**❌ SALAH — OR di WHEN:**
```
WHEN: Saya mengklik tombol "Batal" di modal
      OR saya mengklik area di luar modal (overlay)
THEN: Modal tertutup
```

**✅ BENAR — Dipecah menjadi 2 AC terpisah:**

**AC-XX.03: Membatalkan via tombol Batal**
```
WHEN: Saya mengklik tombol "Batal" di modal
THEN: Modal tertutup AND tidak ada perubahan data
```

**AC-XX.04: Membatalkan via klik overlay**
```
WHEN: Saya mengklik area di luar modal (overlay)
THEN: Modal tertutup AND tidak ada perubahan data
```

#### **Contoh AC yang TIDAK Testable vs Testable:**

**❌ TIDAK TESTABLE:**
- Given: Saya seorang Manager AND saya login
- When: Saya tambah sertifikat
- Then: Sertifikat berhasil ditambahkan

**✅ TESTABLE:**
- Given: Saya seorang Manager AND saya berada di halaman "Detail Talent - John Doe" AND section "Sertifikasi" menampilkan 2 sertifikat existing
- When: Saya mengklik tombol "Tambah Sertifikat" AND saya mengisi field "Nama Sertifikat" dengan "AWS Solutions Architect" AND saya mengisi field "Lembaga Penerbit" dengan "Amazon Web Services" AND saya memilih tanggal "15/03/2024" AND saya klik tombol "Simpan"
- Then: Notifikasi success muncul dengan teks "Sertifikat berhasil ditambahkan" AND section "Sertifikasi" sekarang menampilkan 3 sertifikat (2 existing + 1 baru) AND sertifikat baru "AWS Solutions Architect" muncul di posisi paling atas list dengan status "Active"

---

#### **Tahap 4: MRTM — Master Requirement Test Matrix (Aturan Anti-Bloated AC)**

##### **Prinsip Utama: "The Table IS the AC"**

**DILARANG** membengkakkan deskripsi Acceptance Criteria (Bloated AC) dengan paragraf skenario "Jika x maka y" beruntun bilamana suatu alur memiliki **lebih dari 3 parameter/variabel input atau output kompleks**.

> **Aturan Wajib:** Jika spesifikasi fungsi melibatkan logika komputasi yang rumit (>3 branches), **Matriks Logika Wajib Menggantikan Teks Narasi.**

##### **Kapan Harus Menggunakan MRTM?**

| Kondisi | Gunakan Narasi (Given-When-Then) | Gunakan MRTM |
| :--- | :--- | :--- |
| Jumlah variabel input/output | ≤ 3 parameter | > 3 parameter |
| Jumlah kombinasi logika (branches) | ≤ 3 skenario | > 3 skenario |
| Tipe skenario | Alur tunggal (happy path, single negative) | Kombinasi multi-kondisi |
| Contoh kasus | Tambah/Edit/Hapus sertifikat | Eligibility check, pricing rules, permission matrix |

##### **Contoh Narasi AC yang Buruk (JANGAN Lakukan Ini)**

```
❌ BLOATED AC — Narasi beruntun:

"Jika Status User=Aktif, dan Lokasi=Jakarta, dan Saldo>=1000, maka Tampilkan Tombol Order."
"Jika Status User=Pasif, dan Lokasi=Jakarta, dan Saldo>=1000, maka Sembunyikan Tombol Order dan munculkan Alert."
"Jika Status User=Aktif, tapi Lokasi=Bali..." 
(Seterusnya hingga berjalan halaman-halaman penuh)
```

##### **Konversi Menjadi MRTM**

Di dalam penulisan User Story oleh BA, cukup merujuk pada tabel MRTM:

**Acceptance Criteria:**
> "Refer to **MRTM Rows: TRM_ORD_001 through TRM_ORD_020** for comprehensive logic combinations."

**Format Tabel MRTM:**

| User Story ID | Acceptance Criteria ID | User | Test Case ID | [Variabel 1] | [Variabel 2] | [Variabel 3] | [Variabel 4] | [Variabel 5] | Kondisi Khusus | HASIL (EXPECTED RESULT) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US_05 | AC_01 | Customer | TRM_ORD_001 | Aktif | Jakarta | >= 1000 | [-] | [-] | [-] | Area Order Muncul & Aktif |
| US_05 | AC_01 | Customer | TRM_ORD_002 | Pasif | Jakarta | >= 1000 | [-] | [-] | [-] | Button Order Hide, Alert Pop |
| US_05 | AC_01 | Customer | TRM_ORD_003 | [ANY] | Luar JKT | [ANY] | [-] | [-] | [-] | Tampilkan banner Unavailable |

##### **Aturan Pengisian MRTM**

| Komponen | Pedoman |
| :--- | :--- |
| **User Story ID** | Referensikan US-ID yang relevan (format: `US_XX`) |
| **Acceptance Criteria ID** | Referensikan AC-ID induk (format: `AC_XX`) |
| **User** | Persona yang menjalankan skenario |
| **Test Case ID (TCID)** | ID unik per baris kombinasi (format: `TRM_[MODUL]_XXX`). Diisi oleh BA, diuji kelulusannya oleh QA |
| **[Variabel 1] s.d. [Variabel N]** | Kolom variabel bersifat **kondisional/fleksibel** — dapat dikurangi atau ditambah tergantung kebutuhan skenario dan kompleksitas parameter di lapangan |
| **Kondisi Khusus** | Kondisi tambahan yang tidak tercakup di variabel standar. Isi `[-]` jika tidak ada |
| **HASIL (EXPECTED RESULT)** | Hasil yang diharapkan untuk kombinasi variabel tersebut. Harus **observable dan verifiable** |

##### **Nilai Khusus dalam MRTM**

| Nilai | Arti |
| :--- | :--- |
| `[-]` | Tidak berlaku / tidak relevan untuk skenario ini |
| `[ANY]` | Berlaku untuk semua nilai variabel tersebut |
| Nilai spesifik (misal: `Aktif`, `>= 1000`) | Kondisi eksak yang harus dipenuhi |

##### **Instruksi untuk LLM:**

"Sebelum menulis Acceptance Criteria, evaluasi terlebih dahulu kompleksitas skenario:
1. Jika jumlah variabel input/output **≤ 3** DAN jumlah kombinasi logika **≤ 3**: Gunakan format **Given-When-Then** standar (Tahap 3).
2. Jika jumlah variabel input/output **> 3** ATAU jumlah kombinasi logika **> 3**: **WAJIB** gunakan format **MRTM** (Tahap 4). Tuliskan AC cukup dengan referensi: 'Refer to MRTM Rows: [TCID awal] through [TCID akhir] for comprehensive logic combinations.' Kemudian buat tabel MRTM sesuai format di atas."

---

#### **Referensi Silang ke BA Handbook:**

| Dokumen | Topik Terkait |
| :--- | :--- |
| **Appendix D** — Panduan Praktik US & AC | Anatomi US, Vertical Slicing, Bloated AC vs Standar |
| **Bab 5 §5.3.5** — AC Testability Awareness | Equivalence Partitioning, Boundary Value Analysis, Checklist Testability |
| **Bab 14** — Master Requirement & Test Matrix (MRTM) | Detail format MRTM, Variable Efficiency ([ANY]/[-]), Three Amigos Sync |
| **Appendix B** — Checklist BA | Checklist kelengkapan deliverable BA |
