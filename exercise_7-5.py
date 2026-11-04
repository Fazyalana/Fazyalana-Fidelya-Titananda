while True:
    usia = input("Masukkan usia (ketik 'quit' untuk selesai): ")

    if usia == "quit":
        print("Program selesai.")
        break

    usia = int(usia)

    if usia < 3:
        print("Harga tiket: Gratis")
    elif usia <= 12:
        print("Harga tiket: $10")
    else:
        print("Harga tiket: $15")