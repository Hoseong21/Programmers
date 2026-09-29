def solution(arr):
    result = []
    for x in arr:
        if x >= 50:
            if x % 2 == 0:
                result.append(x/2)
            else:
                result.append(x)
        else:
            if x % 2 == 1:
                result.append(x*2)
            else:
                result.append(x)
    return result