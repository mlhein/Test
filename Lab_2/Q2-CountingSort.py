#counting sort algorithm


def countSort(arr):
    newArray = [0] * (max(arr)+1)
    for a in arr:
        newArray[a]+=1
    i = 0
    for a in range((max(arr)+1)):
        for c in range(newArray[a]):
            arr[i] = a
            i += 1
    return (arr)


array1=([4,29,2,2,110,99,5])
print countSort(array1)