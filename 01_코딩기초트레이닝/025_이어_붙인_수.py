def solution(num_list):
    odd = ''
    even = ''
    for x in num_list:
        if x % 2 == 1:
            odd += f"{x}"
        else:
            even += f"{x}"
    result = int(odd) + int(even)
    return result