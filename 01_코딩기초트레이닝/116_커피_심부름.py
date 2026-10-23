def solution(order):
    total_price = 0
    for od in order:
        if ('americano' in od) or (od == 'anything'):
            total_price += 4500
        else:
            total_price += 5000
    return total_price