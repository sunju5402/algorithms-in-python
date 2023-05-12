import math
def solution(n):
    answer = ''
    tmp = "124"
    
    while n > 0:
        n -= 1
        answer = tmp[n % 3] + answer
        n //= 3
    
    return answer