from itertools import permutations
def solution(numbers):
    answer = 0
    for i in range(1, len(numbers) + 1):
        for comb in set(permutations(numbers, i)):
            if (comb[0] == '0'):
                continue
                
            num = int(''.join(comb))
            isPrime = True
            for j in range(2, int(num**.5) + 1):
                if num % j == 0:
                    isPrime = False
                    break
            if num != 1 and isPrime:
                answer += 1
    return answer