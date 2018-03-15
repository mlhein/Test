def fibonacciNumber(number):
    if(number==0):
        return 1
    elif(number==1):
        return 2
    else:
        fibo = (fibonacciNumber(number - 1) + fibonacciNumber(number - 2))
        return (fibo)

print(fibonacciNumber(5))