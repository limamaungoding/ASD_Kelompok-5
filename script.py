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
                status = parts[5] if len(parts) > 5 else "Tersedia" #jika ada status, gunakan, jika tidak, default "Tersedia"

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

# --- FITUR 3: CEK KETERSEDIAAN (PART LIMAAA)---
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

# --- FITUR 4: SEWA KENDARAAN (PART LIMAAA)---
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
            # Di sini kamu bisa menambahkan fungsi simpan ke file jika diperlukan
        else:
            # Jalur "Tidak" pada flowchart
            print("Tidak Bisa Disewa (Kendaraan sedang dipakai).")
    else:
        print("ID Kendaraan tidak ditemukan.")

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