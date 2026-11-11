import json

with open("favorite_number.json") as file:
    angka = json.load(file)

print("Saya tahu angka favoritmu! Angkanya adalah " + angka)
