# Skill us-ac-writer — Design Spec

- Tanggal: 2026-10-09
- Repo: `my-ba-flow`, branch `us-ac-writer`
- Sumber aturan: BA Handbook v2.1, `Template/SysFunc_US_AC_Guide.md` dan `Appendix_D_Panduan_Praktik_US_AC.md`

## 1. Tujuan

Skill yang menulis User Story (US) dan Acceptance Criteria (AC) mengikuti system prompt US/AC milik pengguna, tanpa pengguna perlu memerintahkan "ikuti aturan system prompt US/AC saya" setiap kali.

Masalah yang diselesaikan:

- Aturan US/AC hanya ada sebagai prompt di handbook; setiap kali dipakai harus ditempel atau disebut ulang.
- Pipeline `my-ba-flow` tidak punya langkah penulisan US/AC. `product-discovery` hanya membuat draf tingkat skenario dan menyebut "the pipeline refines the full Given/When/Then later", tetapi tidak ada skill yang melakukannya. `ba-grooming` hanya mereview.

Kriteria berhasil:

1. Setiap US/AC yang dihasilkan memenuhi seluruh aturan `SysFunc_US_AC_Guide` tanpa diingatkan.
2. Hasil tampil per US (US lalu AC-nya) dan dapat ditempel ke xlsx dua sheet tanpa sel pecah.
3. Penomoran melanjutkan US/AC yang sudah ada; fitur yang sudah tercakup US lama tidak dibuatkan US baru.
4. Salinan aturan di skill tidak bisa diam-diam menyimpang dari handbook.

Di luar cakupan: menulis langsung ke file xlsx; perbaikan sembilan ketidaksesuaian skill lama terhadap handbook v2.1 (pekerjaan terpisah).

## 2. Input

Skill menerima kombinasi apa pun dari:

- Minutes of Meeting (MoM)
- penjelasan naratif di chat
- screenshot atau mockup UI
- dokumen BA di `docs/ba/` (`brd.md`, `business-rules.md`, `process-map-*.md`, draf `product-discovery`)
- daftar US/AC yang sudah ada (`docs/ba/us-ac.md`, atau tabel yang ditempel pengguna)

## 3. Alur kerja

1. **Kumpulkan konteks.** Baca semua input yang tersedia, lalu isi empat input Tahap 1 SysFunc: nama fitur/modul, tujuan bisnis, persona utama, aksi kunci. Yang belum terjawab ditanyakan satu per satu, masing-masing dengan usulan jawaban.
2. **Cek US existing.** Bila ada US/AC lama, tentukan apakah aksi baru sudah tercakup US lama. Jika ya, tambahkan AC di bawah US tersebut. Nomor US dan AC melanjutkan nomor terakhir.
3. **Vertical slicing.** Bila satu US mencakup lebih dari 3 aksi CRUD atau lebih dari 1 sprint, usulkan pemecahan dan minta persetujuan sebelum lanjut.
4. **Tulis US.** Kolom sesuai §4. Aksi tanpa kata "bisa"/"dapat"; hasil nilai bisnis tanpa "agar"/"untuk". Validasi INVEST; perbaiki US yang gagal sebelum menulis AC.
5. **Pilih format AC per US.** Variabel input/output ≤ 3 dan kombinasi logika ≤ 3: Given/When/Then. Selain itu: AC berisi rujukan `Refer to MRTM Rows: <TCID awal> through <TCID akhir> ...` dan tabel MRTM.
6. **Tulis AC.** Wajib minimal satu Happy, satu Negative/Validation, satu Boundary/Edge; State Transition dan Permission bila relevan. GIVEN menyebut halaman; WHEN hanya aksi user tanpa `OR`; THEN observable dengan teks verbatim; hasil sistem di tengah aksi memecah AC.
7. **Checklist sebelum serah** (dijalankan oleh LLM terhadap draf, bukan skrip):
   - WHEN tidak memuat hasil sistem ("aktif", "terbuka", "muncul", "berubah", "menampilkan", "sistem …") dan tidak memuat `OR`
   - satu THEN per AC (Rule P3-01)
   - boundary values dan edge case eksplisit (Rule RE-04)
   - kategori skenario lengkap per US
   - ID konsisten: `US-XX`, `AC-XX.YY`, `TRM_[MODUL]_XXX`
   - tanpa emoji dan tanpa kata "bisa/dapat/agar/untuk" di kolom yang dilarang

   Pelanggaran diperbaiki sebelum hasil ditampilkan.
