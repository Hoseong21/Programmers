def solution(num_list):
    list_mul = 1
    for x in num_list:
        list_mul *= x
    list_add = (sum(num_list))**2
    
    if list_mul < list_add:
        result = 1
    else:
        result = 0
    return result