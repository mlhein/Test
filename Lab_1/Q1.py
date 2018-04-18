
def sum3(A):
	sumMe = 0
	print("Input array: ",A)
	for i in range(len(A)):
		sumMe += A[i]
	return sumMe

ary1 = ([1,2,3],[5,11,2],[7,0,0])

for i in range(len(ary1)):
	print("Length is ", sum3(ary1[i]))
