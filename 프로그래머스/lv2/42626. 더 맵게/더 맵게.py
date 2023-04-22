from heapq import heappop, heappush

def solution(scoville, K):
    answer = 0
    heap = []
    for a in scoville:
        heappush(heap, a)
    
    while len(heap) >= 2:
        if heap[0] >= K: # 제일 작은 게 K 이상일 때
            return answer
        
        s1, s2 =  heappop(heap), heappop(heap)
        new_sco = s1 + s2 * 2
        if new_sco == 0: # 둘 다 0일 때는 더이상 K이상으로 만들 수 없다.
            return -1
        else:
            heappush(heap, new_sco)
            
        answer += 1
    
    return -1 if heap[0] < K else answer # 남은 1개에 대한 검증