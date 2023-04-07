def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    # for i in range(citations[-1], citations[0] - 1, -1):
    #     for j in range(n):
    #         if citations[j] >= i:
    #             if (n - j) >= i:
    #                 return i
    return 0