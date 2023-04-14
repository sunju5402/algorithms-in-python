def solution(sequence, k):
    answer = []
    if k in sequence:
        idx = sequence.index(k)
        return [idx, idx]
    
    p1, p2 = 0, 1
    total = sequence[0] + sequence[1]
    prev_len = len(sequence)
    while p1 < p2 and p2 < len(sequence):
        if total == k:
            cur_len = p2 - p1
            if cur_len == 1:
                return [p1, p2]
            
            if prev_len > cur_len: 
                answer = [p1, p2]
                prev_len = cur_len
                
            total -= sequence[p1]
            p1 += 1
        elif total < k:
            p2 += 1
            if p2 < len(sequence):
                total += sequence[p2]
        else:
            total -= sequence[p1]
            p1 += 1
            
    return answer