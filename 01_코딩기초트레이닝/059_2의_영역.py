def solution(arr):
    first_idx = None
    last_idx = None
    for i, k in enumerate(arr):
        if k == 2:
            if first_idx is None:
                first_idx = i
            last_idx = i
    if 2 not in arr:
        return [-1]
    else:
        return arr[first_idx:last_idx+1]