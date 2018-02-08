#!/bin/python3

import sys
import time


def my_factorial(n):
    # Complete this function
    if n <= 1:
        return 1
    else:
        return n* my_factorial(n-1)


if __name__ == "__main__":
    n = int(input("Please input a number that you want to compute the factorial of:  " ).strip())    
    time_0 = time.time()
    factorial = lambda x : 1 if x<=1 else x*factorial(x-1)
    print("\n",factorial(n))
    print("time to compute: %f"%(time.time()-time_0))

    
