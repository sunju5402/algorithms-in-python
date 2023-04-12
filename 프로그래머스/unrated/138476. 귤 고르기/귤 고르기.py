def solution(k, tangerine):
    answer = 0
    dic = dict()
    
    for t in tangerine:
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1
            
    dic = dict(sorted(dic.items(), key=lambda x : x[1], reverse=True))
    
    for key in dic:
        answer += 1
        k -= dic[key]
        if k <= 0:
            break
            
    return answer