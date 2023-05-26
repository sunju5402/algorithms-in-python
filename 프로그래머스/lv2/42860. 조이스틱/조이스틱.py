def solution(name):
    answer = 0

    if len(name) == name.count('A'): # 모두 A일 경우는 이동 필요 없음
        return 0
    
    l = len(name) - 1 # 최대 이동한 경우
    for i, s in enumerate(name):
        answer += min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) # +1은 A -> Z로 움직이는 경우
        
        nxt = i + 1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1
        
        l =  min([l, 2 * i + len(name) - nxt, i + 2 * (len(name) - nxt)]) # 기존, 오른쪽 이동 다 하고 왼쪽으로 확인, 왼쪽 이동 다 하고 오른쪽으로 확인
    
    return answer + l
        