#CATATAN PERTEMUAN 3

#cuaca = str(input("masukkan cuaca hari ini: "))
#if cuaca == "cerah":
#   print("pergi kekampus")
#elif cuaca == "hujan":
#    print("belajar dirumah")
#else:
#    print("invalid")

#Selain pakai if, bisa juga bisa pakai match
# x = 4
#match x:
#     case 0:
#         print("false")
#     case 4:
#         print("true")

# studi kasus pertama 
#a = int(input("masukkan angka 1: "))
#b = int(input("masukkan  angka 2: "))
#if a > b :
#   print("singa")
#elif a < b :
#    print("sapi")
#elif a == b :
#    print("kura-kura")
#else :
#    print("invalid")

#study kasus ke 2 kondisi dalam kondisi 
angka = int(input("masukkan angka: "))
if angka > 30 :
    print("sapi")
    if angka > 50 :
        print("singa")
else:
    print("invalid")
