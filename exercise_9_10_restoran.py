class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.jumlah_pelanggan = 0

    def deskripsi_restoran(self):
        print(f"Nama restoran: {self.nama_restoran}")
        print(f"Jenis masakan: {self.jenis_masakan}")

    def restoran_buka(self):
        print(f"{self.nama_restoran} sedang buka!")

    def atur_jumlah_pelanggan(self, jumlah):
        self.jumlah_pelanggan = jumlah

    def tambah_jumlah_pelanggan(self, jumlah):
        self.jumlah_pelanggan += jumlah