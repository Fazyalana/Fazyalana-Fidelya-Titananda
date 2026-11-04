# Program Pengelolaan Keuangan Sederhana

print("=== PROGRAM PENGELOLAAN KEUANGAN ===")

# Memasukkan jumlah uang awal
uang_awal = int(input("Masukkan uang awal: Rp"))

# Memasukkan pemasukan
pemasukan = int(input("Masukkan jumlah pemasukan: Rp"))

# Memasukkan pengeluaran
pengeluaran = int(input("Masukkan jumlah pengeluaran: Rp"))

# Menghitung sisa uang
sisa_uang = uang_awal + pemasukan - pengeluaran

# Menampilkan hasil
print("\n=== HASIL PENGELOLAAN KEUANGAN ===")
print(f"Uang awal       : Rp{uang_awal}")
print(f"Pemasukan       : Rp{pemasukan}")
print(f"Pengeluaran     : Rp{pengeluaran}")
print(f"Sisa uang       : Rp{sisa_uang}")

if sisa_uang >= 0:
    print("Keuangan masih mencukupi.")
else:
    print("Pengeluaran melebihi uang yang tersedia.")