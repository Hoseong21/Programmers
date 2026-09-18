def solution(q, r, code):
    result = ""
    for i, ch in enumerate(code):
        if i % q == r:
            result += ch
    return result