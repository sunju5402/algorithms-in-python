from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    wait = deque(truck_weights)
    total_weight, time = 0, 0

    while wait:
        total_weight -= bridge.popleft()
        
        if total_weight + wait[0] > weight:
            bridge.append(0)
        else:
            truck = wait.popleft()
            bridge.append(truck)
            total_weight += truck
            
        time += 1
        
    time += bridge_length

    return time