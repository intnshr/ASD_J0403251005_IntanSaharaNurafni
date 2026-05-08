#==============================
# Nama : Intan Sahara Nurafni
# NIM  : J0403251005
# Praktikum 3 - Konversi Matrix ke List
#==============================

# Adjacency Matrix
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

# Membuat adjacency list kosong
adj_list = {}

# Proses konversi matrix ke adjacency list
for i in range(len(matrix)):

    adj_list[i] = []

    for j in range(len(matrix[i])):

        if matrix[i][j] == 1:
            adj_list[i].append(j)

# Menampilkan hasil adjacency list
print("Adjacency List Representation:\n")

for node in adj_list:

    print(f"{node}:", end=" ")

    for tetangga in adj_list[node]:
        print(tetangga, end=" ")

    print()