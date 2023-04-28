from itertools import product

def solution(word):
    dic = ['A', 'E', 'I', 'O', 'U']
    dic_p = []
    
    for i in range(1, len(dic) + 1):
        for p in list(product(dic, repeat=i)):
            dic_p.append(''.join(p))
    
    dic_p.sort()
        
    return dic_p.index(word) + 1