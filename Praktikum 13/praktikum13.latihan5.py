# Nama : Intan Sahara Nurafni
# NIM : J0403251005
# Kelas : TPL A2
# Praktikum 13 - Latihan 5

# Kasus 1: Jaringan Jalan Antar Kota
# Menggunakan algoritma Kruskal

# Data edge (bobot, kota1, kota2)
edges = [
    (5, "Bogor", "Jakarta"),
    (2, "Bogor", "Depok"),
    (3, "Depok", "Jakarta"),
    (6, "Jakarta", "Bandung"),
    (4, "Depok", "Bandung")
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_bobot = 0
connected = set()

# Memilih edge untuk membentuk MST
for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_bobot += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v} = {weight}")

print("\nTotal bobot MST =", total_bobot)

# Jawaban Analisis:
# 1. Kasus yang dipilih adalah Jaringan Jalan Antar Kota.
# 2. Algoritma yang digunakan adalah Kruskal.
# 3. Edge yang dipilih dalam MST:
#    Bogor - Depok = 2
#    Depok - Jakarta = 3
#    Depok - Bandung = 4
# 4. Total bobot MST adalah 9.
# 5. Edge Bogor - Jakarta dan Jakarta - Bandung tidak dipilih
#    karena terdapat jalur lain yang dapat menghubungkan semua
#    kota dengan total bobot yang lebih kecil.