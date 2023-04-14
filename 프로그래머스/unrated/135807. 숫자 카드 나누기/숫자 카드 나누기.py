# from math import gcd

# def solution(arrayA, arrayB):
#     answer = 0
    
#     a_gcd = arrayA[0]
#     b_gcd = arrayB[0]
#     for i, (a, b) in enumerate(zip(arrayA, arrayB), start = 1):
#         a_gcd = gcd(a_gcd, a)
#         b_gcd = gcd(b_gcd, b)
    
#     a_div = False # arrayA의 최대공약수로 arrayB에 있는 원소들이 나눠지는지
#     b_div = False # arrayB의 최대공약수로 arrayA에 있는 원소들이 나눠지는지
#     for a, b in zip(arrayA, arrayB):
#         if not a_div and b % a_gcd == 0:
#             a_div = True    
#         if not b_div and a % b_gcd == 0:
#             b_div = True
    
#     if not a_div and a_gcd != 1:
#         answer = a_gcd
#     if not b_div and b_gcd != 1:
#         answer = max(answer, b_gcd)
        
#     return answer

from math import gcd
from functools import reduce

def check(arrayA, arrayB):
    gcd_A = reduce(gcd, arrayA, arrayA[0])
    factors = [i for i in range(1, gcd_A//2+1) if not gcd_A % i]
    factors.append(gcd_A)
    for factor in factors[::-1]:
        if all(i % factor for i in arrayB):
            return gcd_A
    return 0

def solution(arrayA, arrayB):
    return max(check(arrayA, arrayB), check(arrayB, arrayA))