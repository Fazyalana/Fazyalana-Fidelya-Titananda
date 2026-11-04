def kirim_pesan(daftar_pesan, pesan_terkirim):
    while daftar_pesan:
        pesan = daftar_pesan.pop()

        print(f"Mengirim pesan: {pesan}")

        pesan_terkirim.append(pesan)


pesan = [
    "Selamat pagi!",
    "Selamat beraktivitas.",
    "Tetap semangat!",
    "Semoga hari ini menyenangkan."
]

pesan_terkirim = []

kirim_pesan(pesan, pesan_terkirim)

print("\nDaftar pesan awal:")
print(pesan)

print("\nDaftar pesan terkirim:")
print(pesan_terkirim)