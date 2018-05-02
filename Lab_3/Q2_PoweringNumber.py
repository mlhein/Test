import math

def powerNumber(number,power):
    total = 0
    if (power>=0):
        #if power is even number
        if(power%2 == 0):
            print("even")
            total = pow(number,(power/2)) * pow(number,(power/2))
        else: #if power is odd
            print("odd")
            total = pow(number, ((power-1) / 2)) * pow(number, ((power-1) / 2)) * number
        return total
    else:
        return "Power must be positive"

print(powerNumber(10,3))
