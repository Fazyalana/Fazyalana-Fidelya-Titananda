# Membuat dictionary bahasa pemrograman favorit
favorite_languages = {
    "Vrysa": "Python",
    "Kala": "Java",
    "Windi": "C++",
    "Ren": "Python",
    "Djilva": "JavaScript"
}

# Membuat daftar orang yang harus mengikuti polling
orang_polling = ["Vrysa", "Kala", "Nadia", "Ren", "Rina", "Andi"]

# Memeriksa siapa yang sudah dan belum mengikuti polling
for nama in orang_polling:
    if nama in favorite_languages:
        print(f"Terima kasih {nama}, sudah mengikuti polling.")
    else:
        print(f"Halo {nama}, silakan ikuti polling bahasa pemrograman favorit.")