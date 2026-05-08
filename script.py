from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data_kendaraan.txt"
TRANSAKSI_FILE = BASE_DIR / "data_transaksi.txt"

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
                status = parts[5].strip().lower() if len(parts) > 5 else "tersedia"

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

# --- CEK KETERSEDIAAN (PART LIMAAA)---
def cek_ketersediaan(data):
    print("\n=== Cek Ketersediaan ===")
    search = input("Input ID (Plat) atau Nama Kendaraan: ").lower()
    found = False
    
    for plat, info in data.items():
        if search == plat.lower() or search in info['nama'].lower():
            found = True
            # YES OR NAUUU
            if info['status'].lower() == "tersedia":
                print(f"[YA] {info['nama']} ({plat}) berstatus TERSEDIA.")
            else:
                print(f"[TIDAK] {info['nama']} ({plat}) sedang DISEWA.")
    
    if not found:
        print("Data kendaraan tidak ditemukan.")

# --- SEWA KENDARAAN (PART LIMAAA)---
def baca_transaksi(nama_file):
    transaksi = []
    try:
        with open(nama_file, 'r', encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if not baris:
                    continue

                parts = baris.split("|")
                if len(parts) < 8:
                    continue

                transaksi.append({
                    "tanggal": parts[0],
                    "plat": parts[1],
                    "kendaraan": parts[2],
                    "penyewa": parts[3],
                    "hari": int(parts[4]),
                    "harga": int(parts[5]),
                    "total": int(parts[6]),
                    "status": parts[7]
                })
    except FileNotFoundError:
        pass
    return transaksi


def simpan_transaksi(transaksi, nama_file):
    with open(nama_file, 'w', encoding="utf-8") as file:
        for t in transaksi:
            file.write(f"{t['tanggal']}|{t['plat']}|{t['kendaraan']}|{t['penyewa']}|{t['hari']}|{t['harga']}|{t['total']}|{t['status']}\n")


def tambah_transaksi(nama_file, plat, info, penyewa, hari, total_biaya):
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(nama_file, 'a', encoding="utf-8") as file:
        file.write(f"{tanggal}|{plat}|{info['nama']}|{penyewa}|{hari}|{info['harga']}|{total_biaya}|disewa\n")


def update_transaksi_dikembalikan(nama_file, plat):
    transaksi = baca_transaksi(nama_file)

    for t in reversed(transaksi):
        if t["plat"] == plat and t["status"].lower() == "disewa":
            t["status"] = "dikembalikan"
            simpan_transaksi(transaksi, nama_file)
            return True

    return False


def sewa_kendaraan(data, nama_file, transaksi_file):
    print("\n=== Sewa Kendaraan ===")
    plat_input = input("Input ID Kendaraan (Plat): ")
    
    if plat_input in data:
        # Logika Flowchart: Status Tersedia?
        if data[plat_input]['status'].lower() == "tersedia":
            print("Status: Tersedia. Silahkan lanjut isi data.")
            penyewa = input("Nama Penyewa: ")
            try:
                hari = int(input("Lama Sewa (hari): "))
            except ValueError:
                print("Lama sewa harus berupa angka.")
                return
            
            # Hitung Total Biaya
            total_biaya = data[plat_input]['harga'] * hari
            print(f"Total Biaya: Rp{total_biaya}")
            
            # Update Status & Simpan Transaksi
            data[plat_input]['status'] = "disewa"
            simpan_data(data, nama_file)
            tambah_transaksi(transaksi_file, plat_input, data[plat_input], penyewa, hari, total_biaya)
            print(f"Transaksi Berhasil! {data[plat_input]['nama']} sekarang berstatus DISEWA.")
        else:
            # Jalur "Tidak" pada flowchart
            print("Tidak Bisa Disewa (Kendaraan sedang dipakai).")
    else:
        print("ID Kendaraan tidak ditemukan.")

# ================== KEMBALIKAN (Nazla)==================
def tambah_kendaraan(data_dict, nama_file):
    print("\n=== Tambah Kendaraan ===")
    plat = input("Plat Kendaraan: ")
    if plat in data_dict:
        print(f"Plat {plat} sudah terdaftar.")
        return

    jenis = input("Jenis Kendaraan: ")
    nama = input("Nama Kendaraan: ")
    warna = input("Warna Kendaraan: ")
    harga_input = input("Harga Sewa per hari: ")

    try:
        harga = int(harga_input)
    except ValueError:
        print("Harga harus berupa angka.")
        return

    with open(nama_file, 'a', encoding="utf-8") as file:
        file.write(f"{plat},{jenis},{nama},{warna},{harga},tersedia\n")

    data_dict[plat] = {
        "jenis": jenis,
        "nama": nama,
        "warna": warna,
        "harga": harga,
        "status": "tersedia"
    }

    print(f"Kendaraan {nama} ({plat}) berhasil ditambahkan.")


def simpan_data(data_dict, nama_file):
    with open(nama_file, 'w', encoding="utf-8") as file:
        for plat, info in data_dict.items():
            file.write(f"{plat},{info['jenis']},{info['nama']},{info['warna']},{info['harga']},{info['status']}\n")

#BAGIAN YUMIKO
def edit_kendaraan(data_dict, nama_file):
    print("\n=== Ubah Data Kendaraan ===")
    plat = input("Plat Kendaraan yang akan diubah: ")
    if plat not in data_dict:
        print("Plat tidak ditemukan.")
        return

    info = data_dict[plat]
    print(f"Data saat ini: Jenis={info['jenis']}, Nama={info['nama']}, Warna={info['warna']}, Harga={info['harga']}, Status={info['status']}")
    print("Pilih bagian yang ingin diubah:")
    print("1. Jenis")
    print("2. Nama")
    print("3. Warna")
    print("4. Harga")
    print("0. Batal")
    pilihan = input("Pilihan: ")

    if pilihan == "1":
        baru = input(f"Jenis baru [{info['jenis']}]: ") or info['jenis']
        data_dict[plat]['jenis'] = baru
    elif pilihan == "2":
        baru = input(f"Nama baru [{info['nama']}]: ") or info['nama']
        data_dict[plat]['nama'] = baru
    elif pilihan == "3":
        baru = input(f"Warna baru [{info['warna']}]: ") or info['warna']
        data_dict[plat]['warna'] = baru
    elif pilihan == "4":
        harga_input = input(f"Harga baru [{info['harga']}]: ")
        if harga_input.strip():
            try:
                harga = int(harga_input)
            except ValueError:
                print("Harga harus berupa angka.")
                return
        else:
            harga = info['harga']
        data_dict[plat]['harga'] = harga
    elif pilihan == "0":
        print("Edit dibatalkan.")
        return
    else:
        print("Pilihan tidak valid.")
        return

    simpan_data(data_dict, nama_file)
    print(f"Data kendaraan {plat} berhasil diperbarui.")


def kembalikan_kendaraan(data_dict, nama_file, transaksi_file):
    plat = input("Masukkan plat kendaraan: ")

    if plat in data_dict:
        if data_dict[plat]["status"].lower() == "disewa":
            data_dict[plat]["status"] = "tersedia"
            simpan_data(data_dict, nama_file)
            update_transaksi_dikembalikan(transaksi_file, plat)
            print("Kendaraan berhasil dikembalikan!")
        else:
            print("Kendaraan tidak sedang disewa.")
    else:
        print("Plat tidak ditemukan.")


# LAPORAN (NAZLA)

def laporan_tersedia(data_dict):
    print("\n=== Kendaraan Tersedia ===")
    ditemukan = False
    for plat, k in data_dict.items():
        if k["status"].lower() == "tersedia":
            ditemukan = True
            print(plat, "-", k["nama"])
    if not ditemukan:
        print("Tidak ada kendaraan yang tersedia.")


def laporan_disewa(data_dict):
    print("\n=== Kendaraan Disewa ===")
    ditemukan = False
    for plat, k in data_dict.items():
        if k["status"].lower() == "disewa":
            ditemukan = True
            print(plat, "-", k["nama"])
    if not ditemukan:
        print("Tidak ada kendaraan yang sedang disewa.")


def laporan_keuangan(transaksi_file):
    total = 0
    transaksi = baca_transaksi(transaksi_file)

    for t in transaksi:
        total += t["total"]

    print("\n=== Laporan Keuangan ===")
    print("Total Pendapatan: Rp", total)


def laporan_riwayat_transaksi(transaksi_file):
    transaksi = baca_transaksi(transaksi_file)

    print("\n=== Riwayat Transaksi ===")
    if not transaksi:
        print("Belum ada riwayat transaksi.")
        return

    for t in transaksi:
        print(f"{t['tanggal']} - {t['plat']} - {t['kendaraan']} - {t['penyewa']} - {t['hari']} hari - Rp{t['total']} - {t['status']}")


def laporan_transaksi_aktif(transaksi_file):
    transaksi = baca_transaksi(transaksi_file)
    ditemukan = False

    print("\n=== Riwayat Kendaraan Sedang Disewa ===")
    for t in transaksi:
        if t["status"].lower() == "disewa":
            ditemukan = True
            print(f"{t['tanggal']} - {t['plat']} - {t['kendaraan']} - {t['penyewa']} - {t['hari']} hari - Rp{t['total']}")

    if not ditemukan:
        print("Tidak ada transaksi sewa yang masih aktif.")


def menu_laporan(data_dict, transaksi_file):
    while True:
        print("\n=== MENU LAPORAN ===")
        print("1. Kendaraan Tersedia")
        print("2. Kendaraan Disewa Saat Ini")
        print("3. Laporan Keuangan")
        print("4. Riwayat Transaksi")
        print("5. Riwayat Sewa Aktif")
        print("0. Kembali")

        pilih = input("Pilih: ")

        if pilih == "1":
            laporan_tersedia(data_dict)
        elif pilih == "2":
            laporan_disewa(data_dict)
        elif pilih == "3":
            laporan_keuangan(transaksi_file)
        elif pilih == "4":
            laporan_riwayat_transaksi(transaksi_file)
        elif pilih == "5":
            laporan_transaksi_aktif(transaksi_file)
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")


# --- MENU SEMENTARAAAA ---
data_kendaraan = baca_data(DATA_FILE)

while True:
    print("\nMenu Utama:")
    print("1. Tambah Kendaraan")
    print("2. Ubah Data Kendaraan")
    print("3. Cek Ketersediaan")
    print("4. Sewa Kendaraan")
    print("5. Kembalikan Kendaraan")
    print("6. Laporan")
    print("0. Keluar")
    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        tambah_kendaraan(data_kendaraan, DATA_FILE)
    elif pilihan == "2":
        edit_kendaraan(data_kendaraan, DATA_FILE)
    elif pilihan == "3":
        cek_ketersediaan(data_kendaraan)
    elif pilihan == "4":
        sewa_kendaraan(data_kendaraan, DATA_FILE, TRANSAKSI_FILE)
    elif pilihan == "5":
        kembalikan_kendaraan(data_kendaraan, DATA_FILE, TRANSAKSI_FILE)
    elif pilihan == "6":
        menu_laporan(data_kendaraan, TRANSAKSI_FILE)
    elif pilihan == "0":
        break
    else:
        print("Pilihan tidak valid.")
        


# # tambah kendaraan ##Bagian yumiko
# def tambah_kendaraan(nama_file, plat, jenis, nama, warna, harga):
#     """
#     Menambahkan kendaraan baru ke file.
#     """
#     try:
#         data_dict = baca_data(nama_file) #untuk pengecekan duplikat
#     except FileNotFoundError:
#         data_dict = {}

#     if plat in data_dict:  #cek plat sudah ada atau belum
#         print(f"Gagal: Plat {plat} sudah terdaftar.")
#         return data_dict
#     with open(nama_file, 'a', encoding="utf-8") as file:
#         file.write(f"{plat},{jenis},{nama},{warna},{int(harga)}\n")

#     data_dict[plat] = {"jenis": jenis, "nama": nama, "warna": warna, "harga": int(harga)}
    
#     print(f"Berhasil menambahkan kendaraan: {plat}")
#     return data_dict

# if __name__ == "__main__":
#     try:
#         buka_data = baca_data(nama_file)
#         print("Jumlah data awal terbaca:", len(buka_data))
#     except FileNotFoundError:
#         print("File belum ada, akan dibuat saat penambahan data.")
#         buka_data = {}

#     print("Jumlah data terbaca:", len(buka_data))

#     buka_data = tambah_kendaraan(nama_file, "B1234XYZ", "Mobil", "Avanza", "Hitam", 300000)
#     print("Jumlah data sekarang:", len(buka_data))
