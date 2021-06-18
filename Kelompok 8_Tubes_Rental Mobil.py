import os
import datetime
import time
import pandas as pd
from validate_email import validate_email
from datetime import date
import threading
import sys
import itertools
import json


def judul():
    #Menampilkan judul
    os.system("cls")
    adr = "Jl. Jalan Terus Biar Asik No. 12 Kota Surabaya"
    print("=====================================================")
    print("========== PT NGABERS BRAKTAKTAK AND FREND ==========")
    print(adr.center(53))                                                    #Agar dapat tertulis rapih di tengah
    print("=====================================================\n")


def menu_utama():
    #Menampilkan menu utama 
    mut = True
    print("====================")
    print("==== Menu Utama ====")
    print("====================")
    jam = datetime.datetime.now()                                           #Mengimpor local time dari komputer saat dioperasikan
    print(jam.strftime("%A, %d %B %Y %H:%M:%S"))                            #Menampilkan local time dari komputer saat dioperasikan
    print("1. Login customer")
    print("2. Login admin")
    print("3. Lupa password customer")
    print("4. Exit program")
    while mut == True:
        # Looping yang berungsi untuk menampilkan "Mohon masukkan angka 1/2/3/4" apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan erlanjut 
        try:
            ut = int(input("Masukkan menu yang anda pilih (1/2/3/4) : "))
        except:
            print("Mohon masukkan angka 1/2/3/4")
        else:
            if ut in [1, 2, 3, 4]:
                break
            else:
                print("Mohon masukkan angka 1/2/3/4")
                pass
    return ut                                                               #Mengembalikan variabel "ut" untuk digunakan pada tahap selanjutnya


def login_cust():
    #Menampilkan menu log in customer
    #Menanyakan kepada user apakah sudah memiliki akun atau belum
    os.system("cls")
    print("========================")
    print("==== Login customer ====")
    print("========================")
    stat_akun = ""
    while True:
        #Looping yang berfungsi untuk menampilkan "Apakah anda sudah memiliki akun (Y/T)" apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan berlanjut
        if stat_akun == "Y" or stat_akun == "T":
            break
        else:
            stat_akun = input("Apakah anda sudah memiliki akun (Y/T) : ")
            stat_akun = stat_akun.upper()
    return stat_akun                                                        #Mengembalikan variabel "stat_akun" untuk proses berikutnya


def custY():
    #Menampilkan menu apabila customer menginput "Y"
    os.system("cls")
    print("========================")
    print("==== Login customer ====")
    print("========================")
    pd.options.mode.chained_assignment = None                              #default='warn', supaya tdk ada warning saat mengganti value
    file = "data_pelanggan.xlsx"
    data_pelanggan = pd.read_excel(file, index_col="No").loc[:, "Nama":]   #Program membuka file excel dengan menggunakan pandas 
    df = pd.DataFrame(data_pelanggan)                                      #Dijadikan DataFrame
    # mengecek data
    perc = 0                                                               #Untuk mengecek percobaan log in yang apabila username dan password yang diinputkan tidak tepat, variabel "perc" akan ter-increment 
    lgn = True
    cy = True
    while cy == True:
        #Looping yang berfungsi untuk menampilkan "Maaf Username atau Password Anda Salah!" apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan berlanjut
        try:
            username = str(input("Username : "))
            password = str(input("Password : "))
        except:
            loading()
            login_gagal()
            print("==== Maaf Username atau Password Anda Salah! ====\n")
            perc += 1
        else:
            aa, nama, n_identitas, j_identitas, akun = cek_login(username, password, df)
            if (aa == True):
                lgn = True
                loading()
                break
            else:
                loading()
                login_gagal()
                print("==== Maaf Username atau Password Anda Salah! ====\n")
                lgn = False
                perc += 1
                pass
            if (perc == 3):                                             #Jika nilai variabel "perc" = 3 atau 3x percobaan salah, program akan kembali ke menu utama secara otomatis
                print("Terlalu banyak percobaan login!")
                cy = False
                input("Tekan enter untuk kembali ke menu utama! ")
    return lgn, True, nama, n_identitas, j_identitas, akun              #mengembalikan variabel "lgn", "nama", "n_identitas", "j_identitas", dan "akun" untuk tahap selanjutnya


def cek_login(username, password, df):
    #Untuk mengecek akun customer (username dan password) apakah ada di database dan apakah username dan password yang diinputkan sesuai atau tidak
    #df yang merupakan DataFrame dari database pelanggan, kita gunakan untuk mengecek kesesuaian username dan password 
    for i in range(1, len(df["Username"]) + 1):
        #Mengecek data yang teradapat pada database mulai dari indeks pertama hingga terakhir untuk mengecek kesesuaian username dan password 
        if ((username == df["Username"][i]) and (password == df["Password"][i])):
            nama = df["Nama"][i]
            akun = df["Username"][i]
            n_identitas = df["No. Identitas"][i]
            j_identitas = df["Identitas (KTP/SIM)"][i]
            aa = True
            break                                                       #jika data ditemukan, akan mengembalikan variable "aa" dengan nilai True untuk menandakan bahwa data cocok dengan database
        else:
            nama = "Not Found!"
            n_identitas = ""
            j_identitas = ""
            akun = ""
            aa = False                                                  #jika data tidak ditemukan akan mengembalikan variabel "aa" dengan nilai False 
            pass
    return aa, nama, n_identitas, j_identitas, akun                     #mengembalikan variabel aa, nama, n_identitas, j_identitas, dan akun


