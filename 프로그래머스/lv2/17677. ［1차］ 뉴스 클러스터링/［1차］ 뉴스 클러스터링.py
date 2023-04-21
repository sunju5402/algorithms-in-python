def to_dic(s):
    dic = {}
    for i in range(len(s) - 1):
        key = s[i:i + 2].lower()
        if key.isalpha():
            if key not in dic:
                dic[key] = 1
            else:
                dic[key] += 1
    return dic

def solution(str1, str2):
    dic1 = to_dic(str1)
    dic2 = to_dic(str2)
    print(dic1, dic2)
    inter = 0
    lst = []
    for key in dic1:
        if key in dic2:
            inter += min(dic1[key], dic2[key])
            for _ in range(max(dic1[key], dic2[key])):
                lst.append(key)
        else:
            for _ in range(dic1[key]):
                lst.append(key)
    for key in dic2:
        if key not in lst:
            for _ in range(dic2[key]):
                lst.append(key)

    if len(lst) == 0 and inter == 0:
        return 65536
    elif inter == 0:
        return 0
    return int(inter / len(lst) * 65536)