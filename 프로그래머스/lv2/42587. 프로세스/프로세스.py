from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    
    for i, p in enumerate(priorities):
        q.append((p, i))   
    
    while q:
        m = max(q, key=lambda x : x[0])
        while q:
            val = q.popleft()
            if m[0] == val[0]:
                answer += 1
                if m[1] == location:
                    return answer
                break
            else:
                q.append(val) 
    return answer