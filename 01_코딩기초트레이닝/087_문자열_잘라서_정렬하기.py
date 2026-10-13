def solution(myString):
    result = [ch for ch in myString.split('x') if ch != '']
    result.sort()
    return result