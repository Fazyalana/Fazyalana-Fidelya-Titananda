def buat_profil(nama_depan, nama_belakang, **informasi):
    profil = {}

    profil["nama_depan"] = nama_depan
    profil["nama_belakang"] = nama_belakang

    for kunci, nilai in informasi.items():
        profil[kunci] = nilai

    return profil


data_diri = buat_profil(
    "Fazyalana",
    "Fidelya",
    umur=19,
    jurusan="Teknik Industri",
    hobi="Membuat kerajinan tangan"
)

print("=== PROFIL PENGGUNA ===")

for kunci, nilai in data_diri.items():
    print(f"{kunci}: {nilai}")