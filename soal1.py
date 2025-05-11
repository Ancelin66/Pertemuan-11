def tiga_terbaik(data):
    if len(data) < 3:
        raise ValueError("List harus memiliki minimal 3 elemen")

    # Inisialisasi tiga bilangan terbesar dengan nilai terkecil
    top1 = top2 = top3 = float('-inf')

    for num in data:
        if num > top1:
            # Geser semuanya ke bawah
            top1, top2, top3 = num, top1, top2
        elif num > top2:
            top2, top3 = num, top2
        elif num > top3:
            top3 = num

    return [top1, top2, top3]

# Contoh penggunaan
angka = [10, 4, 23, 7, 98, 15, 45, 98]
hasil = tiga_terbaik(angka)
print("3 bilangan terbaik:", hasil)
