from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    
    n = sum(q1 + q2)
    if n / 2 != n // 2 or n // 2 < max(q1 + q2): # 두 큐의 합을 같게 만들 수 없는 경우
        return -1
    
    n //= 2 # 같게 만들어야되는 수
    t1, t2 = sum(q1), sum(q2)
    while t1 != n:
        if t1 > t2:
            tmp = q1.popleft()
            q2.append(tmp)
            t1 -= tmp
            t2 += tmp
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            t2 -= tmp
            t1 += tmp
        answer += 1
        
        if answer > len(queue1) * 4:
            return -1
    return answer