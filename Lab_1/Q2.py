#Given an array of ints, return true if 6 appears as either the first
# or last element in the array.
# The array will be length 1 or more.

firstLast1=([1,2,6])
firstLast2=([6,1,2,3])
firstLast3=([13,6,1,2,3])
i=0
print("Array list no. 1")
if(firstLast1[i]==6):
    print("There is 6 at first position (TRUE)")
elif(firstLast1[len(firstLast1)-1]==6):
    print("There is 6 at last position (TRUE)")
else:
    print("No 6 at first/last position (FALSE)")

print("\nArray list no. 1")
if(firstLast2[i]==6):
    print("There is 6 at first position (TRUE)")
elif(firstLast2[len(firstLast2)-1]==6):
    print("There is 6 at last position (TRUE)")
else:
    print("No 6 at first/last position (FALSE)")

print("\nArray list no. 1")
if(firstLast3[i]==6):
    print("There is 6 at first position (TRUE)")
elif(firstLast3[len(firstLast3)-1]==6):
    print("There is 6 at last position (TRUE)")
else:
    print("No 6 at first/last position (FALSE)")