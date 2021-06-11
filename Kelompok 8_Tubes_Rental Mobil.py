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
    os.system("cls")
    adr = "Jl. Jalan Terus Biar Asik No. 12 Kota Surabaya"
    print("=====================================================")
    print("========== PT NGABERS BRAKTAKTAK AND FREND ==========")
    print(adr.center(53))
    print("=====================================================\n")


def menu_utama():
    mut = True
    print("====================")
    print("==== Menu Utama ====")
    print("====================")
    jam = datetime.datetime.now()
    print(jam.strftime("%A, %d %B %Y %H:%M:%S"))
    print("1. Login customer")
    print("2. Login admin")
    print("3. Lupa password customer")
    print("4. Exit program")
    while mut == True:
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
    return ut


def login_cust():
    os.system("cls")
    print("========================")
    print("==== Login customer ====")
    print("========================")
    stat_akun = ""
    while True:
        if stat_akun == "Y" or stat_akun == "T":
            break
        else:
            stat_akun = input("Apakah anda sudah memiliki akun (Y/T) : ")
            stat_akun = stat_akun.upper()
    return stat_akun


def custY():
    os.system("cls")
    print("========================")
    print("==== Login customer ====")
    print("========================")
    pd.options.mode.chained_assignment = None  # default='warn', supaya tdk ada warning saat mengganti value
    file = "data_pelanggan.xlsx"
    data_pelanggan = pd.read_excel(file, index_col="No").loc[:, "Nama":]
    df = pd.DataFrame(data_pelanggan)
    # mengecek data
    perc = 0
    lgn = True
    cy = True
    while cy == True:
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
            if (perc == 3):
                print("Terlalu banyak percobaan login!")
                cy = False
                input("Tekan enter untuk kembali ke menu utama! ")
    return lgn, True, nama, n_identitas, j_identitas, akun


def cek_login(username, password, df):
    for i in range(1, len(df["Username"]) + 1):
        if ((username == df["Username"][i]) and (password == df["Password"][i])):
            nama = df["Nama"][i]
            akun = df["Username"][i]
            n_identitas = df["No. Identitas"][i]
            j_identitas = df["Identitas (KTP/SIM)"][i]
            aa = True
            break
        else:
            nama = "Not Found!"
            n_identitas = ""
            j_identitas = ""
            akun = ""
            aa = False
            pass
    return aa, nama, n_identitas, j_identitas, akun


def custT():
    os.system("cls")
    val = True
    print("========================")
    print("==== Pembuatan akun ====")
    print("========================")
    file = "data_pelanggan.xlsx"
    data_pelanggan = pd.read_excel(file)
    df = pd.DataFrame(data_pelanggan)

    while True:
        user = str(input("username : "))
        if user in list(df["Username"].values):
            print("username sudah ada")
        else:
            break
    password = str(input("password : "))
    nama = str(input("nama lengkap : "))
    nama = nama.title()
    alamat = str(input("alamat : "))
    alamat = alamat.title()
    cjk = True
    while cjk == True:
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
    while validate_email(email) == False:
        email = str(input("masukkan email yang tepat : "))

    df.loc[len(df.index)] = [len(df) + 1, nama, identitas, no_id, user, password, email, alamat, jenis_kelamin]
    export = pd.ExcelWriter(file)
    df.to_excel(export, index=False)
    export.save()
    print("Sedang membuat akun...")
    loading()
    print("\n==== Akun berhasil dibuat! ====")


def login_berhasil():
    os.system("cls")
    print("==== Login Berhasil! ====\n")
    time.sleep(1)


def login_gagal():
    os.system("cls")
    print("==== Login Gagal! ====")
    time.sleep(1)


def menu_cust(nama):
    os.system("cls")
    print("============================")
    print("==== Selamat Datang %s! ====" % nama)
    print("============================")
    print("1. Penyewaan mobil")
    print("2. Pengembalian mobil")
    print("3. Log out")
    while True:
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
    return chs, True


def cek_bisa_pesan(rentang_waktu12, rentang_waktu34):
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
    return cek


def menu_sewa(akun, nama):
    os.system("cls")
    jenis_pembayaran = "DP Awal"
    print("========================")
    print("==== Menu Persewaan ====")
    print("========================")
    data_mobil = pd.read_excel("data_kendaraan.xlsx")
    df = pd.DataFrame(data_mobil)
    kolom = df.columns.tolist()
    kolom.remove("Penyewa")
    print(df.to_string(index=False, columns=kolom))
    while True:
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
    index_mobil = no_mobil - 1
    while True:
        jenis = input("Pesan untuk hari ini?(Y/T): ")
        if jenis.upper() == "Y":
            x = datetime.datetime.now()
            date_awal = x.strftime("%d/%m/%Y")
            break
        elif jenis.upper() == "T":
            tgl_awal = int(input("Masukkan tanggal pemesanan: "))
            bln_awal = int(input("Masukkan bulan pemesanan: "))
            thn_awal = int(input("Masukkan tahun pemesanan: "))
            date_awal = f"{str(tgl_awal).zfill(2)}/{str(bln_awal).zfill(2)}/{thn_awal}"
            break
        else:
            print("Mohon masukkan Y/T")
            pass

    tgl_awal, bln_awal, thn_awal = date_awal.split("/")
    d1 = datetime.date(int(thn_awal), int(bln_awal), int(tgl_awal))

    lama_hari = int(input("Masukkan lama waktu penyewaan (dalam hari): "))
    d = datetime.timedelta(days=lama_hari)
    d2 = d1 + d
    date_akhir = f"{d2.day}/{d2.month}/{d2.year}"
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
        lanjut = input("Apakah anda melanjutkan ke tahap pembayaran?(Y/T): ")
        if lanjut.upper() == "T":
            print("Silahkan melakukan input ulang")
            jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari = " a", " a", " a", " a", " a", " a", " a"
            return jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari, False
        elif lanjut.upper() == "Y":
            if jenis.upper() == "Y":
                df["Status"][index_mobil] = f"Disewakan kepada {nama}"

            sel_dict.update({akun: rentang_sewa, "akun": ["awal", "akhir"]})
            df["Penyewa"][index_mobil] = sel_dict
            plat = df["No Polisi"][index_mobil]
            kendaraan = df["Jenis"][index_mobil]
            bill = int(df["Harga"][index_mobil])
            sel = df["Penyewa"][index_mobil]
            export = pd.ExcelWriter("data_kendaraan.xlsx")
            df.to_excel(export, index=False)
            export.save()
            a = False
        else:
            print("Mohon masukkan (Y/T)")
    return jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari, True


def menu_pengembalian(akun, nama):
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


