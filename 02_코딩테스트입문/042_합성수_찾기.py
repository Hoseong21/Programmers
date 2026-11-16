def solution(n):
    answer = 0
    for i in range(1,n+1):
        cnt = 0
        for x in range(1, i+1):
            if i%x == 0:
                cnt += 1
        if cnt >= 3:
            answer += 1
    return answer