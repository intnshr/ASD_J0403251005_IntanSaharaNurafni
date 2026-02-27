# ==========================================================
# Nama  : Intan Sahara Nurafni
# NIM   : J0403251005
# Kelas : TPL A2
# Latihan 1 : Rekursi Pangkat
# ==========================================================

# Fungsi untuk menghitung a^n dengan rekursi
def pangkat(a, n):

    # Base case: kalau n = 0, hasilnya 1
    # karena a^0 = 1
    if n == 0:
        return 1

    # Recursive case:
    # a^n = a * a^(n-1)
    return a * pangkat(a, n - 1)


# Penjelasan singkat:
# pangkat(2,4)
# = 2 * pangkat(2,3)
# sampai akhirnya pangkat(2,0) = 1
# lalu hasilnya dikalikan kembali ke atas menjadi 16

print(pangkat(2, 4))  # Output: 16