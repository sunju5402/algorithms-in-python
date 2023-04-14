# def solution(cards):
#     answer = 0 
    
#     for i in range(len(cards)): # box1
#         visited1 = [False] * len(cards)
#         j = i
#         cnt1 = 0
#         while visited1[j] == False: 
#             visited1[j] = True
#             j = cards[j] - 1
#             cnt1 += 1
            
#         for k in range(i + 1, len(cards)): # box2
#             visited2 = list(visited1)
#             j = k
#             cnt2 = 0
#             while visited2[j] == False:
#                 visited2[j] = True
#                 j = cards[j] - 1
#                 cnt2 += 1
                
#             answer = max(answer, cnt1 * cnt2)
            
#     return answer

2
3
4
5
6
7
8
9
10
11
12
def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1
        answer.append([] if sorted(tmp) in answer else sorted(tmp))
    answer.sort(key=len)

    return len(answer[-1]) * len(answer[-2])
