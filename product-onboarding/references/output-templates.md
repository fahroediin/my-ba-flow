# Kerangka output product-onboarding

Semua file memakai format ringan: header singkat lalu isi. Ganti teks dalam kurung.

## product-brief.md

```markdown
# Ringkasan Produk: (produk) (versi)

**Produk:** (nama)  
**Versi:** (versi)  
**Tanggal:** (YYYY-MM-DD)  
**Disusun:** (nama BA)  

Disusun dengan bantuan AI, ditinjau oleh BA: (nama)

## Untuk apa
(tiga kalimat: masalah yang dijawab, untuk siapa, hasil yang didapat pengguna)

## Pengguna dan peran
| Peran | Pekerjaan di aplikasi | Batasan akses |
| --- | --- | --- |

## Modul
| Modul | Fungsi | Peran utama |
| --- | --- | --- |

## Alur bisnis hulu ke hilir
1. (langkah, peran, hasil)

## Cara menjalankan lokal
(perintah, akun uji, catatan; atau "Tidak dijalankan: (alasan)")

## Kesiapan
(siap demo / siap pilot / belum), dengan alasan singkat

## Perubahan dari versi sebelumnya
(hanya bila ada versi sebelumnya)
```

## feature-inventory.md

```markdown
| ID | Modul | Fitur | Peran | Bukti (layar/rute/aksi) | Diuji |
| --- | --- | --- | --- | --- | --- |
| F-01 | | | | | Ya/Tidak |
```

## business-rules-found.md

```markdown
| ID | Aturan | Sumber | Bukti | Label |
| --- | --- | --- | --- | --- |
| BR-01 | (aturan) | kode / UI / API | (yang dicoba dan hasilnya) | Terbukti / Asumsi |
```

`Terbukti`: aturan dicoba dan berperilaku konsisten. `Asumsi`: ada di kode atau tampilan tetapi belum pernah dikonfirmasi pengguna nyata, atau belum bisa dicoba.

## assumptions-to-confirm.md

```markdown
| ID | Asumsi | Asal (BR/F) | Pertanyaan ke calon klien | Dampak bila salah |
| --- | --- | --- | --- | --- |
| AS-01 | | BR-03 | | |
```

## demo-traps.md

```markdown
| ID | Jebakan | Di mana | Cara menghindari atau menjelaskan |
| --- | --- | --- | --- |
| DT-01 | | (halaman/langkah) | |
```
