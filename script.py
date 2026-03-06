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

buka_data = baca_data(nama_file)
print ("Jumlah data terbaca", len(buka_data))