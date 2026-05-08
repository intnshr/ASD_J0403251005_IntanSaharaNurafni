#==============================
#Nama : Intan Sahara Nurafni
#NIM : J0403251005
#Praktikum 2 - Adjacency List
#==============================
#Praktikum 2 - Adjacency List 

def buat_adj_list(node, edges):

    # Membuat dictionary kosong
    graph = {}

    # Membuat key untuk setiap node
    for n in node:
        graph[n] = []

    # Menambahkan hubungan antar node
    for awal, tujuan in edges:
        graph[awal].append(tujuan)
        graph[tujuan].append(awal)   # undirected graph

    return graph


# Daftar node
nodes = ["A", "B", "C", "D"]

# Hubungan antar node
hubungan = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D")
]

# Membuat adjacency list
hasil_graph = buat_adj_list(nodes, hubungan)

# Menampilkan hasil
print("Adjacency List:\n")

for key in hasil_graph:
    print(key, "->", end=" ")

    for value in hasil_graph[key]:
        print(value, end=" ")

    print()