# Program Rental Mobil

## Tugas Besar Praktikum Program Komputer 2021 Kelas A
## Kelompok 08

## Program ini dibuat untuk memudahkan pemilik usaha sewa mobil untuk mengatur katalog kendaraan yang disewakan serta memudahkan penyewa untuk memilih katalog mobil yang akan disewa

# Repository

## Berkas "Kelompok 8_flowchart.pdf"
###   Merupakan lampiran berupa diagram alir yang menjelaskan cara kerja program

## Berkas "Kelompok 8_Tubes_Rental Mobil.py" 
###   Merupakan file program rental mobil 

## Berkas "Data_kendaraan.xlsx"
###   Merupakan file penunjang jalannya program yang berisi daftar katalog kendaraan

## Berkas "Data_pelanggan.xlsx"
###   Merupakan file penunjang jalannya program yang berisi identitas dan informasi akun pelanggan

## Berkas "Kelompok 8_TUBES TAHAP 1.pdf"
###   Merupakan file laporan tugas besar tahap 1 Mata Kuliah Praktikum Programa Komputer

## Berkas "README.md"
###   Merupakan penjelasan singkat dari isi repository

## System Requirement
### Python v3
### OS apapun dengan syarat memiliki IDE python
### Library os
### Library time
### Library datetime
### Library pandas
### Library validate_email
### Library threading
### Library sys
### Library itertools
### Berkas tambahan
#### 1. File excel data kendaraan
#### 2. File excel data pelanggan

## Penjelasan singkat program
### 1. Program start
### 2. Tampilan menu utama berisi Login Admin dan Login Pelanggan
### 3. Jika user memilih Login Admin, user akan menginput username dan password admin
### 4. Program menampilkan pilihan menu Tambah Armada, Kurangi Armada, dan Update Harga Sewa
### 5. Jika user memilih menu Tambah Armada, program akan membuka database armada dan akan menambahkan data armada baru
### 6. Jika user memilih menu Kurangi Armada, program akan membuka database armada dan menghapus data armada yang dipilih
### 7. Jika user memilih menu Update Harga Sewa, program akan membuka database armada dan akan mengubah data harga sewa armada yang dipilih
### 8. Jika user tidak memilih Login Admin, program akan menanyakan kepemilikan akun pelanggan
### 9. Jika user belum memiliki akun, program akan mewajibkan untuk membuat akun terlebih dahulu
### 10. Jika user memiliki akun, user akan diminta untuk menginputkan username dan password
### 11. Program akan menampilkan Menu Pengembalian dan Menu Penyewaan
### 12. Jika user memilih Menu Pengembalian, program akan meminta user untuk menginputkan data armada yang ingin dikembalikan
### 13. Program akan mengubah status armada menjadi "Tersedia" pada database
### 14. Setelah status berubah, program akan menghitung jumlah tagihan kepada pelanggan
### 15. Jika user tidak memilih menu pengembalian, program akan secara otomatis menampilkan data harga dan harga armada yang bisa disewakan
### 16. Program akan meminta user menginputkan pilihan armada yang hendak disewakan
### 17. Program akan mengubah status armada menjadi "Tidak Tersedia" pada database
### 18. Program akan menghitung jumlah DP dan asuransi yang harus dibayarkan oleh pelanggan
### 19. Program akan menampilkan pilihan metode pembayaran, yaitu Tunai dan Non Tunai
### 20. Program akan meminta user menginputkan pilihan metode pembayaran yang diinginkan
### 21. Program akan memproses pembayaran sesuai dengan metode yang dipilih
### 22. Cetak struk
### 23. Program selesai
