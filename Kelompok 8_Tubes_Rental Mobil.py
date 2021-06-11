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
