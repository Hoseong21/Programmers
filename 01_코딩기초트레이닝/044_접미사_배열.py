def solution(my_string):
    result = []
    for i in range(len(my_string)):
        result += [my_string[-i:]]
        result.sort()
    return result