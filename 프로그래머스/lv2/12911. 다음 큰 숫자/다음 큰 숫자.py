def solution(n):
    n_cnt = str(bin(n)).count("1")
    i = n + 1
    while True:
        next_cnt = str(bin(i)).count("1")
        if n_cnt == next_cnt:
            return i
        i += 1