def solution(numbers, k):
    for i in range(1, k+1):
        answer = (i-1)*2
    answer %= len(numbers)
    return numbers[answer]