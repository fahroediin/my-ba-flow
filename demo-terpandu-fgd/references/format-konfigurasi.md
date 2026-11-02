# Format konfigurasi panduan demo

Letakkan semua file demo di satu folder khusus proyek (mis. `demo/`). Path relatif dihitung dari folder file konfigurasi.

## demo.config.json

```json
{
  "format": "fgd",
  "title": "FIF Pulse · Gamifikasi Sales",
  "client": "FIF",
  "upstream": "http://localhost:3000",
  "port": 4000,
  "home": "/",
  "steps": "steps.json",
  "questions": "questions.json",
  "seed": "seed.mjs",
  "durationMinutes": 120,
  "roles": [
    {"key": "ow", "name": "Bu Sari (Pemilik)", "role": "OW", "group": "Peternakan Demo Banten",
     "headers": {"x-user-id": "demo-ow", "x-user-email": "ow@demo.test"}},
    {"key": "fa", "name": "Joko (Operator Farm)", "role": "FA", "group": "Peternakan Demo Banten",
     "cookies": {"session": "diisi oleh seed.mjs"}}
  ],
  "notes": ["Data demo dibuat ulang setiap proxy dimulai."]
}
```

| Field | Arti |
|---|---|
| `format` | **Wajib**: `"demo"` atau `"fgd"`, sesuai pilihan pengguna. Untuk dua mode, ini format bawaan; jalankan proxy dengan `--format demo` atau `--format fgd` untuk format lain. |
| `title` | Judul di halaman `/demo`, naskah dan file catatan. |
| `client` | Nama klien/peserta. Dipakai pada kolom **Perlu diubah (masukan …)** (format FGD). |
| `upstream` | Alamat aplikasi yang sudah berjalan. Proxy meneruskan semua permintaan ke sini. |
| `port` | Port proxy. Presenter dan peserta membuka `http://<host>:<port>/demo`. |
| `home` | Halaman yang dibuka bila langkah tidak punya `url`. |
| `steps` | File langkah (lihat bawah). |
| `questions` | Daftar pertanyaan berkode, objek `{"A1": "teks", ...}` atau path file JSON hasil `import-questions.mjs`. Dipakai panel FGD dan naskah cetak; format Demo tidak menampilkannya di layar. Bila ada, harus berasal dari file pengguna atau disusun bersama pengguna. |
| `seed` | Opsional. Modul ES `export default async function ({upstream, roles, config})`, dijalankan sebelum proxy menerima permintaan. Boleh mengubah `roles[i].cookies`/`headers` (mis. hasil login akun uji). |
| `notesFile` | Opsional, default `catatan-<format>.json` (`catatan-demo.json` / `catatan-fgd.json`). Tempat proxy menyimpan catatan. Jangan diisi bila memakai dua mode, agar catatan tiap mode terpisah. |
| `roles[].headers` / `roles[].cookies` | Identitas yang dipaksa untuk peran ini (menimpa nilai dari browser dengan nama sama). |
| `roles[].group` | Pengelompokan di `/demo` (biasanya nama tenant). |
| `notes` | Catatan untuk pembawa; masuk ke naskah cetak. |
| `theme` | Opsional. Warna panel (lihat bagian Warna). |

## steps.json

Array langkah. Nomor langkah dimulai dari **0** (Pembukaan), sama seperti tombol nomor di panel.

```json
[
  {
    "title": "Hari kerja sales dan data",
    "min": "18–30",
    "who": "Fahrudin",
    "as": "spv",
    "url": "/manajemen",
    "nav": [{"clickText": "Buat Misi", "within": "aside"}],
    "spot": "#w-job",
    "goal": "Pekerjaan asli sales dan buktinya. Tunjukkan 7 aksi 16/10 sudah tertampung.",
    "show": ["Web: Buat Misi, langkah 1 Pilih pekerjaan asli", "HP: Misi › Pekerjaan hari ini"],
    "q": ["A1", "A2", "D2"],
    "say": ["Mulai dari cerita sehari-hari, bukan dari fitur."],
    "do": "Klik Buat Misi → tunjukkan daftar pekerjaan asli.",
    "placeholder": {"ubah": "Mis. Follow-up belum tercatat", "berubah": "Mis. Pencairan masuk misi"}
  }
]
```

