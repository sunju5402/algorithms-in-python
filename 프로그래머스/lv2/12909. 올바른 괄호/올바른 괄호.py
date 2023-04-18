def solution(s):
    stack = []
    for ch in s:
        if stack:
            if ch == '(':
                stack.append(ch)
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        else:
            stack.append(ch)
    return len(stack) == 0 