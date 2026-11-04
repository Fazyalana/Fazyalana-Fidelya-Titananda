# Membuat tuple berisi lima jenis makanan
menu_makanan = ("Nasi Goreng", "Ayam Goreng", "Jamur", "Bakso", "Mie")

# Menampilkan menu makanan
print("Menu makanan restoran:")
for makanan in menu_makanan:
    print(makanan)

# Mencoba mengubah isi tuple
print("\nMencoba mengubah menu pertama:")

try:
    menu_makanan[0] = "Nasi Kuning"
except TypeError:
    print("Menu tidak dapat diubah karena tuple bersifat tetap.")

# Membuat tuple baru dengan menu yang diperbarui
menu_makanan = ("Nasi Kuning", "Ayam Bakar", "Jamur", "Bakso", "Mie")

# Menampilkan menu terbaru
print("\nMenu makanan terbaru:")
for makanan in menu_makanan:
    print(makanan)