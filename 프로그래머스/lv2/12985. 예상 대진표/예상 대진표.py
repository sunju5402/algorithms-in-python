import math
def solution(n,a,b):
    answer = 0
    while True:
        if a == b:
            break
        
        if a % 2 == 0:
            a //= 2
        else:
            a += 1
            a //= 2
        
        if b % 2 == 0:
            b //= 2
        else:
            b += 1
            b //= 2
        answer += 1
    return answer