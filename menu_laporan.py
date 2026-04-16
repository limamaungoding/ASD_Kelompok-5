# LAPORAN 

def laporan_tersedia(data_dict):
    print("\n=== Kendaraan Tersedia ===")
    for plat, k in data_dict.items():
        if k["status"] == "tersedia":
            print(plat, "-", k["nama"])


def laporan_disewa(data_dict):
    print("\n=== Kendaraan Disewa ===")
    for plat, k in data_dict.items():
        if k["status"] == "disewa":
            print(plat, "-", k["nama"])


def laporan_keuangan(data_dict):
    total = 0
    for k in data_dict.values():
        if k["status"] == "disewa":
            total += k["harga"]

    print("\n=== Laporan Keuangan ===")
    print("Total Pendapatan: Rp", total)


# MENU LAPORAN 
def menu_laporan(data_dict):
    while True:
        print("\n=== MENU LAPORAN ===")
        print("1. Kendaraan Tersedia")
        print("2. Kendaraan Disewa")
        print("3. Laporan Keuangan")
        print("0. Kembali")

        pilih = input("Pilih: ")

        if pilih == "1":
            laporan_tersedia(data_dict)
        elif pilih == "2":
            laporan_disewa(data_dict)
        elif pilih == "3":
            laporan_keuangan(data_dict)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")


# MENU UTAMA
if __name__ == "__main__":
    data = baca_data(nama_file)

    while True:
        print("\n=== RENTAL MOBIL & MOTOR ===")
        print("5. Kembalikan Kendaraan")
        print("6. Laporan")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "5":
            kembalikan_kendaraan(data)
        elif pilihan == "6":
            menu_laporan(data)
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Menu belum tersedia / tidak valid")