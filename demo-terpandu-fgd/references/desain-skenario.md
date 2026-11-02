# Desain rundown

## Format Demo

Fokusnya memperlihatkan produk berjalan. Layar hanya berisi navigasi langkah dan tombol Catatan, jadi audiens melihat aplikasi, bukan teks panduan.
- Urutan langkah mengikuti alur produk: Pembukaan (0) → pengenalan (termasuk multi-tenant bila ada) → peran → alur bisnis dari hulu ke hilir, satu peran satu tindakan → kontrol/laporan → penutup.
- `title` pendek dan jelas, karena hanya judul yang tampil di bilah.
- `goal`, `show`, `say`, `do` tetap ditulis lengkap: semuanya masuk naskah cetak yang menjadi pegangan pembawa.
- Pertanyaan opsional. Bila pengguna memberi daftar, tempatkan kode di `q` agar muncul di naskah; jangan menulis ulang kalimat pengguna kecuali salah ketik yang jelas.
- `spot` penting: sorotan adalah satu-satunya penunjuk di layar ke bagian yang sedang dibahas.

Bila pengguna memilih **keduanya**, pakai satu `steps.json` untuk kedua mode: tulis langkah seperti untuk FGD (tujuan, pertanyaan berkode); format Demo otomatis menyembunyikannya dari layar.

## Format FGD

Rundown berwaktu dengan nomor mulai 0. Pola yang terbukti dipakai pada Panduan FGD FIF (sesi 120 menit, 10 langkah):

| # | Langkah | Menit (contoh) | Isi |
|---|---|---|---|
| 0 | Pembukaan | 0–8 | Sepakati tujuan sesi. Ringkas masukan sesi sebelumnya dan jawabannya di prototipe. Tampilkan layar ringkasan. |
| 1 | Yang paling dekat dengan pengguna | 8–18 | Apa yang dilihat pengguna utama lebih dulu (mis. performa sales, ringkasan kandang). |
| 2 | Pekerjaan sehari-hari dan datanya | 18–30 | Pekerjaan asli dan buktinya; data mana yang sudah ada di sistem klien. |
| 3 | Satu contoh utuh | 30–33 | Satu alur dari awal sampai akhir sebagai pola untuk langkah berikutnya. |
| 4–5 | Lapisan keputusan utama | 33–80 | Klien memetakan program/proses mereka ke konsep di aplikasi, lalu bedah per tipe: untuk siapa, hadiah/nilai, waktu, validasi, persetujuan. |
| 6 | Pengawas: pantau, verifikasi, bina | 80–90 | Siapa memantau, memverifikasi, dan membuat aturan lokal. |
| 7 | Aturan main | 90–100 | Syarat, jam, privasi peringkat, hal yang tidak boleh ada. |
| 8 | Pilihan konsep | 100–110 | Klien memilih opsi bila ada alternatif. |
| 9 | Ukuran berhasil dan penutup | 110–120 | Angka keberhasilan, data yang diminta, langkah berikutnya. **Unduh catatan sesi.** |

Untuk demo produk yang alurnya transaksional (mis. pesanan → kirim → bayar), langkah 3–8 bisa mengikuti rantai nilai: satu langkah = satu peran = satu tindakan, berganti peran tiap langkah supaya serah terima antarbagian terlihat. Untuk sistem multi-tenant, sisipkan di awal satu langkah yang memperlihatkan tenant lain tidak saling melihat data dan satu orang yang bekerja di dua tenant.

## Menulis langkah

- **title**: kalimat pendek tentang topik, bukan nama menu ("Supervisor: pantau, verifikasi, coaching").
- **goal** (tampil ke klien): satu kalimat keputusan atau pemahaman yang ingin dicapai. Contoh: "FIF memetakan Jusami, 10/5 hari terakhir, target kelas ke tipe misi. Pilih tipe untuk tahap awal."
- **show** (tampil ke klien): 1–3 butir layar yang diperlihatkan, dengan nama layar/menu seperti di aplikasi ("Web: Buat Misi, langkah 1 Pilih pekerjaan asli", "HP: Misi › Hari ini").
- **q** (tampil ke klien): 0–7 kode pertanyaan dari bank. Pertanyaan menuntut jawaban konkret (angka, nama peran, contoh nyata), bukan "bagaimana menurut Anda?".
- **spot**: selector bagian layar yang sedang dibahas; kosongkan pada langkah penutup.
- **min**, **who** (pembawa): rentang menit dan nama pembawa/fasilitator.
- **say** (pembawa): 1–3 poin bicara; **do** (pembawa): urutan klik dengan label persis, nilai contoh, field wajib, dan efek yang akan terlihat ("Saldo menjadi Rp0").
- **placeholder** (opsional): contoh isian kolom catatan yang relevan dengan langkah itu.

