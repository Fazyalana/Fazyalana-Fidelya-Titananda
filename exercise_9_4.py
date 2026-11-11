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


restoran = Restoran("Waroeng Makmur", "Masakan Jawa")

# Menampilkan jumlah pelanggan awal
print("Jumlah pelanggan awal:", restoran.jumlah_pelanggan)

# Mengubah jumlah pelanggan secara langsung
restoran.jumlah_pelanggan = 20
print("Jumlah pelanggan setelah diubah:", restoran.jumlah_pelanggan)

# Mengatur jumlah pelanggan menggunakan method
restoran.atur_jumlah_pelanggan(35)
print("Jumlah pelanggan sekarang:", restoran.jumlah_pelanggan)

# Menambahkan jumlah pelanggan
restoran.tambah_jumlah_pelanggan(15)
print("Jumlah pelanggan setelah ditambahkan:", restoran.jumlah_pelanggan)