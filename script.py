nama_file ="data_kendaraan.txt"

# Baca file ##Bagian Lima
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

# --- CEK KETERSEDIAAN (PART LIMAAA)---
def cek_ketersediaan(data):
    print("\n=== Cek Ketersediaan ===")
    search = input("Input ID (Plat) atau Nama Kendaraan: ").lower()
    found = False
    
    for plat, info in data.items():
        if search == plat.lower() or search in info['nama'].lower():
            found = True
            # YES OR NAUUU
            if info['status'] == "Tersedia":
                print(f"[YA] {info['nama']} ({plat}) berstatus TERSEDIA.")
            else:
                print(f"[TIDAK] {info['nama']} ({plat}) sedang DISEWA.")
    
    if not found:
        print("Data kendaraan tidak ditemukan.")

# --- SEWA KENDARAAN (PART LIMAAA)---
def sewa_kendaraan(data):
    print("\n=== Sewa Kendaraan ===")
    plat_input = input("Input ID Kendaraan (Plat): ")
    
    if plat_input in data:
        # Logika Flowchart: Status Tersedia?
        if data[plat_input]['status'] == "Tersedia":
            print("Status: Tersedia. Silahkan lanjut isi data.")
            # Input Data Penyewa
            nama_penyewa = input("Nama Penyewa: ")
            hari = int(input("Lama Sewa (hari): "))
            
            # Hitung Total Biaya
            total_biaya = data[plat_input]['harga'] * hari
            print(f"Total Biaya: Rp{total_biaya}")
            
            # Update Status & Simpan Transaksi (Simulasi)
            data[plat_input]['status'] = "Disewa"
            print(f"Transaksi Berhasil! {data[plat_input]['nama']} sekarang berstatus DISEWA.")
        else:
            # Jalur "Tidak" pada flowchart
            print("Tidak Bisa Disewa (Kendaraan sedang dipakai).")
    else:
        print("ID Kendaraan tidak ditemukan.")

# ================== KEMBALIKAN (Nazla)==================
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


# LAPORAN (NAZLA)

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


# --- MENU SEMENTARAAAA ---
data_kendaraan = baca_data(nama_file)

while True:
    print("\nMenu Utama:")
    print("3. Cek Ketersediaan")
    print("4. Sewa Kendaraan")
    print("0. Keluar")
    pilihan = input("Pilih Menu: ")

    if pilihan == "3":
        cek_ketersediaan(data_kendaraan)
    elif pilihan == "4":
        sewa_kendaraan(data_kendaraan)
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
