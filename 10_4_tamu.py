nama = input("Masukkan nama kamu: ")

pesan = "Selamat datang, " + nama + "!"

print(pesan)

with open("tamu.txt", "w") as file:
    file.write(pesan)
