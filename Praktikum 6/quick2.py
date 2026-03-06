#=========================
#QUICK SORT ASCENDING
#=========================

def quickSortDesc(data):
    quickSortHelperDesc(data,0,len(data)-1)

def quickSortHelperDesc(data,first,last):
    if first < last:
        splitpoint = partitionDesc(data,first,last)

        quickSortHelperDesc(data,first,splitpoint-1)
        quickSortHelperDesc(data,splitpoint+1,last)

def partitionDesc(data,first,last):
    pivotvalue = data[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark


data = [54,26,93,17,77,31,44,55,20]
quickSortDesc(data)
print("Descending :",data)