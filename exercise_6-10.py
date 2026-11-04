# Membuat dictionary angka favorit
favorite_numbers = {
    "Vrysa": [7, 10, 15],
    "Kala": [3, 8],
    "Windi": [5, 12, 20],
    "Ren": [9, 11],
    "Djilva": [2, 6, 13]
}

# Menampilkan angka favorit setiap orang
for nama, angka in favorite_numbers.items():
    print("\nAngka favorit", nama + ":")

    for nomor in angka:
        print("-", nomor)