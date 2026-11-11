class User:

    def __init__(self, nama_depan, nama_belakang, umur):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur

    def describe_user(self):
        print("Nama:", self.nama_depan, self.nama_belakang)
        print("Umur:", self.umur)