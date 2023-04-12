def solution(name, yearning, photo):
    answer = []
    for i in photo:
        total = 0
        for j in i:
            for k in range(len(name)):
                if j == name[k]:
                    total += yearning[k]
                    break
        answer.append(total)
    return answer