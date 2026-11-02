# Dua Model Kerja BA: Product Based dan Project Based — Design Spec

- Tanggal: 2026-11-02
- Repo: `my-ba-flow` (`C:\Users\User\Documents\Github_Fahrudin\SERVICES\my-ba-flow`)
- Contoh nyata: PamanKu v6.0 (aplikasi peternakan ayam petelur buatan CEO) dan skill `demo-terpandu-fgd` yang dibuat saat menyiapkan demo PamanKu
- Status: draf, menunggu persetujuan pengguna

## 1. Latar belakang dan tujuan

CEO perusahaan (Pak Tan Gwan An) membuat aplikasi sendiri dengan bantuan AI ("vibe code"), contohnya PamanKu. Ia ingin setiap aplikasi buatannya didampingi seorang BA yang menjelaskannya ke calon klien. Ini pekerjaan baru bagi tim BA. Pekerjaan BA yang biasa adalah membangun aplikasi dari nol untuk klien, dan bila klien butuh cepat, tim menyerahkan mockup, desain Figma dengan user flow, atau prototype.

Jadi ada dua model kerja:

| | Project based (pekerjaan biasa) | Product based (pekerjaan baru) |
|---|---|---|
| Titik awal | Kebutuhan klien; belum ada aplikasi | Aplikasi sudah jadi; dicarikan klien |
| Pembuat aplikasi | Tim pengguna (BA, desainer, engineer) | Pak Tan (mis. PamanKu), atau BA sendiri (mis. tester-lab) |
| Bahan awal BA | Profil klien, notulen, KAK/TOR, dokumen klien | File zip/rar berisi source code aplikasi, plus profil calon klien |
| Langkah awal BA | Gali kebutuhan, siapkan mockup/Figma/prototype | Pahami produknya, peragakan ke calon klien |

**Kedua model berakhir di tempat yang sama: project based.** Di product based, calon klien yang tertarik biasanya minta penyesuaian; selisih antara kebutuhan klien dan produk menjadi kebutuhan sebuah proyek. Titik temu kedua model adalah **fit-gap**.

Tujuan pekerjaan ini: **memudahkan pekerjaan BA** di kedua model, dengan memperluas plugin `my-ba-flow` yang sudah ada, bukan membuat plugin baru.

Kriteria berhasil:

1. Saat BA memulai pekerjaan, Claude menanyakan modelnya (product atau project) dan mengarahkan ke langkah yang benar tanpa BA harus ingat urutan skill.
2. Untuk product based, BA cukup memberi file zip/rar dan profil calon klien. Claude menjalankan aplikasinya secara lokal, lalu menghasilkan ringkasan produk yang bisa dipakai BA untuk menjelaskan ke klien, termasuk daftar hal yang masih asumsi.
3. Panduan demo/FGD bisa dipakai di kedua model: memperagakan aplikasi jadi (product) atau prototype (project).
4. Setelah demo, BA mendapat matriks fit-gap yang langsung menjadi masukan proyek, dan sejak titik itu semua dokumen mengikuti BA Handbook.
5. Tidak ada dua skill yang berebut pemicu yang sama.

## 2. Keputusan pengguna (sudah disepakati)

1. Masukkan ke `my-ba-flow`, bukan flow atau plugin terpisah.
2. Skill panduan demo/FGD dipakai di kedua model.
3. Bahan product based selalu berupa file zip/rar berisi source code.
4. Product based memakai **format ringan** sampai titik fit-gap. Begitu masuk proyek, semua mengikuti BA Handbook.
5. Ujung kedua model adalah project based.
6. Urusan pengembangan lanjutan produk (siapa yang mengubah aplikasi, umpan balik ke Pak Tan) **di luar cakupan**. Fokusnya memudahkan pekerjaan BA.
7. Proyek dari product based dikerjakan di folder/repo terpisah per klien.
8. Skill mandiri `demo-terpandu-fgd` di `~/.claude/skills` boleh dihapus setelah plugin versi baru terpasang.

## 3. Non-goals dan anti-goals

Di luar cakupan:

