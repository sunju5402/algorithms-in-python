def convert(num, base):
    tmp = "0123456789ABCDEF"
    a, b = divmod(num, base)
    
    if a == 0:
        return tmp[b]
    return convert(a, base) + tmp[b]

def solution(n, t, m, p):
    answer = ''
    s = '01' # 2진법부터 시작이므로 '01'로 초기화
    
    for i in range(2, m * t):
        s += str(convert(i, n))
    
    while len(answer) < t:
        answer += s[p - 1] # index이므로 -1
        p += m
    
    return answer