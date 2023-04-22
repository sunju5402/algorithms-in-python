def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        time = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                time += 1
            else:
                time = j - i
                break
        answer.append(time)
    answer.append(0)
    return answer