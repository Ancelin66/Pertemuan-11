import string

def tampilkan_kata_unik_dari_file(file_teks):
    try:
        with open(file_teks, 'r', encoding='utf-8') as sumber:
            isi = sumber.read()

        # Bersihkan teks dari tanda baca dan ubah ke huruf kecil
        isi_bersih = isi.translate(str.maketrans('', '', string.punctuation)).lower()

        # Pecah isi menjadi daftar kata
        daftar_kata = isi_bersih.split()

        # Ambil kata-kata unik
        kumpulan_kata_unik = set(daftar_kata)

        # Tampilkan hasilnya
        print("Daftar kata unik dari artikel:")
        for item in sorted(kumpulan_kata_unik):
            print(item)

    except FileNotFoundError:
        print(f"File '{file_teks}' tidak ditemukan.")
    except Exception as kesalahan:
        print(f"Terjadi kesalahan: {kesalahan}")

# Contoh penggunaan
nama_berkas = input("Masukkan nama file teks (misalnya: berita.txt): ")
tampilkan_kata_unik_dari_file(nama_berkas)
