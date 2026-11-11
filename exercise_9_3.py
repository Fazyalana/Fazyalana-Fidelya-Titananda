class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, kota, pekerjaan):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.kota = kota
        self.pekerjaan = pekerjaan

    def deskripsi_pengguna(self):
        print(f"Nama depan: {self.nama_depan}")
        print(f"Nama belakang: {self.nama_belakang}")
        print(f"Umur: {self.umur}")
        print(f"Kota: {self.kota}")
        print(f"Pekerjaan: {self.pekerjaan}")

    def sapa_pengguna(self):
        print(f"Halo, {self.nama_depan}! Selamat datang.")


pengguna1 = Pengguna("Vrysa", "Dewi", 18, "Boyolali", "Mahasiswa")
pengguna2 = Pengguna("Kayla", "Kafka", 19, "Kebumen", "Mahasiswa")
pengguna3 = Pengguna("Windi", "Arlentia", 19, "Surakarta", "Mahasiswa")


pengguna1.deskripsi_pengguna()
pengguna1.sapa_pengguna()

print()

pengguna2.deskripsi_pengguna()
pengguna2.sapa_pengguna()

print()

pengguna3.deskripsi_pengguna()
pengguna3.sapa_pengguna()