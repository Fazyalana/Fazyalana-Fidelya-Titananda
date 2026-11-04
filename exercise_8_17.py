# Program 1: Message
def tampilkan_pesan():
    """Menampilkan pesan tentang belajar Python."""
    print("Saya sedang belajar fungsi Python.")


# Program 2: Favorite Book
def buku_favorit(judul):
    """Menampilkan judul buku favorit."""
    print(f"Buku favorit saya adalah {judul}.")


# Program 3: City Names
def buat_kota(nama_kota, negara="Indonesia"):
    """Menggabungkan nama kota dan negara."""
    kota = f"{nama_kota}, {negara}"
    return kota


# Memanggil semua fungsi
tampilkan_pesan()

buku_favorit("Laskar Pelangi")

hasil = buat_kota("Boyolali")
print(hasil)

hasil = buat_kota("Tokyo", "Jepang")
print(hasil)