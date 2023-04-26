from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    op = set()
    stack = []
    n = ""
    for ch in expression:
        if ch.isdigit():
            n += ch
        else:
            stack.append(int(n))
            stack.append(ch)
            n = ""
            op.add(ch)
    stack.append(int(n))
    
    
    for p in list(permutations(op, len(op))):
        lst = deque(stack)
        for i in p:
            lst2 = deque()
            while lst:
                o = lst.popleft()
                if o == i:
                    if i == "*":
                        lst2.append(lst2.pop() * lst.popleft())
                    elif i == "+":
                        lst2.append(lst2.pop() + lst.popleft())
                    else:
                        lst2.append(lst2.pop() - lst.popleft())
                else:
                    lst2.append(o)
            lst = lst2   
        answer = max(answer, abs(lst[-1]))
    return answer