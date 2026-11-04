# Membuat dictionary berisi nama sungai dan negara
sungai = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china"
}

# Menampilkan kalimat tentang setiap sungai
for nama_sungai, negara in sungai.items():
    print(f"Sungai {nama_sungai.title()} mengalir melalui {negara.title()}.")

print("\nNama-nama sungai:")

# Menampilkan nama setiap sungai
for nama_sungai in sungai.keys():
    print(nama_sungai.title())

print("\nNama-nama negara:")

# Menampilkan nama setiap negara
for negara in sungai.values():
    print(negara.title())