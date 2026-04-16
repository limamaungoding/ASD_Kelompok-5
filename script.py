nama_file ="data_kendaraan.txt"

# Baca file ##Bagian Lima
def baca_data(nama_file):
    """
    Membaca data mahasiswa dari file.
    Format per baris: plat, jenis, nama, warna, harga
    Output:
    - data_dict (dictionary)
    key = plat
    value = {"jenis": jenis, "nama": nama, "warna": warna, "harga": int(harga)}
    """
    data_dict = {}
    with open(nama_file, 'r', encoding="utf-8") as file:
        for baris in file : 
            baris = baris.strip() #mengambil data perbaris
            plat, jenis, nama, warna, harga = baris.split(",") #ambil data per item data
            data_dict[plat]= {"jenis": jenis, "nama": nama, "warna": warna, "harga": int(harga)} #masukkan dalam dictionary 
    return data_dict

# tambah kendaraan ##Bagian yumiko
def tambah_kendaraan(nama_file, plat, jenis, nama, warna, harga):
    """
    Menambahkan kendaraan baru ke file.
    """
    try:
        data_dict = baca_data(nama_file) #untuk pengecekan duplikat
    except FileNotFoundError:
        data_dict = {}

    if plat in data_dict:  #cek plat sudah ada atau belum
        print(f"Gagal: Plat {plat} sudah terdaftar.")
        return data_dict
    with open(nama_file, 'a', encoding="utf-8") as file:
        file.write(f"{plat},{jenis},{nama},{warna},{int(harga)}\n")

    data_dict[plat] = {"jenis": jenis, "nama": nama, "warna": warna, "harga": int(harga)}
    
    print(f"Berhasil menambahkan kendaraan: {plat}")
    return data_dict

if __name__ == "__main__":
    try:
        buka_data = baca_data(nama_file)
        print("Jumlah data awal terbaca:", len(buka_data))
    except FileNotFoundError:
        print("File belum ada, akan dibuat saat penambahan data.")
        buka_data = {}

    print("Jumlah data terbaca:", len(buka_data))

    buka_data = tambah_kendaraan(nama_file, "B1234XYZ", "Mobil", "Avanza", "Hitam", 300000)
    print("Jumlah data sekarang:", len(buka_data))