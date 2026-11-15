def solution(balls, share):
    up = 1
    down = 1
    for i in range(balls, balls-share, -1):
        up *= i
    for i in range(1, share+1):
        down *= i
    return up/down