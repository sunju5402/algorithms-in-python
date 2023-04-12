def solution(data, col, row_begin, row_end):
    data.sort(reverse=True)
    data.sort(key=lambda x:x[col - 1])
    lst = [0] * (row_end - row_begin + 1)
    for i in range(row_begin - 1, row_end):
        for j in range(len(data[i])):
            lst[i - row_begin + 1] += data[i][j] % (i + 1) 

    result = lst[0]
    for i in range(1, len(lst)):
        result ^= lst[i]
    return result