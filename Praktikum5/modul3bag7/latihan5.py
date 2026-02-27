# Buatlah program untuk menghasilkan semua kemungkinan PIN 3 digit menggunakan angka 0 sampai 2 dengan teknik backtracking.  
# ========================================================== 
# Studi Kasus: Generator PIN 
# Hakashi Yumiko  Masfat J0403251023 TPL A2
# ========================================================== 
 
def buat_pin(panjang, hasil=""): 
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
    for angka in ["0", "1", "2"]: 
        buat_pin(panjang, hasil + angka) 
buat_pin(3) 
 
# Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?
# jawab:
# kita tambahin kondisi if angka not in hasil sebelum melakukan pemanggilan rekursif
# sengan logika ini, program hanya kan mengeksploarasi angka yang belym pernah digunakan
# dalam kombinasi string hasil, sehingga menghasilkan pin yang unik