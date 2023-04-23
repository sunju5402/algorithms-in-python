def solution(brown, yellow):
    answer = []
    area = brown + yellow
    for i in range(2, int(area**.5) + 1):
        if area % i == 0:
            b = area // i
            if b * 2 + i * 2 - 4 == brown:
                return [b, i]
    return answer