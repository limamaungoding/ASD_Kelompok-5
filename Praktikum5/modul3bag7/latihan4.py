#Tujuan: Memahami pola choose dan explore. 
#Instruksi: Buat kombinasi huruf A dan B. 
# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# Hakashi Yumiko  Masfat J0403251023 TPL A2
# ========================================================== 

def kombinasi(n, hasil=""): 
    if len(hasil) == n: 
        print(hasil) 
        return 
    kombinasi(n, hasil + "A") 
    kombinasi(n, hasil + "B") 
kombinasi(2) 

#Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan.
#jawab:
# alur program mengikuti pohon biner, dimana setiap level rekursif menggandakan
# jumlah kemungkinan yang ada. jumlah kombinasi yang dihasilkan 2 pangkat n,
# sehingga untuk kombinasi(2) akan dihasilkan 4 kombinasi AA,AB,BA,BB