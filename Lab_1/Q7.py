#Based on 2 array list. compare which list have bigger sum of list.
#Example; ([1,2],[3,4]) -> [3,4]


def biggerTwo(A):
	print("\nInput: ",A)
	if(sum(A[0])>sum(A[1])):
		return A[0]
	elif(sum(A[0])==sum(A[1])):
		print ("Both are equally")
	else:
		return A[1]

bTwo = ([[1,2],[3,4]],[[3,4],[1,2]],[[1,1],[1,2]])
for i in range(len(bTwo)):
	print("Bigger is ", biggerTwo(bTwo[i]))
