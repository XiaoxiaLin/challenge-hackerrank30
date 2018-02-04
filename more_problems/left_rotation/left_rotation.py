
def array_left_rotation(a, n, k):
    lista = [a[k:], a[:k]]
    # https://coderwall.com/p/tszoiq/python-sum-convert-list-of-lists-to-a-list
    return sum(lista, [])
    
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
