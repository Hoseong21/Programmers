def solution(l, r):
    result = []
    for i in range(l, r+1):
        if all(char in '05' for char in str(i)):
            result += [i]
    if result == []:
        result = [-1]
    return result