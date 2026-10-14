def solution(myStr):
    myString = myStr.replace('b', 'a').replace('c', 'a').split('a')
    result = []
    for st in myString:
        if st != "":
            result += [st]
    if result == []:
        result += ["EMPTY"]
    return result