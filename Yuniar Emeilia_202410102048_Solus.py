import os
lagi = "y"

while lagi == "y" :
    print("Selamat Datang\nCari Asal Program Studi Mahasiswa\nFasilkom Angkatan 2020\nMenggunkan NIM\n")
    nim = int(input("Masukkan NIM Lengkap : "))
    os.system("cls")

    angkatan_lain = nim//100000000000
    empat_terakhir = nim%10000
    nim_prodi = empat_terakhir//1000

    if angkatan_lain == 2 :
        if nim_prodi == 1 :
            print("Mahasiswa Dengan NIM {}\nAdalah Mahasiswa Prodi Sistem Informasi".format(nim))
        elif nim_prodi == 2 :
            print("Mahasiswa Dengan NIM {}\nAdalah Mahasiswa Prodi Teknologi Informasi".format(nim))
        elif nim_prodi == 3 :
            print("Mahasiswa Dengan NIM {}\nAdalah Mahasiswa Prodi Informatika".format(nim))
        else :
            print("Mahasiswa Dengan NIM {}\nBukan Mahasiswa Fasilkom".format(nim))
    else :
        print("Mahasiswa Dengan NIM {}\nBukan Mahasiswa Angkatan 2020".format(nim))
    if lagi == "t" :
        break

    lagi = input("\nApakah Masih Ada Lagi? [y/t] ")
    os.system("cls")