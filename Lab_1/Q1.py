sum1 = ([1,2,3])
sum2 = ([5,11,2])
sum3 = ([7,0,0])
total1=0
total2=0
total3=0
i=0

while(i<len(sum1)):
   total1+=sum1[i]
   total2+=sum2[i]
   total3+=sum3[i]
   i+=1

print "Total sum1 is",total1,"\nTotal sum2 is",total2,"\nTotal sum3 is",total3,