# Membuat dictionary orang pertama
orang1 = {
    "first_name": "Fazyalana",
    "last_name": "Fidelya",
    "age": 19,
    "city": "Boyolali"
}

# Membuat dictionary orang kedua
orang2 = {
    "first_name": "Vrysa",
    "last_name": "Dewi",
    "age": 18,
    "city": "Boyolali"
}

# Membuat dictionary orang ketiga
orang3 = {
    "first_name": "Djilva",
    "last_name": "Raihannun",
    "age": 18,
    "city": "Karanganyar"
}

# Menyimpan ketiga dictionary dalam list
people = [orang1, orang2, orang3]

# Menampilkan informasi setiap orang
for orang in people:
    print("\nNama:", orang["first_name"], orang["last_name"])
    print("Umur:", orang["age"])
    print("Kota:", orang["city"])