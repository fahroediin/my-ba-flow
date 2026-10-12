# Bank Pertanyaan Discovery Meeting dan Aanwijzing

Sumber kebenaran untuk skill `discovery-meeting-prep`. Setiap sesi memakai Bagian A (inti) ditambah satu modul sesuai jenis sesi.

**Kode prioritas**

- **P1** wajib terjawab sebelum meeting selesai. Jika belum terjawab, catat sebagai open question dengan PIC dan tanggal.
- **P2** gali jika waktu cukup atau topik relevan. Boleh dilanjutkan lewat email atau sesi follow-up.

Kolom "Yang dicari" menjelaskan jawaban seperti apa yang dianggap cukup.

## Persiapan 30 menit sebelum sesi

- [ ] Baca profil klien (jalankan skill `company-profiling` bila belum ada)
- [ ] Pilih modul (B, C, atau D) dan tandai pertanyaan P1 yang paling relevan, maksimal 15
- [ ] Siapkan template Pain Points Register dan Assumptions Log untuk diisi langsung saat sesi
- [ ] Tentukan pembagian peran: satu BA bertanya, satu BA mencatat dan menjaga checklist
- [ ] Untuk tender: baca KAK/TOR dua kali, tandai setiap kalimat yang ambigu, tidak terukur, atau saling bertentangan
- [ ] Minta izin merekam sesi di awal meeting

---

## Bagian A: Pertanyaan inti (semua sesi)

Urutan mengikuti golden rule handbook: pahami As-Is dan masalahnya dulu, baru bicara solusi.

### A1. Konteks dan pemicu

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-01 | Apa yang membuat inisiatif ini muncul sekarang, bukan tahun lalu atau tahun depan? | P1 | Pemicu nyata: regulasi, target bisnis, audit, kompetitor, kegagalan sistem |
| A-02 | Apa yang terjadi jika proyek ini tidak dijalankan sama sekali? | P1 | Biaya tidak bertindak; menentukan urgensi dan prioritas sebenarnya |
| A-03 | Unit bisnis mana yang paling merasakan masalahnya? | P1 | Titik awal pemetaan stakeholder dan proses |
| A-04 | Apakah ada inisiatif lain (internal atau vendor lain) yang berjalan paralel dan bersinggungan? | P2 | Dependensi dan potensi konflik scope |

### A2. Stakeholder dan pengambil keputusan

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-05 | Siapa sponsor proyek dan siapa yang memberi keputusan akhir (go/no-go, anggaran)? | P1 | Nama dan jabatan; sering berbeda dari orang yang hadir di meeting |
| A-06 | Siapa yang akan memakai sistem setiap hari? Ada berapa kelompok pengguna? | P1 | Daftar role awal untuk stakeholder register |
| A-07 | Siapa narasumber (SME) yang paling paham proses saat ini per area? | P1 | PIC untuk sesi elisitasi lanjutan |
| A-08 | Siapa yang akan menyetujui dokumen requirement (BRD/FSD) dan UAT? | P1 | Jalur sign-off sejak awal |
| A-09 | Apakah ada pihak yang kurang setuju dengan proyek ini, atau yang terdampak tapi belum dilibatkan? | P2 | Resistensi dan politik internal |
| A-10 | Apakah tim IT internal terlibat? Apa perannya (pemilik infrastruktur, reviewer, operator)? | P1 | Batas tanggung jawab vendor vs IT klien |

### A3. Proses berjalan (As-Is)

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-11 | Bisa ceritakan alur kerjanya dari awal sampai akhir, menggunakan satu contoh kasus nyata? | P1 | Alur end-to-end; minta contoh kasus, bukan alur ideal |
| A-12 | Di setiap langkah, siapa yang mengerjakan, alat apa yang dipakai, dan dokumen apa yang dihasilkan? | P1 | Bahan swimlane As-Is |
| A-13 | Di titik mana ada persetujuan (approval)? Berapa level dan apa kriterianya? | P1 | Calon business rules dan workflow approval |
| A-14 | Kasus apa yang tidak mengikuti alur normal (pengecualian, revisi, pembatalan, retur)? | P1 | Edge case; sumber bug paling banyak bila tidak digali |
| A-15 | Apakah ada SOP, form, laporan, atau contoh dokumen yang bisa kami terima? | P1 | Artefak untuk document analysis |
| A-16 | Apa yang dikerjakan di luar sistem (Excel, WhatsApp, kertas, email)? | P2 | Workaround yang menunjukkan kebutuhan tersembunyi |

