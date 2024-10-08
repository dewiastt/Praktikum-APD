menu = [
    ["Ayam Goreng Tepung", 35000],
    ["Ayam Rica-rica", 35000],
    ["Ayam Kuluyuk", 35000],
    ["Nasi Goreng Biasa", 26000],
    ["Nasi Goreng Spesial", 25000],
    ["Bistik Sapi", 35000],
    ["Bistik Ayam", 35000],
    ["Air Es", 1000],
    ["Es Teh", 5000],
    ["Es Jeruk", 8000],
    ["Teh Hangat", 4000],
    ["Jeruk Hangat", 5000]
]

pesanan = []  
riwayat_pesanan = []  

akun = {
    "admin": {"username": "admin", "password": "admin123"},
    "user": []
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
        elif any(user['username'] == username and user['password'] == password for user in akun["user"]):
            print("Login sebagai User berhasil!")
            pengguna = "user"
        else:
            print("Username atau password salah.")
            continue 

        while True:
            if pengguna == "user":
                print("\nPilihan:")
                print("1. Lihat Menu")
                print("2. Tambah Pesanan")
                print("3. Hapus Pesanan")
                print("4. Tampilkan Total Harga")
                print("5. Pesan")
                print("6. Keluar")

                pilihan = input("Pilih opsi (1-6): ")

                if pilihan == "1":
                    print("\nMenu Makanan:")
                    for i, item in enumerate(menu):
                        print(f"{i + 1}. {item[0]} - Rp{item[1]}")

                elif pilihan == "2":
                    try:
                        no_menu = int(input("Masukkan nomor menu yang ingin ditambahkan: ")) - 1
                        if 0 <= no_menu < len(menu):
                            pesanan.append(menu[no_menu])
                            print(f"{menu[no_menu][0]} telah ditambahkan ke pesanan.")
                        else:
                            print("Nomor menu tidak valid.")
                    except ValueError:
                        print("Masukkan angka yang valid.")

                elif pilihan == "3":
                    try:
                        no_menu = int(input("Masukkan nomor menu yang ingin dihapus dari pesanan: ")) - 1
                        if 0 <= no_menu < len(menu):
                            found = False
                            for item in pesanan:
                                if item == menu[no_menu]:
                                    pesanan.remove(item)
                                    print(f"{menu[no_menu][0]} telah dihapus dari pesanan.")
                                    found = True
                                    break
                            if not found:
                                print("Menu tersebut tidak ada dalam daftar pesanan.")
                        else:
                            print("Nomor menu tidak valid.")
                    except ValueError:
                        print("Masukkan angka yang valid.")

                elif pilihan == "4":
                    total = sum(item[1] for item in pesanan)
                    print(f"Total harga yang harus dibayar: Rp{total}")

                elif pilihan == "5":
                    if pesanan:
                        print("Pesanan Anda:")
                        for item in pesanan:
                            print(f"- {item[0]} - Rp{item[1]}")
                        total = sum(item[1] for item in pesanan)
                        print(f"Total yang harus dibayar: Rp{total}")
                        print("\nPesanan yang Anda pilih telah berhasil dipesan.")
                        riwayat_pesanan.append(pesanan.copy())  
                        pesanan.clear()  
                    else:
                        print("Anda belum memesan apa-apa.")

                elif pilihan == "6":
                    print("Terima kasih telah menggunakan layanan kami.")
                    break
                else:
                    print("Opsi tidak valid.")

            elif pengguna == "admin":
                print("\nPilihan Admin:")
                print("1. Lihat Menu")
                print("2. Tambah Menu")
                print("3. Hapus Menu")
                print("4. Update Menu")
                print("5. Keluar")

                pilihan = input("Pilih opsi (1-6): ")

                if pilihan == "1":
                    print("\nMenu Makanan:")
                    for i, item in enumerate(menu):
                        print(f"{i + 1}. {item[0]} - Rp{item[1]}")

                elif pilihan == "2":
                    nama_menu = input("Masukkan nama menu: ")
                    harga_menu = int(input("Masukkan harga menu: "))
                    menu.append([nama_menu, harga_menu])
                    print(f"{nama_menu} telah ditambahkan ke menu.")

                elif pilihan == "3":
                    try:
                        no_menu = int(input("Masukkan nomor menu yang ingin dihapus: ")) - 1
                        if 0 <= no_menu < len(menu):
                            print(f"{menu[no_menu][0]} telah dihapus dari menu.")
                            del menu[no_menu]
                        else:
                            print("Nomor menu tidak valid.")
                    except ValueError:
                        print("Masukkan angka yang valid.")

                elif pilihan == "4":
                    try:
                        no_menu = int(input("Masukkan nomor menu yang ingin diupdate: ")) - 1
                        if 0 <= no_menu < len(menu):
                            nama_menu = input("Masukkan nama menu baru: ")
                            harga_menu = int(input("Masukkan harga baru: "))
                            menu[no_menu] = [nama_menu, harga_menu]
                            print(f"Menu telah diperbarui menjadi {nama_menu} - Rp{harga_menu}.")
                        else:
                            print("Nomor menu tidak valid.")
                    except ValueError:
                        print("Masukkan angka yang valid.")

                elif pilihan == "5":
                    print("Keluar dari admin.")
                    break

                else:
                    print("pilihan tidak valid.")

    elif opsi == "2":
        print("=== Registrasi ===")
        while True:
            username = input("Masukkan username baru: ")
            if any(user['username'] == username for user in akun["user"]):
                print("Username sudah terdaftar, silakan coba username lain.")
            else:
                password = input("Masukkan password baru: ")
                akun["user"].append({"username": username, "password": password})
                print(f"Registrasi berhasil! Username '{username}' telah dibuat.")
                break

    elif opsi == "3":
        print("Terima kasih telah menggunakan program kami.")
        break
    else:
        print("opsi tidak valid")

