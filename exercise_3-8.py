# Membuat list tempat yang ingin dikunjungi
tempat = ["Jepang", "Korea", "Bali", "Raja ampat", "Finland"]

# Menampilkan urutan asli
print("Urutan asli:")
print(tempat)

# Mengurutkan berdasarkan abjad tanpa mengubah list asli
print("\nUrutan berdasarkan abjad:")
print(sorted(tempat))

# Menampilkan kembali urutan asli
print("\nUrutan asli:")
print(tempat)

# Mengurutkan berdasarkan abjad terbalik tanpa mengubah list asli
print("\nUrutan abjad terbalik:")
print(sorted(tempat, reverse=True))

# Menampilkan kembali urutan asli
print("\nUrutan asli:")
print(tempat)

# Membalik urutan list
tempat.reverse()
print("\nSetelah menggunakan reverse():")
print(tempat)

# Mengembalikan urutan list seperti semula
tempat.reverse()
print("\nSetelah reverse() kedua:")
print(tempat)

# Mengurutkan list berdasarkan abjad
tempat.sort()
print("\nSetelah menggunakan sort():")
print(tempat)

# Mengurutkan list berdasarkan abjad terbalik
tempat.sort(reverse=True)
print("\nSetelah sort() terbalik:")
print(tempat)