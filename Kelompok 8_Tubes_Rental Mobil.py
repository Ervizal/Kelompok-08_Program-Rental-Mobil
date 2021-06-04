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
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", index_col="No", sheet_name="Sheet1", header=0, )
    df = pd.DataFrame(data)
    print(df)

    up = int(input("Mobil yang akan di update harga[ex:1]:"))
    # print("Berikut data mobil yang Anda sewa:")
    print(df.iloc[up - 1])
    harga_baru = str(input("Masukkan harga mobil terbaru:"))
    # ubah harga mobil
    df["Harga"][up] = harga_baru
    export5=pd.ExcelWriter("data_kendaraan.xlsx")
    df.to_excel(export5)
    export5.save()
    print(df)

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

def tunai():
    print()
    bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
    bayar = int(input("Masukkan jumlah uang yang dibayarkan : "))
    change = bayar - bill
    print("Anda berhasil membayar tagihan sebesar Rp %d" % bill)
    if(change == 0):
        print("terima kasih telah membayar dengan uang pas!")
    elif(change > 0):
        print("Jangan lupa ambil kembalian anda sebesar Rp %d, terima kasih!" % change)
    else:
        print("Bayar dengan jumlah uang yang sesuai!")
        pembayaran()

def nontunai():
    print("\n=== Metode bayar non tunai ===")
    print("1. Kartu Kredit")
    print("2. Kartu Debit")
    print("3. Gopay")
    print("4. OVO")
    print("5. Shopee Pay")
    print("6. Dana")
    met = int(input("Pilih nomor metode bayar yang diinginkan [1/2/3/4/5/6] : "))
    if(met == 1):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        rek = str(input("Masukkan nomor rekening anda : "))
        idkartu = str(input("Masukkan nama pemilik kartu rekening : "))
        bank = str(input("Masukkan nama bank : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui kartu kredit bank %s nomor rekening %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (bank, rek, idkartu, bill))
    elif(met == 2):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        rek = str(input("Masukkan nomor rekening anda : "))
        idkartu = str(input("Masukkan nama pemilik kartu rekening : "))
        bank = str(input("Masukkan nama bank : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui kartu debit bank %s nomor rekening %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (bank, rek, idkartu, bill))
    elif(met == 3):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        no = str(input("Masukkan nomor Gopay anda : "))
        id = str(input("Masukkan nama pemilik akun Gopay : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui Gopay %d atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, id, bill))
    elif(met == 4):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        no = str(input("Masukkan nomor OVO anda : "))
        id = str(input("Masukkan nama pemilik akun OVO : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui OVO %d atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, id, bill))
    elif(met == 5):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        no = str(input("Masukkan nomor Shopee Pay anda : "))
        id = str(input("Masukkan nama pemilik akun Shopee Pay : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui Shopee Pay %d atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, id, bill))
    elif(met == 6):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        no = str(input("Masukkan nomor Dana anda : "))
        id = str(input("Masukkan nama pemilik akun Dana : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui Dana %d atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, id, bill))
    else:
        print("Input salah!")
        pembayaran()
        
def pembayaran():
    print("=== Pembayaran ===")
    print("1. Tunai")
    print("2. Non tunai")
    byr = int(input("Pilih metode pembayaran [1/2] : "))
    if(byr == 1):
        tunai()
    elif(byr == 2):
        nontunai()
    else:
        print("Masukkan input yang valid!")

def loading():    
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(5)
    done = True  
   


#Bagian Program Utama   
lagi = "Y"  
while (lagi == "Y"):  
    os.system("cls")
    judul()
    ut = 0
    ut = menu_utama()
    if(ut == 1):
        stat_akun = login_cust()
        if(stat_akun.upper() == "Y"):
            custY()
        elif(stat_akun.upper() == "T"):
            custT()
        else:
            print("Input anda salah!")
    elif(ut == 2):
        log, st = login_admin()
        if(log == True):
            login_berhasil()
            ma = menu_admin()
            if(ma == 1):
                T_armada() 
            elif(ma == 2):
                K_armada()
            elif(ma == 3):
                U_harga()
            else:
                print("Input anda salah!")
                menu_admin()
        else:
            raise Exception("==== Maaf Username atau Password Anda Salah! ====")
    elif(ut == 3):
        print("Terima kasih telah menggunakan program kami, sampai jumpa kembali!")
        print("Program ditutup...")
        sys.exit()
    else:
        print("Input anda salah!")
    print("Sampai jumpa kembali!\n")