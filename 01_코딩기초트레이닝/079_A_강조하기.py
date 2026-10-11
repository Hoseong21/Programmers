def solution(myString):
    result = ''
    for ch in myString:
        if 'a' in ch:
            result += ch.upper()
        elif not 'A' in ch:
            result += ch.lower()
        else:
            result += ch
    return result