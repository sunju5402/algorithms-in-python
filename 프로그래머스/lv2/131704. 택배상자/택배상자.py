def solution(order):
    stack = []
    size = len(order)
    i = 1
    idx = 0
    while i < size + 1:
        stack.append(i)
        while stack[-1] == order[idx]:
            idx += 1
            stack.pop()
            if len(stack) == 0:
                break
        i += 1
    return idx