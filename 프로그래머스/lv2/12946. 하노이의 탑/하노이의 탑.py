def solution(n):
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