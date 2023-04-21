def solution(n):
    # answer = [[0, 0] for _ in range(2 * n - 1)]
    
    # for i in range(len(answer)):
    #     if i + 1 <= n - 1:
    #         answer[i][0], answer[i][1] = 1, 2
    #     elif i + 1 == n:
    #         answer[i][0], answer[i][1] = 1, 3
    #     else:
    #         answer[i][0], answer[i][1] = 2, 3
    answer = []
    def hanoi(start, to, mid, n):
        if n == 1:
            answer.append([start, to])
        else:
            hanoi(start, mid, to, n - 1)
            hanoi(start, to, mid, 1)
            hanoi(mid, to, start, n - 1)
    
    hanoi(1, 3, 2, n)
    return answer