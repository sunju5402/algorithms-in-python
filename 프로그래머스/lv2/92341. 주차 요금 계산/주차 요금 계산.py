import math
def solution(fees, records):
    answer = []
    dic = {}
    for r in records:
        t, n, s = r.split() # 시간, 차량번호, 상태
        t1, t2 = t.split(":") # 시, 분
        if n in dic:
            dic[n].append(int(t1) * 60 + int(t2))
        else:
            dic[n] = [int(t1) * 60 + int(t2)]
            
    dic = dict(sorted(dic.items())) # 차량번호 오름차순 정렬
    for d in dic:
        time = 0
        size = len(dic[d])
        if size % 2 == 0:
            for i in range(0, len(dic[d]), 2):
                time += (dic[d][i + 1] - dic[d][i])
        else: # 홀수번의 입/출차일 경우
            for i in range(0, len(dic[d]) - 1, 2):
                time += (dic[d][i + 1] - dic[d][i])
            time += 23 * 60 + 59 - dic[d][-1] # 마지막 차량은 출차 기록이 없음.

        if time - fees[0] > 0:  
            answer.append(fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3])
        else: #기본 요금만 내도 되는 경우
            answer.append(fees[1])
            
    return answer