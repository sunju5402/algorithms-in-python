def solution(people, limit):
    cnt = 0
    people.sort()
    p1, p2 = 0, len(people) - 1
    while p1 < p2:
        if people[p1] + people[p2] <= limit:
            p1 += 1
            cnt += 1
        p2 -= 1
        
    return len(people) - cnt

