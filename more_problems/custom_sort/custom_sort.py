from collections import Counter
from operator import itemgetter, attrgetter

def freq_sort_1(arr):
    '''
    A Counter is a dict subclass for counting hashable objects.
    most_common([n]): Return a list of the n most common elements and their counts from the most common to the least.
    '''
    counter=Counter(arr)
    com = sorted(counter.most_common(), key=itemgetter(1,0), reverse=False)
    print (com)
    com = map(lambda x: [x[0]] * x[1], com)
    return [item for sublist in com for item in sublist]

def freq_sort_2(l):
    '''
    Same as freq_sort_1() function. 
    The collections.Counter method most_common()returns the pairs (value, frequency) sorted by frequency.
    '''
    c = Counter(l)
    sc = sorted(c.most_common(), key=lambda x: (x[1], x[0])) # sorting happens here
    print (sc)
    sl = [([v] * n) for (v, n) in sc]
    print (sl)
    ss = sum(sl, [])
    return ss


def freq_sort_3(L):
    '''
    Doing two sorts is often faster than the extra overhead of a lambda function.
    This works because Python's sort is stable
    '''
    c = Counter(L)
    return sorted(sorted(L), key=c.get, reverse=False)

def main():
    lista = [4,2,3,1,3,1,8,1]
    print ("\n\nmi lista es: ", lista)

    print ("\nfunction 1: ")
    print (freq_sort_1(lista))

    print ("\nfunction 2: ")
    print (freq_sort_2(lista))

    print ("\nfunction 3: ")
    print (freq_sort_3(lista))

if __name__ == "__main__":
    main()
