cnt = 0
def dfs(n, cur, v1, v2, v3):
    global cnt
    if cur == n:
        cnt += 1
        return

    for i in range(n):
        if v1[i] or v2[cur + i] or v3[cur - i + n - 1]:
            continue
        v1[i] = 1            
        v2[cur + i] = 1
        v3[cur - i + n - 1] = 1
        dfs(n, cur + 1, v1, v2, v3)
        v1[i] = 0
        v2[cur + i] = 0
        v3[cur - i + n - 1] = 0
            
def solution(n):
    v1 = [0] * n
    v2 = [0] * (n * 2 - 1)
    v3 = [0] * (n * 2 - 1)
    dfs(n, 0, v1, v2, v3)
    return cnt