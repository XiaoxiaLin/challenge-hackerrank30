#!/bin/python3

import sys

n = int(input().strip())
for i in range(1,11):
   # print (n, "x", i, "=", n*i )
    print("{} x {} = {}".format(n, i, n * i))
