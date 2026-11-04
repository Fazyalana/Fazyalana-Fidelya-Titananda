# Membuat dictionary istilah pemrograman
glossary = {
    "variable": "Tempat untuk menyimpan data.",
    "list": "Digunakan untuk menyimpan beberapa data dalam satu variabel.",
    "if": "Digunakan untuk membuat kondisi dalam program.",
    "loop": "Digunakan untuk mengulang perintah.",
    "dictionary": "Digunakan untuk menyimpan data dalam bentuk key dan value."
}

# Menampilkan istilah dan artinya
for kata, arti in glossary.items():
    print(kata.title() + ":")
    print("  " + arti + "\n")