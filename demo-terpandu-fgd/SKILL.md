---
name: demo-terpandu-fgd
description: Menyiapkan panduan demo terpandu untuk aplikasi web apa pun dalam format pilihan pengguna, yaitu Demo (panel ringkas berisi tombol langkah, Sebelumnya/Berikutnya dan Catatan, dengan naskah pembawa tercetak), FGD (format Panduan FGD FIF dengan tujuan, pertanyaan berkode, catatan "Perlu diubah" dan "Sudah diubah / disepakati" yang bisa diunduh), atau keduanya, untuk aplikasi jadi (product based) maupun prototype (project based). Aplikasi dijalankan lokal, data contoh diisi lewat API aplikasi sendiri, identitas berganti per peran/tenant, langkah 0..n membuka dan menyorot layar yang dibahas, dan warna panel mengikuti aplikasi. Gunakan setiap kali pengguna ingin mendemokan, mempresentasikan, memperagakan, menyiapkan FGD, UAT, walkthrough, uji coba pengguna atau "show ke user/klien" sebuah aplikasi, termasuk saat mereka bilang "panduan demo", "biar saya tinggal klik-klik", "urutan demo", "rundown", "mode demo" atau "seperti Panduan FGD FIF", walau kata "skill" tidak disebut.
---

# Panduan demo terpandu

Tujuannya: penyaji cukup menekan **Berikutnya ›** (atau nomor langkah). Setiap langkah otomatis berganti peran/tenant, membuka dan menyorot bagian layar yang dibahas, dan menampilkan tujuan serta pertanyaan untuk audiens. Fokus utamanya adalah **panduan demo**; format FGD menambahkan pencatatan masukan peserta.

## Langkah 0: tanyakan format (wajib, sebelum mengerjakan apa pun)

Setiap kali skill ini dipakai, tanyakan dulu format mana yang diinginkan dengan alat tanya-pilihan (AskUserQuestion) bila tersedia, atau dengan pertanyaan langsung: **Demo**, **FGD**, atau **keduanya**. Jangan memilih sendiri; format menentukan isi panel, data yang diminta, dan naskahnya.

| Format | Panel di layar | Pertanyaan | Cocok untuk |
|---|---|---|---|
| **Demo** | "Panduan Demo", **ringkas satu baris**: tombol nomor langkah, ‹ Sebelumnya / Berikutnya ›, tombol **Catatan** (membuka satu kolom tulis masukan untuk langkah itu, plus unduh .md/.csv), ×. Tujuan, poin bicara dan instruksi klik tidak tampil; semuanya ada di naskah cetak. | Tidak wajib. Bila pengguna punya daftar, masukkan ke naskah cetak, bukan ke layar. | Presentasi produk, demo ke klien/atasan, UAT, pelatihan |
| **FGD** | "Panduan FGD" format FIF: tujuan, Tampilkan, pertanyaan berkode, Info pembawa, Sorot, kolom **Perlu diubah (masukan {klien})** dan **Sudah diubah / disepakati**, unduh catatan .md/.csv | Bank pertanyaan berkode; dari file pengguna, atau disusun bersama pengguna | Diskusi kebutuhan, menggali keputusan dan masukan klien |
| **Keduanya** | Satu `steps.json` dan satu konfigurasi; format dipilih saat menjalankan dengan `--format demo` atau `--format fgd` (mis. dua skrip `npm run demo` dan `npm run fgd`). Catatan tersimpan terpisah per format. | Seperti FGD | Tim yang memakai demo singkat dan sesi FGD untuk aplikasi yang sama |

**Bila ada daftar pertanyaan dari pengguna** (wajib dipakai untuk FGD bila ada; opsional untuk Demo), impor dengan:
```bash
node <skill>/scripts/import-questions.mjs <file> --out demo/questions.json [--sheet "Nama sheet"]
```
Pengimpor membaca .md, .xlsx, .csv, .tsv (Google Sheets diunduh sebagai .xlsx/.csv): kolom **Pertanyaan** (alias: Question, Soal), kolom kode opsional (Kode, No, ID) dan kolom topik opsional (Langkah, Topik, Bagian, Fitur, Menu, Tema). Di Markdown, judul `##` menjadi topik dan butir daftar/tabel menjadi pertanyaan. Pertanyaan tanpa kode diberi Q1, Q2, …. Ringkasan JSON di stdout memuat topik per pertanyaan; pakai untuk menempatkan kode ke langkah yang sesuai (`q`). Jangan mengarang pertanyaan atas nama pengguna tanpa persetujuannya.

**Bila FGD (atau keduanya) dipilih**, tanyakan juga nama klien (untuk label "masukan {klien}"), durasi, pembawa, dan keputusan apa yang ingin didapat. Bila tidak ada file pertanyaan, susun bank pertanyaan berkode bersama pengguna (lihat `references/desain-skenario.md`).

Tulis pilihan ke konfigurasi sebagai `"format": "demo"` atau `"format": "fgd"` (untuk keduanya: format bawaan di config, format lain lewat `--format`). Proxy menolak berjalan tanpa format yang jelas.

