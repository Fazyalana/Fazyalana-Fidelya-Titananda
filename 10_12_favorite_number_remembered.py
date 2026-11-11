import json

try:
    with open("favorite_number.json") as file:
        angka = json.load(file)

    print("Angka favoritmu adalah " + angka)

except FileNotFoundError:
    angka = input("Masukkan angka favoritmu: ")

    with open("favorite_number.json", "w") as file:
        json.dump(angka, file)

    print("Angka favorit berhasil disimpan.")