def custT():
    #Menampilkan menu apabila customer tidak memiliki akun
    #Menyajikan menu pembuatan akun baru 
    os.system("cls")
    val = True
    print("========================")
    print("==== Pembuatan akun ====")
    print("========================")
    file = "data_pelanggan.xlsx"                                        
    data_pelanggan = pd.read_excel(file)                                #Membaca file excel "data_pelanggan.xlsx" menggunakan pandas
    df = pd.DataFrame(data_pelanggan)                                   #Dijadikan DataFrame

    while True:
        #Memeriksa apakah username yang baru dibuat sudah ada atau belum pada database
        user = str(input("username : "))
        if user in list(df["Username"].values):
            print("username sudah ada")
        else:
            break
    #Input data-data yang dibutuhkan untuk keperluan pembuatan akun baru
    password = str(input("password : "))
    nama = str(input("nama lengkap : "))
    nama = nama.title()
    alamat = str(input("alamat : "))
    alamat = alamat.title()
    cjk = True
    while cjk == True:
        #Memastikan data jenis kelamin dimasukkan dengan tepat sesuai kriteria (L/P) yang telah disediakan program
        try:
            jk = str(input("jenis kelamin [L/P]: "))
        except:
            print("Pilih jenis kelamin yang benar! [L/P]")
        else:
            if (jk.upper() == "L"):
                jenis_kelamin = "Laki - Laki"
                # cjk = False
                break
            elif (jk.upper() == "P"):
                jenis_kelamin = "Perempuan"
                # cjk = False
                break
            else:
                print("Pilih jenis kelamin yang benar! [L/P]")
                pass
    identitas = str(input("pilih kartu identitas (SIM/KTP) : "))
    no_id = str(input("no identitas %s : " % identitas.upper()))
    email = str(input("email : "))
    while validate_email(email) == False:                                       #Mengecek apakah email yang dimasukkan sudah seesuai atau belum (pengecekan dilakukan berdasarkan ada tidaknya domain)
        email = str(input("masukkan email yang tepat : "))

    df.loc[len(df.index)] = [len(df) + 1, nama, identitas, no_id, user, password, email, alamat, jenis_kelamin]     #Menambahkan akun yang baru dengan menambah baris baru pada database
    export = pd.ExcelWriter(file)
    df.to_excel(export, index=False)
    export.save()
    print("Sedang membuat akun...")
    loading()
    print("\n==== Akun berhasil dibuat! ====")


def login_berhasil():
    #Menampilkan keterangan log in berhasil
    os.system("cls")
    print("\n==== Login Berhasil! ====\n") 
    time.sleep(1)                                       #Membuat jeda waktu 1 detik untuk menampilkan "\n==== Login Berhasil! ====\n" setelah menu sebelumnya


def login_gagal():
    #Menampilkan keterangan log in gagal
    os.system("cls")
    print("\n==== Login Gagal! ====")
    time.sleep(1)                                       #Membuat jeda waktu 1 detik untuk menampilkan "\n"==== Login Gagal! ===="\n" setelah menu sebelumnya


def menu_cust(nama):
    #Menampilkan fitur-fitur yang terdapat di menu customer
    os.system("cls")
    print("============================")
    print("==== Selamat Datang %s! ====" % nama)
    print("============================")
    print("1. Penyewaan mobil")
    print("2. Pengembalian mobil")
    print("3. Log out")
    while True:
    #Looping yang berfungsi untuk menampilkan "Mohon masukkan angka 1/2/3" apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan berlanjut
        try:
            chs = int(input("Masukkan menu yang anda pilih (1/2/3) : "))
        except:
            print("Mohon masukkan angka 1/2/3")
        else:
            if chs in [1, 2, 3]:
                break
            else:
                print("Mohon masukkan angka 1/2/3")
                pass
    return chs, True                                    #mengembalikan variabel chs untuk tahap selanjutnya


