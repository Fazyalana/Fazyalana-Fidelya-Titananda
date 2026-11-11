class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsi_restoran(self):
        print(f"Nama restoran: {self.nama_restoran}")
        print(f"Jenis masakan: {self.jenis_masakan}")


class KedaiEsKrim(Restoran):
    def __init__(self, nama_restoran, jenis_masakan):
        super().__init__(nama_restoran, jenis_masakan)
        self.daftar_rasa = ["Cokelat", "Vanila", "Stroberi"]

    def tampilkan_rasa(self):
        print("Daftar rasa es krim:")
        for rasa in self.daftar_rasa:
            print(f"- {rasa}")


kedai = KedaiEsKrim("del' Ice Cream", "Es Krim")

kedai.deskripsi_restoran()
kedai.tampilkan_rasa()