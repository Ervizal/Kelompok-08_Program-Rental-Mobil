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

def login_admin():
    os.system("cls")
    log = True
    print("=====================")
    print("==== Login Admin ====")
    print("=====================")
    file_pass_Admin = open("File Password Admin.txt", "r")
    data_str = file_pass_Admin.readlines()
    data = data_str[0]
    datanw = json.loads(data)
    file_pass_Admin.close()
    user_Admin = str(datanw["username"])
    pass_Admin = str(datanw["password"])
    perc = 0
    ladmin = True
    while ladmin == True:
        try:
            username = str(input("Username : "))
            password = str(input("Password : "))
        except:
            loading()
            login_gagal()
            print("==== Maaf Username atau Password Anda Salah! ====")
            perc += 1
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
            if (perc == 3):
                print("Terlalu banyak percobaan!")
                ladmin = False
                input("Tekan enter untuk kembali ke menu utama!")
    return log, True


def ganti_pwadmin():
    print("==============================")
    print("==== Ganti Password Admin ====")
    print("==============================")
    file_pass_Admin = open("File Password Admin.txt", "w")
    user_baru = str(input("Masukkan username baru : "))
    pass_baru = str(input("Masukkan password baru : "))
    data_pw = '{"username" : "%s", "password" : "%s"}\n\n==== Username dan Password Admin ====\nUsername : %s\nPassword : %s' % (
    user_baru, pass_baru, user_baru, pass_baru)
    file_pass_Admin.writelines(data_pw)
    file_pass_Admin.close()
    succ_pw()


def menu_admin():
    print("====================")
    print("==== Menu Admin ====")
    print("====================")
    print("1. Menambah armada")
    print("2. Mengurangi armada")
    print("3. Update data kendaraan")
    print("4. Ganti password admin")
    print("5. Log out")
    while True:
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
    return ma


def T_armada():
    print("========================")
    print("==== Tambah Armada ====")
    print("========================")
    # data_kendaraan()
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", sheet_name="Sheet1", header=0)
    df = pd.DataFrame(data)
    print(df.to_string(index=False))

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
    df.loc[(jlh_mbl + 1)] = mobil_baru
    df = df.sort_values(by="Jenis")
    df["No"] = [x for x in range(1, len(df) + 1)]
    df = df.reset_index(drop=True)
    export3 = pd.ExcelWriter("data_kendaraan.xlsx")
    df.to_excel(export3, index=False)
    export3.save()
    print("Data mobil terbaru:\n", df.to_string(index=False))


def K_armada():
    print("=======================")
    print("==== Kurangi Armada ====")
    print("=======================")
    # data_kendaraan()
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", header=0)
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    while True:
        try:
            jml = int(input("Pilih nomor kendaraan yang akan dikurangi: "))
        except:
            print("Mohon masukkan angka saja")
        else:
            break
    pd.options.mode.chained_assignment = None

    df = df.drop(jml - 1)
    df["No"] = [x for x in range(1, len(df) + 1)]

    df = df.reset_index(drop=True)
    export4 = pd.ExcelWriter("data_kendaraan.xlsx")
    df.to_excel(export4, index=False)
    export4.save()
    print("Data mobil terbaru:\n", df.to_string(index=False))


def U_data():
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
        try:
            upd = int(input("Masukkan menu yang Anda ingin ubah (1/2/3/4/5/6) : "))
        except:
            print("Input anda salah!")
        else:
            if (upd == 1):
                jns_baru = str(input("Masukkan jenis mobil terbaru:"))
                df["Jenis"][update] = jns_baru
                ud = False
            elif (upd == 2):
                hrg_baru = str(input("Masukkan harga mobil terbaru:"))
                df["Harga"][update] = hrg_baru
                ud = False
            elif (upd == 3):
                thn_baru = str(input("Masukkan tahun mobil terbaru:"))
                df["Tahun"][update] = thn_baru
                ud = False
            elif (upd == 4):
                kps_baru = str(input("Masukkan kapasitas mobil terbaru:"))
                df["Kapasitas"][update] = kps_baru
                ud = False
            elif (upd == 5):
                nopol_baru = str(input("Masukkan no polisi mobil terbaru:"))
                df["No Polisi"][update] = nopol_baru
                ud = False
            elif (upd == 6):
                stat_baru = str(input("Masukkan status mobil terbaru:"))
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
    print("============================")
    print("==== Menu Lupa Password ====")
    print("============================")
    pd.options.mode.chained_assignment = None  # default='warn', supaya tdk ada warning saat mengganti value
    file = "data_pelanggan.xlsx"
    data_pelanggan = pd.read_excel(file, index_col="No").loc[:, "Nama":]
    df = pd.DataFrame(data_pelanggan)
    # mengecek data
    while True:
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
    os.system("cls")
    print("====================================")
    print("==== Password berhasil diganti! ====")
    print("====================================")


def fail_pw():
    os.system("cls")
    print("=============================================")
    print("====      Gagal mengganti password!      ====")
    print("==== Username atau ID Anda Mungkin Salah ====")
    print("=============================================")


def tunai(total):
    print("\n=== Metode bayar non tunai ===")
    print("Tagihan anda sebesar Rp %d" % total)
    print("Bayar dengan uang pas!")
    via = " "
    idrek = " "
    no = " "
    lptun = True
    while lptun == True:
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
    print("=== Pembayaran ===")
    print("1. Tunai")
    print("2. Non tunai")
    pj = True
    while pj == True:
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
    time.sleep(4)
    done = True


def processing_bayar():
    done = False

    def animate():
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
                    # jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari, cek = menu_sewa(akun, nama)
                    # print("871", jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari, cek)
                    while True:
                        # print("873", jenis_pembayaran, tgl_awal, tgl_akhir, plat, kendaraan, bill, lama_hari, cek)
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

