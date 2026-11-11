def city_country(kota, negara, populasi=''):
    if populasi:
        hasil = f"{kota.title()}, {negara.title()} - population {populasi}"
    else:
        hasil = f"{kota.title()}, {negara.title()}"

    return hasil

