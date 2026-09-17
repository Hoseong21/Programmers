def solution(my_string, is_suffix):
    res = []
    for i in range(len(my_string)):
        res += [my_string[i:]]
    return int(True if is_suffix in res else False)