# Praktikum 1 - Adjacency Matrix

def buat_matrix(jumlah_node, sisi):

    # Membuat matrix awal berisi 0
    matrix = []

    for i in range(jumlah_node):
        baris = []

        for j in range(jumlah_node):
            baris.append(0)

        matrix.append(baris)

    # Menambahkan edge / hubungan
    for a, b in sisi:
        matrix[a][b] = 1
        matrix[b][a] = 1   # karena graph tidak berarah

    return matrix


# Jumlah node
node = 4

# Daftar edge
edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 3)
]

# Membuat adjacency matrix
hasil = buat_matrix(node, edges)

# Menampilkan matrix
print("Adjacency Matrix:\n")

for i in hasil:
    for j in i:
        print(j, end=" ")
    print()


# Penjelasan setiap baris
print("\nPenjelasan Matrix:")

print("Baris ke-0 : Node 0 terhubung dengan node 1 dan node 2")
print("Baris ke-1 : Node 1 terhubung dengan node 0 dan node 2")
print("Baris ke-2 : Node 2 terhubung dengan node 0, node 1, dan node 3")
print("Baris ke-3 : Node 3 hanya terhubung dengan node 2")