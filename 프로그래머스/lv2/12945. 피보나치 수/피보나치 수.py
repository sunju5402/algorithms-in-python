def solution(n):
    answer = 0
    pre = 0
    nx = 1
    for i in range(n - 1):
        answer = pre + nx
        pre = nx
        nx = answer
    return answer % 1234567