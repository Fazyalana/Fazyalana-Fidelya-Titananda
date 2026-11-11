import json

def get_new_user():
    pengguna = {}

    pengguna["nama"] = input("Masukkan nama pengguna: ")
    pengguna["umur"] = input("Masukkan umur: ")
    pengguna["warna_favorit"] = input("Masukkan warna favorit: ")

    with open("user_info.json", "w") as file:
        json.dump(pengguna, file)

    return pengguna


def get_new_username(pengguna):
    nama_baru = input("Masukkan nama pengguna yang benar: ")
    pengguna["nama"] = nama_baru

    with open("user_info.json", "w") as file:
        json.dump(pengguna, file)

    return pengguna


def greet_user():
    try:
        with open("user_info.json") as file:
            pengguna = json.load(file)

        print("Apakah nama pengguna ini benar?")
        print("Nama:", pengguna["nama"])

        jawaban = input("Benar? (ya/tidak): ")

        if jawaban.lower() == "ya":
            print("Selamat datang kembali, " + pengguna["nama"] + "!")

        else:
            pengguna = get_new_username(pengguna)
            print("Selamat datang, " + pengguna["nama"] + "!")

    except FileNotFoundError:
        pengguna = get_new_user()
        print("Data berhasil disimpan.")
        print("Selamat datang, " + pengguna["nama"] + "!")


greet_user()
