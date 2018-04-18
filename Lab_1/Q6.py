#Given an array length, return an array with the elemtns "rotated left".
#Example [1,2,3] -> [3,2,1]

def shiftleft(A):
	print("\nInput: ",A)
	temp = []
	while(len(A)>0):
		temp.append(A.pop())
	return temp

rorateLeft1=([1,2,3],[5,11,9],[7,0,0])
for i in range(len(rorateLeft1)):
	print("Rotated: ", shiftleft(rorateLeft1[i]))
