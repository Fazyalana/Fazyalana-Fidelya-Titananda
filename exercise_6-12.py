# Membuat dictionary informasi teman
teman = {
    "Vrysa": {
        "umur": 18,
        "kota": "Boyolali",
        "angka_favorit": [7, 10, 15]
    },

    "Kala": {
        "umur": 19,
        "kota": "Kebumen",
        "angka_favorit": [3, 8]
    },

    "Windi": {
        "umur": 19,
        "kota": "Surakarta",
        "angka_favorit": [5, 12, 20]
    },

    "Ren": {
        "umur": 18,
        "kota": "Bekasi",
        "angka_favorit": [9, 11]
    },

    "Djilva": {
        "umur": 18,
        "kota": "Karanganyar",
        "angka_favorit": [2, 6, 13]
    }
}

# Menampilkan seluruh informasi teman
print("===== DATA TEMAN =====")

for nama, informasi in teman.items():
    print("\nNama:", nama)
    print("Umur:", informasi["umur"])
    print("Kota:", informasi["kota"])
    print("Angka favorit:", informasi["angka_favorit"])

print("\n===== DATA SELESAI DITAMPILKAN =====")