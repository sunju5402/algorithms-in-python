def solution(s):
    answer = ''
    lst = list(map(str, s.lower().split(" ")))
    for x in lst:
        if x == '':
            answer += " "
            continue
        if answer.strip():
            answer += " "
        if x[0].isalpha():
            answer += x[0].upper()
        else:
            answer += x[0]
        answer += x[1:]
    return answer