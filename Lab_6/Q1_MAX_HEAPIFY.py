
def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)

def heapSort(A):
    build_max_heap(A)
    for i in range(len(A) // 2):
        A[1] = A[i]
        len(A) = len(A) - 1
        max_heapify(A, left)

def heap_maximum(A):
    return A[1]

def heap_extract_max(A):
    if len(A)< left:
        print("Heap underflow")
    max = A[1]
    A[1] = A[len(A)]
    len(A) = len(A) - 1
    max_heapify(A, 1)
    return max

def heap_increase_key(A, i, key):
    if key < A[i]:
        print("New key is smaller than current key")
    A[i] =  key
    while i > 1 and A[] <A[i]:

def max_heap_insert(A, key):
    len(A) = len(A) + 1
    A[len(A)] = -
    heap_increase_key(A, len(A), key)

alist = ([11, 4, 74, 55, 3, 17, 8, 46, 43, 33])
print("Unsorted array: ", alist)
build_max_heap(alist)
print('Sorted array: ', alist)
