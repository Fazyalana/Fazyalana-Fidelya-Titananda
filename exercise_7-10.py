responses = {}

while True:
    nama = input("Siapa nama kamu? ")
    tempat = input("Jika bisa mengunjungi satu tempat di dunia, ke mana kamu akan pergi? ")

    responses[nama] = tempat

    lagi = input("Apakah ada orang lain yang ingin mengikuti survei? (ya/tidak): ")

    if lagi == "tidak":
        break

print("\n=== HASIL SURVEI LIBURAN IMPIAN ===")

for nama, tempat in responses.items():
    print(f"{nama} ingin berlibur ke {tempat}.")