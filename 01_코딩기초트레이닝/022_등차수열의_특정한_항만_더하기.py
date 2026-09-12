def solution(a, d, included):
    result = 0
    n = len(included)
    for i in range(n):
        if included[i] is True: # if cluded[i]도 됨!!
            result += (a + i*d)
    return result