class Pengguna:
    def __init__(self, nama_depan, nama_belakang, umur, kota):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.kota = kota

    def deskripsi_pengguna(self):
        print(f"Nama: {self.nama_depan} {self.nama_belakang}")
        print(f"Umur: {self.umur}")
        print(f"Kota: {self.kota}")


class Admin(Pengguna):
    def __init__(self, nama_depan, nama_belakang, umur, kota):
        super().__init__(nama_depan, nama_belakang, umur, kota)
        self.hak_akses = [
            "Dapat membuat postingan",
            "Dapat menghapus postingan",
            "Dapat memblokir pengguna"
        ]

    def tampilkan_hak_akses(self):
        print("Hak akses administrator:")
        for hak in self.hak_akses:
            print(f"- {hak}")


admin = Admin("Vrysa", "Dewi", 18, "Boyolali")

admin.deskripsi_pengguna()
admin.tampilkan_hak_akses()