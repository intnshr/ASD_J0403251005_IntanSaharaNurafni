# Nama : Intan Sahara Nurafni
# NIM : J0403251005
# Kelas : TPL A2
# Praktikum 13 - Latihan 3

import heapq

# Representasi graph berbobot
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge dari node yang baru dikunjungi
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal yang digunakan adalah A.
# 2. Edge pertama yang dipilih adalah A-C.
# 3. Prim memilih edge terkecil yang terhubung ke node yang sudah dikunjungi.
# 4. Total bobot MST adalah 6.
# 5. Prim dimulai dari node awal, sedangkan Kruskal memilih edge terkecil secara global.