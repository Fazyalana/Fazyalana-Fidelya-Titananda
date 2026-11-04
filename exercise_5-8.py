# Membuat daftar nama pengguna
nama_pengguna = ["Vrysa", "Windi", "Kala", "Djilva", "Nissa"]

# Menampilkan sapaan kepada setiap pengguna
for pengguna in nama_pengguna:
    if pengguna == "Vrysa":
        print("Halo Vrysa, apakah kamu ingin melihat laporan status?")
    else:
        print(f"Halo {pengguna}, terima kasih sudah login kembali.")