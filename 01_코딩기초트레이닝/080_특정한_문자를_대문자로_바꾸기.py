def solution(my_string, alp):
    result = ''
    for ch in my_string:
        if ch in alp:
            result += ch.upper()
        else:
            result += ch
    return result