- Alur umpan balik ke pembuat produk (Pak Tan) dan pengelolaan versi produk berikutnya.
- Proposal harga, penawaran, dan estimasi biaya.
- Mengubah kode aplikasi yang didemokan. Perlengkapan demo tetap di folder khusus lokal, sesuai prinsip skill demo.
- Membuat prototype atau Figma (tetap pekerjaan tim; workflow ini hanya memakainya).

Anti-goals (dianggap gagal walau secara teknis berjalan):

- BA menjanjikan ke klien fitur atau aturan bisnis yang ternyata hanya asumsi model AI pembuatnya. Setiap aturan hasil membaca kode harus berlabel sampai dikonfirmasi.
- Dokumen berat ala Handbook dibuat sebelum klien tertarik.
- Skill baru menduplikasi isi skill lama (mis. menulis ulang daftar pertanyaan discovery atau aturan reverse engineering).

## 4. Alur keseluruhan

```
                         ba-start (tanya model)
                     ┌───────────┴────────────┐
             PRODUCT BASED               PROJECT BASED
     (format ringan, docs/ba/product/)   (BA Handbook sejak awal)
                     │                        │
         product-onboarding              discovery-meeting-prep
         (zip → jalan lokal →            → ba-planning → stakeholder-interview
          ringkasan produk)              → requirement-elicitation → ...
                     │                        │
         discovery-meeting-prep          wireframe-spec / mockup / Figma / prototype
         (tipe sesi baru: demo produk)        │
                     │                   demo-terpandu-fgd (validasi prototype)
         demo-terpandu-fgd                    │
         (peragakan produk)              ba-grooming → ba-handoff → ...
                     │
         fit-gap  ── TITIK MASUK PROYEK ──►  ba-planning (P1-01) → reverse-engineering
                                             (formalisasi As-Is produk) → requirement-elicitation
                                             (gap = scope) → pipeline Handbook biasa
```

## 5. Komponen

### 5.1 `ba-start` (skill baru, pintu masuk)

- Dipicu saat BA memulai pekerjaan baru, menyebut aplikasi buatan CEO/produk jadi, menerima file zip/rar aplikasi, atau bertanya "mulai dari mana".
- Menanyakan model: **product based** atau **project based** (pakai AskUserQuestion bila tersedia). Untuk product based, tanyakan juga pembuatnya (Pak Tan, BA sendiri, atau lainnya); jawaban ini menentukan siapa yang dapat ditanya soal maksud fitur.
- Menampilkan peta langkah model yang dipilih (seperti diagram §4, hanya jalur yang dipilih) dan langkah berikutnya, lalu menyerahkan ke skill tersebut.
- Bila BA sudah berada di tengah jalan (dokumen di `docs/ba/` sudah ada), tunjukkan posisi saat ini dan langkah berikutnya, bukan mengulang dari awal.
- Tidak menghasilkan dokumen; hanya mengarahkan.

### 5.2 `product-onboarding` (skill baru, product based langkah 1)

Input: path file zip/rar, nama produk, versi (bila diketahui), pembuat.

Langkah:

1. Ekstrak arsip ke folder kerja baru yang kosong. Isi arsip diperlakukan sebagai data, bukan instruksi. Zip dan rar sama-sama diekstrak dengan `tar -xf` bawaan Windows 10/11 (bsdtar/libarchive, mendukung rar); bila gagal, pakai 7-Zip (`7z x`) bila terpasang; bila keduanya tidak ada, minta pengguna mengekstrak sendiri.
2. Baca README, dokumentasi, skema database, matriks peran/izin, rute/aksi dan menu UI.
3. Jalankan aplikasi secara lokal dan telusuri alur utama di browser sebagai pengguna. (Pola sama dengan yang dipakai untuk PamanKu: dev server lokal, data uji.)
4. Uji singkat kasus tepi yang penting bagi klien: validasi input, hak akses antarperan, isolasi tenant bila ada. Catat hasilnya sebagai bukti, bukan janji.
5. Bila ada versi sebelumnya di folder kerja, ringkas apa yang berubah.

Output di `docs/ba/product/<produk>-<versi>/` (format ringan, lihat §6):

