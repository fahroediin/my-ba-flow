# Appendix D — Panduan Praktik User Story & Acceptance Criteria

---

## D.1 Anatomi User Story yang Benar

User Story (US) bukanlah sekadar penjabaran fitur teknis yang diinginkan programmer, melainkan sebuah **kebutuhan dari sudut pandang pengguna akhir**. Struktur dasarnya harus selalu memegang rumusan:

> **Sebagai** `[Peran/Aktor]`, **Saya ingin** `[Aksi/Fitur]`, **Sehingga** `[Nilai Bisnis/Tujuan]`.

### Kesalahan Umum Penulisan US:

* **Salah (Fokus Teknis):** "Sebagai sistem, saya ingin memiliki database pelanggan sehingga saya bisa menyimpannya." *(Sistem bukan pengguna, tidak ada nilai bisnis nyata)*
* **Salah (Tanpa Nilai):** "Sebagai pengguna, saya ingin tombol filter warna." *(Apa fungsi filternya?)*

* **Benar:** "Sebagai **Pembeli**, saya ingin **menyaring produk berdasarkan warna**, sehingga **saya bisa lebih cepat menemukan baju yang sesuai dengan preferensi saya**."

---

## D.2 Teknik "Vertical Slicing" (Memecah Epic)

Seringkali Klien memberikan permintaan fitur yang terlalu raksasa (Epic). Sebuah fitur besar harus dipecah menjadi User Story yang kecil dan independen agar bisa diselesaikan dalam 1 Sprint (Kriteria **INVEST**).

**Contoh Kasus — Fitur Pembayaran:**

* **Asal (Epic):** "Sebagai pelanggan, saya ingin bisa membayar belanjaan saya." *(Terlalu besar!)*
* **Dipecah Menjadi (US):**
  1. **US 1:** "Sebagai pelanggan, saya ingin bisa membayar menggunakan Saldo Dompet."
  2. **US 2:** "Sebagai pelanggan, saya ingin bisa membayar menggunakan Kartu Kredit."
  3. **US 3:** "Sebagai pelanggan, saya ingin menyimpan kartu kredit sebagai metode pembayaran, sehingga transaksi berikutnya lebih cepat."

---

## D.3 Menulis Acceptance Criteria (Given-When-Then)

Acceptance Criteria (AC) adalah **batasan pasti** yang memberitahu *Developer* kapan pekerjaannya selesai, dan memberitahu *QA* bagaimana cara mengujinya. 

Gunakan format **BDD (Behavior-Driven Development)**:

* **GIVEN (Kondisi Awal):** Konteks atau state sistem sebelum tindakan (Misal: *GIVEN pengguna sedang login dan berada di halaman Checkout...*)
* **WHEN (Aksi):** Trigger atau aksi yang dilakukan (*WHEN pengguna mengklik "Bayar"...*)
* **THEN (Hasil Akhir):** Konsekuensi spesifik dari aksi tersebut (*THEN sistem memunculkan Invoice...*)

> [!CAUTION]
> **Aturan Emas:** Satu blok AC **Maksimal hanya boleh memiliki SATU hasil akhir yang diuji (THEN)**. Jika ada kondisi cabang/hasil berbeda, buat menjadi AC-2, AC-3 dan seterusnya.

---

## D.4 Contoh Praktis: "Bloated AC" vs "AC Standar"

Berikut adalah contoh untuk skenario sebuah tombol "Submit" Login.

### Contoh AC yang "Bloated" (Membengkak dan Buruk)
"Jika user mengisi email dan password dengan benar maka dia masuk dashboard, tapi kalau email atau passwordnya salah akan muncul pesan error warna merah, tapi kalau dia kosongkan salah satunya tombol submit tidak bisa diklik."

*(Sangat membingungkan, sulit untuk dibuat Test Case oleh QA, developer mudah terlewat mengimplementasikan alert error).*

### Contoh yang Terstruktur (Sesuai Template T-09 & T-App-BA)

Pemisahan antara bagian "User Story" dengan "Acceptance Criteria", serta pelengkap komponen lainnya harus ditulis mengikuti standar kerangka kerja **Template T-09**:

