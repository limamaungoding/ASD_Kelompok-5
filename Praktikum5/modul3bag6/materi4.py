# ========================================================== 
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ========================================================== 
def biner(n, hasil=""): 
    # Base case: jika panjang string sudah n, cetak hasil 
    if len(hasil) == n: 
        print(hasil) 
        return    
    # Choose + Explore: tambah '0' 
    biner(n, hasil + "0") 
    
    # Choose + Explore: tambah '1' 
    biner(n, hasil + "1") 
biner(3)