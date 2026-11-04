# Cara 1: import nama_module
import exercise_f8_16

print(exercise_f8_16.buat_kota("Surakarta", "Indonesia"))


# Cara 2: from nama_module import nama_fungsi
from exercise_f8_16 import buat_kota

print(buat_kota("Jakarta", "Indonesia"))


# Cara 3: from nama_module import nama_fungsi as fn
from exercise_f8_16 import buat_kota as fn

print(fn("Tokyo", "Jepang"))


# Cara 4: import nama_module as mn
import exercise_f8_16 as mn

print(mn.buat_kota("Paris", "Prancis"))


# Cara 5: from nama_module import *
from exercise_f8_16 import *

print(buat_kota("London", "Inggris"))