def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        s = s[1:] + s[:1] if i != 0 else s
        
        for j in range(len(s)):
            if stack:
                if s[j] == '(' or s[j] == '{' or s[j] == '[':
                    stack.append(s[j])
                else:
                    if (s[j] == ')' and stack[-1] == '(') or (s[j] == '}' and stack[-1] == '{') or (s[j] == ']' and stack[-1] == '['):
                        stack.pop()
            else:
                stack.append(s[j])
        if not stack:
            answer += 1
    
    return answer