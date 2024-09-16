nama = input("Masukkan nama lengkap: ")  
panggilan = input("Masukkan nama panggilan: ")  
nim = int(input("Masukkan NIM: "))  
prodi = input("Masukkan program studi: ")  
umur = int(input("Masukkan umur: "))
asal_sekolah = (input("masukkan asal sekolah:"))
alasan_masuk_informatika = (input("alasan masuk informatika:"))
tinggi = float(input("Masukkan tinggi badan: "))
berat = float(input("masukkan berat badan:"))

print(f"\nNama lengkap saya {nama}, biasa dipanggil {panggilan}.")
print(f"Saya berusia {umur} tahun dan saya adalah mahasiswa dari prodi {prodi}.")
print(f"dengan NIM {nim} asal sekolah saya dari{asal_sekolah}.")
print(f"alasan saya masuk informatika adalah {alasan_masuk_informatika}.")
print(f"tinggi badan saya {tinggi} cm, dan berat badan saya adalah {berat} kilo.")

angka_terakhir_nim = nim % 1000  
modulus = angka_terakhir_nim % 6
print(f"Tiga angka terakhir dari NIM saya adalah {angka_terakhir_nim} dan jika dimoduluskan dengan 6, hasilnya adalah {modulus}.")
