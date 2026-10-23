def solution(picture, k):
    result = []
    for st in picture:
        new_pic = ""
        for ch in st:
            new_pic += ch*k
        for _ in range(k):
            result.append(new_pic)
    return result