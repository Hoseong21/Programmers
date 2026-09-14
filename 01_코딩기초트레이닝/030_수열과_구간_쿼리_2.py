def solution(arr, queries):
    result = []
    for s, e, k in queries:
        res = []
        for i in range(s, e+1):
            if arr[i] > k:
                res += [arr[i]]
        if res == []:
            result += [-1]
        else:
            result += [min(res)]
    return result