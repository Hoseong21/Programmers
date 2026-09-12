def solution(a, b, c):
    result = a + b + c
    if a == b == c:
        result *= (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or b == c or c == a:
        result *= (a**2 + b**2 + c**2)
    return result