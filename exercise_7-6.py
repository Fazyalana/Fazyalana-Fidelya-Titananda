print("=== PROGRAM TOPPING PIZZA ===")

# Cara 1: Menggunakan kondisi while
print("\n1. Menggunakan kondisi while")

topping = ""

while topping != "quit":
    topping = input("Masukkan topping (quit untuk selesai): ")

    if topping != "quit":
        print(f"Menambahkan {topping} ke pizza.")


# Cara 2: Menggunakan active variable
print("\n2. Menggunakan active variable")

aktif = True

while aktif:
    topping = input("Masukkan topping (quit untuk selesai): ")

    if topping == "quit":
        aktif = False
    else:
        print(f"Menambahkan {topping} ke pizza.")


# Cara 3: Menggunakan break
print("\n3. Menggunakan break")

while True:
    topping = input("Masukkan topping (quit untuk selesai): ")

    if topping == "quit":
        break

    print(f"Menambahkan {topping} ke pizza.")

print("\nSemua program selesai!")