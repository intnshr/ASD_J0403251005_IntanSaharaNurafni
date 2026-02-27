# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

# Fungsi kombinasi bertujuan untuk menghasilkan semua
# kemungkinan kombinasi huruf "A" dan "B"
# dengan panjang sebanyak n.
#
# Parameter:
# n     -> panjang kombinasi yang diinginkan
# hasil -> string sementara untuk menyimpan kombinasi
#         (default = "" dan akan bertambah setiap rekursi)

def kombinasi(n, hasil=""):

    # =========================
    # Base Case (Kondisi Berhenti)
    # =========================
    # Jika panjang string 'hasil' sudah sama dengan n,
    # maka kombinasi sudah lengkap.
    # Cetak hasil tersebut lalu hentikan rekursi.
    if len(hasil) == n:
        print(hasil)
        return

    # =========================
    # Recursive Case
    # =========================
    # Jika panjang hasil belum mencapai n,
    # maka tambahkan huruf "A" dan lanjutkan rekursi.
    kombinasi(n, hasil + "A")

    # Tambahkan huruf "B" dan lanjutkan rekursi.
    kombinasi(n, hasil + "B")


# =========================
# Diskusi dan Alur Program
# =========================
# Contoh pemanggilan: kombinasi(2)
#
# Langkah rekursi:
#
# kombinasi(2, "")
# → tambah "A" → kombinasi(2, "A")
#     → tambah "A" → kombinasi(2, "AA") → cetak "AA"
#     → tambah "B" → kombinasi(2, "AB") → cetak "AB"
# → tambah "B" → kombinasi(2, "B")
#     → tambah "A" → kombinasi(2, "BA") → cetak "BA"
#     → tambah "B" → kombinasi(2, "BB") → cetak "BB"
#
# Output:
# AA
# AB
# BA
# BB
#
# Konsep yang digunakan adalah rekursi bercabang (tree recursion),
# karena setiap pemanggilan fungsi menghasilkan dua cabang baru.

kombinasi(2)