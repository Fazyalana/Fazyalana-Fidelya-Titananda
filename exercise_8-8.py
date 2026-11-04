def buat_album(penyanyi, judul):
    album = {
        "penyanyi": penyanyi,
        "judul_album": judul
    }

    return album


while True:
    print("\nMasukkan data album musik.")

    penyanyi = input("Masukkan nama penyanyi (ketik 'quit' untuk selesai): ")

    if penyanyi == "quit":
        break

    judul = input("Masukkan judul album: ")

    hasil = buat_album(penyanyi, judul)

    print("\nData album:")
    print(hasil)

print("\nProgram selesai.")