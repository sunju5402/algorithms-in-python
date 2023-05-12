def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i - 1 >= 0 and j - 1 >= 0 and board[i][j]:
                board[i][j] += min(board[i][j - 1], board[i - 1][j], board[i - 1][j- 1])
            answer = max(answer, board[i][j])
    return answer ** 2 