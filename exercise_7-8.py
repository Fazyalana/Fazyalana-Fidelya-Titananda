pesanan_sandwich = ["tuna", "ayam", "daging sapi", "keju"]

sandwich_selesai = []

while pesanan_sandwich:
    sandwich = pesanan_sandwich.pop()

    print(f"Saya telah membuat sandwich {sandwich} pesanan Anda.")

    sandwich_selesai.append(sandwich)

print("\nDaftar sandwich yang telah selesai dibuat:")

for sandwich in sandwich_selesai:
    print(sandwich)