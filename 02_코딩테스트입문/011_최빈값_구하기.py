def solution(array):
    cnt = [0]*(max(array)+1)
    for i in array:
        cnt[i] += 1
    if cnt.count(max(cnt)) > 1:
        return -1
    else:
        return cnt.index(max(cnt))