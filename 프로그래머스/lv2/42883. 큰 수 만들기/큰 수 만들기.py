def solution(number, k):
    answer = ''
    stack = []
    cnt = 0
    for n in number:
        while stack and stack[-1] < n and cnt < k:
            stack.pop()
            cnt += 1 
        stack.append(n)
        
    if cnt < k:
        stack = stack[:-(k - cnt)]
    return ''.join(stack)