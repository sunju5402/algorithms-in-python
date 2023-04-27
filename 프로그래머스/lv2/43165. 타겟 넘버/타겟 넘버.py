from itertools import product

def solution(numbers, target):
    answer = 0
    
    for p in list(product(['+', '-'], repeat=len(numbers))):
        total = 0
        for n, op in zip(numbers, p):
            if op == '+':
                total += n
            else:
                total -= n
            
        if total == target:
            answer += 1
    
    return answer