def cek_bisa_pesan(rentang_waktu12, rentang_waktu34):
    #untuk mengecek tanggal pesanan pada armada yang dipilih pelanggan apakah armada tersebut telah disewa, dibooking atau belum
    string12 = rentang_waktu12
    tanggal1, tanggal2 = string12
    tgl1, bln1, thn1 = tanggal1.split("/")
    tgl2, bln2, thn2 = tanggal2.split("/")

    d1 = datetime.date(int(thn1), int(bln1), int(tgl1))
    d2 = datetime.date(int(thn2), int(bln2), int(tgl2))

    lst_tanggal12 = [d1 + datetime.timedelta(days=x) for x in range((d2 - d1).days + 1)]

    string34 = rentang_waktu34
    tanggal3, tanggal4 = string34
    tgl3, bln3, thn3 = tanggal3.split("/")
    tgl4, bln4, thn4 = tanggal4.split("/")

    d3 = datetime.date(int(thn3), int(bln3), int(tgl3))
    d4 = datetime.date(int(thn4), int(bln4), int(tgl4))

    lst_tanggal34 = [d3 + datetime.timedelta(days=x) for x in range((d4 - d3).days + 1)]

    set_tanggal12 = set(lst_tanggal12)
    set_tanggal34 = set(lst_tanggal34)

    cek = set_tanggal12.isdisjoint(set_tanggal34)
    return cek                                           #mengembalikan nilai dari variabel cek untuk menentukan status kendaraan sudah disewa, dibooking atau belum


def menu_sewa(akun, nama):
    #Menampilkan menu penyewaan
    os.system("cls")
    jenis_pembayaran = "DP Awal"
    print("========================")
    print("==== Menu Persewaan ====")
    print("========================")
    data_mobil = pd.read_excel("data_kendaraan.xlsx")   #membaca file database excel
    df = pd.DataFrame(data_mobil)                       #menjadikan DataFrame
    kolom = df.columns.tolist()                         #mengubah kolom menjadi list
    kolom.remove("Penyewa")                             #menghilangkan kolom "Penyewa" agar tidak ditampilkan
    print(df.to_string(index=False, columns=kolom))     #menampilkan dataframe sebagai string dengan kolom yang baru
    while True:
        #Looping yang berfungsi untuk menampilkan "Mohon masukkan angka" apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan berlanjut
        try:
            no_mobil = int(input("Masukkan nomor mobil yang anda pilih: "))
        except:
            print("Mohon masukkan angka")
        else:
            if no_mobil in range(1, len(df) + 1):
                break
            else:
                print("Mohon masukkan angka sesuai tabel")
                pass
    index_mobil = no_mobil - 1                          #karena nomor mobil yang kita gunakan merupakan bilangan asli, sedangkan penomoran index menggunakan bilangan cacah. oleh karena itu, 
    while True:
        #looping yang berfungsi untuk menampilkan "Mohon masukkan Y/T" apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan berlanjut
        jenis = input("Pesan untuk hari ini?(Y/T): ")
        if jenis.upper() == "Y":
            x = datetime.datetime.now()
            date_awal = x.strftime("%d/%m/%Y")          #mengimpor local time komputer sekarang untuk menentukan tanggal awal sewa apabila mulai sewa hari ini
            break
        elif jenis.upper() == "T":
            tgl_awal = int(input("Masukkan tanggal pemesanan: "))
            bln_awal = int(input("Masukkan bulan pemesanan: "))
            thn_awal = int(input("Masukkan tahun pemesanan: "))
            date_awal = f"{str(tgl_awal).zfill(2)}/{str(bln_awal).zfill(2)}/{thn_awal}" #mwngubah tanggal, bulan, dan tahun yang diinput dengan fitur zfill agar angkanya menjadi 2 digit
            break
        else:
            print("Mohon masukkan Y/T")
            pass

    tgl_awal, bln_awal, thn_awal = date_awal.split("/") #memisahkan tanggal, bulan, dan tahun hasil input menggunakan fitur ".split()"
    d1 = datetime.date(int(thn_awal), int(bln_awal), int(tgl_awal))

    lama_hari = int(input("Masukkan lama waktu penyewaan (dalam hari): "))
    d = datetime.timedelta(days=lama_hari)              #menentukan tanggal akhir dengan menambahkan lama sewa ke tanggal awal
    d2 = d1 + d
    date_akhir = f"{d2.day}/{d2.month}/{d2.year}"       #membuat data tanggal akhir menjadi berformat tanggal
    rentang_sewa = [date_awal, date_akhir]              
    tgl_awal = str(date_awal)
    tgl_akhir = str(date_akhir)
    sel = df["Penyewa"][index_mobil]
    sel = sel.replace("\'", "\"")
    sel_dict = json.loads(sel)                          
    sel_dict.pop("akun")
    for i in sel_dict.values():
        cek = cek_bisa_pesan(i, rentang_sewa)  # False artinya ada tanggal yang overlap, jd ga bisa pesan
        if cek == False:
            print(f"Mobil tersebut sudah dibooking untuk tanggal {i[0]} sampai {i[1]}")
            input("Tekan enter untuk melanjutkan")
            jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari = " a", " a", " a", " a", " a", " a", " a"
            return jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari, cek
        elif cek == True:
            pass
    print(f"Anda akan menyewa {df['Jenis'][index_mobil]} selama {lama_hari} hari")
    a = True
    while a:
        #looping untuk menampilkan "Mohon masukkan (Y/T)" apabila user memasukkan input yang salah. apabila user memasukkan input yang benar, program akan berlannjut sesuai pilihan user
        lanjut = input("Apakah anda melanjutkan ke tahap pembayaran?(Y/T): ")
        if lanjut.upper() == "T":
            print("Silahkan melakukan input ulang")
            jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari = " a", " a", " a", " a", " a", " a", " a"
            return jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari, False
        elif lanjut.upper() == "Y":
            if jenis.upper() == "Y":
                df["Status"][index_mobil] = f"Disewakan kepada {nama}"

            sel_dict.update({akun: rentang_sewa, "akun": ["awal", "akhir"]})    #menambahkan data penyewa/booking ke database
            df["Penyewa"][index_mobil] = sel_dict
            plat = df["No Polisi"][index_mobil]
            kendaraan = df["Jenis"][index_mobil]
            bill = int(df["Harga"][index_mobil])
            sel = df["Penyewa"][index_mobil]
            export = pd.ExcelWriter("data_kendaraan.xlsx")                      #menulis ulang database
            df.to_excel(export, index=False)                                    #mengekspor hasil database baru tanpa nomor index
            export.save()                                                       #menyimpan database
            a = False
        else:
            print("Mohon masukkan (Y/T)")
    return jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari, True    #mengembalikan nilai dari variabel jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari untuk tahap selanjutnya


