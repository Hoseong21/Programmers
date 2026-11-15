def solution(numbers, direction):
    result = []
    n = len(numbers)
    for i in range(n):
        if direction == 'right':
            result.append(numbers[i-1])
        else:
            result.append(numbers[(i+1)%n])
    return result