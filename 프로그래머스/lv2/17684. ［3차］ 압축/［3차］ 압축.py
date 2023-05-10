def solution(msg):
    answer = []
    dic = {chr(ord('A') + i):i + 1 for i in range(26)}
    
    i = 0
    while i < len(msg): 
        w = msg[i]
        c = w
        for j in range(i + 1, len(msg)):
            c += msg[j]
            if c not in dic:
                break
            else:
                i += 1
                w = c
        answer.append(dic[w])
        dic[c] = len(dic) + 1
        i += 1
        
    return answer