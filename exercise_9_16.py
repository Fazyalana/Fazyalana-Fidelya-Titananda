import random

daftar_nama = ["Vrysa", "Kala", "Windi", "Ren", "Djilva"]

# Memilih satu nama secara acak
nama_terpilih = random.choice(daftar_nama)

print("Nama yang terpilih:", nama_terpilih)

# Menghasilkan angka acak
angka = random.randint(1, 100)

print("Angka acak:", angka)

# Mengacak urutan nama
random.shuffle(daftar_nama)

print("Urutan nama setelah diacak:", daftar_nama)