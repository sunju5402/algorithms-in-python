def solution(files):
    lst = []
    for i, file in enumerate(files):
        head = ''
        number = ''
        tail = False
        for ch in file:
            if '0' <= ch <= '9':
                number += ch
                tail = True
            elif not tail:
                head += ch
            else:
                break
        lst.append((i, head.lower(), int(number))) 
        
    lst.sort(key=lambda x:(x[1], x[2], x[0]))
    
    return [files[x[0]] for x in lst]