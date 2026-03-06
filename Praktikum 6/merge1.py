#=========================
#MERGE SORT ASCENDING
#=========================

def mergeSortAscending(data):
    if len(data) > 1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]

        mergeSortAscending(lefthalf)
        mergeSortAscending(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
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


data = [54,26,93,17,77,31,44,55,20]
mergeSortAscending(data)
print("Ascending :", data)
    