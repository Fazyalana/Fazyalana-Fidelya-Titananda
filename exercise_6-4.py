# Membuat dictionary istilah pemrograman
glossary = {
    "variable": "Tempat untuk menyimpan data.",
    "list": "Digunakan untuk menyimpan beberapa data dalam satu variabel.",
    "if": "Digunakan untuk membuat kondisi dalam program.",
    "loop": "Digunakan untuk mengulang perintah.",
    "dictionary": "Digunakan untuk menyimpan data dalam bentuk key dan value.",

    # Lima istilah tambahan
    "string": "Jenis data yang berisi teks atau kumpulan karakter.",
    "integer": "Jenis data yang berupa bilangan bulat.",
    "float": "Jenis data yang berupa bilangan desimal.",
    "input": "Digunakan untuk menerima masukan dari pengguna.",
    "print": "Digunakan untuk menampilkan informasi ke layar."
}

# Menampilkan semua istilah dan artinya
for kata, arti in glossary.items():
    print(kata.title() + ":")
    print("  " + arti + "\n")