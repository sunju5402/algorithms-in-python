def solution(p):
    answer = ''
    
    if not p:
        return ''
    
    cnt1, cnt2 = 0, 0
    u, v = '', ''
    stack = []
    for ch in p:
        if cnt1 != 0 and cnt1 == cnt2:
            v += ch
        else:
            if ch == "(":
                cnt1 +=1
            else:
                cnt2 += 1
            u += ch
            
            if stack:
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                 stack.append(ch)   
    
    if not stack: # 올바른 괄호 문자열
        return u + solution(v)
    else: # 올바르지 않은 괄호 문자열
        answer += '(' + solution(v) + ')'
        u = u[1:-1]
        for a in u:
            if a == '(':
                answer += ')'
            else:
                answer += '('
    
    return answer