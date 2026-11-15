def solution(emergency):
    data = sorted(emergency)[::-1]
    result = [data.index(i)+1 for i in emergency]
    return result