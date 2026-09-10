def solution(s1, s2):
    n = len(s1)
    result = ''
    for i in range(n):
        if s1[i] in s1:               ## 사실 if문은 필요가 없다...
            result += s1[i]
        if s2[i] in s2:
            result += s2[i] 
            
    return result

# 다른 풀이
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer+=str1[i]+str2[i]
    return answer