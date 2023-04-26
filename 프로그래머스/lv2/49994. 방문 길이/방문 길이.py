def solution(dirs):
    dic = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    x, y = 0, 0
    s = set()
    
    for d in dirs:
        nx = x + dic[d][0]
        ny = y + dic[d][1]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    
    return len(s) // 2