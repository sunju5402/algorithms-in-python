def solution(n):
    if n <= 2:
        return n

    cur, nxt = 1, 2
    answer = 0
    for i in range(3, n + 1):
        answer = cur + nxt
        cur, nxt = nxt, answer
        
    return answer % 1000000007