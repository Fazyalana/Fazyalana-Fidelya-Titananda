class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, kota, pekerjaan):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.kota = kota
        self.pekerjaan = pekerjaan
        self.percobaan_login = 0

    def deskripsi_pengguna(self):
        print(f"Nama depan: {self.nama_depan}")
        print(f"Nama belakang: {self.nama_belakang}")
        print(f"Umur: {self.umur}")
        print(f"Kota: {self.kota}")
        print(f"Pekerjaan: {self.pekerjaan}")

    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan}! Selamat datang.")

    def tambah_percobaan_login(self):
        self.percobaan_login += 1

    def reset_percobaan_login(self):
        self.percobaan_login = 0


pengguna = Pengguna("Vrysa", "Dewi", 18, "Boyolali", "Mahasiswa")

# Menambahkan percobaan login beberapa kali
pengguna.tambah_percobaan_login()
pengguna.tambah_percobaan_login()
pengguna.tambah_percobaan_login()
pengguna.tambah_percobaan_login()

# Menampilkan jumlah percobaan login
print("Jumlah percobaan login:", pengguna.percobaan_login)

# Mengatur ulang percobaan login
pengguna.reset_percobaan_login()

# Menampilkan jumlah percobaan setelah direset
print("Jumlah percobaan login setelah direset:", pengguna.percobaan_login)