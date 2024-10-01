user1= {"dewi" : 7}
user2= {"tuti" : 19}

percobaan = 0
maks_percobaan = 3
for percobaan in range(maks_percobaan)
    username = input("masukkan username")
    password = input("masukkan password")

    if username in user1 and password 

jenis_kelamin = input("Pilihan (p/w): ")
berat = float(input("Masukkan berat badan Anda (kg): "))
tinggi = float(input("Masukkan tinggi badan Anda (cm) : "))
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

if tdee !=0:
    print(f"Kebutuhan Kalori Harian (TDEE) yang Anda butuhkan adalah sebesar {round(tdee)} kkal.")
else:
    print("Pilihan level aktivitas tidak valid!")
