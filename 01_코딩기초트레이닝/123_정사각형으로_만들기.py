def solution(arr):
    n = len(arr)
    k = len(arr[0])
    if n<k:
        arr += [[0]*k]*(k-n)
        return arr
    elif n>k:
        for i in range(n):
            arr[i] += [0]*(n-k)
        return arr
    else:
        return arr