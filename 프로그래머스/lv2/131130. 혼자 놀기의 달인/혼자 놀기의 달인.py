def solution(cards):
    answer = 0 
    
    for i in range(len(cards)): # box1
        visited1 = [False] * len(cards)
        j = i
        cnt1 = 0
        while visited1[j] == False: 
            visited1[j] = True
            j = cards[j] - 1
            cnt1 += 1
            
        for k in range(i + 1, len(cards)): # box2
            visited2 = list(visited1)
            j = k
            cnt2 = 0
            while visited2[j] == False:
                visited2[j] = True
                j = cards[j] - 1
                cnt2 += 1
                
            answer = max(answer, cnt1 * cnt2)
            
    return answer