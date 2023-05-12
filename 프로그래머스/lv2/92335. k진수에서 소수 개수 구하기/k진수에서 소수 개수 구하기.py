def solution(n, k):
    answer = 0
    s = ""
    while n > 0: # 10진수 -> k진수
        s = str(n % k) + s
        n //= k
        
    lst = s.split("0") 
    for a in lst:
        if a.isdigit():
            a = int(a)
            for i in range(2, int(a**.5) + 1):
                if a % i == 0:
                    break
            else:
                if a != 1:
                    answer += 1
    
    return answer