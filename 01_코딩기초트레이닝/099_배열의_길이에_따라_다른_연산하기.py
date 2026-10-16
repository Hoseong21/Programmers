def solution(arr, n):
    result = []
    if len(arr) % 2 == 0:
        for i, x in enumerate(arr):
            if i % 2 == 1:
                result.append(x+n)
            else:
                result.append(x)
    else:
        for i, x in enumerate(arr):
            if i % 2 == 0:
                result.append(x+n)
            else:
                result.append(x)
    return result