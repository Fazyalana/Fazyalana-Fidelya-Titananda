def cetak_model(desain_belum_dicetak, desain_selesai_dicetak):
    while desain_belum_dicetak:
        desain = desain_belum_dicetak.pop()

        print(f"Mencetak desain: {desain}")
        desain_selesai_dicetak.append(desain)


def tampilkan_model(desain_selesai_dicetak):
    print("\nDesain yang sudah dicetak:")

    for desain in desain_selesai_dicetak:
        print(desain)