### A4. Pain point dan dampaknya

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-17 | Dari alur tadi, langkah mana yang paling lama, paling sering salah, atau paling dikeluhkan? | P1 | Daftar pain point untuk register |
| A-18 | Seberapa sering masalah itu terjadi, dan berapa dampaknya (jam kerja, uang, denda, keluhan pelanggan)? | P1 | Angka. Pain point tanpa angka sulit dijadikan prioritas |
| A-19 | Bagaimana cara tim mengatasinya saat ini? | P1 | Workaround; menjelaskan perilaku pengguna |
| A-20 | Jika hanya tiga masalah yang boleh diselesaikan, yang mana? | P1 | Prioritas versi klien, bukan versi BA |

### A5. Tujuan dan ukuran sukses

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-21 | Enam bulan setelah sistem berjalan, apa yang berubah sehingga Bapak/Ibu menyebut proyek ini berhasil? | P1 | Kriteria sukses yang bisa diamati |
| A-22 | Angka apa yang ingin bergerak, dari berapa ke berapa? | P1 | KPI terukur: waktu proses, error rate, biaya, SLA |
| A-23 | Bagaimana kondisi itu diukur hari ini? Apakah datanya ada? | P2 | Baseline; tanpa baseline keberhasilan tidak bisa dibuktikan |

### A6. Scope dan prioritas

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-24 | Modul atau proses apa saja yang masuk? Apa yang jelas tidak masuk? | P1 | In-scope dan out-of-scope tertulis |
| A-25 | Cakupannya untuk unit, cabang, wilayah, atau entitas mana saja? | P1 | Batas organisasi dan geografi |
| A-26 | Jika harus bertahap, apa yang wajib ada di fase pertama (MVP)? | P1 | Bahan MoSCoW dan phasing |
| A-27 | Apakah ada fitur yang sudah dibayangkan secara spesifik? Masalah apa yang ingin diselesaikan fitur itu? | P2 | Mengubah permintaan solusi menjadi kebutuhan |

### A7. Pengguna, volume, dan kanal

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-28 | Berapa jumlah pengguna total dan yang aktif bersamaan pada jam sibuk? | P1 | Dasar sizing dan lisensi |
| A-29 | Berapa volume transaksi per hari/bulan, dan kapan puncaknya (akhir bulan, musiman)? | P1 | Dasar NFR performa |
| A-30 | Diakses lewat apa: web desktop, mobile app, tablet di lapangan? Bagaimana kondisi jaringannya? | P1 | Kanal, offline mode, spesifikasi perangkat |
| A-31 | Apakah ada pengguna eksternal (pelanggan, mitra, supplier)? | P2 | Kebutuhan portal dan keamanan tambahan |

### A8. Data

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-32 | Data utama apa yang dikelola, dan di mana disimpan saat ini? | P1 | Entitas awal untuk data dictionary |
| A-33 | Apakah ada data lama yang harus dimigrasikan? Berapa tahun, berapa volume, seberapa bersih? | P1 | Scope migrasi; sering menjadi biaya tersembunyi |
| A-34 | Siapa pemilik data master (produk, pelanggan, karyawan)? | P2 | Sumber kebenaran data dan aturan sinkronisasi |
| A-35 | Laporan apa yang wajib dihasilkan, untuk siapa, dan seberapa sering? | P1 | Kebutuhan reporting; minta contoh laporan saat ini |

