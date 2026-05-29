# Nama : Intan Sahara Nurafni
# NIM : J0403251005
# Kelas : TPL A2
# Praktikum 13 - Latihan 1

# Daftar edge pada graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Salah satu contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Graph awal memiliki lebih banyak edge dan bisa membentuk cycle,
#    sedangkan spanning tree tidak memiliki cycle.
# 2. Karena cycle membuat penggunaan edge menjadi berlebihan.
# 3. Karena spanning tree hanya membutuhkan edge yang diperlukan
#    untuk menghubungkan semua node.