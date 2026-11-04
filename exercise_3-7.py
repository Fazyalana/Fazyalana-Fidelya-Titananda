# Membuat list tamu
daftar_tamu = [
    "Vrysa",
    "Windi",
    "Kala",
    "Djilva",
    "Ren",
    "Nissa"
]

# Memberi tahu bahwa hanya dua tamu yang bisa diundang
print("Maaf, aku hanya bisa mengundang dua orang untuk makan malam.")

# Menghapus tamu menggunakan pop()
tamu = daftar_tamu.pop()
print(f"Maaf {tamu}, aku tidak bisa mengundang kamu.")

tamu = daftar_tamu.pop()
print(f"Maaf {tamu}, aku tidak bisa mengundang kamu.")

tamu = daftar_tamu.pop()
print(f"Maaf {tamu}, aku tidak bisa mengundang kamu.")

tamu = daftar_tamu.pop()
print(f"Maaf {tamu}, aku tidak bisa mengundang kamu.")

# Memberi tahu dua tamu yang masih diundang
print("\nTamu yang tetap diundang:")
print(f"Halo {daftar_tamu[0]}, kamu tetap diundang untuk makan malam.")
print(f"Halo {daftar_tamu[1]}, kamu tetap diundang untuk makan malam.")

# Menghapus dua nama terakhir
del daftar_tamu[1]
del daftar_tamu[0]

# Menampilkan list kosong
print("\nDaftar tamu setelah dihapus:")
print(daftar_tamu)