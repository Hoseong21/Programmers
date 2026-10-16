def solution(arr):
    n, k = len(arr), 1
    while(k<n):
        k *= 2
    return arr + [0]*(k-n)