# Membuat dictionary tempat favorit
favorite_places = {
    "Vrysa": ["Bali", "Yogyakarta", "Bandung"],
    "Kala": ["Jakarta", "Malang"],
    "Windi": ["Surakarta", "Lombok", "Bromo"]
}

# Menampilkan nama dan tempat favorit
for nama, tempat in favorite_places.items():
    print("\nTempat favorit", nama + ":")

    for lokasi in tempat:
        print("-", lokasi)