def solution(price):
    if price >= 500000:
        return int(price*(80/100))
    elif 300000 <= price < 500000:
        return int(price*(90/100))
    elif 100000 <= price < 300000:
        return int(price*(95/100))
    else:
        return price