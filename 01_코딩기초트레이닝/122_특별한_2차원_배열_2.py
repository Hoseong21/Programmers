def solution(arr):
    n = len(arr)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]==arr[j][i]:
                cnt += 1
    return int(cnt==n*n)