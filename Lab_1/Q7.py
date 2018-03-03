#Based on 2 array list. compare which list have bigger sum of list.
#Example; ([1,2],[3,4]) -> [3,4]


def biggerTwo(array1,array2):
    if(sum(array1)>sum(array2)):
        return array1
    elif(sum(array1)==sum(array2)):
        print "Both are equaly"
    else:
        return array2

print "([1,2],[3,4]) -> ",biggerTwo([1,2],[3,4]),"\n([3,4],[1,2]) -> ",\
    biggerTwo([3,4],[1,2]),"\n([1,1],[1,2]) -> ",biggerTwo([1,1],[1,2])