
x = int(input('Enter an integer: '))
y = int(input('Enter another integer: '))
formatStr = '{0} + {1} = {2}; {0} * {1} = {3}.'
equations = formatStr.format(x, y, x+y, x*y)
print(equations)



a = set(input('Enter a list:' ).split())
b = set(input('Enter a list:' ).split())
print (a, "\n", b)

print (*sorted(a^b, key=int), sep = "\n")
