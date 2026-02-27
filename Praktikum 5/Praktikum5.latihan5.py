# ==========================================================
# Nama  : Intan Sahara Nurafni
# NIM   : J0403251005
# Kelas : TPL A2
# Studi Kasus: Generator PIN
# ==========================================================

# Fungsi untuk membuat semua kemungkinan PIN
# dengan panjang tertentu dari angka 0, 1, dan 2
def buat_pin(panjang, hasil=""):

    # Base case: jika panjang PIN sudah sesuai,
    # tampilkan hasilnya lalu berhenti
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    # Recursive case:
    # tambahkan setiap angka (0,1,2)
    # lalu lanjutkan rekursi
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)


# Penjelasan singkat:
# buat_pin(3) akan menghasilkan semua kombinasi
# 3 digit dari angka 0,1,2 (total 3^3 = 27 PIN)

buat_pin(3)