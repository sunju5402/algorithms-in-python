def solution(s):
    answer = []
    lst = list(map(str, s.split("},")))
    
    for i in range(len(lst)):
        lst[i] = lst[i].replace("{", "").replace("}", "").split(",")
    
    lst.sort(key=lambda x : len(x))
    
    for a in lst:
        answer.append(list((set(a) - set(answer)))[0])
            
    return [int(a) for a in answer]