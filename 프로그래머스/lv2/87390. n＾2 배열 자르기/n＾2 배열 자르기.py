def solution(n, left, right):
    answer = []  
    for i in range(left, right + 1):
        row = i // n + 1 # 행
        col = i % n + 1 # 열
        answer.append(max(row, col))
    return answer