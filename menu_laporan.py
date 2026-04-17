nama_file =  "data_kendaraan.txt"
# Baca file bagian Lima
def baca_data(nama_file):
    data_dict = {}
    try:
        with open(nama_file, 'r', encoding="utf-8") as file:
            for baris in file : 
                baris = baris.strip() #mengambil data perbaris
                if not baris: continue
                parts = baris.split(",")
                plat, jenis, nama, warna, harga = parts[0], parts[1], parts[2], parts[3], parts[4]
                status = parts[5] if len(parts) > 5 else "Tersedia" #jika ada status, gunakan, if not, default "Tersedia"

                data_dict[plat]= {
                    "jenis": jenis, 
                    "nama": nama, 
                    "warna": warna, 
                    "harga": int(harga),
                    "status": status
                    } 
    except FileNotFoundError:
        print("File tidak ditemukan!")
    return data_dict

# ================== KEMBALIKAN ==================
def kembalikan_kendaraan(data_dict):
    plat = input("Masukkan plat kendaraan: ")

    if plat in data_dict:
        if data_dict[plat]["status"] == "disewa":
            data_dict[plat]["status"] = "tersedia"
            print("Kendaraan berhasil dikembalikan!")
        else:
            print("Kendaraan tidak sedang disewa.")
    else:
        print("Plat tidak ditemukan.")



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