def solution(n):
    if n <= 2:
        return n

    cur, nxt = 1, 2
    for _ in range(3, n + 1):
        cur, nxt = nxt, cur + nxt
        
    return nxt % 1000000007