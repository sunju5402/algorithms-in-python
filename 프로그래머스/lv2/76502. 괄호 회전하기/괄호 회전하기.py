def solution(s):
    answer = 0
    
    if len(s) % 2 != 0: # 홀수개의 괄호는 무조건 짝이 안 맞는다.
        return 0
    
    for i in range(len(s)):
        stack = []
        s = s[1:] + s[:1] if i != 0 else s
        
        for j in range(len(s)):
            if s[j] == '(' or s[j] == '{' or s[j] == '[':
                stack.append(s[j])
            else:
                if not stack:
                    break
                if (s[j] == ')' and stack[-1] == '(') or (s[j] == '}' and stack[-1] == '{') or (s[j] == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    break
        else:
            answer += 1
    
    return answer