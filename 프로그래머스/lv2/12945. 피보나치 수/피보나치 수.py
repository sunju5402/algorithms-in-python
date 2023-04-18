def solution(n):
    answer = 1
    pre = 1
    for i in range(n - 2):
        pre, answer = answer, pre + answer
    return answer % 1234567