def menu_pengembalian(akun, nama):
    #Menampilkan menu pengembalian 
    os.system("cls")
    jenis_pembayaran = "Pelunasan"
    print("===========================")
    print("==== Menu Pengembalian ====")
    print("===========================")
    data_mobil = pd.read_excel("data_kendaraan.xlsx")
    df = pd.DataFrame(data_mobil)
    kolom = df.columns.tolist()
    kolom.remove("Penyewa")
    print(df.to_string(index=False, columns=kolom))
    while True:
        while True:
            try:
                no_mobil = int(input("Masukkan nomor mobil yang akan anda kembalikan: "))
            except:
                print("Mohon masukkan angka")
            else:
                if no_mobil in range(1, len(df) + 1):
                    break
                else:
                    print("Mohon masukkan angka sesuai tabel")
                    pass
        index_mobil = no_mobil - 1
        plat = df["No Polisi"][index_mobil]
        kendaraan = df["Jenis"][index_mobil]
        bill = int(df["Harga"][index_mobil])
        if df["Status"][index_mobil] == f"Disewakan kepada {nama}":
            df["Status"][index_mobil] = "Tersedia"
            sel = df["Penyewa"][index_mobil]
            sel = sel.replace("\'", "\"")
            sel_dict = json.loads(sel)
            df["Penyewa"][index_mobil] = sel_dict
            d1, d2 = df["Penyewa"][index_mobil][akun]
            tgl1, bln1, thn1 = d1.split("/")
            d1 = date(int(thn1), int(bln1), int(tgl1))
            tgl2, bln2, thn2 = d2.split("/")
            d2 = date(int(thn2), int(bln2), int(tgl2))
            d3 = d2 - d1
            lama_hari = d3.days
            lama_hari = int(lama_hari)
            tgl_awal = df["Penyewa"][index_mobil][akun][0]
            tgl_akhir = df["Penyewa"][index_mobil][akun][1]
            del df["Penyewa"][index_mobil][akun]
            print(df.to_string(index=False))
            export = pd.ExcelWriter("data_kendaraan.xlsx")
            df.to_excel(export, index=False)
            export.save()
            break
        else:
            print("Mohon masukkan nomor mobil yang tepat")
    return jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, True, bill, lama_hari

def login_admin():
    os.system("cls")
    log = True
    print("=====================")
    print("==== Login Admin ====")
    print("=====================")
    file_pass_Admin = open("File Password Admin.txt", "r")                  #membuka file database login admin dengan aturan read only            
    data_str = file_pass_Admin.readlines()                                  #membaca file database per baris
    data = data_str[0]                                                      #membaca file database baris pertama
    datanw = json.loads(data)                                               #melakukan loads database sebagai dictionary dalam variabel "datanw"
    file_pass_Admin.close()                                                 #menutup file database
    user_Admin = str(datanw["username"])
    pass_Admin = str(datanw["password"])
    perc = 0
    ladmin = True
    while ladmin == True:
        #looping untuk menampilkan "==== Maaf Username atau Password Anda Salah! ====" apabila username dan password yang dimasukkan tidak sesuai, dan berlanjut ke tahap selanjutnya apabila sesuai database
        try:
            username = str(input("Username : "))
            password = str(input("Password : "))
        except:
            loading()
            login_gagal()
            print("==== Maaf Username atau Password Anda Salah! ====")
            perc += 1                                                       #terjadi increment setiap kali salah percobaan
        else:
            if ((username == user_Admin) and (password == pass_Admin)):
                log = True
                loading()
                break
            else:
                loading()
                login_gagal()
                print("==== Maaf Username atau Password Anda Salah! ====")
                log = False
                perc += 1
                pass
            if (perc == 3):                                                 #ketika username dan password yang dimasukkan tidak tepat dalam 3x percobaan, program akan otomatis kembali ke menu utama
                print("Terlalu banyak percobaan!")
                ladmin = False
    return log, True


