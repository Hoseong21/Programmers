def solution(arr, intervals):
    result = []
    for i, j in intervals:
        result += arr[i:j+1]
    return result