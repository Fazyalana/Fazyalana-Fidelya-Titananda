# PROGRAM 1: ANGKA GANJIL

print("=== DAFTAR ANGKA GANJIL ===")

angka_ganjil = list(range(1, 21, 2))

for angka in angka_ganjil:
    print(angka)


# PROGRAM 2: BILANGAN KUBIK

print("\n=== DAFTAR BILANGAN KUBIK ===")

bilangan_kubik = []

for angka in range(1, 11):
    bilangan_kubik.append(angka ** 3)

for hasil in bilangan_kubik:
    print(hasil)


# PROGRAM 3: DAFTAR GUNUNG

print("\n=== DAFTAR NAMA GUNUNG ===")

nama_gunung = ["Merapi", "Semeru", "Bromo", "Rinjani"]

for gunung in nama_gunung:
    print(gunung)

print("Jumlah gunung:", len(nama_gunung))