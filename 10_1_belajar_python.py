# Membaca seluruh isi file
with open("belajar_python.txt") as file:
    isi = file.read()

print("Membaca seluruh isi file:")
print(isi)

# Membaca file dan menyimpan setiap baris ke dalam list
with open("belajar_python.txt") as file:
    daftar_baris = file.readlines()

print("Membaca menggunakan list:")
for baris in daftar_baris:
    print(baris.rstrip())

