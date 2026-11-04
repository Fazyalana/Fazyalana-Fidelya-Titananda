# Membuat daftar pengguna yang sudah terdaftar
pengguna_lama = ["Vrysa", "Kala", "Windi", "Ren", "Djilva"]

# Membuat daftar pengguna baru
pengguna_baru = ["Vrysa", "Nissa", "Key", "KALA", "Ael"]

# Mengubah semua nama menjadi huruf kecil
pengguna_lama_kecil = []

for nama in pengguna_lama:
    pengguna_lama_kecil.append(nama.lower())

# Memeriksa nama pengguna baru
for nama in pengguna_baru:
    if nama.lower() in pengguna_lama_kecil:
        print(f"Maaf, nama {nama} sudah digunakan. Silakan gunakan nama lain.")
    else:
        print(f"Nama {nama} masih tersedia.")