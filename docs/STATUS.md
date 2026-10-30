# Status produksi — 2026-10-30

- Branch aktif: `arena/969f2d03-yt-1`. Referensi branch lama pada handoff adalah historis, bukan tujuan push.
- Handoff asli disimpan di folder ini.
- Repo awal hanya berisi README; belum ada naskah atau media lokal.
- Folder Metadata & Naskah Drive berhasil dibaca. Nomor Short tertinggi yang terlihat: 12 (pesulap menelan pedang). Nomor 13 sementara, perlu cek benturan sebelum publikasi.
- Fase aktif: riset dan menunggu pilihan topik. Jangan membuat naskah sebelum pengguna memilih.
- Media hanya ke Google Drive, tidak ke git.
- Voice ID dari sesi lama tidak dapat diasumsikan tersedia; lakukan audisi baru sebelum sintesis.
- Mascot berkacamata hanya scene pertama dan terakhir; intro scene 2–3 memakai karakter biasa agar sesuai aturan karakter yang lebih ketat.
- Durasi harus diukur dari audio aktual, bukan diasumsikan dari jumlah kata. Jangan memaksa tempo lambat demi target 155–168 detik; batas keras <180 detik.

## Setelah pemilihan
- Pengguna memilih opt_3 (kehilangan lidah).
- Draf Short 13 tersedia di `script/13-SHORT-APA-YANG-TERJADI-KALAU-MANUSIA-KEHILANGAN-LIDAH.md`.
- Validasi otomatis awal: 30 VO, masing-masing 12 kata, total 360 kata, enam kelompok lima adegan.
- Riset medis menggunakan Cancer Research UK, review rekonstruksi 2019, dan studi glosektomi parsial 2017. Rujukan anatomi NIDCD masih perlu verifikasi langsung sebelum rekaman.
- Berikutnya: pemeriksaan medis akhir, unggah naskah ke Drive, lalu produksi gambar batch 1. Belum ada gambar/VO/video yang dibuat atau diunggah.

## Kelanjutan produksi setelah referensi karakter
- Acuan karakter pengguna disimpan lokal; aturan tertulis di `docs/VISUAL_STYLE.md`.
- Intro 01 sudah dibuat ulang bergaya 2D, tetapi belum mendapat persetujuan final dan belum dinormalisasi.
- Percobaan adegan 02 dengan referensi pengguna gagal: layanan generate_image mengembalikan 403 PERMISSION_DENIED (akun ditandai). Tidak ada gambar adegan 02 yang berhasil dibuat.
- Jangan menandai batch 1 selesai: baru satu file lokal, belum ZIP/preview/upload Drive.
- Ditambahkan `pipeline/check_short.py`: validasi 30 adegan, 6 chunk, jumlah kata, nama file; normalisasi opsional ke direktori terpisah dengan LANCZOS dan UnsharpMask sesuai handoff. Tidak menggambar overlay.
- Tiga tes unittest lolos. Naskah lolos validasi: 360 kata.
- Upload naskah ke Drive masih tertunda. Pencarian Drive sebelumnya tidak menemukan nama mengandung 13-SHORT.
