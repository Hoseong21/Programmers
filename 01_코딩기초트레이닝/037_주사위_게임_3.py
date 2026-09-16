def solution(a, b, c, d):
    dice = sorted([a, b, c, d])
    
    if dice[0] == dice[3]: # 정렬 후이므로 4개의 눈이 모두 같다는 의미
        return 1111*dice[0]
    elif dice[0] == dice[2] or dice[1] == dice[3]: # 3개의 눈이 같은 경우
        p = dice[1]
        q = dice[0] if dice[0] != p else dice[3]
        return (10*p + q)**2
    elif dice[0] == dice[1] and dice[2] == dice[3]: # 두 개씩 같은 경우
        return (dice[0] + dice[2])*abs(dice[0]-dice[2])
    elif dice[0] == dice[1] or dice[1] == dice[2] or dice[2] == dice[3]:
        pairs = [dice[i] for i in range(3) if dice[i] == dice[i+1]][0]
        others = [x for x in dice if x != pairs]
        return others[0]*others[1]
    else:
        return dice[0]