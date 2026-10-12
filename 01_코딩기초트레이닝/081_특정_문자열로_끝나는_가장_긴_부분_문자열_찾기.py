def solution(myString, pat):
    result = ''
    for i in range(len(myString)):
        if myString[i:len(pat)+i] == pat:
            result = myString[:len(pat)+i]
    return result