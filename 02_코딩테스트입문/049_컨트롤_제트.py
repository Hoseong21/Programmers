def solution(s):
    answer = s.split()
    for i, x in enumerate(answer):
        if x == 'Z':
            answer.pop(i-1)
    return sum([int(k) for k in answer if k != 'Z'])