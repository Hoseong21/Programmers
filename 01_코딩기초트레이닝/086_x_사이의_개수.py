def solution(myString):
    result = []
    count = 0
    for i in range(len(myString)):
        if myString[i] != 'x':
            count += 1
        else:
            result.append(count)
            count = 0
    if myString[-1] != 'x':
        result.append(count)
    else:
        count = 0
        result.append(count)
    return result