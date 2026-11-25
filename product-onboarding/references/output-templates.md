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

## Nilai komersial
| Aspek | Isi | Status |
| --- | --- | --- |
| Pembeli (pemegang anggaran) | (peran, bukan nama orang) | Asumsi / Dikonfirmasi (oleh, tanggal) |
| Pengguna utama | (peran) | |
| Masalah bernilai uang | (per alur utama: yang dihemat, yang naik, atau risiko yang hilang) | |
| Segmen sasaran | (industri atau jenis perusahaan, dan alasannya) | |
| Momen nilai di demo | (satu atau dua layar/alur tempat nilai uang paling terlihat) | |
| Kesiapan dijual | (dijual apa adanya / perlu konfigurasi per klien / perlu pengembangan sebelum penjualan pertama) | |

Tidak memuat harga, diskon, model lisensi, atau timeline. Itu wewenang BD.

## Cara menjalankan lokal
(perintah, akun uji, catatan; atau "Tidak dijalankan: (alasan)")

## Kesiapan
(siap demo / siap pilot / siap dijual / belum), dengan alasan singkat

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

`Terbukti`: aturan dicoba di aplikasi yang berjalan dan berperilaku konsisten. `Asumsi`: terlihat di kode atau tampilan tetapi belum dicoba atau tidak bisa dicoba. Label ini hanya menyatakan perilaku aplikasi; kecocokan dengan cara kerja klien dicatat terpisah sebagai status klien (`dikonfirmasi`, `dibantah`, `belum`) di debrief.

## assumptions-to-confirm.md

```markdown
| ID | Hal yang dikonfirmasi | Asal (BR/F) | Label | Pertanyaan ke calon klien | Dampak bila salah | Status klien |
| --- | --- | --- | --- | --- | --- | --- |
| AS-01 | | BR-03 | Terbukti / Asumsi | | | dikonfirmasi / dibantah / belum |
```

Isi semua aturan `Asumsi`, aturan `Terbukti` yang menentukan proses harian klien, dan fitur tanpa kebutuhan jelas. Kolom Status klien diisi saat debrief.

## demo-traps.md

```markdown
| ID | Jebakan | Di mana | Cara menghindari atau menjelaskan |
| --- | --- | --- | --- |
| DT-01 | | (halaman/langkah) | |
```