### A9. Integrasi dan lingkungan teknis

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-36 | Sistem apa yang sudah ada dan harus terhubung (ERP, core banking, HRIS, payment gateway, pajak)? | P1 | Daftar integrasi untuk context diagram |
| A-37 | Untuk setiap integrasi: arah data, frekuensi, metode (API, file, database), dan siapa pemilik sistemnya? | P1 | Kompleksitas dan dependensi pihak ketiga |
| A-38 | Apakah ada dokumentasi API atau akses sandbox? | P2 | Kesiapan teknis; tanpa ini estimasi integrasi berisiko |
| A-39 | Sistem akan di-hosting di mana (on-premise, cloud klien, cloud vendor)? Ada standar teknologi wajib? | P1 | Tech stack constraint |
| A-40 | Login memakai apa: akun terpisah, SSO, Active Directory? | P2 | Kebutuhan autentikasi |

### A10. Kualitas sistem (NFR)

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-41 | Berapa lama sistem boleh tidak bisa diakses tanpa mengganggu bisnis? Jam operasionalnya kapan? | P1 | Target availability dan jendela maintenance |
| A-42 | Berapa waktu respons yang dianggap wajar untuk transaksi utama? | P2 | Target performa terukur (ISO 25010) |
| A-43 | Data apa yang sensitif? Siapa boleh melihat apa? | P1 | Hak akses berbasis role dan klasifikasi data |
| A-44 | Apakah perlu jejak audit (siapa mengubah apa, kapan)? | P1 | Audit trail requirement |
| A-45 | Berapa lama data harus disimpan dan bagaimana backup/recovery-nya? | P2 | Retensi, RPO, RTO |

### A11. Regulasi dan kepatuhan

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-46 | Regulasi apa yang mengikat proses ini (OJK, BI, UU PDP, PSE Kominfo, pajak, standar industri)? | P1 | Batasan wajib dan kebutuhan dokumen kepatuhan |
| A-47 | Apakah ada audit internal/eksternal yang memeriksa proses ini? Temuan apa yang pernah muncul? | P2 | Requirement tersembunyi dari temuan audit |
| A-48 | Apakah data wajib disimpan di Indonesia? | P2 | Batasan hosting |

### A12. Anggaran, waktu, dan pengadaan

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-49 | Apakah ada tanggal yang tidak bisa mundur? Apa yang terjadi jika terlewat? | P1 | Hard deadline dan konsekuensinya |
| A-50 | Apakah anggaran sudah dialokasikan? Kisarannya, dan untuk periode apa (capex, opex, multi-tahun)? | P1 | Kelayakan solusi dan model komersial |
| A-51 | Bagaimana proses pengadaannya: penunjukan langsung, beauty contest, atau tender? Kapan keputusan diambil? | P1 | Timeline penjualan dan dokumen yang dibutuhkan |
| A-52 | Vendor lain siapa saja yang sedang dipertimbangkan? Apa yang membuat Bapak/Ibu tertarik bicara dengan kami? | P2 | Posisi kompetitif |

### A13. Setelah go-live

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| A-53 | Setelah go-live, siapa yang mengelola sistem sehari-hari? Ada tim IT yang akan mengambil alih? | P1 | Model support dan handover |
| A-54 | Kebutuhan pelatihan seperti apa, untuk berapa orang, di lokasi mana? | P2 | Transition requirement |
| A-55 | Bagaimana penanganan bug dan permintaan perubahan setelah serah terima diharapkan berjalan? | P2 | Ekspektasi SLA, garansi, dan alur Change Request |

---

## Bagian B: Sistem baru dari nol

