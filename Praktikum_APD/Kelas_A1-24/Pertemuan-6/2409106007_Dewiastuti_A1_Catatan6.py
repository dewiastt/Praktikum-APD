#Contoh 1:
# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku = {}
# daftar_buku["Buku1"] = "Harry Potter"
# daftar_buku["Buku2"] = "Percy Jackson"
# daftar_buku["Buku3"] = "Twillight"
# print(daftar_buku)

# musik = {
# "judul" : "All we Know",
# "judul1" : "Something Just Like This"
# }
# print(musik["judul"])

# nama_dict = {
#     "key": "value"
# }

# Biodata = {
#         "Nama" : "Aldy Ramadhan Syahputra",
#         "NIM" : 2109106079,
#         "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#         "Mahasiswa_Aktif" :True,
#         "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }
# pinjam = Biodata.copy()
# print(pinjam)
# # print(Biodata["Alamat"])
# print(Biodata.get("alamat", "kosong bang"))


# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = "FPS")

# print(games)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# for i, j in Nilai.items():
#     print(f"key = {i} dan Value = {j}")

#Sebelum Ditambah
# print(Film)
# Film.update({"Hour" : "Triller"}) #Fungsi update
# print(Film)

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# for i in Film.values():
#     print(i, end=" ")
# #Sebelum Diubah
# print(Film)
# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# #Setelah diubah
# print(Film)

# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# # del data["Nama"]
# #Setelah diubah
# # print(data)
# #memanggil data yang telah dihapus
# # hapus = data.pop(data)
# # # print(data.get("Nama"))
# # print(data)
# data.clear()
# print(data)

# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print("Jumlah Data = ", len(data))

# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)

# key = "apel", "jeruk", "Mangga"
# value = 2
# buah = dict.fromkeys(key, value)
# print(buah)

# Musik = {
#         "The Chainsmoker" : ["All we Know", "TheParis"],
#         "Alan Walker" : ["Alone", "Lily"],
#         "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# print(F"Sebelum : {mahasiswa}")
# # mahasiswa[101]["Angkatan"] = 2023
# del mahasiswa[111]["Nama"]
# print(F"sesudah : {mahasiswa}")
# print(F"Sesudah : {mahasiswa}")
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

# Biodata = {
#     "Nama" :"Dewi",
#     "Umur" : "20",
#     "NIM"  : "2409106007",
#     "jurusan" : "informatika"
# }
# print(Biodata.get("NIM"))
# Biodata.update({"Umur" : "19"})
# print(Biodata)

Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")