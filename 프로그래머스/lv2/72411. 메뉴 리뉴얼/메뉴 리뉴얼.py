from itertools import combinations

def solution(orders, course):
    answer = []
    
    for n in course:
        dic = {}
        for order in orders: 
            order = sorted(order)
            if n > len(order):
                continue
            
            for c in combinations(order, n):
                menu = ''.join(c)
                if menu in dic:
                    dic[menu] += 1
                else:
                    dic[menu] = 1
                    
        if dic:
            m = max(dic.items(), key = lambda x:x[1])
            for d in dic:
                if m[1] > 1 and dic[d] == m[1]:
                    answer.append(d)
                    
    answer.sort()
    return answer