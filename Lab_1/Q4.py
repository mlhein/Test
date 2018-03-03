#Using a linear search, write a program that takes in an integer and search an array of size 100 that contain random numbers between 1-­‐ 1000.
#If the search is successful (number is in the generated array) the output will be the array index number containing the integer;
#else display “Number is not in the array”. Calculate the time complexity of the program.
import random

randomarray = []
i=0


while (i<100):
    randomarray.append(random.randint(1,1000))
    i+=1

print randomarray
i=0
inVar=input("Search your number: ")

while(i<100):
    if(randomarray[i]==inVar):
        print"There is ",inVar,"!\nOn index ",i
        break
    elif(i==99):
        print "There no ",inVar
        break
    i+=1