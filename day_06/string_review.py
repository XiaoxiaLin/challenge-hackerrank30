for _ in range(int(input())):
    S = input()
    print(S[::2], S[1::2])
    
"""    
    == long version ==
    odd_ind = [S[o] for o in range(len(S)) if o%2 ==0]
    even_ind = [S[e] for e in range(len(S)) if e%2!=0]
    print ("".join(odd_ind)+" "+"".join(even_ind))
"""  
