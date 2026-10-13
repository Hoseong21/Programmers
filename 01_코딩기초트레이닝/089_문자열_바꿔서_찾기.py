def solution(myString, pat):
    new = ''
    for ch in myString:
        if ch == 'A':
            new += 'B'
        else:
            new += 'A'
    return int(pat in new)