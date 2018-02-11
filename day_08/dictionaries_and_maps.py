#!/bin/python3

d = {}
for i in range(int(input())):
    k, v = input().split()
    d[k] = v
while True: 
    try:
        name = input()
        if name in d:
            #print ('%s=%s' % (name, d[name]))
            print("{}={}".format(name, d[name]))
        else:
            print('Not found')
    except EOFError:
        break


"""
# shorter version:

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break

"""
