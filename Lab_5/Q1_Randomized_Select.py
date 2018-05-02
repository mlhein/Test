# RANDOMIZED-SELECT(A, p, r, i)
# if p == r
# 	return A[p]
# q = RANDOMIZED-PARTITION(A, p, r)
# k = q - p + 1
# if i == k	//the pivot value is the answer
# 	return A[q]
# elseif i < k
# 	return RANDOMIZED-SELECT(A, p, q-1, i)
#	else
#		return RANDOMIZED-SELECT(A, q+1, r, i - k)

from random import randrange

def partition(x, pivot_index = 0):
    i = 0
    if pivot_index !=0: x[0],x[pivot_index] = x[pivot_index],x[0]
    for j in range(len(x)-1):
        if x[j+1] < x[0]:
            x[j+1],x[i+1] = x[i+1],x[j+1]
            i += 1
    x[0],x[i] = x[i],x[0]
    return x,i

def RSelect(x,k):
    if len(x) == 1:
        return x[0]
    else:
        xpart = partition(x,randrange(len(x)))
        x = xpart[0] # partitioned array
        j = xpart[1] # pivot index
        if j == k:
            return x[j]
        elif j > k:
            return RSelect(x[:j],k)
        else:
            k = k - j - 1
            return RSelect(x[(j+1):], k)

x = [11,4,74,55,3,17,8,46,43,33]
newArray = []
print("Unsorted array: ", x)
for i in range(len(x)):
	newArray.append(RSelect(x,i))
print("Sorted array: ", newArray)
print("Min: ",newArray[0])
print("Max: ",newArray[len(x)-1])
print("i = 5: ",newArray[5])
print("i = 8: ",newArray[8])
