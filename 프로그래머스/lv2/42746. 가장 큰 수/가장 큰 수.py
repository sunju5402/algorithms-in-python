def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(key=lambda x: (x * 3), reverse=True)
    answer = ''.join(numbers)
    return '0' if answer[0] == '0' else answer
