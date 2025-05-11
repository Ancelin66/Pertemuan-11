# program untuk menghitung rata-rata dari input pengguna
# inisialisasi variabel
total = 0
count = 0

print("Masukkan bilangan satu per satu. Ketik 'done' untuk selesai.")

while True:
    user_input = input("Masukkan bilangan: ")

    if user_input.lower() == "done":
        break

    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Input tidak valid. Harap masukkan angka atau 'done'.")

# Hitung dan tampilkan rata-rata
if count > 0:
    rata_rata = total / count
    print(f"Rata-rata dari bilangan yang dimasukkan adalah: {rata_rata}")
else:
    print("Tidak ada bilangan yang dimasukkan.")
