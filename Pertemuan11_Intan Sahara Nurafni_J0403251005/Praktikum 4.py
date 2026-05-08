#==============================
# Nama : Intan Sahara Nurafni
# NIM  : J0403251005
# Kelas : TPL A2
# Praktikum 4 - Jaringan Komputer
#==============================

nodes = ["Router", "Switch", "PC1", "PC2", "Server"]

graph = {
    "Router": ["Switch"],
    "Switch": ["Router", "PC1", "PC2", "Server"],
    "PC1": ["Switch", "PC2"],
    "PC2": ["Switch", "PC1", "Server"],
    "Server": ["Switch", "PC2"]
}

matrix = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

print("Nama Node:")
for i in range(len(nodes)):
    print(i, "=", nodes[i])

print("\nAdjacency List:")
for node in graph:
    print(node, "->", graph[node])

print("\nAdjacency Matrix:")
for row in matrix:
    print(row)

print("\nHubungan Antar Node:")
print("Router <-> Switch")
print("Switch <-> PC1")
print("Switch <-> PC2")
print("Switch <-> Server")
print("PC1 <-> PC2")
print("PC2 <-> Server")