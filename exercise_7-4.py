while True:
    topping = input("Masukkan topping pizza (ketik 'quit' untuk selesai): ")

    if topping == "quit":
        print("Pesanan pizza selesai.")
        break
    else:
        print(f"Menambahkan {topping} ke pizza.")