def solution(arr, queries):
    for x in range(len(queries)):
        query = queries[x]
        i = query[0]
        j = query[1]
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp   
    return arr