def ganti_pwadmin():
    #Menampilkan menu ketika admin ingin mengganti password
    print("==============================")
    print("==== Ganti Password Admin ====")
    print("==============================")
    file_pass_Admin = open("File Password Admin.txt", "w")              #Program membuka dokumen "File Password Admin.txt"
    user_baru = str(input("Masukkan username baru : "))                 
    pass_baru = str(input("Masukkan password baru : "))
    data_pw = '{"username" : "%s", "password" : "%s"}\n\n==== Username dan Password Admin ====\nUsername : %s\nPassword : %s' % (
    user_baru, pass_baru, user_baru, pass_baru)                         #Program menginput data username dan password yang baru ke dalam dokumen "File Password Admin.txt"
    file_pass_Admin.writelines(data_pw)                                 #program menulis ulang file database
    file_pass_Admin.close()                                             #menutup file database
    succ_pw()


def menu_admin():
    #Menampilkan fitur-fitur yang terdapat di menu admin 
    print("====================")
    print("==== Menu Admin ====")
    print("====================")
    print("1. Menambah armada")
    print("2. Mengurangi armada")
    print("3. Update data kendaraan")
    print("4. Ganti password admin")
    print("5. Log out")
    while True:
         #Looping yang berfungsi untuk menampilkan "Mohon masukkan angka 1/2/3/4/5 apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan berlanjut
        try:
            ma = int(input("Masukkan menu yang anda pilih [1/2/3/4/5] : "))
        except:
            print("Mohon masukkan angka 1/2/3/4/5")
        else:
            if ma in [1, 2, 3, 4, 5]:
                break
            else:
                print("Mohon masukkan angka 1/2/3/4/5")
                pass
    return ma                                                       #mengembalikan nilai variabel "ma" untuk tahap selanjutnya


def T_armada():
    #Menampilkan menu tambah armada
    print("========================")
    print("==== Tambah Armada ====")
    print("========================")
    # data_kendaraan()
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", sheet_name="Sheet1", header=0)              #Membuka dokumen "data_kendaraan.xlsx"
    df = pd.DataFrame(data)                                                                 #Menjadikannya DataFrame
    print(df.to_string(index=False))                                                        #menampilkan data armada tanpa index dan berbentuk string

    # tambah mobil
    print("===== Masukkan data mobil baru =====")
    mob = str(input("Masukkan jenis mobil: "))
    hrg = str(input("Masukkan harga sewa mobil: "))
    thn = str(input("Masukkan tahun mobil: "))
    kap = str(input("Masukkan kapasitas penumpang mobil: "))
    no_pol = str(input("Masukkan nomor polisi mobil: "))
    dummy = str({"akun": ["awal", "akhir"]})
    stat = "Tersedia"
    mobil_baru = ["dor", mob, hrg, thn, kap, no_pol, stat, dummy]                     
    jlh_mbl = len(df["Harga"])
    print(jlh_mbl)
    print("Jumlah mobil saat ini", jlh_mbl)
    df.loc[(jlh_mbl + 1)] = mobil_baru                                      #Mengimpor data mobil baru yang ditambahkan ke dalam database
    df = df.sort_values(by="Jenis")                                         #Mengurutkan data mobil terbaru sesuai dengan urutan abjadnya pada kriteria "jenis"
    df["No"] = [x for x in range(1, len(df) + 1)]
    df = df.reset_index(drop=True)                                          #mengurutkan kembali nomor index agar urut kembali
    export3 = pd.ExcelWriter("data_kendaraan.xlsx")                         #menulis ulang file database
    df.to_excel(export3, index=False)                                       #mengekspor database
    export3.save()                                                          #menyimpan database
    print("Data mobil terbaru:\n", df.to_string(index=False))


def K_armada():
    #Menampilan menu kurangi armada
    print("=======================")
    print("==== Kurangi Armada ====")
    print("=======================")
    # data_kendaraan()
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", header=0)
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    while True:
        #Looping yang berungsi untuk menampilkan "Mohon masukkan angka saja" apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan berlanjut
        try:
            jml = int(input("Pilih nomor kendaraan yang akan dikurangi: "))
        except:
            print("Mohon masukkan angka saja")
        else:
            break
    pd.options.mode.chained_assignment = None

    df = df.drop(jml - 1)                               #Menghapus baris data mobil yang dihapus
    df["No"] = [x for x in range(1, len(df) + 1)]

    df = df.reset_index(drop=True)
    export4 = pd.ExcelWriter("data_kendaraan.xlsx")
    df.to_excel(export4, index=False)
    export4.save()
    print("Data mobil terbaru:\n", df.to_string(index=False))


