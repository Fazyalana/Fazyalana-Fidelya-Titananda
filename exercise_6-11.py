# Membuat dictionary informasi kota
cities = {
    "Surakarta": {
        "country": "Indonesia",
        "population": "Sekitar 526 ribu jiwa",
        "fact": "Dikenal sebagai Kota Batik."
    },

    "Tokyo": {
        "country": "Jepang",
        "population": "Sekitar 14 juta jiwa",
        "fact": "Merupakan ibu kota Jepang."
    },

    "Paris": {
        "country": "Prancis",
        "population": "Sekitar 2 juta jiwa",
        "fact": "Terkenal dengan Menara Eiffel."
    }
}

# Menampilkan informasi setiap kota
for nama_kota, informasi in cities.items():
    print("\nNama kota:", nama_kota)
    print("Negara:", informasi["country"])
    print("Jumlah penduduk:", informasi["population"])
    print("Fakta:", informasi["fact"])