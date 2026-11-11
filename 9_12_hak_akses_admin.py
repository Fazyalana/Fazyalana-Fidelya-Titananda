from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location("pengguna", "9_12_pengguna.py")
modul = module_from_spec(spec)
spec.loader.exec_module(modul)

User = modul.User


class Privileges:

    def __init__(self):
        self.privileges = [
            "Dapat menambahkan postingan",
            "Dapat menghapus postingan",
            "Dapat memblokir pengguna"
        ]

    def show_privileges(self):
        print("Hak akses admin:")
        for hak in self.privileges:
            print("-", hak)


class Admin(User):

    def __init__(self, nama_depan, nama_belakang, umur):
        super().__init__(nama_depan, nama_belakang, umur)
        self.privileges = Privileges()