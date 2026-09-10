def solution(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    ab, ba = int(ab), int(ba)
    if ab != ba:
        result = max(ab, ba)
    else:
        result = ab
    return result