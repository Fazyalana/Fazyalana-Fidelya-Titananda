# Membuat dictionary hewan peliharaan
hewan1 = {
    "jenis": "Kucing",
    "pemilik": "Lana"
}

hewan2 = {
    "jenis": "Kelinci",
    "pemilik": "Djilva"
}

hewan3 = {
    "jenis": "Ikan",
    "pemilik": "Vrysa"
}

hewan4 = {
    "jenis": "Burung",
    "pemilik": "Kala"
}

# Menyimpan dictionary ke dalam list
pets = [hewan1, hewan2, hewan3, hewan4]

# Menampilkan informasi setiap hewan
for hewan in pets:
    print("\nJenis hewan:", hewan["jenis"])
    print("Nama pemilik:", hewan["pemilik"])