import json

angka = input("Masukkan angka favoritmu: ")

with open("favorite_number.json", "w") as file:
    json.dump(angka, file)

print("Angka favorit berhasil disimpan.")
