class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsi_restoran(self):
        print(f"Nama restoran: {self.nama_restoran}")
        print(f"Jenis masakan: {self.jenis_masakan}")

    def restoran_buka(self):
        print(f"{self.nama_restoran} sedang buka!")


restoran = Restoran("Waroeng Makmur", "Masakan Jawa")

print(restoran.nama_restoran)
print(restoran.jenis_masakan)

restoran.deskripsi_restoran()
restoran.restoran_buka()