## Dipakai di dua model

Skill ini bagian dari plugin my-ba-flow dan dipakai di kedua model kerja BA, product based dan project based (lihat skill `ba-start`).

| | Product based | Project based |
|---|---|---|
| Yang diperagakan | Aplikasi jadi dari file zip/rar, dijalankan lokal | Prototype tim yang berjalan sebagai web (HTML, React, dan sejenisnya) |
| Bahan langkah dan Info pembawa | `docs/ba/product/<produk>-<versi>/product-brief.md`, `feature-inventory.md`, `demo-traps.md` hasil `product-onboarding` | Kebutuhan dan layar dari `wireframe-spec` (`screen-inventory.md`, `navigation-flow.md`) |
| Pertanyaan | Prep sheet `discovery-meeting-prep` (tipe sesi demo produk) bila ada, termasuk asumsi produk yang harus dikonfirmasi | Bank pertanyaan FGD bersama pengguna, atau file pertanyaan pengguna |
| Salin catatan sesi ke | `docs/ba/product/<produk>-<versi>/sessions/<klien>-<tanggal>/` | `docs/ba/demo-sessions/<tanggal>/` |
| Dibaca oleh | `fit-gap` | `ba-grooming` (masukan validasi prototype); `change-request` bila requirement sudah baseline |

Desain Figma tidak bisa disisipi panel karena bukan halaman yang dilayani proxy. Untuk Figma, buat hanya rundown cetak (`scripts/build-script.mjs`) dan lembar catatan berisi tabel kosong per langkah; pembawa membuka prototype Figma di layar seperti biasa.

Setelah sesi, salin unduhan catatan (.md dan .csv dari `/__demo/notes.md` dan `/__demo/notes.csv`) ke folder sesi di atas, lalu kosongkan catatan untuk sesi berikutnya.

## Prinsip

- **Layar dilihat audiens.** Format Demo hanya menampilkan navigasi langkah dan tombol Catatan. Format FGD menampilkan tujuan, yang ditampilkan, dan pertanyaan; menit, pembawa, poin bicara dan instruksi klik ada di **Info pembawa** yang mati secara bawaan.
- **Kode aplikasi tidak diubah.** Perlengkapan demo hidup di folder khusus lokal (proxy, seed, langkah). Yang dipresentasikan sama dengan yang akan dirilis.
- **Data contoh dibuat lewat API/aksi aplikasi itu sendiri, sebagai peran yang benar**, sehingga validasi, hak akses dan isolasi tenant ikut teruji.
- **Setiap peran punya pekerjaan hidup**: transaksi dihentikan di tahap berbeda untuk dikerjakan langsung di depan audiens.
- **Teks langkah dicocokkan dengan layar sebenarnya**: semua langkah dijalani ujung ke ujung sebelum diserahkan.

Komunikasikan dengan bahasa pengguna (default Bahasa Indonesia), hindari jargon teknis tanpa penjelasan singkat.

## Alur kerja

### 1. Kenali sistem
Dari README, dokumentasi, skema, matriks izin/RBAC, rute API dan menu UI, kumpulkan cara menjalankan lokal, **mekanisme identitas** (header gateway, cookie sesi, token Bearer, atau identitas tetap di dev server), peran dan izinnya, tenant/ruang kerja, alur bisnis dari hulu ke hilir, serta aturan yang membatasi seed (tanggal tidak boleh mundur, persetujuan orang kedua, data bawaan, field wajib). Untuk paket tanpa sumber yang jelas (bundle hasil build), REA/reverse-engineering membantu memetakan rute dan aksi.

### 2. Jalankan dan coba sendiri
Kerjakan satu alur utama lewat browser sebagai pengguna biasa. Catat jebakan yang akan membingungkan audiens (pesan error umum, data bawaan, tombol yang tampil tapi ditolak, tampilan HP). Jebakan ini masuk "Catatan untuk pembawa" dan sering juga temuan untuk tim produk.

### 3. Pilih cara berganti peran
| Mekanisme identitas aplikasi | Cara | Catatan |
|---|---|---|
| Header dari gateway/proxy tepercaya | `roles[].headers` di proxy | Paling bersih; tidak ada login. |
| Cookie sesi setelah login | Seed login sekali per peran (akun uji), simpan cookie sesi ke `roles[].cookies` | Pakai akun dan kata sandi uji dari seed/fixture proyek, bukan akun asli. |
| Token Bearer | `roles[].headers.Authorization` | Token uji/dev saja. |
| Dev server dengan identitas tetap | Tambah opsi demo di dev server (file khusus lokal) yang membaca cookie peran, lalu proxy mengisi cookie itu lewat `roles[].cookies` | Lihat `references/contoh-pamanku.md`. |
| Aplikasi satu halaman tanpa login (prototipe) | Satu peran saja; langkah memakai `nav` untuk berpindah layar | Seperti prototipe FIF Pulse. |
| Tidak mungkin diganti otomatis | Info pembawa menyebut akun uji mana untuk login | Daftar akun uji di naskah. |

