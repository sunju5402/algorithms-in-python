def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    answer = 0
    s = set()
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                if not board[i][j]: # 빈 블록일 경우
                    continue
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    s.add((i, j))
                    s.add((i + 1, j))
                    s.add((i, j + 1))
                    s.add((i + 1, j + 1))
        
        if s:
            answer += len(s)
            for i, j in s:
                board[i][j] = []
            s = set()
        else: # 아예 겹치는 게 없을 때 반환한다.
            return answer
        
        # 겹치는 걸 지웠을 때 빈 블록을 채우기 위해 블록을 내린다.
        while True:
            move = False
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and not board[i + 1][j]:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        move = True
            if not move:
                break
                
    return answer