#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)


""" 
input sample:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

output sample: 19

"""

max = -63  # constrain -9<=arr[i][j]<=9
for i in range(1,5):
    for j in range(1,5):
        suma = arr[i][j]+ sum(arr[i-1][j-1:j+2]) + sum(arr[i+1][j-1:j+2])
        if suma > max: max = suma
print (max)