Risiko terbesar: klien datang membawa solusi ("kami butuh aplikasi seperti X"), bukan masalah. Modul ini memaksa percakapan kembali ke kebutuhan, kesiapan organisasi, dan definisi produk.

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| B-01 | Apakah ini proses baru yang belum pernah dijalankan, atau proses lama yang ingin didigitalkan? | P1 | Proses baru berarti aturan bisnis belum matang dan perlu workshop desain proses |
| B-02 | Jika ada contoh aplikasi yang dijadikan acuan, bagian mana yang disukai dan mengapa? | P1 | Kebutuhan di balik referensi; jangan menyalin fitur tanpa alasan |
| B-03 | Apakah sudah pernah mencoba solusi siap pakai (SaaS, aplikasi paket)? Mengapa tidak cocok? | P1 | Alasan build vs buy |
| B-04 | Apa yang membuat proses di perusahaan ini berbeda dari perusahaan sejenis? | P1 | Diferensiasi yang benar-benar butuh kustomisasi |
| B-05 | Siapa yang akan menjadi product owner di sisi klien, dengan waktu yang cukup untuk menjawab pertanyaan tim setiap minggu? | P1 | Ketersediaan pengambil keputusan |
| B-06 | Apakah aturan bisnis sudah tertulis dan disepakati antar divisi, atau masih berbeda-beda per orang/cabang? | P1 | Kebutuhan standardisasi proses sebelum sistem dibangun |
| B-07 | Seberapa siap pengguna berpindah dari cara lama? Pernah ada sistem yang gagal diadopsi? | P1 | Risiko adopsi dan kebutuhan change management |
| B-08 | Apakah sistem ini direncanakan berkembang ke modul atau unit lain dalam 2 sampai 3 tahun? | P2 | Arsitektur dan skalabilitas jangka panjang |
| B-09 | Siapa yang memiliki source code dan hak kekayaan intelektual setelah proyek selesai? | P2 | Ekspektasi kepemilikan; berdampak pada harga dan kontrak |
| B-10 | Lebih nyaman dengan pendekatan bertahap (sprint dan demo rutin) atau spesifikasi lengkap di awal lalu dibangun sekaligus? | P1 | Pilihan Agile, Waterfall, atau Hybrid untuk BA Approach |
| B-11 | Apakah ada branding, desain, atau standar UI yang harus diikuti? | P2 | Masukan untuk tim UI/UX |
| B-12 | Berapa lama waktu yang bisa disediakan tim klien untuk workshop, review, dan UAT? | P1 | Kapasitas klien sebagai constraint timeline |

**Bawa pulang:** context diagram kasar, daftar role pengguna, 3 sampai 5 pain point dengan angka, dan kandidat scope MVP.

---

## Bagian C: Ganti vendor / proyek bermasalah

Klien yang kecewa cenderung menyalahkan vendor lama sepenuhnya. Tugas BA adalah memisahkan penyebab teknis, penyebab proses, dan penyebab di sisi klien sendiri, karena penyebab di sisi klien akan terulang pada vendor baru. Hindari mengomentari vendor lama secara negatif.

### C1. Riwayat proyek

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| C-01 | Proyek dengan vendor sebelumnya dimulai kapan, scope awalnya apa, dan sampai tahap mana sekarang? | P1 | Status aktual: belum jadi, jadi tapi tidak dipakai, atau dipakai tapi bermasalah |
| C-02 | Apa yang sudah berjalan baik dan ingin dipertahankan? | P1 | Aset yang bisa dipakai ulang |
| C-03 | Menurut Bapak/Ibu, di titik mana proyek mulai bermasalah? Apa yang terjadi saat itu? | P1 | Akar masalah dan kronologi |
| C-04 | Apakah requirement dulu didokumentasikan dan ditandatangani? Boleh kami lihat? | P1 | Kualitas requirement; sering menjadi akar masalah sebenarnya |
| C-05 | Bagaimana perubahan kebutuhan ditangani selama proyek? Berapa banyak perubahan yang terjadi? | P1 | Scope creep dan disiplin Change Request di sisi klien |
| C-06 | Bagaimana keterlibatan tim klien selama proyek (review, UAT, kecepatan memberi keputusan)? | P2 | Kontribusi klien terhadap masalah, ditanyakan secara netral |
| C-07 | Apa yang paling ingin Bapak/Ibu lakukan berbeda di proyek berikutnya? | P1 | Ekspektasi terhadap cara kerja vendor baru |

