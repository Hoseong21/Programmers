def solution(n):
    fact = 1
    for i in range(2, 11):
        fact *= i
        if fact > n:
            return i-1
        elif fact == n:
            return i
        else:
            continue