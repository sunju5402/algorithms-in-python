import math
def solution(n):
    answer = ''
    tmp = "124"
    
    while n > 0:
        if n % 3 == 0:
            answer = tmp[2] + answer
            n //= 3
            n -= 1
        else:
            answer = tmp[n % 3 - 1] + answer
            n //= 3
    
    return answer