from collections import deque

def solution(dirs):
    answer = 0
    q = deque()
    x, y = 0, 0
    nx, ny = 0, 0

    for d in dirs:
        if d == "U":
            ny = y + 1 
        elif d == "D":
            ny = y - 1 
        elif d == "R":
            nx = x + 1
        else:
            nx = x - 1
            
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            nx, ny = x, y
            continue
        
        if (x, y, nx, ny) not in q and (nx, ny, x, y) not in q:
            q.append((x, y, nx, ny))
            answer += 1
            
        x, y = nx, ny
    
    return answer