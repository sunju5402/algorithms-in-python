def solution(skill, skill_trees):
    answer = 0
    dic = {s : -1 for s in skill}
    
    if len(skill) == 1:
        return len(skill_trees)
    
    
    for st in skill_trees:
        dic2 = dict(dic)
        available = True
        for i, ch in enumerate(skill):
            idx = st.find(ch)
            if idx != -1:
                if i != 0:
                    if dic2[skill[i - 1]] == -1 or dic2[skill[i - 1]] > idx:
                        available = False
                        break
                dic2[ch] = idx
                
        print(dic2)
        if available:
            answer += 1
    
    return answer