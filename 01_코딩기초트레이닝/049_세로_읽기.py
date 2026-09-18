def solution(my_string, m, c):
    n = len(my_string) // m
    ch = []
    result = ""
    for i in range(n):
        ch += [my_string[i*m:(i+1)*m]]
    for j in range(len(ch)):
        result += ch[j][c-1]
    return result