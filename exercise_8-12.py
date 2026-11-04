def buat_sandwich(*bahan):
    print("\nSandwich yang dipesan berisi:")

    for isi in bahan:
        print(f"- {isi}")


buat_sandwich("Keju", "Sosis")

buat_sandwich("Ayam", "Selada", "Tomat")

buat_sandwich("Telur", "Keju", "Mayones", "Selada")