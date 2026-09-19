def solution(my_string, indices):
    result = ''
    for i, ch in enumerate(my_string):
        if i not in indices:
            result += ch
    return result