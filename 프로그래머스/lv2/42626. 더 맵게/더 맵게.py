from heapq import heappop, heappush

def solution(scoville, K):
    answer = 0
    heap = []
    for a in scoville:
        heappush(heap, a)
    
    while len(heap) >= 2:
        if heap[0] >= K:
            return answer
        
        s1, s2 =  heappop(heap), heappop(heap)
        new_sco = s1 + s2 * 2
        if new_sco == 0:
            return -1
        else:
            heappush(heap, new_sco)    
        answer += 1
    
    return -1 if heap[0] < K else answer