| Field | Tampil ke | Arti |
|---|---|---|
| `title` | Semua | Judul langkah di bilah panel dan tooltip nomor. |
| `goal` | Semua | Satu kalimat tujuan langkah: keputusan atau pemahaman yang ingin dicapai bersama peserta. |
| `show` | Semua | Daftar "Tampilkan": layar/bagian yang diperlihatkan. |
| `q` | Semua | Kode pertanyaan dari bank `questions` (ditampilkan sebagai chip kode + teks). Teks tanpa kode juga boleh. |
| `min` | Pembawa | Rentang menit di rundown (mis. `"18–30"`). |
| `who` | Pembawa | Nama pembawa langkah. |
| `say` | Pembawa | Poin bicara. |
| `do` | Pembawa | Instruksi klik dengan label tombol persis seperti di layar. |
| `act` | `/demo` | Opsional: nama babak untuk pengelompokan di halaman `/demo`. |
| `as` | – | `key` peran dari konfigurasi; langkah ini dibuka sebagai peran itu. |
| `url` | – | Halaman yang dibuka saat langkah dimulai. |
| `nav` | – | Aksi otomatis menyiapkan layar (lihat bawah). |
| `spot` | – | Selector bagian layar yang disorot (bingkai warna aksen, sisanya diredupkan). |
| `placeholder` | Semua | Opsional: contoh isian untuk kolom catatan `ubah` dan `berubah` (FGD) atau `catatan` (Demo). |

"Pembawa" berarti hanya tampil saat sakelar **Info pembawa** dinyalakan. Sakelar ini mati secara bawaan karena layar presentasi dilihat klien.

### Aksi `nav`

Setiap aksi menunggu elemennya muncul (maks. 8 detik) lalu dijalankan berurutan. Untuk aplikasi dengan URL per halaman cukup isi `url`.

| Aksi | Contoh | Efek |
|---|---|---|
| `select` + `option` | `{"select": "#tenant", "option": "Cabang Serang", "rerender": "[data-page]"}` | Memilih opsi yang teksnya diawali `option`, memicu `change`; `rerender` menunggu elemen itu digambar ulang. |
| `click` | `{"click": "[data-page=orders]"}` | Klik elemen pertama yang cocok; dilewati jika sudah `active`/`aria-current`. |
| `clickText` | `{"clickText": "Pesanan", "within": "nav"}` | Klik tombol/tautan dengan teks persis. |
| `fill` + `value` | `{"fill": "#search", "value": "Toko Berkah"}` | Mengisi input untuk menyiapkan tampilan. |
| `waitFor` | `{"waitFor": ".table-loaded"}` | Menunggu elemen muncul. |
| `wait` | `{"wait": 500}` | Jeda milidetik. |

## Daftar pertanyaan dari pengguna

```bash
node <skill>/scripts/import-questions.mjs pertanyaan.xlsx --out demo/questions.json --sheet "Persiapan"
```

| Sumber | Yang dibaca |
|---|---|
| Excel `.xlsx`/`.xlsm` | Sheet pertama (atau `--sheet`). Baris judul di atas tabel dilewati; header dicari dari kolom bernama Pertanyaan/Question/Soal. |
| `.csv` / `.tsv` | Pemisah koma, titik koma (Excel berbahasa Indonesia) atau tab dideteksi otomatis. |
| Markdown `.md` | Tabel dengan kolom Pertanyaan; atau judul `##` sebagai topik dengan butir `- A1: teks`, `- **A1** teks`, `1. teks`. Paragraf biasa diabaikan. |
| Google Sheets | Unduh lewat File › Download sebagai .xlsx atau .csv. |

Kolom opsional: **Kode** (Kode/Code/No/ID) dan **Topik** (Langkah/Step/Topik/Bagian/Fitur/Modul/Menu/Halaman/Tema/Kategori). Tanpa kode, pertanyaan diberi Q1, Q2, …. Hasil: `questions.json` berisi `{kode: pertanyaan}`, dan ringkasan JSON di stdout (kode, pertanyaan, topik, baris) untuk memetakan pertanyaan ke `steps[].q`.

