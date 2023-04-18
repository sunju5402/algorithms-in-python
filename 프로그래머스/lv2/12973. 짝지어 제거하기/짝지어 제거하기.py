def solution(s):
    stack = []
    for ch in s:
        if stack:
            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        else:
             stack.append(ch)   
    return 0 if stack else 1 