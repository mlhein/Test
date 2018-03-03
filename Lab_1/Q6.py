#Given an array length, return an array with the elemtns "rotated left".
#Example [1,2,3] -> [3,2,1]

rorateLeft1=([1,2,3])
rorateLeft2=([5,11,9])
rorateLeft3=([7,0,0])


def shiftleft(array):
    temp = []
    while(len(array)>0):
        temp.append(array.pop())
    return temp

print "Array 1",rorateLeft1,"->",shiftleft(rorateLeft1),"\nArray 2 ",rorateLeft2,"->",shiftleft(rorateLeft2),"\nArray 3 ",rorateLeft3,"->",shiftleft(rorateLeft3)


