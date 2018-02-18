#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numberOfSwaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            numberOfSwaps += 1
            a[j], a[j+1] = a[j+1], a[j]
    if numberOfSwaps == 0:
        break
        
print ("Array is sorted in %d swaps."%numberOfSwaps)
print ("First Element:",a[0])
print ("Last Element:",a[-1])

