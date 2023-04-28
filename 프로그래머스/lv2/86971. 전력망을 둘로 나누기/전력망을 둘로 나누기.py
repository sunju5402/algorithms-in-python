from collections import deque

def bfs(start, graph):
    q = deque([start])
    visited = [0] * (len(graph) + 1)
    visited[start] = 1
    cnt = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt
    
def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(a, graph) - bfs(b, graph)), answer)
        
        graph[a].append(b)
        graph[b].append(a)
    
    return answer