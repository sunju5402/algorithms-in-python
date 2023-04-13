from collections import deque
def solution(order):
    answer = 0
    stack = []
    q = deque(i for i in range(1, len(order) + 1))
    
    for i in range(len(q)):
        if q[0] != order[0]:
            stack.append(q.popleft())
        else:
            q.popleft()
            answer += 1
            break
        
    for i in range(1, len(order)):
        if order[i] < order[i - 1]:
            if stack and order[i] == stack[-1]:
                stack.pop()
                answer += 1
            else:
                break
        else:
            if q and order[i] == q[0]:
                q.popleft()
                answer += 1
            elif q and order[i] > q[0]:
                for j in range(len(q)):
                    if q[0] != order[i]:
                        stack.append(q.popleft())
                    else:
                        q.popleft()
                        answer += 1
                        break
            else:
                break
    
    return answer