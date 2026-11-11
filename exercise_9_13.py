import random

class Dadu:
    def __init__(self, jumlah_sisi=6):
        self.jumlah_sisi = jumlah_sisi

    def lempar_dadu(self):
        angka = random.randint(1, self.jumlah_sisi)
        print(angka)


# Dadu 6 sisi
print("Dadu 6 sisi:")
dadu6 = Dadu()

for i in range(10):
    dadu6.lempar_dadu()


# Dadu 10 sisi
print("\nDadu 10 sisi:")
dadu10 = Dadu(10)

for i in range(10):
    dadu10.lempar_dadu()


# Dadu 20 sisi
print("\nDadu 20 sisi:")
dadu20 = Dadu(20)

for i in range(10):
    dadu20.lempar_dadu()