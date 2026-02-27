# ========================================================== 
# Contoh Rekursi 3: Menjumlahkan Elemen List 
# ========================================================== 
def jumlah_list(data, index=0): 
    # Base case: jika index sudah mencapai panjang list 
    if index == len(data): 
        return 0 
    # Recursive case: elemen sekarang + jumlah elemen setelahnya 
    return data[index] + jumlah_list(data, index + 1) 
print(jumlah_list([2, 4, 6, 8]))  # Output: 20 