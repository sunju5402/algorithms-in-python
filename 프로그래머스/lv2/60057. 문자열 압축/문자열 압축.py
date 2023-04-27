def solution(s):
    answer = 1e9
    
    for i in range(1, len(s) + 1):
        st = ""
        stack = []
        cnt = 1
        for j in range(i, len(s) + 1, i):
            if stack:
                if stack[-1] == s[j - i:j]:
                    cnt += 1
                else:
                    if cnt != 1:
                        st += str(cnt)
                    st += stack.pop()
                    cnt = 1
                    stack.append(s[j - i:j])
            else:
                stack.append(s[j - i:j])
        st += str(cnt) + s[j - i:j] if cnt != 1 else s[j - i:j]
        st += s[j:] if j < len(s) else ""
        answer = min(answer, len(st))
        
    return answer