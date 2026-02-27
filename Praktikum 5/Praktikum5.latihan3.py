# ==========================================================
# Nama  : Intan Sahara Nurafni
# NIM   : J0403251005
# Kelas : TPL A2
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

# Fungsi untuk mencari nilai terbesar dalam list dengan rekursi
def cari_maks(data, index=0):

    # Base case: jika sudah di elemen terakhir, langsung kembalikan nilainya
    if index == len(data) - 1:
        return data[index]

    # Recursive case: cari maksimum dari sisa elemen
    maks_sisa = cari_maks(data, index + 1)

    # Bandingkan elemen sekarang dengan maksimum sisa
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


# Penjelasan singkat:
# Fungsi akan membandingkan setiap angka dari depan
# dengan maksimum dari sisa list sampai elemen terakhir.
# Contoh [3,7,2,9,5] hasil akhirnya adalah 9.

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))