def solution(numbers, n):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
        if result > n:
            return result