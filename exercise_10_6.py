
try:
    angka1 = input("Masukkan angka pertama: ")
    angka2 = input("Masukkan angka kedua: ")

    angka1 = int(angka1)
    angka2 = int(angka2)

    hasil = angka1 + angka2
    print("Hasil penjumlahan:", hasil)

except ValueError:
    print("Maaf, masukkan angka yang benar!")
