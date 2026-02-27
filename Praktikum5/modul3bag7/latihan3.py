# Tujuan: Mengolah struktur data menggunakan rekursi. 
# Instruksi: Buat fungsi untuk mencari nilai maksimum. 
# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# Hakashi Yumiko  Masfat J0403251023 TPL A2
# ========================================================== 
def cari_maks(data, index=0): 
    # Base case 
    if index == len(data) - 1: 
        return data[index] 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) 
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        return maks_sisa 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka))

# Diskusi dan jelaskan alur program serta base case dan recursive call.
# jawab:
# 1. base case
# saat kondisi if index == len(data) -1: terpenuhi, saat penanda indeks 
# sudah sampai di elemen terakhir, lalu fungsi akan berenti manggil dirinya sendiri
# dan mengembalikan nilai dari elemen terakhiir ke maksimum sementara

# 2. recursive call
# pada baris maks_sisa = cari_maks(data, index + 1), dimana fungsi memanggil dirinya sendiri
# dengan manaikkan nilai index untuk memeriksa elemen sampai ke ujung. pemanggilan ini menunda
# perbandingan nilai dan menyimpen di memori stack sampai semua elemen sudah diakses

# 3. alur program
# dengan menumpuk seluruh elemen lalu melakukan perbandingan mundur setelah mencapai yang terakhir
# elemen dibandingkan dengan nilai terbesar, dan yang paling besar akan terus di bawa ke
# tumpukan paling atas sampai terakhir
