def solution(s):
    answer = []
    lst = list(map(str, s.split("},")))
    
    for i in range(len(lst)):
        lst[i] = lst[i].replace("{", "")
        lst[i] = lst[i].replace("}", "")
        lst[i] = lst[i].split(",")
    
    lst.sort(key=lambda x : len(x))
    
    for a in lst:
        for b in answer:
            a.remove(b)
        answer.append(a[0])
            
    return [int(a) for a in answer]