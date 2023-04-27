def solution(skill, skill_trees):
    answer = 0
    dic = {s : -1 for s in skill}
    
    if len(skill) == 1: # 스킬 순서가 하나밖에 없으면 무조건 다 가능한 스킬트리이다.
        return len(skill_trees)
    
    for st in skill_trees:
        dic2 = dict(dic)
        
        for i, ch in enumerate(skill):
            idx = st.find(ch)
            if idx != -1: # 스킬트리에 스킬이 있을 경우
                if i != 0: 
                    # 현재의 스킬이 이전 스킬보다 앞에 나오거나 이전 스킬이 존재하지 않는데 현재 스킬이 존재하는 경우
                    if dic2[skill[i - 1]] == -1 or dic2[skill[i - 1]] > idx: 
                        break
                dic2[ch] = idx
                
        else:
            answer += 1
    
    return answer