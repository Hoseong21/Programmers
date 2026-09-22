def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            k = query[i]
            del arr[k+1:]
        else:
            k = query[i]
            del arr[:k]
    return arr