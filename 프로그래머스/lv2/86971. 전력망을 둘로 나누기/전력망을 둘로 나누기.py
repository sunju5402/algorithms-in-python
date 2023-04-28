# from collections import deque

# def bfs(start, graph):
#     q = deque([start])
#     visited = [0] * (len(graph) + 1)
#     visited[start] = 1
#     cnt = 1
#     while q:
#         v = q.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = 1
#                 cnt += 1
#     return cnt
    
# def solution(n, wires):
#     answer = n
#     graph = [[] for _ in range(n + 1)]
#     for a, b in wires:
#         graph[a].append(b)
#         graph[b].append(a)
        
    
#     for a, b in wires:
#         graph[a].remove(b)
#         graph[b].remove(a)
        
#         answer = min(abs(bfs(a, graph) - bfs(b, graph)), answer)
        
#         graph[a].append(b)
#         graph[b].append(a)
    
#     return answer

def solution(n, wires):
    parent = [i for i in range(n + 1)]
    
    def find_parent(parent, x):
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    
    answer = n
    for i in range(len(wires)):
        p2 = list(parent)
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            union_parent(p2, a, b)
        
        for a, b in wires:
            p2[a] = find_parent(p2, a)
            p2[b] = find_parent(p2, b)
            
        answer = min(abs(p2.count(p2[wires[i][0]]) - p2.count(p2[wires[i][1]])), answer)
        
    return answer