# Membuat variabel
nama_mobil = "Toyota"
warna_mobil = "Hitam"
tahun_produksi = 2022
harga_mobil = 200000000

# Membuat list mobil
daftar_mobil = ["Toyota", "Honda", "Suzuki", "Mitsubishi"]

# 1. Tes kesamaan dan ketidaksamaan string
print("Apakah nama mobil == 'Toyota'? Prediksi True.")
print(nama_mobil == "Toyota")

print("\nApakah nama mobil != 'Toyota'? Prediksi False.")
print(nama_mobil != "Toyota")

# 2. Tes menggunakan lower()
print("\nApakah warna.lower() == 'hitam'? Prediksi True.")
print(warna_mobil.lower() == "hitam")

print("\nApakah warna.lower() == 'putih'? Prediksi False.")
print(warna_mobil.lower() == "putih")

# 3. Tes perbandingan angka
print("\nApakah tahun produksi == 2022? Prediksi True.")
print(tahun_produksi == 2022)

print("\nApakah tahun produksi != 2022? Prediksi False.")
print(tahun_produksi != 2022)

print("\nApakah harga mobil > 100000000? Prediksi True.")
print(harga_mobil > 100000000)

print("\nApakah harga mobil < 100000000? Prediksi False.")
print(harga_mobil < 100000000)

print("\nApakah tahun produksi >= 2022? Prediksi True.")
print(tahun_produksi >= 2022)

print("\nApakah tahun produksi <= 2020? Prediksi False.")
print(tahun_produksi <= 2020)

# 4. Tes menggunakan and
print("\nApakah nama mobil Toyota dan warna Hitam? Prediksi True.")
print(nama_mobil == "Toyota" and warna_mobil == "Hitam")

print("\nApakah nama mobil Toyota dan warna Putih? Prediksi False.")
print(nama_mobil == "Toyota" and warna_mobil == "Putih")

# Tes menggunakan or
print("\nApakah mobil Toyota atau Honda? Prediksi True.")
print(nama_mobil == "Toyota" or nama_mobil == "Honda")

print("\nApakah mobil BMW atau Honda? Prediksi False.")
print(nama_mobil == "BMW" or nama_mobil == "Honda")

# 5. Tes apakah item terdapat dalam list
print("\nApakah Toyota ada dalam daftar mobil? Prediksi True.")
print("Toyota" in daftar_mobil)

print("\nApakah BMW ada dalam daftar mobil? Prediksi False.")
print("BMW" in daftar_mobil)

# 6. Tes apakah item tidak terdapat dalam list
print("\nApakah BMW tidak ada dalam daftar mobil? Prediksi True.")
print("BMW" not in daftar_mobil)

print("\nApakah Toyota tidak ada dalam daftar mobil? Prediksi False.")
print("Toyota" not in daftar_mobil)