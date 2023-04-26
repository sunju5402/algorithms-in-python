from collections import deque

def solution(maps):
    dx = [0, 0, 1, -1] # 동서남북
    dy = [1, -1, 0, 0]
    
    q = deque()
    q.append((0, 0))
    
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for i in range(m)] for i in range(n)]

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽을 만나는 경우
            if maps[nx][ny] == 0:
                continue
            if not visited[nx][ny] and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    return -1 if maps[n - 1][m - 1] == 1 else maps[n - 1][m - 1]