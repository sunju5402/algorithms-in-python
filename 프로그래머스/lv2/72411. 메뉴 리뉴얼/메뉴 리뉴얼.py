from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for n in course:
        c = []
        for order in orders: 
            c += combinations(sorted(order), n)
             
        lst = Counter(c).most_common()   # 많이 나온 메뉴 순서대로 정렬
        for a, b in lst:
            if b > 1 and b == lst[0][1]:
                answer.append(''.join(a))
        
    return sorted(answer)