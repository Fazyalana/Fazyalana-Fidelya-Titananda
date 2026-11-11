nama_file = "buku.txt"

try:
    with open(nama_file, encoding="utf-8") as file:
        isi = file.read()

        jumlah = isi.lower().count("the")

        print("Jumlah kata 'the':", jumlah)

except FileNotFoundError:
    print("File tidak ditemukan.")