# def fibo(n):
    
def solution(n):
    answer = 0
    pre = 0
    nx = 1
    for i in range(n - 1):
        answer = pre + nx
        pre = nx
        nx = answer
    # n -= 
    # if n == 0 or n == 1:
    #     return 1
    # return solution(n - 1) + solution(n - 2)
    return answer % 1234567