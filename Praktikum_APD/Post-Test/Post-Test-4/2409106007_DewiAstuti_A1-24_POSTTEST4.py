print("KALKULATOR KALORI (TDEE)")
print("Sebelum lanjut buatlah username dan password terlebih dahulu")

user = input("buatlah username dengan nama panggilan anda : ")
pw  = input("buatlah password menggunakan tiga angka terkhir nim tanpa 0 : ")


print("anda telah berhasil membuat user silahkan login kembali")

maks_percobaan = 3
while True:
    percobaan = 0
    while percobaan < maks_percobaan:
        username = input("Masukkan username yang telah anda buat : ")
        password = input("Masukkan password : ")
        if username == user and pw == password:
            print("Login berhasil!")
            break  
        else:
            print("Username atau password salah.")
            percobaan += 1
            if percobaan == 3:
                print("Anda telah salah sebanyak 3 kali, mohon untuk login kembali ")
                exit
    else:
        exit()

    jenis_kelamin = input("Pilihan jenis kelamin (p/w): ")
    berat = float(input("Masukkan berat badan Anda : "))
    tinggi = float(input("Masukkan tinggi badan Anda : "))
    umur = int(input("Masukkan umur Anda: "))

    if jenis_kelamin == 'p':
        bmr = (10 * berat) + (6.25 * tinggi) - (5 * umur) + 5
    elif jenis_kelamin == 'w':
        bmr = (10 * berat) + (6.25 * tinggi) - (5 * umur) - 161
    else:
        print("Pilihan jenis kelamin tidak valid!")
    
    print("Silakan Pilih Level Aktivitas Harian Anda:")
    print("r = Rendah - jarang berolahraga")
    print("s = Sedang - olahraga 1-2 kali perminggu")
    print("b = Berat - olahraga 3-5 kali perminggu")

    aktivitas = input("Pilihan (r/s/b): ")

    if aktivitas == 'r':
        tdee = bmr * 1.25
    elif aktivitas == 's':
        tdee = bmr * 1.36
    elif aktivitas == 'b':
        tdee = bmr * 1.72
    else:
        tdee = 0

    if tdee != 0:
        print(f"Kebutuhan Kalori Harian (TDEE) yang Anda butuhkan adalah sebesar {round(tdee)} kkal.")
    else:
        print("Pilihan level aktivitas tidak valid!")

    ulang = input("Apakah Anda ingin menghitung ulang? (ya/tidak): ")
    if ulang != 'ya':
        print("Terima kasih, Telah menggunakan program ini.")
        break
