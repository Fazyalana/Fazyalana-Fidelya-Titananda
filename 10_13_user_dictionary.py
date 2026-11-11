import json

# Meminta informasi pengguna
pengguna = {}

pengguna["nama"] = input("Masukkan nama: ")
pengguna["umur"] = input("Masukkan umur: ")
pengguna["warna_favorit"] = input("Masukkan warna favorit: ")

# Menyimpan dictionary ke file
with open("user_info.json", "w") as file:
    json.dump(pengguna, file)

# Membaca kembali isi file
with open("user_info.json") as file:
    data = json.load(file)

# Menampilkan ringkasan
print("\nInformasi pengguna yang diingat:")
print("Nama:", data["nama"])
print("Umur:", data["umur"])
print("Warna favorit:", data["warna_favorit"])
