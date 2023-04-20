import math
def solution(arr):
    lcm = 0
    for a in arr:
        if not lcm:
            lcm = a
        else:
            lcm *= a // math.gcd(lcm, a) 
    return lcm