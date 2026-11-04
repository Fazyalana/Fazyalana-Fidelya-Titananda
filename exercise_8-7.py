def buat_album(penyanyi, judul, jumlah_lagu=None):
    album = {
        "penyanyi": penyanyi,
        "judul_album": judul
    }

    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu

    return album


# Membuat tiga album
album1 = buat_album("Tulus", "Manusia")
album2 = buat_album("Hindia", "Menari dengan Bayangan")
album3 = buat_album("Sheila On 7", "Kisah Klasik untuk Masa Depan")

# Membuat album dengan jumlah lagu
album4 = buat_album("Taylor Swift", "Midnights", 13)

# Menampilkan hasil
print(album1)
print(album2)
print(album3)
print(album4)