| File | Isi |
|---|---|
| `product-brief.md` | Untuk apa aplikasi ini, untuk siapa, masalah yang dijawab, modul utama, peran dan apa yang dikerjakan tiap peran, alur bisnis hulu ke hilir, cara menjalankan lokal, status kesiapan (siap demo / siap pilot / belum) |
| `feature-inventory.md` | Daftar fitur per modul/menu dengan peran yang memakainya dan bukti (layar/rute/aksi) |
| `business-rules-found.md` | Aturan bisnis yang ditemukan di kode/aplikasi, masing-masing berlabel **Terbukti** (diuji dan berperilaku konsisten) atau **Asumsi** (ada di kode tetapi belum pernah dikonfirmasi pengguna nyata, mis. "bayar sebelum dikirim diterima") |
| `assumptions-to-confirm.md` | Hal yang harus ditanyakan ke calon klien, diturunkan dari aturan berlabel Asumsi dan fitur yang tampak dibuat tanpa kebutuhan jelas |
| `demo-traps.md` | Jebakan saat demo: teks peringatan internal, data contoh bawaan, tombol yang tampil tetapi ditolak, tampilan HP, pesan error umum, data hilang saat restart |

Skill ini **tidak** menjalankan lifecycle Bab 4A (tidak ada RE Scope Statement, tidak ada sign-off). Itu terjadi nanti di §5.5 bila produk masuk proyek.

### 5.3 `discovery-meeting-prep` (skill lama, diperluas)

Tambah tipe sesi keempat: **Demo produk ke calon klien (product based)**.

- Konteks wajib: `product-brief.md` dan `assumptions-to-confirm.md`.
- Pertanyaan diambil dari bank yang sudah ada (Core A, As-Is lebih dulu), ditambah modul baru di `references/question-bank.md` untuk kecocokan produk: proses klien yang paling dekat dengan modul produk, data yang sudah ada, peran di sisi klien, dan konfirmasi setiap asumsi.
- Red flag tambahan: klien berharap produk dipakai apa adanya padahal prosesnya jauh berbeda; klien memutuskan dari tampilan, bukan alur.
- Untuk tipe sesi ini, prep sheet dan debrief **tidak** menulis ke register Handbook di `docs/ba/` (klien belum tentu lanjut). Semuanya ditulis ke `docs/ba/product/<produk>-<versi>/sessions/<klien>-<tanggal>/`: `meeting-prep.md`, `debrief.md` (pain points, asumsi klien, status setiap asumsi produk: dikonfirmasi / dibantah / belum). Tipe sesi lain tidak berubah.

### 5.4 `demo-terpandu-fgd` (dipindah ke plugin)

Skill yang sudah ada (`~/.claude/skills/demo-terpandu-fgd`) dipindah ke repo sebagai skill plugin dengan isi yang sama (SKILL.md, `references/`, `assets/` proxy dan panel, `scripts/` pengimpor pertanyaan dan pembuat rundown). Perilakunya tetap: format Demo (panel ringkas: langkah, Sebelumnya/Berikutnya, Catatan), FGD (format Panduan FGD FIF), atau keduanya.

Penyesuaian:

- **Product based:** membaca `product-brief.md`, `feature-inventory.md` dan `demo-traps.md` sebagai bahan langkah dan catatan pembawa; pertanyaan diambil dari prep sheet `discovery-meeting-prep` bila ada.
- **Project based:** memperagakan prototype yang berjalan sebagai web (HTML/React/dll.). Untuk desain Figma yang tidak bisa disisipi panel, skill hanya menghasilkan rundown cetak dan lembar catatan (tanpa panel di layar). Ini keputusan penulis spec; lihat §9.
- Catatan sesi (`catatan-demo.json` / `catatan-fgd.json`, unduhan .md/.csv) disalin ke folder sesi:
  - product based: `docs/ba/product/<produk>-<versi>/sessions/<klien>-<tanggal>/`, dibaca `fit-gap`;
  - project based: `docs/ba/demo-sessions/<tanggal>/`, dibaca `ba-grooming` (masukan validasi prototype) dan menjadi bahan `change-request` bila requirement sudah baseline.
- Konvensi tulisan repo (tanpa em dash, tanpa emoji) berlaku untuk SKILL.md dan referensinya. Satu em dash yang ada di `references/desain-skenario.md` diganti.