8. **Serahkan.** Tampilkan hasil per US di chat, tulis/tambahkan ke `docs/ba/us-ac.md`, jalankan `scripts/us_ac_to_tsv.py` untuk TSV, lalu tampilkan daftar pertanyaan terbuka dan saran lanjut ke `ba-grooming`.

## 4. Format keluaran

### 4.1 Susunan per US (chat dan `docs/ba/us-ac.md`)

```markdown
## US-06: Menambahkan Sertifikat Talent

| Persona | Aksi yang dilakukan | Hasil nilai bisnis |
|---|---|---|
| Manager | menambahkan data sertifikat baru ke profil talent | data kualifikasi talent selalu lengkap dan terbaru |

### Acceptance Criteria US-06

| AC-ID | Skenario | GIVEN | WHEN | THEN | Status |
|---|---|---|---|---|---|
| AC-06.01 | Happy: Menambahkan sertifikat dengan data valid | Saya seorang Manager<br>AND saya berada di halaman "Detail Talent" | Saya mengklik tombol "Tambah Sertifikat"<br>AND ... | Sistem menampilkan notifikasi "..."<br>AND ... | Draft |

### MRTM US-06   (hanya bila dipakai)

| User Story ID | Acceptance Criteria ID | User | Test Case ID | <Variabel 1> | ... | Kondisi Khusus | HASIL (EXPECTED RESULT) |
```

- Judul US memakai format Kata Kerja + Objek.
- Kolom Skenario diawali kategori: `Happy:`, `Negative:`, `Boundary:`, `Edge:`, `State:`, `Permission:`.
- Status AC baru selalu `Draft` (siklus status Bab 5: Draft, Reviewed, Approved).
- Di `.md`, baris AND dipisah `<br>`.

### 4.2 TSV untuk xlsx

`scripts/us_ac_to_tsv.py <path us-ac.md> [--out <dir>]` membaca `us-ac.md` dan menulis ke `docs/ba/` (default: folder yang sama):

| File | Kolom |
|---|---|
| `us.tsv` | US-ID, Judul, Persona, Aksi yang dilakukan, Hasil nilai bisnis |
| `ac.tsv` | AC-ID, US-ID, Skenario, GIVEN, WHEN, THEN, Status |
| `mrtm-<modul>.tsv` | kolom tabel MRTM apa adanya, satu file per modul (bagian `TRM_<MODUL>_`) |

- Encoding UTF-8 dengan BOM; pemisah tab; baris dipisah CRLF.
- `<br>` diubah menjadi baris baru di dalam sel; sel yang memuat baris baru, tab, atau tanda kutip dibungkus tanda kutip ganda dengan kutip di dalamnya digandakan.
- `ac.tsv` mengisi US-ID dari judul kelompok US.
- Skrip gagal dengan pesan yang menyebut nomor baris bila: tabel AC muncul tanpa judul US di atasnya, jumlah kolom tidak sesuai, atau ID tidak sesuai format.
- Pustaka standar Python saja.

### 4.3 Bahasa

- Kalimat US/AC dalam bahasa Indonesia mengikuti pola guide ("Saya seorang …", "Saya mengklik …", "Sistem menampilkan …").
- Teks UI verbatim (label tombol, nama field, isi pesan) dalam bahasa aplikasinya. Bila belum diketahui, ditanyakan sekali di langkah 1.
- Penanda kategori bergambar di guide diganti teks; keluaran tanpa emoji.

### 4.4 Menambah, bukan menimpa

