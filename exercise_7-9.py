pesanan_sandwich = [
    "tuna",
    "jagung",
    "ayam",
    "daging sapi",
    "keju"
]

sandwich_selesai = []

print("Maaf, toko kehabisan sandwich ayam.")

while "ayam" in pesanan_sandwich:
    pesanan_sandwich.remove("ayam")

while pesanan_sandwich:
    sandwich = pesanan_sandwich.pop()

    print(f"Saya telah membuat sandwich {sandwich} pesanan Anda.")

    sandwich_selesai.append(sandwich)

print("\nDaftar sandwich yang telah selesai dibuat:")

for sandwich in sandwich_selesai:
    print(sandwich)