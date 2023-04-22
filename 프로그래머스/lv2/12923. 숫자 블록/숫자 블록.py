def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        n = 0 if i == 1 else 1
        for j in range(2, int(i**.5) + 1):
            if i % j == 0:
                if i // j <= 1e7:
                    n = i // j
                    break
                else:
                    n = j
        answer.append(n)
    return answer