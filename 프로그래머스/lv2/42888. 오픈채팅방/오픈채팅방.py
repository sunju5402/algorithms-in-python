def solution(record):
    dic = {}
    for r in record:
        s = r.split()
        if len(s) == 3:
            dic[s[1]] = s[2]
            
    answer = []
    for r in record:
        s = r.split()
        word = dic[s[1]]
        if s[0] == "Enter":
            word += "님이 들어왔습니다."
        elif s[0] == "Leave":
            word += "님이 나갔습니다."
        else:
            continue
        answer.append(word)
        
    return answer