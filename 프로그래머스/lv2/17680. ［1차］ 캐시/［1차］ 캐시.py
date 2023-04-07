def solution(cacheSize, cities):
    answer = 0
    lst = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for i, city in enumerate(cities):
        if lst and len(lst) == cacheSize:
            if city.lower() in lst:
                lst.remove(city.lower())
                answer += 1
            else:
                lst.pop(0)
                answer += 5
        else:
            if city.lower() in lst:
                lst.remove(city.lower())
                answer += 1
            else:
                answer += 5
        lst.append(city.lower())
    return answer