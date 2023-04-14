def solution(k, ranges):
    answer = []
    
    k_list = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k *= 3
            k += 1
        k_list.append(k)
    
    k_area = []
    for i in range(1, len(k_list)):
        mi = min(k_list[i], k_list[i - 1])
        ma = max(k_list[i], k_list[i - 1])
        k_area.append(mi + (ma - mi) / 2)
        
    for i in range(len(ranges)):
        end = len(k_area) + ranges[i][1]
        if ranges[i][0] > end:
            answer.append(-1)
        else:
            answer.append(sum(k_area[ranges[i][0]:end]))
    
    return answer