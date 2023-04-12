def solution(park, routes):
    dx = {"E":0, "W":0, "S":1, "N":-1} 
    dy = {"E":1, "W":-1, "S":0, "N":0}

    x, y = -1, -1
    for i in range(len(park)):
        idx = park[i].find("S")
        if idx > -1:
            x = i
            y = idx
            break
            
    w = len(park[0])
    h = len(park)
    for s in routes:
        op, n = s.split()
        for i in range(1, int(n) + 1):
            curX, curY = x + dx[op] * i, y + dy[op] * i
            if curX < 0 or curX >= h or curY < 0 or curY >= w:
                curX, curY = x, y
                break
            elif park[curX][curY] == 'X':
                curX, curY = x, y
                break
        x, y = curX, curY
    
    return [x, y]