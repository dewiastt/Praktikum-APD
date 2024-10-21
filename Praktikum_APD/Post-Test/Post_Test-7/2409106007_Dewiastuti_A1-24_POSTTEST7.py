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
akun = {"admin": {"username": "admin", "password": "admin123"}, "user": {}}  

def lihat_menu():
    print("\nMenu Makanan:")
    for key, item in menu.items():
        print(f"{key}. {item['nama']} - Rp{item['harga']}")

def lihat_total():
    total = sum(menu[next(key for key, val in menu.items() if val["nama"] == nama_menu)]["harga"] * jumlah
                for nama_menu, jumlah in pesanan.items())
    print(f"Total tagihan yang harus dibayar: Rp{total}")

def hapus_menu(nama_menu, jumlah):
    lihat_menu() 
    if nama_menu in pesanan:
        if pesanan[nama_menu] >= jumlah:
            pesanan[nama_menu] -= jumlah
            if pesanan[nama_menu] == 0:
                pesanan.pop(nama_menu)
            print(f"{jumlah} porsi {nama_menu} telah dihapus dari pesanan.")
        else:
            print(f"Tidak cukup porsi untuk menghapus {jumlah} porsi {nama_menu}.")
    else:
        print("Menu tidak ada dalam daftar pesanan.")

def login(username, password):
    if username == akun["admin"]["username"] and password == akun["admin"]["password"]:
        print("Login sebagai Admin berhasil!")
        return "admin"
    elif username in akun["user"] and akun["user"][username]["password"] == password:
        print("Login sebagai User berhasil!")
        return "user"
    else:
        print("Username atau password yang Anda masukkan salah.")
        return None

def registrasi():
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

def konfirmasi_pesanan():
    if pesanan:
        print("Pesanan yang telah ditambahkan:")
        for nama_menu, jumlah in pesanan.items():
            harga = menu[next(key for key, val in menu.items() if val["nama"] == nama_menu)]["harga"]
            print(f"- {nama_menu} (x{jumlah}) - Rp{harga * jumlah}")
    else:
        print("Anda belum menambahkan pesanan.")

def update_menu():
    lihat_menu()  
    no_menu = input_angka("Masukkan nomor menu yang ingin diupdate: ")

    if no_menu in menu:
        print(f"Anda akan mengubah menu: {menu[no_menu]['nama']} - Rp{menu[no_menu]['harga']}")
        opsi_update = input("Apa yang ingin anda update? 1.Nama, 2.Harga, 3.semua: ")
        if opsi_update == "1":
            nama_baru = input("Masukkan nama baru: ")
            menu[no_menu]["nama"] = nama_baru
            print(f"Nama menu nomor {no_menu} telah diubah menjadi {nama_baru}.")
        
        elif opsi_update == "2":
            harga_baru = input_angka("Masukkan harga baru: ")
            menu[no_menu]["harga"] = harga_baru
            print(f"Harga menu nomor {no_menu} telah diubah menjadi Rp{harga_baru}.")

        elif opsi_update == "3":
            nama_baru = input("Masukkan nama baru: ")
            harga_baru = input_angka("Masukkan harga baru: ")
            menu[no_menu]["nama"] = nama_baru
            menu[no_menu]["harga"] = harga_baru
            print(f"Menu nomor {no_menu} telah diubah menjadi {nama_baru} - Rp{harga_baru}.")

        else:
            print("Opsi update tidak valid.")
    else:
        print("Nomor menu tidak valid.")

def tambah_menu(no_menu):
    if no_menu in menu:
        nama_menu = menu[no_menu]["nama"]
        jumlah = input_angka(f"Berapa jumlah makanan/minuman {nama_menu} yang ingin dipesan? ")
        if nama_menu in pesanan:
            pesanan[nama_menu] += jumlah
        else:
            pesanan[nama_menu] = jumlah
        print(f"{jumlah} porsi {nama_menu} telah ditambahkan ke pesanan.")
    else:
        print("Nomor menu tidak valid.")

def pesan():
    if pesanan:
        print("Pesanan Anda:")
        for nama_menu, jumlah in pesanan.items():
            harga = menu[next(key for key, val in menu.items() if val["nama"] == nama_menu)]["harga"]
            print(f"- {nama_menu} (x{jumlah}) - Rp{harga * jumlah}")
    else:
        print("Anda belum memesan apa-apa.")

def input_angka(angkavalid):
    try:
        return int(input(angkavalid))
    except ValueError:
        print("Masukkan angka yang valid.")
        return input_angka(angkavalid)  
def restoran():
    print("======SELAMAT DATANG======")
    print("SILAHKAN MEMESAN MENU MAKANAN ANDA HARI INI")
    print("Lakukan Registrasi terlebih dahulu")

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

            pengguna = login(username, password)
            if pengguna is None:
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
                    |   4. Konfirmasi Pesanan        |
                    |   5. pesan                     |
                    |   6. Keluar                    |
                    =================================
                    """)
                    pilihan = input("Pilih opsi (1-6): ")

                    if pilihan == "1":
                        lihat_menu()

                    elif pilihan == "2":
                        while True:  
                            lihat_menu()
                            no_menu = input_angka("Masukkan nomor menu yang ingin ditambahkan: ")
                            tambah_menu(no_menu)
                            while True:
                                tambah_lagi = input("Apakah Anda ingin menambah pesanan lain? (ya/tdk): ").lower()
                                if tambah_lagi in ['ya', 'tdk']:
                                    break
                                else:
                                    print("Input salah, silakan masukkan 'ya' untuk melanjutkan atau 'tdk' untuk keluar.")
                            
                            if tambah_lagi == 'tdk':
                                break 

                    elif pilihan == "3":
                        konfirmasi_pesanan()
                        nama_menu = input("Masukkan nama menu yang ingin dihapus dari pesanan: ")
                        jumlah_hapus = input_angka("Masukkan jumlah makanan yang ingin dihapus: ")
                        hapus_menu(nama_menu, jumlah_hapus)
                        konfirmasi_pesanan()
                    elif pilihan == "4":
                        konfirmasi_pesanan()
                        lihat_total()
                    elif pilihan == "5":
                        pesan()
                        lihat_total()
                        print("menu yang Anda pilih telah berhasil dipesan, silahkan menunggu beberapa menit makanan akan diantarkan")
                    elif pilihan == "6":
                        print("Keluar dari user.")
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
                        lihat_menu()

                    elif pilihan == "2":
                        nama_menu = input("Masukkan nama menu: ")
                        harga_menu = input_angka("Masukkan harga menu: ")
                        no_menu = max(menu.keys()) + 1
                        menu[no_menu] = {"nama": nama_menu, "harga": harga_menu}
                        print(f"{nama_menu} telah ditambahkan ke menu.")
                        lihat_menu()

                    elif pilihan == "3":
                        lihat_menu()
                        no_menu = input_angka("Masukkan nomor menu yang ingin dihapus: ")
                        if no_menu in menu:
                            print(f"{menu[no_menu]['nama']} telah dihapus dari menu.")
                            del menu[no_menu]
                            lihat_menu()
                        else:
                            print("Nomor menu tidak valid.")

                    elif pilihan == "4": 
                        lihat_menu() 
                        update_menu()
                        lihat_menu()

                    elif pilihan == "5":
                        print("Keluar dari admin.")
                        break

                    else:
                        print("Pilihan tidak valid.")

        elif opsi == "2":
            registrasi()

        elif opsi == "3":
            print("Terima kasih telah menggunakan program kami.")
            break

        else:
            print("Opsi tidak valid.")
restoran()
