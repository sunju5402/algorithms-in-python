from itertools import combinations

def solution(relation):
    col = len(relation[0])
    lst = [i for i in range(col)]
    com = [c for i in range(1, len(lst) + 1) for c in list(combinations(lst, i))]
    
    com_set = list()
    for c in com:
        s = set()
        for cs in com_set:
            if set(cs).issubset(set(c)):
                break
        else :
            for r in relation:
                l = []
                for i in c:
                    l.append(r[i])
                s.add(tuple(l))
        
            if len(s) == len(relation):
                com_set.append(c)
                
    return len(com_set)