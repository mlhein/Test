def fibonacciNumber(number):
    if(number == 0):
        return 0
    elif(number <= 1):
        return number
    else:
        return (fibonacciNumber(number - 1) + fibonacciNumber(number - 2))

# Set how many fibonacci number you want.
HowMany = 5
for i in range(HowMany+1):
    print(fibonacciNumber(i), end=' ')
