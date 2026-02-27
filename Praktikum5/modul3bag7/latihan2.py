# Tujuan: Memahami alur masuk dan keluar fungsi. 
# Instruksi: Jalankan dan amati output program berikut. 
# ========================================================== 
# Latihan 2: Tracing Rekursi 
# Hakashi Yumiko  Masfat J0403251023 TPL A2
# ========================================================== 

def countdown(n): 
    if n == 0: 
        print("Selesai") 
        return 
    print("Masuk:", n) 
    countdown(n - 1) 
    print("Keluar:", n) 
countdown(3) 
 
# Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?
# jawab:
# karena alur programnya LIFO (last in first out), pemanggilan fungsi terakhir
# yang pertama kali diselesaikan. output "keluar" muncul terbalik karena instruksi
# dibawah kode rekursif, jadi pas countdown(3) memanggil countdown(2), perintah 
# print untuk angka 3 disimpen di memori stack dan akan dieksekusi setelah semua
# pemanggilan di bawah (2,1,0) sudah diselesai, saat tumpukan naik lagi, program menjalankan
# sisa instruksi yang tertunda, sehingga angka terakhir yang masuk, jadi pertama keluar