from heapq import heappop, heappush

def solution(n, k, enemy):
    answer = 0
    total = 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e) # 최대힙
        total += e
        
        if total > n:
            if k == 0: 
                break
            h = heappop(heap) 
            total += h
            k -= 1
            
        answer += 1
    return answer