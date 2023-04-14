from math import gcd

def div(array, g):
    for val in array:
        if val % g == 0:
            return True
    return False
        
def solution(arrayA, arrayB):
    answer = 0
    
    a_gcd = arrayA[0]
    b_gcd = arrayB[0]
    for i, (a, b) in enumerate(zip(arrayA, arrayB), start = 1):
        a_gcd = gcd(a_gcd, a)
        b_gcd = gcd(b_gcd, b)
    
    a_div = div(arrayB, a_gcd) # arrayA의 최대공약수로 arrayB에 있는 원소들이 나눠지는지
    b_div = div(arrayA, b_gcd) # arrayB의 최대공약수로 arrayA에 있는 원소들이 나눠지는지
    
    if not a_div and a_gcd != 1:
        answer = a_gcd
    if not b_div and b_gcd != 1:
        answer = max(answer, b_gcd)
        
    return answer