from collections import Counter

def solution(strArr):
    len_arr = []
    len_arr += [len(st) for st in strArr]
    cnt_arr = Counter(len_arr)
    return max(cnt_arr.values())