def solution(age):
    alphabet = 'abcdefghij'
    result = ''
    for i in str(age):
        result += alphabet[int(i)]
    return result