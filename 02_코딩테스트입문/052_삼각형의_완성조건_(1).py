def solution(sides):
    side = sorted(sides)
    if side[-1] < side[0] + side[1]:
        return 1
    else:
        return 2