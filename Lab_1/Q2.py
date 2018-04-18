#Given an array of ints, return true if 6 appears as either the first
# or last element in the array.
# The array will be length 1 or more.


def firstLast6(A):
	print("Input: ",A)
	if len(A) >= 1:
		if A[0] == 6:
			return True
		if A[len(A)-1] == 6:
			return True
		else:
			return False

firstLast1=([1,2,6],[6,1,2,3],[13,6,1,2,3])

for i in range(len(firstLast1)):
	print("There is 6 at first/last position: ", firstLast6(firstLast1[i]))
