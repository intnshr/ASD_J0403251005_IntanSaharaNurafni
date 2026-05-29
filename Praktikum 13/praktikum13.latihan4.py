# Nama : Intan Sahara Nurafni
# NIM : J0403251005
# Kelas : TPL A2
# Praktikum 13 - Latihan 4

# Studi kasus jaringan kabel antar gedung

edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge dari biaya terkecil
edges.sort()

mst = []
total_biaya = 0
connected = set()

for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_biaya += weight

        connected.add(u)
        connected.add(v)

print("Jaringan kabel yang dipilih:")
for edge in mst:
    print(edge)

print("Total biaya minimum =", total_biaya)

# Jawaban Analisis:
# 1. Algoritma yang digunakan adalah Kruskal.
# 2. Edge yang dipilih yaitu C-D, A-C, dan B-D.
# 3. Total biaya minimum adalah 6.
# 4. MST cocok karena dapat menghubungkan semua gedung dengan biaya minimum.