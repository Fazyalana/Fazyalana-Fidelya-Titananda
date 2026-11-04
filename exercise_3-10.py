# Membuat list nama gunung
nama_gunung = ["Merapi", "Semeru", "Bromo", "Rinjani"]

# Menampilkan list awal
print("Daftar gunung:")
print(nama_gunung)

# Menambahkan gunung menggunakan append()
nama_gunung.append("Kerinci")
print("\nSetelah append():")
print(nama_gunung)

# Menambahkan gunung menggunakan insert()
nama_gunung.insert(1, "Lawu")
print("\nSetelah insert():")
print(nama_gunung)

# Menghapus gunung menggunakan del
del nama_gunung[0]
print("\nSetelah del:")
print(nama_gunung)

# Menghapus gunung menggunakan pop()
gunung = nama_gunung.pop()
print("\nGunung yang dihapus:", gunung)
print(nama_gunung)

# Menghapus gunung menggunakan remove()
nama_gunung.remove("Bromo")
print("\nSetelah remove():")
print(nama_gunung)

# Mengurutkan menggunakan sorted()
print("\nUrutan berdasarkan abjad:")
print(sorted(nama_gunung))

# Membalik urutan menggunakan reverse()
nama_gunung.reverse()
print("\nSetelah reverse():")
print(nama_gunung)

# Mengurutkan menggunakan sort()
nama_gunung.sort()
print("\nSetelah sort():")
print(nama_gunung)

# Menghitung jumlah gunung menggunakan len()
print("\nJumlah gunung:", len(nama_gunung))