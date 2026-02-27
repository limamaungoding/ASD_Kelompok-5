#Tujuan: Memahami base case dan recursive case. 
#Instruksi: Buat fungsi rekursif untuk menghitung nilai pangkat. 
# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# Hakashi Yumiko  Masfat J0403251023 TPL A2
# ========================================================== 

def pangkat(a, n): 
    # Base case 
    if n == 0: 
        return 1 
    # Recursive case 
    return a * pangkat(a, n - 1) 
print(pangkat(2, 4))  # Output: 16 

#Diskusi dan jelaskan alur program serta base case dan recursive call.
#jawab: 
# 1. base case
# terletak di baris if n == 0:
#                        return  1
# ini titik fungsi berhentu memanggil dirinya sendiri,
# karena bilangan apapun yang pangkanya 0 hasilnya 1.
# kalo gaada kondisi ini, fungsi akan terus berjalan (looping)
# sampai menyebabkan error stack overflow 

# 2. recursive call
# terletak di baris return a * pangkat (a,n-1)
# fungsi memanggil dirinnya sendiri dengan mengurangi nilai n sebesar 1
# setiap langkahnya, sampai n mencapai 0, yaitu base casenya

# 3. alur program
# programnya bekerja dengan menumpuk pemanggilan fungsi dalam memori
# misal pada pangkat (2,4) alurnya 2 * pangkat(2,3) -> 2 * pangkat(2,2)
# -> 2 * pangkat(2,1) -> 2 * pangkat(2,0) trus mengembalikan nilai 1
# lalu dikali mundur ke atas 1x2=2 -> 2x2=4 -> 4x2=8 -> 8x2=16