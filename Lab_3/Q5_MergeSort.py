# Reference:
# https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
def merge(a, b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort
def mergeSort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = mergeSort(x[:middle])
        b = mergeSort(x[middle:])
        return merge(a,b)

alist = ([54, 26, 93, 17, 77, 31, 44, 55, 20])
print "Before: ", alist,"\nAfter: ", mergeSort(alist)
