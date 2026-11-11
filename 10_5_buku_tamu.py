while True:
    nama = input("Masukkan nama kamu (ketik 'q' untuk keluar): ")

    if nama == 'q':
        break

    print("Selamat datang, " + nama + "!")

    with open("buku_tamu.txt", "a") as file:
        file.write(nama + "\n")

print("Semua nama berhasil disimpan.")
