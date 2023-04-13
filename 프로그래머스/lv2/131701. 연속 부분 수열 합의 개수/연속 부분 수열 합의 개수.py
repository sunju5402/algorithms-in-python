def solution(elements):
    answer = 0
    s = set(elements)
    e = elements * 2
    
    for i in range(2, len(elements) + 1):
        for j in range(len(e) - i):
            s.add(sum(e[j:j + i]))
    
    return len(s)