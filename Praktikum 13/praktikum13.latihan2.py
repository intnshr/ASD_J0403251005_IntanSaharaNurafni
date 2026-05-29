# Nama : Intan Sahara Nurafni
# NIM : J0403251005
# Kelas : TPL A2
# Praktikum 13 - Latihan 2

# Data edge (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang masih menghubungkan node baru
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge pertama yang dipilih adalah C-D.
# 2. Karena bobotnya paling kecil dibanding edge lainnya.
# 3. Total bobot MST adalah 6.
# 4. Edge A-B dan A-D tidak dipilih karena semua node sudah terhubung.