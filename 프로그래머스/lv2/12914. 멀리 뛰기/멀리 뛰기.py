import math
def solution(n):
    answer = 1 # 1칸짜리로만 채워졌을 경우
    cnt_2 = n // 2 # n에 들어갈 수 있는 2의 최대 개수
    for i in range(1, cnt_2 + 1):
        cnt_1 = n - i * 2 # 1이 들어갈 수 있는 개수
        if cnt_1 == 0:
            answer += 1
        else:
            answer += math.comb(cnt_1 + i, i)
    return answer % 1234567