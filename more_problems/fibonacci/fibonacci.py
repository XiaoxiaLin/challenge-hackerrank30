
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


"""
# more fancy way:
 
def mem_fib(n, _cache={}):
    '''efficiently memoized recursive function, returns a Fibonacci number'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n

"""
