#!/bin/python3

import sys

N = int(input().strip())

if N%2!=0 or (N%2==0 and N in range(6,20+1)):
    print ("Weird")
else: 
    print ("Not Weird")
