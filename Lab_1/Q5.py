#Create aniterative and recursive method to compute the first n numbers in the
# Fibonacci sequence. Calculate the time complexity of the program

from math import sqrt

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

inVar=input("Enter a number (RECURSIVE): ")
print F(inVar)

import sys

table = [0]*1000

def FastFib(n):
    if n<=1:
        return n
    else:
        if(table[n-1]==0):
            table[n-1] = FastFib(n-1)
        if(table[n-2]==0):
            table[n-2] = FastFib(n-2)
        table[n] = table[n-1] + table[n-2]
        return table[n]

def main():
    print('Enter a number (ITERATIVE): ')
    num = int(sys.stdin.readline())
    print(FastFib(num))

if __name__=='__main__':
    main()
