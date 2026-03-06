#=========================
#SOAL
#=========================

def mergeSort(data):
    if len(data) > 1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        # Perbandingan untuk descending
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] >= righthalf[j]:
                data[k] = lefthalf[i]
                i += 1
            else:
                data[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            data[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            data[k] = righthalf[j]
            j += 1
            k += 1


# Data nilai kandidat
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Mengurutkan data
mergeSort(data)

print("Data setelah diurutkan (descending):", data)

# Mengambil 5 nilai tertinggi
lolos = data[:5]

print("Lima skor tertinggi:", lolos)

print("Kandidat yang lolos:")
for i in range(len(lolos)):
    print("Kandidat", i+1, "dengan skor", lolos[i])
    