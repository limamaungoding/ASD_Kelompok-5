# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 
def hitung(n): 
    # Base case 
    if n == 0: 
        print("Selesai") 
        return 
    print("Masuk:", n)      # fase stacking 
    hitung(n - 1)           # pemanggilan rekursif 
    print("Keluar:", n)     # fase unwinding
hitung(3) 