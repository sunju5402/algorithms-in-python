from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for pm in permutations(dungeons, len(dungeons)):
        total = k 
        cnt = 0
        for p in pm:
            if total >= p[0]:
                total -= p[1]
                cnt += 1
        answer = max(answer, cnt)   
    
    return answer