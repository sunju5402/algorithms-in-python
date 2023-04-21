'''
    다익스트라 - 최단경로 (음의 간선 x, 하나의 정점에서 다른 모든 정점)
    작은 문제가 큰 문제의 부분 집합에 속함
    하나의 최단 거리를 구할 때 그 이전까지 구했던 최단 거리 정보를 그대로 사용
    현재까지 알고 있던 최단 경로를 계속해서 갱신
'''
from heapq import heappop, heappush

def dijkstra(dist, adj):
    heap = []
    heappush(heap, [0, 1])
    while heap:
        di, town = heappop(heap) # 거리, 마을 번호
        for d, t in adj[town]:
            if di + d < dist[t]:
                dist[t] = di + d
                heappush(heap, [di + d, t])
    
def solution(N, road, K):
    dist = [1e9] * (N + 1)
    dist[1] = 0 # 1번부터 시작하므로 거리는 0
    adj = [[] for _ in range(N + 1)]
    
    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])
        
    dijkstra(dist, adj)
    
    return len([i for i in dist if i <= K])