### C2. Kondisi sistem saat ini

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| C-08 | Masalah yang dirasakan berupa apa: bug, performa lambat, fitur tidak sesuai proses, sulit dipakai, atau sering down? | P1 | Klasifikasi masalah; menentukan perbaikan atau bangun ulang |
| C-09 | Apakah ada daftar bug atau keluhan pengguna yang tercatat? Berapa jumlah dan tingkat keparahannya? | P1 | Bukti kuantitatif |
| C-10 | Teknologi apa yang dipakai (bahasa, framework, database, platform low-code), dan di mana di-hosting? | P1 | Kelayakan ambil alih oleh tim kita |
| C-11 | Siapa yang memiliki source code, akses server, database, dan akun pihak ketiga (domain, cloud, API key)? | P1 | Penghambat terbesar takeover; harus jelas sebelum penawaran |
| C-12 | Dokumentasi apa yang tersedia: BRD, FSD, desain database, dokumentasi API, user manual? | P1 | Kebutuhan reverse engineering (skill `reverse-engineering`) |
| C-13 | Berapa pengguna aktif dan volume data yang sudah ada di sistem lama? | P1 | Risiko dan scope migrasi |
| C-14 | Apakah sistem lama terintegrasi dengan sistem lain yang tidak boleh terganggu? | P1 | Risiko cutover |

### C3. Hubungan dengan vendor lama dan arah ke depan

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| C-15 | Apakah kontrak dengan vendor lama sudah selesai? Ada kewajiban serah terima atau sengketa? | P1 | Batasan hukum dan risiko keterlambatan akses |
| C-16 | Apakah vendor lama masih bisa dihubungi untuk transfer pengetahuan? | P2 | Sumber informasi teknis |
| C-17 | Harapannya: perbaiki dan lanjutkan sistem yang ada, atau bangun ulang dari awal? Apakah sudah ada keputusan? | P1 | Arah solusi; jangan menjanjikan sebelum assessment |
| C-18 | Apakah sistem lama harus tetap berjalan selama transisi? | P1 | Strategi cutover (paralel, bertahap, big bang) |
| C-19 | Apakah klien terbuka dengan fase assessment berbayar (audit kode dan requirement) sebelum komitmen penuh? | P2 | Mengurangi risiko estimasi pada sistem yang belum dikenal |

**Bawa pulang:** kronologi masalah, daftar akses dan dokumen yang harus diserahkan, klasifikasi masalah (requirement, teknis, proses, adopsi), dan rekomendasi awal perbaiki atau bangun ulang.

---

## Bagian D: Aanwijzing tender

Pertanyaan dan jawaban bersifat resmi, terlihat oleh peserta lain, dan yang mengikat hanya yang tercatat di Berita Acara Pemberian Penjelasan atau adendum. Tujuan BA: menghilangkan ambiguitas yang bisa membuat estimasi meleset atau penawaran gugur.

### D1. Sebelum sesi: bedah dokumen tender

- [ ] Pecah KAK/TOR menjadi daftar requirement bernomor (fungsional, non-fungsional, deliverable, dokumen)
- [ ] Tandai setiap requirement: Jelas, Ambigu, Tidak terukur, Bertentangan, Tidak realistis untuk timeline
- [ ] Cocokkan jangka waktu pelaksanaan dengan volume pekerjaan
- [ ] Cek syarat administrasi dan kualifikasi: sertifikasi, pengalaman sejenis, tenaga ahli, TKDN, jaminan
- [ ] Cek kriteria evaluasi teknis dan bobotnya
- [ ] Susun pertanyaan tertulis, urutkan dari dampak biaya terbesar
- [ ] Saring pertanyaan yang membocorkan strategi solusi kita; ajukan secara netral

