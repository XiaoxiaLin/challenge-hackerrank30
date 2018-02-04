#!/bin/python3

# https://www.hackerrank.com/challenges/symmetric-difference/forum/comments/187449
# * unpack the list
# a^b equivalent to a.symmetric_difference(b)

a,b = [set(input('').split()) for _ in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')

''' 
equivalent to: 
_ , M = input(), set(map(int,input().split()))
_ , N = input(), set(map(int,input().split()))
print(*sorted(list(M.symmetric_difference(N))),sep='\n')
''' 