Tiap babak alur bisnis sebaiknya punya setidaknya satu tindakan langsung (input, setujui, kirim) agar peserta melihat sistem bekerja, bukan tangkapan layar.

## Bank pertanyaan berkode

Kode per tema memudahkan notulen, rundown cetak, dan rujukan di diskusi ("soal B3 tadi…"). Contoh pengelompokan:

| Kode | Tema | Contoh |
|---|---|---|
| A | Pekerjaan sehari-hari | Ceritakan satu hari kerja kemarin, dari absen pagi sampai lapor sore. Aplikasi apa saja yang dibuka? |
| B | Target, insentif, nilai | Insentif yang tampil dihitung siapa, dan kapan angkanya final? |
| C | Aturan dan ambang | Sudah ada ambang baku untuk kategori A/B/C? Apa yang terjadi bila kuota habis? |
| D | Peran dan data | Nama tiap level dari staf sampai pimpinan, apa yang dilihat dan diputuskan tiap level? Data apa yang bisa diunggah tanpa tim IT? |
| E | Ukuran berhasil | Enam bulan berjalan, angka berapa yang dianggap berhasil? |
| F | Konfirmasi rancangan | Bukti lokasi dan foto sudah cukup, atau atasan tetap menyetujui satu per satu? |
| K | Kepatuhan dan hal sensitif | Ada hal yang tidak boleh muncul di aplikasi (istilah, perbandingan antarpegawai, untung-untungan)? |
| P2-xx | Cadangan / sesi lanjutan | Ada aplikasi lain yang pernah diluncurkan lalu tidak dipakai? Kenapa? |

Pertanyaan umum yang hampir selalu berguna:
- Bagian mana yang paling sering dikerjakan, dan siapa yang mengerjakannya sekarang?
- Data apa yang selama ini dicatat di buku, Excel atau WhatsApp dan belum ada di sini?
- Langkah mana yang terasa terlalu panjang atau membingungkan?
- Laporan apa yang diminta pimpinan tiap minggu dan bulan?
- Perangkat apa yang dipakai di lapangan, dan bagaimana koneksinya?
- Ada wilayah atau cabang yang cocok jadi pilot? Kenapa?
- Jika besok mulai dipakai, apa yang harus disiapkan lebih dulu?

## Data contoh

- Realistis untuk domain dan lokasi: nama orang/usaha lokal, alamat masuk akal, angka sesuai skala.
- Riwayat 3–5 minggu dengan tanggal relatif hari ini sehingga laporan periode default langsung terisi.
- Hentikan transaksi di tahap berbeda; satu per tahap cukup. Petakan tiap tahap ke peran yang melanjutkannya saat demo.
- Biarkan input hari ini kosong untuk diisi langsung.
- Satu celah data yang disengaja bila sistem menampilkan kelengkapan/anomali.
- Isi semua data bawaan yang kosong (master data default) agar tidak muncul tanda strip kosong atau error yang tidak relevan.
- Jika aturan bisnis melarang tanggal mundur, buat transaksi hari ini dan bedakan tahapnya, bukan tanggalnya.
- Seed lewat API sebagai peran yang semestinya; jika aksi ditolak, itu informasi penting tentang aturan, bukan sesuatu untuk dilewati dengan menulis langsung ke database.

## Catatan untuk pembawa (isi dari uji coba)

Tulis jebakan nyata yang ditemukan saat menjalankan aplikasi: tombol yang tampil tetapi ditolak, pesan error yang terlalu umum, tampilan HP yang harus digeser, nilai yang tampil sebagai ID bukan nama, data yang hilang saat restart. Pembawa yang tahu lebih dulu tidak akan kaget di depan klien, dan daftar ini juga berguna untuk tim produk.
