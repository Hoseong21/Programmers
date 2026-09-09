def solution(my_string, overwrite_string, s):
    s = int(s)
    n = len(my_string)
    p = len(overwrite_string)
    
    result = ''
    for i in range(0, n):
        if i < s:
            result += my_string[i]
        elif s <= i <= (s+p-1):
            result += overwrite_string[i-s]
        else:
            result += my_string[i]
    
    return result

# 슬라이싱을 이용한 깔끔한 풀이
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]