def solution(number):
    sum_num = 0
    for x in number:
        sum_num += int(x)
    return sum_num % 9