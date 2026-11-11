
while True:
    print("\nKalkulator Penjumlahan")
    print("Ketik 'q' untuk keluar.")

    angka1 = input("Masukkan angka pertama: ")
    if angka1 == 'q':
        break

    angka2 = input("Masukkan angka kedua: ")
    if angka2 == 'q':
        break

    try:
        angka1 = int(angka1)
        angka2 = int(angka2)

        hasil = angka1 + angka2
        print("Hasil penjumlahan:", hasil)

    except ValueError:
        print("Maaf, masukkan angka yang benar!")
