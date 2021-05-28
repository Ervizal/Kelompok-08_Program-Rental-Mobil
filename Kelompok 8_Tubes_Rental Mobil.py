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