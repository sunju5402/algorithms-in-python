from collections import deque

def solution(bridge_length, weight, truck_weights):
    wait = deque(truck_weights)
    q = deque()
    reserve = deque([bridge_length] * len(truck_weights))
    
    time, total = 0, 0
    while reserve:
        if reserve[0] == 0:
            total -= q.popleft()
            reserve.popleft()
        
        if wait and len(q) <= bridge_length and total + wait[0] <= weight:
            total += wait[0]
            q.append(wait.popleft())
        
        for i in range(len(q)):
            reserve[i] -= 1
                
        time += 1
    
#     total, time, l = 0, 0, 0
#     while True:
#         if l >= bridge_length:
#             print(time, q)
#             total -= q.popleft()
#             if len(q) == 0:
#                 l = 0
            
#         if wait and len(q) <= bridge_length and total + wait[0] <= weight:
#             total += wait[0]
#             q.append(wait.popleft())
            
#         l += 1           
#         time += 1
#         if len(q) == 0:
#             break
        
    return time