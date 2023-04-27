from itertools import combinations

def solution(relation):
    col = len(relation[0])
    lst = [i for i in range(col)]
    com = [c for i in range(1, len(lst) + 1) for c in list(combinations(lst, i))] # 속성에 대한 조합
    
    ck_com = set() # 후보키가 될 수 있는 조합
    for c in com:
        s = set()
        for ck in ck_com:
            if set(ck).issubset(set(c)): # 최소성 검증
                break
        else :
            for r in relation:
                l = []
                for i in c:
                    l.append(r[i])
                s.add(tuple(l))
        
            if len(s) == len(relation): # 유일성 검증
                ck_com.add(c)
                
    return len(ck_com)