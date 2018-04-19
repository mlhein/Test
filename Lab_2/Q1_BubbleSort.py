# Bubble sort algorithm

def bubblesort(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if(array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

array1 = ([4, 29, 2, 2, 110, 99, 5])
print(bubblesort(array1))
