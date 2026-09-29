def solution(num_list):
    result = 0
    for x in num_list:
        while(x!=1):
            if x % 2 == 0:
                x /= 2
                result += 1
            else:
                x = (x-1)/2
                result += 1
    return result