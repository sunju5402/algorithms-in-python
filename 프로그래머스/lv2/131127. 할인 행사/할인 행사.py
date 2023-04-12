def solution(want, number, discount):
    answer = 0
    dic = {}
    for d in discount:
        if d not in dic:
            dic[d] = 1
        else:
            dic[d] += 1

    lst = [discount.index(w) for w in want if w in dic]
    
    if len(lst) != len(want):
        return 0

    min_idx = min(lst)
    for i in range(min_idx, len(discount) - 9):
        l = discount[i:i + 10]
        same = True
        for j in range(len(want)):
            cnt = l.count(want[j])
            if cnt < number[j]:
                same = False
                break
        
        if same:
            answer += 1
    
    return answer