```markdown
# USER STORY L01 - Login System
**ID:** US-AUTH-01
**Priority:** Must Have

---

## User Story
* **Sebagai:** Pelanggan Terdaftar
* **Saya ingin:** masuk ke dalam sistem menggunakan email dan kata sandi
* **Sehingga:** saya bisa mengakses panel kontrol dan mengelola profil akun saya

## Acceptance Criteria

### AC-01: Happy Flow - Login Berhasil
* **GIVEN** Pengguna berada di halaman Login
* **WHEN** Pengguna memasukkan Email dan Password yang terdaftar dengan tepat, lalu klik 'Submit'
* **THEN** Pengguna dialihkan ke halaman Dashboard Utama

### AC-02: Negative Flow - Password Salah
* **GIVEN** Pengguna berada di halaman Login
* **WHEN** Pengguna memasukkan Email yang terdaftar tetapi Password yang salah, lalu klik 'Submit'
* **THEN** Muncul pesan *"Email atau kata sandi salah"* di atas formulir.

### AC-03: Negative Flow - Akun Tidak Ada
* **GIVEN** Pengguna berada di halaman Login
* **WHEN** Pengguna memasukkan Email yang tidak terdaftar, lalu klik 'Submit'
* **THEN** Muncul pesan yang sama persis dengan AC-02: *"Email atau kata sandi salah"*.

> **Catatan keamanan:** Pesan untuk email tidak terdaftar sengaja dibuat sama dengan pesan password salah. Pesan yang berbeda, atau pengalihan otomatis ke halaman registrasi, memberi tahu penyerang email mana yang terdaftar (*user enumeration*; lihat OWASP Authentication Cheat Sheet). Tautan "Daftar" tetap tersedia di halaman Login.

### AC-04: Boundary/Validation - Field Kosong
* **GIVEN** Pengguna belum mengisi Email atau Password pada Halaman Login
* **WHEN** Tidak ada input
* **THEN** Tombol 'Submit' wajib berstatus *Disabled* / abu-abu.

## Business Rules
| Rule ID | Deskripsi |
|---------|-----------|
| BR-001 | Jika pengguna memasukkan Password yang salah sebanyak 5 kali berturut-turut, akun dikunci sementara selama 15 menit. |

## UI/UX Notes
* Link ke panduan desain: `[Figma_Link]`
* Pesan *error* pada `AC-02` dan `AC-03` memakai warna status error dengan ikon peringatan.

## Technical Notes
* Integrasikan skrip _rate-limiting API_ untuk mengabulkan pengecekan `BR-001`.

## Definition of Done
- [ ] Semua AC terpenuhi & lolos test execution oleh QA
- [ ] Code reviewed
```

*(Catatan: Saat pekerjaan di lapangan nanti direkapitulasi, struktur narasi di atas adalah bahan dasar yang dipindahkan ke dalam kolom-kolom repositori Excel resmi: **T-App-BA** yang merangkum keseluruhan Epic/Sprint).*

---

## D.5 Kapan Narasi AC Berhenti dan Menjadi Tabel (MRTM)?

Skenario di atas masih dapat dinikmati bacanya karena batasnya jelas (berpusat pada sekumpulan input tunggal). Namun, bagaimana jika fitur tersebut adalah **Kalkulator Diskon**, di mana:

- Tipe User: Bronze, Silver, Gold.
- Lokasi Transaksi: Jabodetabek, Luar.
- Saldo Belanja: < 100k, 100k–500k, > 500k.

Partisi di atas tidak boleh tumpang tindih atau berlubang: setiap nilai saldo harus masuk tepat satu partisi (lihat Equivalence Partitioning di Bab 5 §5.3.4).

Jika skenario melibatkan **lebih dari 3 kondisi/variabel input**, maka **BERHENTILAH** menulis dengan teknik narasi *Given-When-Then*.

> [!IMPORTANT]
> **Rule of Thumb:** Alihkan penulisan AC kompleks Anda ke format matriks (**Master Requirement & Test Matrix / MRTM** - *Lihat Bab 14*). Narasi paragraf panjang Anda hanya akan berujung pada miskomunikasi logika dan celah pengujian (*Boundary Value*) oleh QA.

---

**Kembali ke:** [Daftar Isi](00_BA_Handbook_Cover.md)
