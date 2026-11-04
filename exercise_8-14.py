def buat_mobil(merek, tipe, **informasi):
    mobil = {
        "merek": merek,
        "tipe": tipe
    }

    for kunci, nilai in informasi.items():
        mobil[kunci] = nilai

    return mobil


mobil_saya = buat_mobil(
    "Honda",
    "HRV",
    warna="Putih",
    transmisi="Matic"
)

print(mobil_saya)