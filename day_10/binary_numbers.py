#!/bin/python3

import sys

n = int(input().strip())
print (len(max(bin(n)[2:].split('0'))))

"""
Alternative:

print (max(bin(n)[2:].split('0')).count('1'))
print (max([len(x) for x in '{0:b}'.format(n).split('0')]))
"""
