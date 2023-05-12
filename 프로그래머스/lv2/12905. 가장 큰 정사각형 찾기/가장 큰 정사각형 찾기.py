def solution(board):
    answer = 0
    
    dx = [0, -1, -1] # 왼쪽, 위, 대각선 위
    dy = [-1, 0, -1]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                answer = max(answer, 1)
                n = 10001
                for k in range(3):
                    nx, ny = i + dx[k], j + dy[k]
            
                    if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[i]):
                        break
                    if board[nx][ny] == 0:
                        break
                    n = min(n, board[nx][ny])
                else:
                    board[i][j] += n
                    answer = max(answer, board[i][j])
    return answer ** 2