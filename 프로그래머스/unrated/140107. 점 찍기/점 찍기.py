def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k): # x를 기준으로 
        dt = int((d**2 - x**2)**.5)
        answer += dt // k + 1 # y 개수 구하기
    return answer
    
    '''
    시간초과
        a = 0
        b = 0
        while a <= d:
            x = a * k
            b = 0
            while b <= d:
                y = b * k
                dt = (x**2 + y**2)**.5
                if dt > d:
                    break
                else:
                    answer += 1
                b += 1     
            a += 1
    '''