Jalur pergantian identitas hanya untuk lokal; beri penjaga (mis. tolak saat `NODE_ENV=production`) dan katakan di laporan.

### 4. Seed data demo
Ikuti `references/desain-skenario.md` bagian "Data contoh": nama lokal yang realistis dan satu nama per peran, dua tenant bila multi-tenant (plus satu orang di keduanya), riwayat beberapa minggu relatif hari ini, transaksi di tahap berbeda, "hari ini" kosong untuk diisi langsung, satu celah data yang disengaja bila relevan, dan seed otomatis setiap start.

### 5. Tulis rundown
Ikuti `references/desain-skenario.md`. Rundown berwaktu, nomor mulai **0 (Pembukaan)** sampai penutup. Untuk tiap langkah di `steps.json`: `title`, `min`, `who`, `goal`, `show`, `q` (kode pertanyaan dari daftar), `spot`, lalu untuk pembawa `say` dan `do` (label tombol persis). Format Demo: urutkan langkah mengikuti alur produk dan tempatkan pertanyaan pengguna di langkah yang topiknya cocok. Format FGD: susun langkah di sekitar keputusan yang ingin didapat. Targetkan 8–16 langkah.

### 6. Pasang panduan
Salin `assets/demo-proxy.mjs` dan `assets/presenter-panel.js` ke folder demo proyek (mis. `demo/`) bersama `demo.config.json` (dengan `format`), `steps.json`, `questions.json`, dan `seed.mjs` bila perlu. Jalankan aplikasinya, lalu:
```bash
node demo/demo-proxy.mjs demo/demo.config.json
```
Proxy menyajikan `/demo`, menyisipkan panel ke setiap halaman HTML, dan meneruskan permintaan dengan identitas peran aktif; menyimpan catatan di `demo/catatan-demo.json` atau `demo/catatan-fgd.json` sesuai format. Panel memakai warna utama (bilah) dan warna aksen (nomor aktif, Berikutnya, bingkai sorot) serta jenis huruf aplikasi target; isi `theme.primary`/`theme.accent` bila deteksi meleset atau klien punya warna merek sendiri. Bila aplikasi butuh lebih dari satu proses, buat satu peluncur (`npm run demo`) yang menjalankan aplikasi di port internal lalu proxy di port yang dibuka audiens. Detail di `references/format-konfigurasi.md`.

### 7. Jalani semua langkah sampai selesai
Buka tiap langkah di lebar layar laptop/proyektor dan kerjakan instruksi `do` persis seperti pembawa. Periksa: warna panel menyatu dengan aplikasi, peran/tenant benar, layar dan bagian yang disorot benar, isi aplikasi tidak tertutup panel, label tombol sama, field wajib disebut, hasil langkah terlihat di langkah berikutnya, dan pertanyaan tampil di langkah yang tepat. Pada format FGD, coba tambah/hapus catatan dan unduh .md/.csv. Perbaiki sampai cocok, lalu restart (dan kosongkan catatan uji).

### 8. Buat rundown cetak
```bash
node <skill>/scripts/build-script.mjs demo/demo.config.json [--format demo|fgd] > docs/Rundown.md
```
Mengikuti format: untuk Demo, naskah ini adalah pegangan utama pembawa karena tujuan, poin bicara, instruksi klik dan pertanyaan tidak tampil di layar; FGD menambahkan tabel kosong "Perlu diubah / Sudah diubah" per langkah untuk notulen. Untuk keduanya, buat dua naskah.

### 9. Serahkan
Laporkan singkat: format yang dipakai, perintah memulai, URL `/demo`, tabel rundown (nomor, menit, judul, peran, pertanyaan, langkah yang dikerjakan langsung), apa yang disesuaikan setelah uji coba, tips hari-H (Info pembawa hanya di layar tim; FGD: kosongkan catatan sebelum mulai dan unduh di akhir; audiens bisa masuk bebas lewat WiFi yang sama), dan keterbatasan yang jujur.

## File dalam skill ini
- `references/desain-skenario.md`: struktur rundown untuk kedua format, cara menulis tujuan dan pertanyaan, aturan data contoh.
- `references/format-konfigurasi.md`: format `demo.config.json` (termasuk `format`), `steps.json`, daftar pertanyaan dan impornya, aksi `nav`, tampilan panel dan warna.
- `references/contoh-pamanku.md`: contoh lengkap yang sudah terbukti (aplikasi multi-tenant, 15 peran, dua mode Demo dan FGD).
- `assets/demo-proxy.mjs`: proxy Node tanpa dependency (identitas per peran, sisip panel, catatan FGD).
- `assets/presenter-panel.js`: panel di layar untuk kedua format (Shadow DOM, warna mengikuti aplikasi).
- `scripts/import-questions.mjs`: impor daftar pertanyaan dari .md, .xlsx, .csv, .tsv menjadi `questions.json`.
- `scripts/build-script.mjs`: pembuat rundown Markdown sesuai format.
