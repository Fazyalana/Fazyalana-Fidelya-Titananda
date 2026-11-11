class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsi_restoran(self):
        print(f"Nama restoran: {self.nama_restoran}")
        print(f"Jenis masakan: {self.jenis_masakan}")


restoran1 = Restoran("Waroeng Makmur", "Masakan Indonesia")
restoran2 = Restoran("Pizza Hut", "Masakan Italia")
restoran3 = Restoran("RAMEN YA!", "Masakan Jepang")


restoran1.deskripsi_restoran()
print()

restoran2.deskripsi_restoran()
print()

restoran3.deskripsi_restoran()