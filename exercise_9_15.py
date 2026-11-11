import random

daftar_undian = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

tiket_saya = [1, 3, "A", "C"]

jumlah_perulangan = 0

while True:
    hasil_undian = random.sample(daftar_undian, 4)
    jumlah_perulangan += 1

    if set(hasil_undian) == set(tiket_saya):
        break

print("Tiket saya:", tiket_saya)
print("Hasil undian:", hasil_undian)
print("Tiket berhasil menang!")
print("Jumlah perulangan:", jumlah_perulangan)