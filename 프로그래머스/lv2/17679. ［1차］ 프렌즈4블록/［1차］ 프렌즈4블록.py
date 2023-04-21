def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    answer = 0
    s = set()
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                ch = board[i][j]
                if not ch:
                    continue
                if board[i + 1][j] == ch and board[i][j + 1] == ch and board[i + 1][j + 1] == ch:
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