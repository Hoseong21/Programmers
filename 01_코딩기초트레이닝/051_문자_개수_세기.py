def solution(my_string):
    result = [0]*52
    for ch in my_string:
        if ch.isupper():
            i = ord(ch) - ord('A')
            result[i] += 1
        else:
            i = ord(ch) - ord('a') + 26
            result[i] += 1
    return result