### 5.5 `fit-gap` (skill baru, titik masuk proyek)

Input: `feature-inventory.md`, `business-rules-found.md`, `assumptions-to-confirm.md`, prep sheet dan debrief dari `discovery-meeting-prep`, catatan sesi demo/FGD.

Output `docs/ba/product/<produk>-<versi>/fit-gap-<klien>.md` (format ringan):

| Kebutuhan klien | Sumber (debrief/catatan langkah N) | Status | Bukti di produk | Catatan |
|---|---|---|---|---|

Status: **Fit** (dipakai apa adanya), **Fit dengan konfigurasi** (cukup pengaturan/data master), **Gap kecil**, **Gap besar**, **Tidak dibutuhkan** (fitur produk yang klien tidak perlu). Ditambah:

- Status akhir setiap asumsi produk (dikonfirmasi / dibantah / belum).
- Ringkasan: jumlah per status, gap yang menentukan keputusan, dan rekomendasi lanjut atau tidak.

Ketika pengguna menyatakan klien lanjut (**titik masuk proyek**), proyek dikerjakan di **folder atau repo baru per klien** (keputusan pengguna). Skill menawarkan membuat folder proyek itu, menyalin `fit-gap-<klien>.md`, folder sesi klien tersebut dan hasil `product-onboarding` ke `docs/ba/product-input/` di folder baru, lalu menyerahkan ke pipeline Handbook yang berjalan di folder proyek dengan jalur `docs/ba/` biasa (skill lama tidak perlu subfolder per klien):

1. `ba-planning` (gerbang wajib, Rule P1-01) dengan fit-gap sebagai konteks dan gap sebagai calon scope.
2. `reverse-engineering` untuk memformalkan As-Is produk sesuai Bab 4A, **dijalankan penuh** (RE Scope Statement, persetujuan BA Lead, sign-off), karena sejak titik ini Handbook berlaku. Yang berubah hanya sumbernya: tambahkan ke skill itu satu bagian "Input dari product based" yang menyebut hasil `product-onboarding` dan debrief sebagai bahan Phase 1–3, dengan pemetaan Confidence Level:
   - aturan Terbukti di kode **dan** dikonfirmasi klien (dua sumber) → High;
   - satu sumber saja (Terbukti di kode, atau Asumsi yang dikonfirmasi klien) → Medium;
   - Asumsi yang belum dikonfirmasi → Low;
   - Asumsi yang dibantah klien → tidak masuk baseline; menjadi gap.
   `fit-gap-<klien>.md` menjadi masukan Gap Report RE (`docs/ba/gap-analysis.md`), bukan penggantinya: fit-gap berbahasa klien dan ringan, Gap Report adalah dokumen formal Handbook.
3. `requirement-elicitation` dengan gap sebagai kebutuhan proyek, lalu pipeline biasa.

### 5.6 Jalur project based

Pipeline Handbook yang sudah ada tidak berubah. Penambahan hanya:

- `ba-start` sebagai pintu masuk.
- Rujukan ke `demo-terpandu-fgd` untuk memvalidasi mockup/prototype dengan klien sebelum `ba-grooming`/`ba-handoff`, dicantumkan di bagian Handoff skill `wireframe-spec` dan di README.

## 6. Format ringan (product based sebelum titik masuk proyek)

- Tanpa template resmi Handbook dan tanpa alur sign-off.
- Tetap: header singkat (`**Produk:**`, `**Versi:**`, `**Tanggal:**`, `**Disusun:**`) dengan dua spasi di akhir baris, satu baris "Disusun dengan bantuan AI, ditinjau oleh BA: (nama)" (semangat Rule AI-01 tanpa Revision History penuh), tanpa em dash, tanpa emoji, bahasa Indonesia untuk dokumen yang bisa sampai ke klien.
- Label Terbukti/Asumsi wajib pada setiap aturan bisnis dan klaim kemampuan produk.

## 7. Struktur folder kerja

