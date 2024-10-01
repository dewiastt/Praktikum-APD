#perulangan merupakan sebuah cara untuk mengulangi sebuah kode yang sama beberapa kali,perulangan ada 2 yaitu for and while 
#pebedaan keduanya yaitu for digunakan untuk perulangan yang sudah jelas berapa kali diakan mengulang sedangkan while digunakan apabila jumlah perulangannya belum diketahui secara jelas.
#Indeks adalah posisi numerik dari sebuah elemen dalam struktur data berurutan, seperti list, tuple, atau string. Indeks dimulai dari 0, sehingga elemen pertama dalam struktur data memiliki indeks 0, elemen kedua memiliki indeks 1, dan seterusnya.

#contoh penggunaan for
#siswa = 20
#dewi = 2
#for i in range(siswa):
#    print("siswa berjumlah mulai dari "+ str(i))
#for i in range(dewi):
#    print("nama siswa ini disebut terus hinggah ke "+ str(i))

#ulang = 10
#for i in range(ulang)
#print("perulangan ke-" + str(i)) 

#sigma = [12,"udin petot", 14.5, True,'A']
#for i in sigma:
#    print(i)

#contoh penggunaan for didalm for
#for i in range(1, 10, 2):  #(awal, akhir, lompatan)
#    print(i)

#for i in range(1, 4):
#   for j in range (1, 4):
#       print(f"{i} x {j} = {i * j}")
#   print ()

#a = 10
#b = 7
#print(f"nilai a : (a) dan nilai b : (b)")
#print("nilai a: (a)")

#contoh perulangan while
#jawab = 'ya'
#hitung = 0 
#while(jawab == 'ya'):
#    hitung +=1
#    jawab = input("ulang lagi atau tidak? ")
#print(f"total perulangan yang dilakukan:{hitung}")

#print("daftar bilangan ganjil dari 1-10")
#for i in range(10):
#    if i % 4 == 0:
#        continue
#    print(i)


#studi kasus
#range_bilangan = int(input("Masukkan batas atas range bilangan: "))
#jumlah_prima = 0
#for angka in range(4, range_bilangan + 1): 
#    pembagi = 4
#    prima = True  
#    while pembagi * pembagi <= angka: 
#        if angka % pembagi == 0:  
#            prima = False
#            break
#        pembagi += 1  
#    if prima:  
#        jumlah_prima += 1
#print(f"Jumlah bilangan prima dari 1 hingga {range_bilangan} adalah: {jumlah_prima}")

#hitung = 0
#while True:
#    hitung +=1
#    ulang = input("masih ingin mengulang? ")
#    if ulang == "tidak" or ulang =="tidak":
#        break
#print(f"Total perulangan:{hitung}")

#contoh study kasus no 2

#bilangan = 0 
#while True:
#    angka = int(input("masukan angka: "))
#    if angka < 0:
#        break
#    bilangan += angka
#print ("total bilangan: " + str(bilangan))

#for i in range(1, 20, 3):
#    if i % 2 == 0:
  #    continue
    # print(i)




