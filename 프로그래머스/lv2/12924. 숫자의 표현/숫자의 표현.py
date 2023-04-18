def solution(n):
    answer = 1
    total = 0
    for i in range(1, n // 2 + 1):
        total = i
        for j in range(i + 1, n // 2 + 2):
            total += j
            if total == n:
                answer += 1
            elif total > n:
                break
    return answer