### D2. Scope dan deliverable

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| D-01 | Pada butir [x] KAK disebut "[istilah]". Mohon penjelasan batasan dan contoh yang dimaksud. | P1 | Template untuk setiap istilah ambigu; selalu rujuk nomor butir |
| D-02 | Berapa jumlah modul, role pengguna, laporan, dan form yang termasuk dalam lingkup? | P1 | Angka untuk estimasi effort |
| D-03 | Apakah migrasi data termasuk lingkup? Jika ya, berapa volume, format sumber, dan siapa yang membersihkan data? | P1 | Biaya tersembunyi yang sering tidak tertulis |
| D-04 | Integrasi dengan sistem apa saja yang diwajibkan? Apakah API dan dokumentasinya disediakan pemberi kerja? | P1 | Dependensi teknis dan risiko jadwal |
| D-05 | Deliverable dokumen apa saja yang wajib diserahkan, dan apakah ada template dari pemberi kerja? | P1 | Effort dokumentasi BA dan QA |
| D-06 | Apakah pelatihan, pendampingan pasca go-live, dan masa pemeliharaan termasuk? Berapa lama dan berapa peserta? | P1 | Komponen biaya non-development |
| D-07 | Bagaimana mekanisme jika ada perubahan kebutuhan selama pelaksanaan? | P2 | Perlindungan terhadap scope creep |

### D3. Teknis dan lingkungan

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| D-08 | Infrastruktur (server, cloud, lisensi database, sertifikat SSL) disediakan oleh pemberi kerja atau penyedia? | P1 | Komponen biaya besar yang menentukan harga |
| D-09 | Apakah ada standar teknologi, arsitektur, atau keamanan yang wajib diikuti (misalnya pengujian keamanan oleh pihak ketiga)? | P1 | Constraint dan biaya pengujian |
| D-10 | Berapa target jumlah pengguna, volume transaksi, dan availability yang diharapkan? | P1 | NFR terukur bila KAK hanya menulis "handal" atau "cepat" |
| D-11 | Apakah source code dan hak cipta diserahkan kepada pemberi kerja? | P2 | Model kepemilikan |
| D-12 | Lingkungan apa yang disediakan untuk development, testing, dan UAT? | P2 | Kesiapan teknis |

### D4. Pelaksanaan dan penerimaan

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| D-13 | Bagaimana kriteria penerimaan pekerjaan (BAST)? Siapa yang menandatangani UAT? | P1 | Definisi selesai |
| D-14 | Bagaimana termin pembayaran dikaitkan dengan milestone? | P1 | Arus kas proyek |
| D-15 | Apakah ada SLA dan denda? Bagaimana perhitungannya? | P1 | Risiko finansial |
| D-16 | Apakah tim harus bekerja di lokasi pemberi kerja? Berapa hari per minggu? | P2 | Biaya operasional tim |
| D-17 | Siapa PIC pemberi kerja selama pelaksanaan, dan berapa cepat waktu respons untuk konfirmasi requirement? | P2 | Dependensi keputusan klien |

### D5. Evaluasi penawaran

| ID | Pertanyaan | Prio | Yang dicari |
| --- | --- | --- | --- |
| D-18 | Bagaimana metode evaluasi dan bobot teknis terhadap harga? | P1 | Strategi penyusunan proposal |
| D-19 | Apakah ada presentasi, demo, atau proof of concept? Skenarionya ditentukan pemberi kerja? | P1 | Persiapan demo |
| D-20 | Apakah boleh mengajukan solusi alternatif atau produk siap pakai yang dikustomisasi? | P2 | Ruang untuk diferensiasi solusi |

### D6. Setelah aanwijzing

- [ ] Pastikan setiap jawaban penting tercantum di Berita Acara Pemberian Penjelasan atau adendum; jawaban lisan tidak bisa dijadikan dasar
- [ ] Perbarui daftar requirement dan asumsi berdasarkan jawaban
- [ ] Tulis asumsi yang tetap dipakai secara eksplisit di proposal teknis
- [ ] Pertanyaan yang tidak terjawab jelas dimasukkan ke risk register beserta dampaknya ke harga

---

## Teknik menggali

