def solution(s):
    answer = [0, 0]
    
    while s != '1':
        size = len(s)
        s = s.replace('0', '')
        answer[1] += size - len(s)
        
        s = bin(len(s))[2:]
        answer[0] += 1
    return answer