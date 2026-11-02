# Contoh terbukti: PamanKu v6.0 (dua mode: Demo dan FGD)

Aplikasi operasional usaha ayam petelur (kandang → produksi → mutu → stok depo → pesanan → kirim → bayar → keluhan). Satu Worker JavaScript dengan SQLite/D1; identitas dari header gateway `oai-authenticated-user-id` dan `oai-authenticated-user-email`. Multi-tenant (ruang kerja per pemilik), 13 peran RBAC.

Lokasi di mesin pengguna (jika masih ada): `C:\Users\User\Documents\Work\Egg Farm\pamanku-v6.0.0\web`
- `scripts/dev-demo.mjs`: 15 identitas demo (13 peran di Peternakan Demo Banten + pemilik dan operator Peternakan Maju Serang) dan seed lewat `worker.fetch`.
- `scripts/dev-team.mjs --demo`: dev server yang memakai identitas dari cookie `pamanku_demo` dan menjalankan seed.
- `scripts/demo-launch.mjs demo|fgd` (`npm run demo` / `npm run fgd`): menjalankan dev server di port 3100 lalu `demo/demo-proxy.mjs demo/demo.config.json --format <mode>` di port 3000. Catatan: dev server membaca `PORT` lebih dulu daripada `--port`, jadi peluncur memberi `PORT` sendiri ke proses anak.
- `demo/demo.config.json`: `format: "fgd"` (bawaan; mode Demo lewat `--format demo`), tanpa `notesFile` sehingga catatan terpisah di `catatan-demo.json` dan `catatan-fgd.json`, `roles[].cookies: {pamanku_demo: <key>}`, `theme` cokelat `#704529` + kuning `#f8c54b` (nama variabel `--brown`/`--yellow` tidak terdeteksi otomatis).
- `demo/steps.json` (16 langkah 0–15, 90 menit, dipakai kedua mode; naskah `Rundown-Demo-…md` dan `Rundown-FGD-…md` dibuat dari file yang sama) dan `demo/questions.json` (A pekerjaan kandang, B mutu, C penjualan-kirim-bayar, D peran-data, E ukuran berhasil, K kepatuhan, P2 cadangan).

## Keputusan yang terbukti berguna

- **Seed lewat API dengan identitas per peran**: pemilik membuat ruang kerja → mengundang peran → masing-masing bergabung dengan token → pemilik melengkapi master kandang → operator mencatat 29 hari produksi → petugas mutu meloloskan batch lama → penjualan membuat 5 pesanan → depo/koordinator/kurir/keuangan/layanan pelanggan memajukan masing-masing ke tahap berbeda. ±0,5 detik.
- **Tenant kedua** dengan pemilik dan operator sendiri, plus auditor di kedua tenant (langkah 1–2 memperlihatkan isolasi dan pergantian tenant, 2.801 vs 3.621 ekor).
- **Celah data sengaja** (satu kandang dilewati tiap hari ke-4) dan **hari ini dikosongkan** untuk input langsung.
- **Sorot**: `#app .cards` untuk kartu ringkasan, `#app table` untuk tabel, `#teamSelect` untuk pergantian ruang kerja. Navigasi: `{"select":"#teamSelect","option":"<nama usaha>","rerender":"[data-page]"}` lalu `{"click":"[data-page=\"orders\"]"}`.

## Jebakan yang ditemukan saat uji coba

- Ruang kerja baru berisi kandang bawaan kosong; nama yang sama ditolak dengan pesan umum "tidak valid atau duplikat". Seed mengisi kandang bawaan.
- "Tanggal kirim tidak boleh mundur": semua pesanan contoh bertanggal hari ini, tahapnya yang dibedakan.
- Kategori pelanggan tidak valid diam-diam jatuh ke default; cek nilai yang diizinkan.
- Form timbang mewajibkan "Catatan pemeriksaan"; keluhan ditampilkan dengan isi keluhan, bukan nama pelanggan; audit menampilkan ID akun.
- Tampilan HP melebar (scrollWidth 1478px pada 375px); presentasi utama pakai laptop.
- Tombol aksi tetap tampil pada pesanan selesai dan ditolak server bila diklik.
- Bilah format Demo harus muat satu baris di 1280px dengan 16 langkah: judul langkah diberi `flex-basis` kecil agar dipotong (…), bukan mendorong tombol × ke baris kedua.
- Panel dibaca proxy saat start; setelah mengubah `presenter-panel.js`, restart proxy.
