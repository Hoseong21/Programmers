def solution(intStrs, k, s, l):
    result = []
    for i in intStrs:
        num = int(i[s:s+l])
        if num > k:
            result += [num]
    return result