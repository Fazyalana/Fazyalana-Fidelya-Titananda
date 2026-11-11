# Membaca file kucing
try:
    with open("kucing.txt") as file:
        isi_kucing = file.read()
        print("Daftar nama kucing:")
        print(isi_kucing)

except FileNotFoundError:
    print("File kucing.txt tidak ditemukan.")

# Membaca file anjing
try:
    with open("anjing.txt") as file:
        isi_anjing = file.read()
        print("Daftar nama anjing:")
        print(isi_anjing)

except FileNotFoundError:
    print("File anjing.txt tidak ditemukan.")