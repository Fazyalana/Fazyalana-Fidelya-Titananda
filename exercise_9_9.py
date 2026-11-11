class Baterai:
    def __init__(self, kapasitas_baterai=40):
        self.kapasitas_baterai = kapasitas_baterai

    def deskripsi_baterai(self):
        print(f"Kapasitas baterai: {self.kapasitas_baterai} kWh")

    def jarak_tempuh(self):
        if self.kapasitas_baterai == 40:
            jarak = 150
        elif self.kapasitas_baterai == 65:
            jarak = 225

        print(f"Mobil dapat menempuh jarak {jarak} mil.")

    def tingkatkan_baterai(self):
        if self.kapasitas_baterai != 65:
            self.kapasitas_baterai = 65


class MobilListrik:
    def __init__(self, merek, nama_mobil):
        self.merek = merek
        self.nama_mobil = nama_mobil
        self.baterai = Baterai()

    def deskripsi_mobil(self):
        print(f"Merek mobil: {self.merek}")
        print(f"Nama mobil: {self.nama_mobil}")


mobil = MobilListrik("Tesla", "Model S")

mobil.deskripsi_mobil()

print("\nSebelum baterai ditingkatkan:")
mobil.baterai.deskripsi_baterai()
mobil.baterai.jarak_tempuh()

print("\nSetelah baterai ditingkatkan:")
mobil.baterai.tingkatkan_baterai()
mobil.baterai.deskripsi_baterai()
mobil.baterai.jarak_tempuh()