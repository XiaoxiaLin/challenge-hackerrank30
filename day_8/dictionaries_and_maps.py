#!/bin/python3

n = int(input().strip())
phonebook = {}
for i in range(n):
    line = input()
    k, v = line.split()
    phonebook[k] = v

while True:
    try:
        number = input()
    except EOFError:
        break
    if number in phonebook:
        print("{}={}".format(number, phonebook[number]))
    else:
        print("Not found")


"""
# my version:

d = {}
for i in range(int(input())):
    k, v = input().split()
    d[k] = v
while True: 
    try:
        name = input()
        if name in d:
            print ('%s=%s' % (name, d[name]))
        else:
            print('Not found')
    except:
        break


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
