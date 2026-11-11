with open("belajar_python.txt") as file:
    isi = file.read()

for baris in isi.splitlines():
    print(baris)
