def shellSort(myList):
    gap = len(myList) // 2
    while gap > 0:
        for i in range(gap, len(myList)):
            currentItem = myList[i]
            j = i
            while j >= gap and myList[j - gap] > currentItem:
                myList[j] = myList[j - gap]
                j -= gap
            myList[j] = currentItem
        gap //= 2

    return myList

array1 = ([4, 29, 2, 2, 110, 99, 5])
print(shellSort(array1))
