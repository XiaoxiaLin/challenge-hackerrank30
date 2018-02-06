
# https://stackoverflow.com/questions/4935957/fibonacci-numbers-with-an-one-liner-in-python-3/37509291#37509291

memory = {}
def fibonacci(n):
    if n<2:
        return n
    else:
        try: 
            return memory[n]
        except:
            memory[n] = fibonacci(n-1)+fibonacci(n-2)
            return memory[n]
    
n = int(input())
print(fibonacci(n))
