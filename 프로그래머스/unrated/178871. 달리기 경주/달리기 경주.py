def solution(players, callings):
    dic = {players[i]:i for i in range(len(players))}
    for c in callings:
        idx = dic[c]
        dic[c] -= 1
        dic[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players