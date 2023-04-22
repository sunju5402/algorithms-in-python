from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    q = deque()

    for p, s in zip(progresses, speeds):
        q.append(math.ceil((100 - p) / s))
    
    while q:
        cnt = 1
        day = q.popleft()
        while q and q[0] <= day:
            q.popleft()
            cnt += 1
        answer.append(cnt)
        
    return answer