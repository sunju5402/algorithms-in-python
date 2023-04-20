import math
def solution(arr):
    lcm = 1
    for i in range(len(arr)):
        g = 0
        for j in range(i + 1, len(arr)):
            g = math.gcd(arr[i], arr[j])
            if g:
                arr[j] //= g
    for a in arr:
        lcm *= a
    
    return lcm