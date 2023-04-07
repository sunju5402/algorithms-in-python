from itertools import combinations

def solution(clothes):
    answer = 1
    dic = {}

    for clothe in clothes:
        if clothe[1] not in dic:
            dic[clothe[1]] = []
        dic[clothe[1]].append(clothe[0])

    for key in dic:
        answer *= len(dic[key]) + 1
    
    return answer - 1 # 모두 안 입은 경우

    # 1번 시간 초과
    # answer = len(clothes)
    # for i in range(2, len(dic)):
    #     for c in combinations(dic, i):
    #         cnt = 1
    #         for key in c:
    #             cnt *= len(dic[key]) 
    #         answer += cnt