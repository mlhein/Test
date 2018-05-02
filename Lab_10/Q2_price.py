# A	= [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Given	an	array	of	prices	A	=	[1	5	8	9	10	17	17	20	24	30] where	price	at	each
# index	is	the	price	obtained	by	selling	rod	of	length	equal	to	that	index. Write	a
# program	that	calculate	the	maximum	price	which	can	be	obtained	by	selling
# pieces	of	that	rod.
# A Naive recursive solution
# for Rod cutting problem
# A Dynamic Programming solution for Rod cutting problem
INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cutRod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
    return val[n]

# Driver code
A = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print cutRod(A, len(A))
