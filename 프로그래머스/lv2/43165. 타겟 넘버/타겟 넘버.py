from itertools import product

def solution(numbers, target):
    lst = [(n, -n) for n in numbers]
    s = list(map(sum, product(*lst))) # == product(iterator1, iterator2 ..., repeat = 1)
    return s.count(target)