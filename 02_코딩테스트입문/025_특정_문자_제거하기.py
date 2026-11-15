def solution(my_string, letter):
    result = ''
    for ch in my_string:
        if ch not in letter:
            result += ch
    return result