menu = {
    1: {"nama": "Ayam Goreng Tepung", "harga": 35000},
    2: {"nama": "Ayam Rica-rica", "harga": 35000},
    3: {"nama": "Ayam Kuluyuk", "harga": 35000},
    4: {"nama": "Nasi Goreng Biasa", "harga": 26000},
    5: {"nama": "Nasi Goreng Spesial", "harga": 25000},
    6: {"nama": "Bistik Sapi", "harga": 35000},
    7: {"nama": "Bistik Ayam", "harga": 35000},
    8: {"nama": "Air Es", "harga": 1000},
    9: {"nama": "Es Teh", "harga": 5000},
    10: {"nama": "Es Jeruk", "harga": 8000},
    11: {"nama": "Teh Hangat", "harga": 4000},
    12: {"nama": "Jeruk Hangat", "harga": 5000}
}

pesanan = {}  
riwayat_pesanan = []  

akun = {
    "admin": {"username": "admin", "password": "admin123"},
    "user": {}
}

print("======SELAMAT DATANG======")
print("SILAHKAN MEMESAN MENU MAKANAN ANDA HARI INI")
print("Lakukan Registrasi terlebih dahulu ")

while True:
    print("""
    ===========================
    |   Restoran Cari Jodoh    |
    ===========================
    |    1. Login              |           
    |    2. Registrasi         |          
    |    3. Keluar             |      
    ===========================
    """)

    opsi = input("Pilih opsi (1-3): ")
    if opsi == "1":
        print("=== Login ===")
        username = input("Username: ")
        password = input("Password: ")

        if username == akun["admin"]["username"] and password == akun["admin"]["password"]:
            print("Login sebagai Admin berhasil!")
            pengguna = "admin"
        elif username in akun["user"] and akun["user"][username]["password"] == password:
            print("Login sebagai User berhasil!")
            pengguna = "user"
        else:
            print("Username atau password yang anda masukkan salah.")
            continue

        while True:
            if pengguna == "user":
                print("""
                =================================      
                |      Pilihan                   |   
                =================================
                |   1. Lihat Menu                |
                |   2. Tambah Pesanan            |
                |   3. Hapus Pesanan             |
                |   4. Tampilkan Total Harga     |
                |   5. Konfirmasi Pesanan        |
                |   6. Pesan                     |   
                |   7. Keluar                    |
                =================================
                """)
                pilihan = input("Pilih opsi (1-7): ")

                if pilihan == "1":
                    print("\nMenu Makanan:")
                    for key, item in menu.items():
                        print(f"{key}. {item['nama']} - Rp{item['harga']}")

                elif pilihan == "2":
                    try:
                        no_menu = int(input("Masukkan nomor menu yang ingin ditambahkan: "))
                        if no_menu in menu:
                            nama_menu = menu[no_menu]["nama"]
                            if nama_menu in pesanan:
                                pesanan[nama_menu] += 1
                            else:
                                pesanan[nama_menu] = 1
                            print(f"{nama_menu} telah ditambahkan ke pesanan.")
                        else:
                            print("Nomor menu tidak valid.")
                    except ValueError:
                        print("Masukkan angka yang valid.")

                elif pilihan == "3":
                    try:
                        nama_menu = input("Masukkan nama menu yang ingin dihapus dari pesanan: ")
                        if nama_menu in pesanan:
                            pesanan.pop(nama_menu)
                            print(f"{nama_menu} telah dihapus dari pesanan.")
                        else:
                            print("Menu tidak ada dalam daftar pesanan.")
                    except ValueError:
                        print("Masukkan nama yang valid.")

                elif pilihan == "4":
                    total = sum(menu[next(key for key, val in menu.items() if val["nama"] == nama_menu)]["harga"] * jumlah for nama_menu, jumlah in pesanan.items())
                    print(f"Total harga yang harus dibayar: Rp{total}")

                elif pilihan == "5":
                    if pesanan:
                        print("Pesanan yang telah ditambahkan:")
                        for nama_menu, jumlah in pesanan.items():
                            harga = menu[next(key for key, val in menu.items() if val["nama"] == nama_menu)]["harga"]
                            print(f"- {nama_menu} (x{jumlah}) - Rp{harga * jumlah}")
                    else:
                        print("Anda belum menambahkan pesanan.")

                elif pilihan == "6":
                    if pesanan:
                        print("Pesanan Anda:")
                        for nama_menu, jumlah in pesanan.items():
                            harga = menu[next(key for key, val in menu.items() if val["nama"] == nama_menu)]["harga"]
                            print(f"- {nama_menu} (x{jumlah}) - Rp{harga * jumlah}")
                        total = sum(menu[next(key for key, val in menu.items() if val["nama"] == nama_menu)]["harga"] * jumlah for nama_menu, jumlah in pesanan.items())
                        print(f"Total yang harus dibayar: Rp{total}")
                        print("Pesanan yang Anda pilih telah berhasil dipesan.")
                        nomor_pesanan = len(riwayat_pesanan) + 1  
                        pesanan.clear()  
                    else:
                        print("Anda belum memesan apa-apa.")

                elif pilihan == "7":
                    print("Terima kasih telah menggunakan layanan ini, selamat berjumpa kembali.")
                    break
                else:
                    print("Opsi tidak valid.")

            elif pengguna == "admin":
                print("""
                =================================      
                |      Pilihan                   |   
                =================================
                |   1. Lihat Menu                |
                |   2. Tambah Menu               |
                |   3. Hapus Menu                |
                |   4. Update Menu               |
                |   5. Keluar                    |
                =================================
                """)
                pilihan = input("Pilih opsi (1-5): ")

                if pilihan == "1":
                    print("\nMenu Makanan:")
                    for key, item in menu.items():
                        print(f"{key}. {item['nama']} - Rp{item['harga']}")

                elif pilihan == "2":
                    nama_menu = input("Masukkan nama menu : ")
                    if not nama_menu: 
                        print("Silakan isi kembali nama menu yang ingin ditambahkan.")
                        continue  
                    try:
                        harga_menu = int(input("Masukkan harga menu: "))
                    except ValueError:  
                        print("Silakan isi kembali.")
                        continue 

                    no_menu = max(menu.keys()) + 1
                    menu[no_menu] = {"nama": nama_menu, "harga": harga_menu}
                    print(f"{nama_menu} telah ditambahkan ke menu.")
                    break 
                    
                elif pilihan == "3":
                    try:
                        no_menu = int(input("Masukkan nomor menu yang ingin dihapus: "))
                        if no_menu in menu:
                            print(f"{menu[no_menu]['nama']} telah dihapus dari menu.")
                            del menu[no_menu]
                        else:
                            print("Nomor menu tidak valid.")
                    except ValueError:
                        print("Masukkan angka yang valid.")

                elif pilihan == "4":
                    try:
                        no_menu = int(input("Masukkan nomor menu yang ingin diupdate: "))
                        if no_menu in menu:
                            nama_menu = input("Masukkan nama menu baru: ")
                            harga_menu = int(input("Masukkan harga baru: "))
                            menu[no_menu] = {"nama": nama_menu, "harga": harga_menu}
                            print(f"Menu telah diperbarui menjadi {nama_menu} - Rp{harga_menu}.")
                        else:
                            print("Nomor menu tidak valid.")
                    except ValueError:
                        print("Masukkan angka yang valid.")

                elif pilihan == "5":
                    print("Keluar dari admin.")
                    break

                else:
                    print("Pilihan tidak valid.")

    elif opsi == "2":
        print("=== Registrasi ===")
        while True:
            username = input("Masukkan username baru: ")
            if username in akun["user"]:
                print("Username sudah terdaftar, silakan coba username lain.")
            else:
                password = input("Masukkan password baru: ")
                akun["user"][username] = {"password": password}
                print(f"Registrasi berhasil! Username '{username}' telah dibuat.")
                break

    elif opsi == "3":
        print("Terima kasih telah menggunakan program kami.")
        break
    else:
        print("Opsi tidak valid.")
