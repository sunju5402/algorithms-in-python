def solution(n):
    n_cnt = bin(n).count("1")
    i = n + 1
    while True:
        next_cnt = bin(i).count("1")
        if n_cnt == next_cnt:
            return i
        i += 1