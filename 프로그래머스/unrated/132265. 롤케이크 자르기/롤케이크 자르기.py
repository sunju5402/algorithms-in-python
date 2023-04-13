from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    s = set()
    
    for t in topping:
        dic[t] -= 1
        s.add(t)
        
        if dic[t] == 0:
            dic.pop(t)
        
        if len(dic) == len(s):
            answer += 1
            
    return answer