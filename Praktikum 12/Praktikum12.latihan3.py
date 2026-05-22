# ==========================================================
# Nama  : Intan Sahara Nurafni
# NIM   : J0403251005
# Kelas : TPL A2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 3 - Bellman Ford
# ==========================================================

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):

    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    for _ in range(len(graph) - 1):

        for node in graph:

            for neighbor, weight in graph[node].items():

                if distances[node] != float('inf') and \
                   distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# 1. Bobot langsung A ke B adalah 5
# 2. Total bobot jalur A -> C -> B adalah 2
# 3. Jalur melalui C menghasilkan jarak lebih kecil
# 4. Karena Bellman-Ford mampu memproses bobot negatif
# 5. Relaksasi edge adalah proses memperbarui jarak
#    minimum jika ditemukan jalur lebih pendek
# 6. Dijkstra menggunakan greedy sedangkan
#    Bellman-Ford menggunakan relaksasi berulang
# ==========================================================