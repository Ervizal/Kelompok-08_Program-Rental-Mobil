import os
import datetime
import time
import pandas as pd
from validate_email import validate_email
import threading
import sys
import itertools


def judul():
    os.system("cls")
    print("[======================================]")
    print("[=== PT NGABERS BRAKTAKTAK AND FREND ===]")
    print("[======================================]\n")


def menu_utama():
    print("====================")
    print("==== Menu Utama ====")
    print("====================")
    jam = datetime.datetime.now()
    print(jam.strftime("%A") + ",", jam.strftime("%d"), jam.strftime("%B"), jam.strftime("%Y"),
          jam.strftime("%H") + ":" + jam.strftime("%M") + ":" + jam.strftime("%S"))
    print("1. Login customer")
    print("2. Login admin")
    print("3. Exit program")
    ut = int(input("Masukkan menu yang anda pilih (1/2/3) : "))
    return ut


def login_cust():
    os.system("cls")
    print("========================")
    print("==== Login customer ====")
    print("========================")
    stat_akun = str(input("Apakah anda sudah memiliki akun (Y/T) : "))
    return stat_akun
    # if(akun.upper == "Y"):    lanjutan


def custY():
    os.system("cls")
    print("========================")
    print("==== Login customer ====")
    print("========================")
    # open data login dari csv atau excel
    user = str(input("username : "))
    password = str(input("password : "))

    # if username dan password sama dengan di csv atau excel then


def custT():
    os.system("cls")
    val = True
    print("========================")
    print("==== Pembuatan akun ====")
    print("========================")
    # open data csv atau excel
    # mode append pada data
    user = str(input("username : "))
    password = str(input("password : "))
    nama = str(input("nama lengkap : "))
    alamat = str(input("alamat : "))
    jenis_kelamin = str(input("jenis kelamin : "))
    identitas = str(input("pilih kartu identitas (SIM/KTP/PASPOR) : "))
    no_id = str(input("no identitas %s : " % identitas))
    email = str(input("email : "))
    while validate_email(email) == False:
        email = str(input("masukkan email yang tepat : "))
    # if (val == True):
    #     pass
    # else:
    #     print("Email yang anda masukkan salah!")
    #     custT()


    # append data ke csv atau excel


def login_berhasil():
    os.system("cls")
    print("==== Login Berhasil! ====\n")
    time.sleep(1)


def login_gagal():
    os.system("cls")
    print("==== Login Gagal! ====\n")
    time.sleep(1)


def menu_cust():
    os.system("cls")
    print("============================")
    print("==== Selamat Datang %s! ====" % username)
    print("============================")
    print("1. Penyewaan mobil")
    print("2. Pengembalian mobil")


def menu_sewa():
    os.system("cls")
    print("========================")
    print("==== Menu Persewaan ====")
    print("========================")
    # tampilkan kendaraan yang tersedia dan harga sewa nya


def menu_pengembalian():
    os.system("cls")
    print("===========================")
    print("==== Menu Pengembalian ====")
    print("===========================")


# mencari data mobil yang disewa dengan plat nomor, lalu statusnya diubah menjadi "Tersedia", dan nama penyewa diganti "-"

def login_admin():
    os.system("cls")
    pw1 = "Admin123"
    pw2 = "Admin123"
    log = True
    print("=====================")
    print("==== Login Admin ====")
    print("=====================")
    while True:
        try:
            user = str(input("Username : "))
            password = str(input("Password : "))
        except:
            loading()
            print("\n==== Maaf Username atau Password Anda Salah! ====")
        else:
            if ((user == pw1) and (password == pw2)):
                log = True
                break
            else:
                loading()
                print("\n==== Maaf Username atau Password Anda Salah! ====")
                log = False
                pass
    loading()
    return log, True


def data_kendaraan():
    os.system("cls")
    kendaraan = pd.read_excel("data_kendaraan.xlsx", sheetname="Sheet1")
    for jumlah in kendaraan:
        print("jumlah")
    # menyimpan data kendaraan di excel atau csv (sebisa mungkin excel shg menggunakan pandas sambil mempelajari pandas


def pesan():
    os.system("cls")
    print("========================")
    print("==== Menu Persewaan ====")
    print("========================")
    # memilih mobil yang tersedia, lalu pengisian biodata, pembayaran dll


def booking():
    os.system("cls")
    print("======================")
    print("==== Menu Booking ====")
    print("======================")
    # mencari mobil berdasarkan plat nomor, lalu status diubah menjadi disewakan pada .... hingga ....

def menu_admin():
    print("====================")
    print("==== Menu Admin ====")
    print("====================")
    print("1. Menambah armada")
    print("2. Mengurangi armada")
    print("3. Update harga sewa")
    ma = int(input("Masukkan menu yang anda pilih : "))
    return ma


def T_armada():
    print("========================")
    print("==== Kurangi Armada ====")
    print("========================")
    data_kendaraan()
    jml = int(input("Masukkan jumlah armada yang akan dikurangi : "))
    # menambahkan data mobil ke database csv


def K_armada():
    print("=======================")
    print("==== Kurangi Armada ====")
    print("=======================")
    n = int(input("Masukkan nomor mobil yang akan dijual : "))
    # menghapus data mobil berdasarkan pencarian plat nomor


def U_harga():
    print("======================")
    print("==== Update Harga ====")
    print("======================")


def pengembalian():
    print("===========================")
    print("==== Menu Pengembalian ====")
    print("===========================")
    # mencari mobil berdasarkan plat lalu diganti statusnya menjadi tersedia


def lupa_pw():
    print("============================")
    print("==== Menu Lupa Password ====")
    print("============================")
    uname = str(input("Masukkan username anda : "))
    id = str(input("Masukkan no. id anda (KTP/SIM) : "))
    # cari unamenya, if id == no_id then fix pilih data dan ganti


def succ_pw():
    print("====================================")
    print("==== Password berhasil diganti! ====")
    print("====================================")
    print("\n\nTekan Enter!")


def fail_pw():
    print("===================================")
    print("==== Gagal mengganti password! ====")
    print("===================================")
    print("\n\nTekan Enter!")