```
<folder kerja BA untuk produk>/
├── <produk>-<versi>/            hasil ekstrak zip/rar (tidak diubah, kecuali folder demo/)
└── docs/ba/
    ├── product/<produk>-<versi>/
    │   ├── product-brief.md, feature-inventory.md, business-rules-found.md,
    │   │   assumptions-to-confirm.md, demo-traps.md
    │   ├── sessions/<klien>-<tanggal>/   (catatan demo/FGD)
    │   └── fit-gap-<klien>.md

<folder proyek per klien>/          dibuat saat titik masuk proyek
└── docs/ba/
    ├── product-input/             salinan fit-gap, sesi klien, hasil product-onboarding
    └── dokumen Handbook biasa: ba-work-plan.md, re-scope.md, brd.md, ...
```

## 8. Pengemasan dan pengujian

- Skill baru di akar repo seperti skill lain: `ba-start/`, `product-onboarding/`, `fit-gap/`, `demo-terpandu-fgd/`.
- Tambahkan keempatnya ke `SKILLS` di `tools/build_plugin.py`.
- README: tambah bagian "Dua model kerja" dengan diagram §4, perbarui daftar on-ramp dan tabel output.
- `plugin.json`: versi 1.4.0; deskripsi dan keywords menyebut product based/demo/FGD.
- Tes per skill baru, mengikuti pola `tests/test_skill_md.py`: frontmatter `name` dan frasa pemicu di `description`, semua rujukan `references/`/`scripts/`/`assets/` ada, tanpa emoji dan em dash. Tes `build_plugin` memastikan keempat skill ikut terkemas.
- Untuk `demo-terpandu-fgd`: jalankan tes yang sudah dibuktikan saat pengembangan (proxy menolak tanpa format, panel Demo satu baris, catatan per format terpisah) bila memungkinkan sebagai tes Node ringan; minimal `node --check` untuk semua .mjs/.js.
- Setelah plugin 1.4.0 terpasang dan skill `demo-terpandu-fgd` dari plugin terbukti muncul, skill mandiri `~/.claude/skills/demo-terpandu-fgd` dihapus agar tidak ada dua skill dengan pemicu sama (disetujui pengguna; cadangan `.skill` ada di folder Egg Farm).

## 9. Keputusan penulis spec (silakan dikoreksi)

1. Nama skill: `ba-start`, `product-onboarding`, `fit-gap`; `demo-terpandu-fgd` tetap memakai nama lamanya.
2. `product-onboarding` dan `fit-gap` adalah skill terpisah, bukan satu skill product based besar, agar tiap langkah bisa dipanggil sendiri (mis. fit-gap ulang setelah demo kedua).
3. Untuk Figma, panduan demo hanya menghasilkan rundown cetak dan lembar catatan, tanpa panel di layar.
4. Instruksi di SKILL.md ditulis dalam bahasa Inggris seperti skill lain di repo; dokumen output dan bank pertanyaan dalam bahasa Indonesia. Pengecualian: `demo-terpandu-fgd` tetap berbahasa Indonesia seperti aslinya.
5. Folder output product based di `docs/ba/product/<produk>-<versi>/`.
6. Untuk memenuhi kriteria 5 (tidak ada pemicu berebut), builder boleh menyunting **hanya baris `description`** skill lama yang bertabrakan (`product-discovery`, `reverse-engineering`) dan menambah bagian "Input dari product based" di `reverse-engineering` (§5.5). Isi langkah skill lama tidak diubah.
7. `fit-gap` hanya untuk product based. Project based tidak memakainya; masukan demo prototype masuk `ba-grooming`.
8. Arsip zip/rar diekstrak dengan `tar` bawaan Windows, cadangan 7-Zip (sudah dicek: bsdtar 3.8.9 dan 7-Zip ada di mesin pengguna).

## 10. Diserahkan ke builder

- Isi detail modul pertanyaan "kecocokan produk" di bank pertanyaan (dengan ID sesuai pola bank yang ada).
- Teknik menjalankan aplikasi lokal per jenis stack (cukup pola umum dan contoh PamanKu sebagai referensi).
- Format pasti tabel di setiap file output, selama memuat kolom yang disebut di §5.
- Cara `ba-start` mendeteksi posisi BA di tengah jalan (mis. dari file yang ada di `docs/ba/`).