def U_data():
    #Menampilkan menu update data
    print("===============================")
    print("==== Update Data Kendaraan ====")
    print("===============================")
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", index_col="No", sheet_name="Sheet1", header=0)
    df = pd.DataFrame(data)
    print(df.to_string(index=False))

    update = int(input("Mobil yang akan diubah datanya[ex:1]:"))
    print("Berikut data mobil yang ingin Anda ubah:")
    print(df.iloc[update - 1])
    print("1. Ubah jenis mobil")
    print("2. Ubah harga sewa mobil")
    print("3. Ubah tahun mobil")
    print("4. Ubah kapasitas mobil")
    print("5. Ubah No polisi mobil")
    print("6. Ubah status mobil")
    ud = True
    while ud == True:
        #Looping yang berungsi untuk menampilkan "Input anda salah!" apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan berlanjut
        try:
            upd = int(input("Masukkan menu yang Anda ingin ubah (1/2/3/4/5/6) : "))
        except:
            print("Input anda salah!")
        else:
            if (upd == 1):
                jns_baru = str(input("Masukkan jenis mobil terbaru:"))          
                df["Jenis"][update] = jns_baru                                  #Memperbarui jenis yang terakhir diubah
                ud = False
            elif (upd == 2):
                hrg_baru = str(input("Masukkan harga mobil terbaru:"))
                df["Harga"][update] = hrg_baru                                   #Memperbarui harga yang terakhir diubah
                ud = False
            elif (upd == 3):
                thn_baru = str(input("Masukkan tahun mobil terbaru:"))
                df["Tahun"][update] = thn_baru                                   #Memperbarui tahun yang terakhir diubah
                ud = False
            elif (upd == 4):
                kps_baru = str(input("Masukkan kapasitas mobil terbaru:"))
                df["Kapasitas"][update] = kps_baru                               #Memperbarui kapasitas yang terakhir diubah
                ud = False
            elif (upd == 5):
                nopol_baru = str(input("Masukkan no polisi mobil terbaru:"))        #Memperbarui no polisi yang terakhir diubah
                df["No Polisi"][update] = nopol_baru
                ud = False
            elif (upd == 6):
                stat_baru = str(input("Masukkan status mobil terbaru:"))            #Memperbarui status yang terakhir diubah
                df["Status"][update] = stat_baru
                ud = False
            else:
                print("Input anda salah!")

    # ubah data mobil
    export5 = pd.ExcelWriter("data_kendaraan.xlsx")
    df.to_excel(export5, index=False)
    export5.save()
    print(df)

def change_pwcust(username, identitas, df):
    # mengganti password customer
    for i in range(1, len(df["Username"]) + 1):
        if ((username == df["Username"][i]) and (identitas == df["No. Identitas"][i])):
            pw_baru = str(input("Masukkan Password baru : "))
            df["Password"][i] = pw_baru
            ab = True
            break
        else:
            ab = False
    return ab


def lupa_pw():
    # menu lupa password customer
    print("============================")
    print("==== Menu Lupa Password ====")
    print("============================")
    pd.options.mode.chained_assignment = None  # default='warn', supaya tdk ada warning saat mengganti value
    file = "data_pelanggan.xlsx"
    data_pelanggan = pd.read_excel(file, index_col="No").loc[:, "Nama":]
    df = pd.DataFrame(data_pelanggan)
    # mengecek data
    while True:
        # Looping yang berungsi untuk menampilkan "Maaf Username atau Nomor ID Anda Salah!" apabila input yang dimasukkan oleh user salah, tetapi jika inputnya benar, program akan berlanjut
        try:
            username = str(input("Masukkan username anda : "))
            identitas = int(input("Masukkan no. id anda yang telah didaftarkan (KTP/SIM) : "))
        except:
            loading()
            print("\n==== Maaf Username atau Nomor ID Anda Salah! ====\n")
        else:
            ab = change_pwcust(username, identitas, df)
            if (ab == True):
                loading()
                succ_pw()
                break
            else:
                loading()
                fail_pw()
                pass
    export7 = pd.ExcelWriter("data_pelanggan.xlsx")
    df.to_excel(export7)
    export7.save()
    return True


def succ_pw():
    # menampilkan keterangan berhasil mengganti password
    os.system("cls")
    print("====================================")
    print("==== Password berhasil diganti! ====")
    print("====================================")


def fail_pw():
    # menampilkan keterengan gagal mengganti password
    os.system("cls")
    print("=============================================")
    print("====      Gagal mengganti password!      ====")
    print("==== Username atau ID Anda Mungkin Salah ====")
    print("=============================================")


def tunai(total):
    # menu pembayaran secara tunai
    print("\n=== Metode bayar non tunai ===")
    print("Tagihan anda sebesar Rp %d" % total)
    print("Bayar dengan uang pas!")
    via = " "
    idrek = " "
    no = " "
    lptun = True
    while lptun == True:
        # looping untuk menghitung pembayaran
        try:
            bayar = int(input("Masukkan jumlah uang yang anda bayarkan : "))
            change = bayar - total
        except:
            print("Bayar dengan jumlah uang yang sesuai!")
        else:
            if (change == 0):
                print("Anda berhasil membayar tagihan sebesar Rp %d" % total)
                print("terima kasih telah membayar dengan uang pas!")
                break
            elif (change > 0):
                print("Anda berhasil membayar tagihan sebesar Rp %d" % total)
                print("Jangan lupa ambil kembalian anda sebesar Rp %d, terima kasih!" % change)
                break
            else:
                print("Bayar dengan jumlah uang yang sesuai!")
                pass
    return total, via, no, idrek


