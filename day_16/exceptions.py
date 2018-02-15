#!/bin/python3

# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer

S = input().strip()

try:
    print (int(S))
except:
    print ("Bad String")