## Panel di layar

Judul panel **Panduan Demo** (format demo) atau **Panduan FGD** (format fgd). Warna, sorot otomatis dan navigasi sama untuk keduanya.

Format **demo** sengaja ringkas, satu baris di bawah layar: judul, tombol nomor langkah 0…n (badge jumlah catatan), judul langkah, **‹ Sebelumnya / Berikutnya ›**, tombol **Catatan** dan **×**. Tujuan, Tampilkan, pertanyaan dan Info pembawa tidak tampil (ada di naskah cetak), dan bagian layar `spot` selalu disorot. **Catatan** membuka laci berisi satu kolom tulis untuk langkah aktif, daftar catatannya, dan tautan unduh .md/.csv; laci tertutup secara bawaan dan statusnya diingat browser.

Format **fgd** mengikuti Panduan FGD FIF:
- **Bilah** (warna utama aplikasi): judul "Panduan FGD", tombol nomor langkah 0…n dengan badge jumlah catatan, judul langkah, sakelar **Info pembawa** dan **Sorot**, **‹ Sebelumnya / Berikutnya ›** (warna aksen), **▾** perkecil, **×** tutup (muncul tombol kecil "Buka panduan").
- **Isi tiga kolom**: tujuan + Tampilkan + pertanyaan (+ kotak Info pembawa) · **Perlu diubah (masukan {client})** · **Sudah diubah / disepakati**. Langkah terakhir menampilkan ringkasan catatan seluruh sesi.
- **Kaki**: jumlah catatan, **Unduh catatan (.md)**, **Unduh (.csv)**, **Kosongkan catatan**.
- Panel menempel di bawah layar dan memberi ruang di bawah halaman agar isi aplikasi tidak tertutup. Panel berada di Shadow DOM sehingga CSS aplikasi tidak memengaruhinya.
- Catatan disimpan proxy di `notesFile`, sehingga tetap ada saat halaman dimuat ulang atau peran berganti, dan bisa diunduh dari `/demo`.

### Warna

- **Warna utama** (bilah, judul tujuan): `theme.primary`, atau dideteksi dari variabel CSS umum (`--primary`, `--color-primary`, `--brand`, `--navy`, `--blue`, `--bs-primary`, `--mdc-theme-primary`, `--mui-palette-primary-main`, …), `<meta name="theme-color">`, lalu warna latar tersaturasi yang paling sering pada tombol/menu/header.
- **Warna aksen** (nomor aktif, Berikutnya, bingkai sorot, garis atas panel): `theme.accent`, atau variabel `--accent`, `--secondary`, `--orange`, `--bs-warning`, …, atau warna tersaturasi berikutnya yang huenya berbeda jauh dari warna utama; bila tidak ada, amber.
- Teks di atas warna utama/aksen otomatis putih atau hitam sesuai keterbacaan (putih diutamakan bila kontras ≥ 4,5:1). Jenis huruf mengikuti `body` aplikasi.

```json
"theme": {"primary": "#0E3F70", "accent": "#F5A524", "font": "Inter, sans-serif"}
```

## Rute proxy

| Rute | Fungsi |
|---|---|
| `/demo` | Daftar langkah, tombol mulai, unduh catatan, daftar peran untuk masuk bebas. |
| `/demo?step=N` | Membuka langkah N (mulai 0). |

Menjalankan: `node demo-proxy.mjs demo.config.json [--format demo|fgd]`.
| `/demo?as=KEY` | Masuk bebas sebagai peran (panel menjadi tombol kecil "Ganti peran"). |
| `/__demo/notes.md`, `/__demo/notes.csv` | Unduhan catatan sesi. |
| `/__demo/panel.js`, `/__demo/state`, `/__demo/notes` | Dipakai panel. |

Keterbatasan: WebSocket (mis. hot reload) tidak diteruskan; proxy hanya untuk jaringan lokal saat demo.