| Situasi | Teknik | Contoh kalimat |
| --- | --- | --- |
| Jawaban abstrak ("prosesnya ribet") | Minta contoh kasus terakhir | "Boleh ceritakan kejadian terakhir minggu ini, langkah demi langkah?" |
| Klien menyebut fitur, bukan masalah | 5 Whys | "Kalau fitur itu ada, masalah apa yang hilang?" |
| Kata sifat tanpa angka ("cepat", "banyak") | Kuantifikasi | "Cepat itu berapa detik? Banyak itu kira-kira berapa per hari?" |
| Ada istilah internal | Konfirmasi definisi | "Saat Bapak bilang 'closing', itu tepatnya terjadi di langkah mana?" |
| Jawaban "semua penting" | Paksa trade-off | "Kalau go-live harus bulan depan dan hanya tiga yang sempat, pilih yang mana?" |
| Ragu pemahaman sudah benar | Parafrase balik | "Saya ulangi untuk memastikan: ... Apakah sudah tepat?" |
| Topik terlalu dalam untuk sesi ini | Parkir | "Ini penting, saya catat sebagai sesi terpisah dengan [PIC]." |

## Red flags

| Red flag | Mengapa berbahaya | Tindakan |
| --- | --- | --- |
| Pengambil keputusan tidak pernah hadir | Requirement bisa dibatalkan di akhir | Minta sesi validasi dengan sponsor |
| Deadline tetap, scope belum jelas | Estimasi tidak bisa dipertanggungjawabkan | Usulkan scope MVP atau fase discovery berbayar |
| "Nanti tinggal ikuti sistem lama saja" | Logika sistem lama sering tidak terdokumentasi | Jadwalkan reverse engineering |
| Antar divisi memberi jawaban berbeda untuk aturan yang sama | Aturan bisnis belum disepakati | Catat sebagai konflik, minta keputusan sponsor |
| Akses source code dan server vendor lama belum jelas | Takeover bisa macet berbulan-bulan | Jadikan syarat sebelum kontrak |
| Anggaran belum ada atau "tergantung harga" | Peluang belum matang | Informasikan ke tim BD |
| Integrasi dengan sistem pihak ketiga tanpa dokumentasi | Risiko jadwal terbesar | Masukkan sebagai asumsi dan risiko tertulis |
| KAK tender sangat detail mengarah ke satu produk tertentu | Kemungkinan sudah ada calon pemenang | Diskusikan go/no-go dengan BD sebelum menyusun proposal |

## Aturan sikap di ruang meeting

- Jangan menjanjikan solusi, harga, atau timeline di sesi pertama; catat sebagai pertanyaan untuk dijawab setelah analisis
- Jangan menyimpulkan tanpa konfirmasi; setiap anggapan dicatat di Assumptions Log (Rule P2-03)
- Tutup meeting dengan merangkum: 3 temuan utama, open questions beserta PIC dan tanggal, serta langkah berikutnya

## Output wajib setelah sesi

| Output | Sistem baru | Ganti vendor | Aanwijzing |
| --- | --- | --- | --- |
| Minutes of Meeting dengan open questions, PIC, tanggal | Wajib | Wajib | Wajib |
| Pain Points Register | Wajib | Wajib | Opsional |
| Assumptions Log | Wajib | Wajib | Wajib |
| Stakeholder register awal | Wajib | Wajib | Opsional |
| Context diagram kasar | Wajib | Wajib | Wajib |
| Daftar akses dan dokumen dari vendor lama | Tidak | Wajib | Tidak |
| Daftar requirement KAK berlabel dan jawaban aanwijzing | Tidak | Tidak | Wajib |
| Catatan red flags untuk BD dan Head of BA | Wajib | Wajib | Wajib |

Notulen wajib final dalam 24 jam (Rule P2-01) dan dikonfirmasi peserta (Rule P2-02).

## Perawatan bank pertanyaan

- Setelah setiap sesi, tambahkan pertanyaan yang ternyata penting tetapi belum ada di sini (ID baru melanjutkan nomor terakhir di bagiannya)
- Review bulanan oleh Head of BA: hapus yang tidak pernah dipakai, naikkan ke P1 yang sering menjadi sumber masalah
- Selaraskan versi stabil dengan BA-Handbook (Appendix B, Checklist)