def nontunai(total):
    # menu pembayaran secara nontunai
    truu = True
    print("\n=== Metode bayar non tunai ===")
    print("1. Kartu Kredit")
    print("2. Kartu Debit")
    print("3. Gopay")
    print("4. OVO")
    print("5. Shopee Pay")
    print("6. Dana\n")
    print("Tagihan anda sebesar Rp %d" % total)
    while truu == True:
        # looping untuk menentukan metode non tunai yang dipilih
        try:
            met = int(input("Pilih nomor metode bayar yang diinginkan [1/2/3/4/5/6] : "))
        except:
            print("Mohon masukkan angka [1/2/3/4/5/6]!")
        else:
            if (met not in [1, 2, 3, 4, 5, 6]):
                print("Mohon masukkan angka [1/2/3/4/5/6]!")
                pass
            else:
                truu = False
    if (met == 1):
        via = "Kartu Kredit"
        no = str(input("Masukkan nomor rekening anda : "))
        idrek = str(input("Masukkan nama pemilik kartu rekening : "))
        bank = str(input("Masukkan nama bank : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        processing_bayar()
        print(
            "\nPembayaran melalui kartu kredit bank %s nomor rekening %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (
            bank, no, idrek.title(), total))
    elif (met == 2):
        via = "Kartu Debit"
        no = str(input("Masukkan nomor rekening anda : "))
        idrek = str(input("Masukkan nama pemilik kartu rekening : "))
        bank = str(input("Masukkan nama bank : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        processing_bayar()
        print(
            "\nPembayaran melalui kartu debit bank %s nomor rekening %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (
            bank, no, idrek.title(), total))
    elif (met == 3):
        via = "Gopay"
        no = str(input("Masukkan nomor Gopay anda : "))
        idrek = str(input("Masukkan nama pemilik akun Gopay : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        processing_bayar()
        print("\nPembayaran melalui Gopay %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (
        no, idrek.title(), total))
    elif (met == 4):
        via = "Ovo"
        no = str(input("Masukkan nomor OVO anda : "))
        idrek = str(input("Masukkan nama pemilik akun OVO : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        processing_bayar()
        print(
            "\nPembayaran melalui OVO %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, idrek.title(), total))
    elif (met == 5):
        via = "Shopee Pay"
        no = str(input("Masukkan nomor Shopee Pay anda : "))
        idrek = str(input("Masukkan nama pemilik akun Shopee Pay : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        processing_bayar()
        print("\nPembayaran melalui Shopee Pay %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (
        no, idrek.title(), total))
    elif (met == 6):
        via = "Dana"
        no = str(input("Masukkan nomor Dana anda : "))
        idrek = str(input("Masukkan nama pemilik akun Dana : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        processing_bayar()
        print(
            "\nPembayaran melalui Dana %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, idrek.title(), total))
    else:
        print("Input salah!")
        pembayaran()
    return total, via, truu, no, idrek


def pembayaran(total):
    # menu untuk memilih metode pembayaran
    print("=== Pembayaran ===")
    print("1. Tunai")
    print("2. Non tunai")
    pj = True
    while pj == True:
        # looping untuk memilih metode pembayaran
        try:
            byr = int(input("Pilih metode pembayaran [1/2] : "))
        except:
            print("Masukkan input yang valid!")
        else:
            if (byr == 1):
                total, via, no, idrek = tunai(total)
                byr_stat = "Tunai"
                pj = False
            elif (byr == 2):
                total, via, truu, no, idrek = nontunai(total)
                byr_stat = "Non Tunai"
                pj = False
            else:
                print("Masukkan input yang valid!")
                pj == True
    print("\n")
    return byr_stat, total, via, no, idrek

def loading():
    # fungsi untuk menampilkan loading
    done = False

    def animate():
        # menampilkan animasi loading
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()
    time.sleep(4)
    done = True

    
def processing_bayar():
    # menampilkan animasi proses pembayaran
    done = False

    def animate():
        # proses menampilkan animas pembayaran
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rmemproses pembayaran ' + c)
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()
    time.sleep(5)
    done = True


def struk(nama, j_identitas, n_identitas, kendaraan, plat, tgl_awal, tgl_akhir, jenis_pembayaran, byr_stat, via, total,
          idrek, lama_hari):
    # menampilkan struk pembayaran
    os.system("cls")
    judul = "PT NGABERS BRAKTAKTAK AND FRENDS"
    address = "Jl. Jalan Terus Biar Asik No. 12 Kota Surabaya"
    thx = "Terima Kasih Telah Menyewa!"
    print("=====================================================")
    print(judul.center(53))
    print(address.center(53))
    print()
    print("Sewa Mobil")
    print("=====================================================")
    print("%s\t\t %s : %s" % (nama.title(), j_identitas.upper(), n_identitas))
    print("=====================================================")
    print("Kendaraan\t\t:\t%s" % kendaraan)
    print("No Polisi\t\t:\t%s" % plat)
    print("Tanggal Pinjam\t:\t" + str(tgl_awal))
    print("Tanggal Kembali\t:\t" + str(tgl_akhir))
    print("Lama Sewa\t\t:\t%d Hari" % lama_hari)
    print("=====================================================")
    print("______________________ %s ______________________" % jenis_pembayaran)
    print("Dibayar dengan\t:\t%s" % byr_stat)
    if (byr_stat == "Non Tunai"):
        print("Via\t\t:\t%s" % via)
        print("Nomor akun\t:\t%s" % no)
        print("Atas nama\t:\t%s" % idrek)
    print("Nominal bayar\t:\tRp %s\n" % total)
    print("=====================================================")
    print("============ Terima Kasih Telah Menyewa! ============")
    print("=====================================================\n")


def cust_byr(jenis_pembayaran, bill, lama_hari):
    # menghitung tagihan yang harus dibayarkan oleh customer
    bill = int(bill)
    asuransi = 0.1 * bill
    total = 0
    if (jenis_pembayaran == "DP Awal"):
        total = (asuransi + (0.5 * bill * lama_hari))
    elif (jenis_pembayaran == "Pelunasan"):
        denda = int(input("Masukkan jumlah denda : "))
        total = (0.5 * bill * lama_hari) + denda
    return total, jenis_pembayaran

#Bagian Program Utama
lagi = "Y"
while (lagi == "Y"):
    # looping agar selalu kembali ke menu utama
    os.system("cls")
    judul()
    ut = 0
    ut = menu_utama()
    if(ut == 1):
        stat_akun = login_cust()
        if(stat_akun.upper() == "Y"):
            akunY, tr, nama, n_identitas, j_identitas, akun = custY()
            if(akunY == True):
                login_berhasil()
                chs, truuuu = menu_cust(nama)
                if(chs == 1):
                    while True:
                        jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari, cek = menu_sewa(akun, nama)
                        if cek:
                            break
                        else:
                            pass
                    total, jenis_pembayaran = cust_byr(jenis_pembayaran, bill, lama_hari)
                    byr_stat, total, via, no, idrek = pembayaran(total)
                    input("Tekan enter untuk cetak struk... ")
                    print()
                    struk(nama, j_identitas, n_identitas, kendaraan, plat, tgl_awal, tgl_akhir, jenis_pembayaran, byr_stat, via, total, idrek, lama_hari)
                    input("Tekan enter untuk kembali ke menu utama! ")
                elif(chs == 2):
                    jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, true, bill, lama_hari = menu_pengembalian(akun, nama)
                    total, jenis_pembayaran = cust_byr(jenis_pembayaran, bill, lama_hari)
                    byr_stat, total, via, no, idrek = pembayaran(total)
                    input("Tekan enter untuk cetak struk... ")
                    print()
                    struk(nama, j_identitas, n_identitas, kendaraan, plat, tgl_awal, tgl_akhir, jenis_pembayaran, byr_stat, via, total, idrek, lama_hari)
                    input("Tekan enter untuk kembali ke menu utama! ")
                elif(chs == 3):
                    print("\nBerhasil Log Out!")
                    input("Tekan enter untuk kembali ke menu utama! ")
                else:
                    print("Input anda salah!")
        elif(stat_akun.upper() == "T"):
            custT()
            input("Tekan enter untuk kembali ke menu utama! ")
        else:
            print("Input anda salah!")
    elif(ut == 2):
        log, st = login_admin()
        if(log == True):
            login_berhasil()
            ma = menu_admin()
            if(ma == 1):
                T_armada()
                input("\nTekan enter untuk kembali ke menu utama! ")
            elif(ma == 2):
                K_armada()
                input("\nTekan enter untuk kembali ke menu utama! ")
            elif(ma == 3):
                U_data()
                input("\nTekan enter untuk kembali ke menu utama! ")
            elif(ma == 4):
                ganti_pwadmin()
                input("\nTekan enter untuk kembali ke menu utama! ")
            elif(ma == 5):
                print("\nBerhasil Log Out!")
                input("Tekan enter untuk kembali ke menu utama! ")
        else:
            input("Tekan enter untuk kembali ke menu utama! ")
    elif(ut == 3):
        lupa_pw()
        input("\nTekan enter untuk kembali ke menu utama! ")
    elif(ut == 4):
        print("Terima kasih telah menggunakan program kami, sampai jumpa kembali!")
        print("Program ditutup...")
        sys.exit()
    else:
        print("Input anda salah!")

    print("                    Sampai jumpa kembali!")

