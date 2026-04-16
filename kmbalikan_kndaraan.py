nama_file = "data_kendaraan.txt"

# ================== BACA DATA ==================
def baca_data(nama_file):
    data_dict = {}
    with open(nama_file, 'r', encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            plat, jenis, nama, warna, harga = baris.split(",")

            data_dict[plat] = {
                "jenis": jenis,
                "nama": nama,
                "warna": warna,
                "harga": int(harga),
                "status": "tersedia"   # TAMBAHAN
            }
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


