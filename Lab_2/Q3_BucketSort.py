# Bucket sort
# I dont know

from insertion_sort import insertionSort
import math

DEFAULT_BUCKET_SIZE = 5

def bucketSort(myList, bucketSize=DEFAULT_BUCKET_SIZE):
    if(len(myList) == 0):
        print('You don\'t have any elements in array!')

    minValue = myList[0]
    maxValue = myList[0]

    # For finding minimum and maximum values
    for i in range(0, len(myList)):
        if myList[i] < minValue:
            minValue = myList[i]
        elif myList[i] > maxValue:
            maxValue = myList[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(myList)):
        buckets[math.floor((myList[i] - minValue) / bucketSize)].append(myList[i])

    # Sort buckets and place back into input array
    sortedArray = []
    for i in range(0, len(buckets)):
        insertionSort(buckets[i])
        for j in range(0, len(buckets[i])):
            sortedArray.append(buckets[i][j])

    return sortedArray

array1 = ([4, 29, 2, 2, 110, 99, 5])
print(bucketSort(array1))
