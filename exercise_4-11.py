# Membuat daftar pizza favorit saya
pizza_saya = ["Pepperoni", "Cheese", "Meat lover"]

# Membuat salinan daftar pizza
pizza_teman = pizza_saya[:]

# Menambahkan pizza ke daftar saya
pizza_saya.append("Jamur")

# Menambahkan pizza ke daftar teman
pizza_teman.append("Tuna")

# Menampilkan pizza favorit saya
print("Pizza favorit saya adalah:")
for jenis_pizza in pizza_saya:
    print(jenis_pizza)

# Menampilkan pizza favorit teman
print("\nPizza favorit teman saya adalah:")
for jenis_pizza in pizza_teman:
    print(jenis_pizza)