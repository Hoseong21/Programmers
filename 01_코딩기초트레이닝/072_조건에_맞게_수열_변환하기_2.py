def solution(arr):
    cnt = 0
    while(True):
        arr_next = []
        for x in arr:
            if x >= 50:
                if x % 2 == 0:
                    arr_next.append(x//2)
                else:
                    arr_next.append(x)
            else:
                if x % 2 == 1:
                    arr_next.append(x*2+1)
                else:
                    arr_next.append(x)
        if arr_next == arr:
            return cnt
        arr = arr_next
        cnt += 1