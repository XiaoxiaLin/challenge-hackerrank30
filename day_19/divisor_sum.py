import math
import numpy

def divisorGenerator1(n):
    divisor = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n%i == 0: 
            divisor.append(i)
            if i*i!=n:
                divisor.append(int(n/i))
    #print (sorted(divisor))
    return sum(divisor)

print ("sum of all the divisors of 6 is: ", divisorGenerator1(6))
print ("sum of all the divisors of 100 is: ",divisorGenerator1(100))
