def dfs(v, n, computers, visited):
    visited[v] = 1
    
    for i in range(n):
        if not visited[i] and computers[v][i]:
            dfs(i, n, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i, n, computers, visited)
            answer += 1

    return answer
 