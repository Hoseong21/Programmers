def solution(arr, k):
    result = []
    for i in range(len(arr)):
        if arr[i] not in result:
            result.append(arr[i])
    if len(result) > k:
        while(len(result)!=k):
            result.pop()
    elif len(result) < k:
        while(len(result)!=k):
            result.append(-1)
    return result