Bila `docs/ba/us-ac.md` sudah ada, US baru ditambahkan di akhir dan AC untuk US lama disisipkan di akhir tabel AC US tersebut. Baris lama tidak diubah kecuali pengguna memintanya secara eksplisit.

## 5. Struktur repo

```
us-ac-writer/
  SKILL.md
  references/
    sysfunc-us-ac-guide.md     salinan persis Template/SysFunc_US_AC_Guide.md
    appendix-d-us-ac.md        salinan persis Appendix_D_Panduan_Praktik_US_AC.md
  scripts/
    us_ac_to_tsv.py
tools/
  sync_handbook.py
tests/
  test_us_ac_to_tsv.py
  test_handbook_sync.py
```

- `SKILL.md` berisi frontmatter (`name`, `description` dengan frasa pemicu seperti "buatkan US AC", "tulis user story", "acceptance criteria", "Given When Then", "MRTM"), alur §3, format §4, dan checklist §3 langkah 7. Isi aturan tidak diulang; `SKILL.md` mewajibkan membaca kedua file `references/` sebelum menulis.
- Kedua file `references/` disalin byte-per-byte, termasuk emoji di dalamnya, agar pemeriksaan sinkron tetap valid.

## 6. Sinkronisasi dengan handbook

`tools/sync_handbook.py`:

- Folder handbook dari variabel lingkungan `BA_HANDBOOK_DIR`; default `C:\Users\User\OneDrive\Documents\Work\ba-handbook`.
- Pasangan file didefinisikan di satu tabel di skrip (sumber handbook → salinan di skill).
- Tanpa argumen: membandingkan isi setelah menormalkan akhir baris (CRLF/LF), mencetak `sinkron` atau diff ringkas per file, exit 1 bila ada yang berbeda.
- `--update`: menyalin versi handbook ke skill.
- Exit 2 dengan pesan jelas bila folder handbook tidak ditemukan.

`tests/test_handbook_sync.py` menjalankan pemeriksaan yang sama dan di-skip bila folder handbook tidak ada.

## 7. Integrasi

- `README.md`: tambah baris pipeline Fase 3 `us-ac-writer` → `us-ac.md`, `us.tsv`, `ac.tsv`, `mrtm-*.tsv`; sebut `tools/sync_handbook.py`.
- `product-discovery/SKILL.md`: kalimat "the pipeline refines the full Given/When/Then later" menunjuk ke `us-ac-writer`.
- `ba-grooming/SKILL.md`: baca `docs/ba/us-ac.md` sebagai input bila ada.
- `my-ba-flow.plugin`: dirakit ulang memuat `skills/us-ac-writer/` (termasuk `references/` dan `scripts/`); `.claude-plugin/plugin.json` versi `1.2.0`. Pemasangan ulang plugin dilakukan pengguna.

## 8. Pengujian

`tests/test_us_ac_to_tsv.py` (pytest):

- `us-ac.md` contoh dengan dua US, AC multi-baris, dan satu MRTM menghasilkan `us.tsv`, `ac.tsv`, `mrtm-<modul>.tsv` dengan jumlah baris dan kolom yang benar.
- File diawali BOM UTF-8.
- Sel dengan `<br>` menjadi satu sel bertanda kutip berisi baris baru; dibaca kembali dengan `csv` (dialect tab) menghasilkan teks semula.
- Tanda kutip di dalam sel digandakan.
- Setiap baris `ac.tsv` punya US-ID sesuai kelompoknya.
- Tabel AC tanpa judul US di atasnya, atau AC-ID berformat salah, menghasilkan galat yang menyebut nomor baris.
- Karakter Indonesia dan teks Inggris verbatim tetap utuh.

`tests/test_handbook_sync.py`: salinan `references/` sama dengan handbook (skip bila handbook tidak ada).

Verifikasi manual oleh pengguna: minta skill membuat US/AC untuk satu fitur nyata, periksa kepatuhan terhadap guide, tempel TSV ke xlsx.
