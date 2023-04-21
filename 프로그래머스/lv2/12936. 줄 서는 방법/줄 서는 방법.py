import math
        
def solution(n, k):
    result = []
    lst = [i for i in range(1, n + 1)]
    
    while n != 0:
        cnt = math.factorial(n - 1) # 첫번째 자리를 제외하고 나머지 자리의 경우의 수 1, x, x -> 2 * 1  
        idx = k // cnt
        k %= cnt
        
        if k == 0:
            result.append(lst.pop(idx - 1))
        else:
            result.append(lst.pop(idx))
            
        n -= 1
        
    return result
    
    