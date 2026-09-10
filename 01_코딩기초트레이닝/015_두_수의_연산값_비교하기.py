def solution(a, b):
    num1 = str(a)+str(b)
    num1 = int(num1)
    num2 = 2*a*b
    
    if num1 != num2:
        result = max(num1, num2)
    else:
        result = num1
        
    return result