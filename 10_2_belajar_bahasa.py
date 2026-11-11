with open("belajar_python.txt") as file:
    for baris in file:
        baris_baru = baris.replace("Python", "C")
        print(baris_baru.rstrip())
