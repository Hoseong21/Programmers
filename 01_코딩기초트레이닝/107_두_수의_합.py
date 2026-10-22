def solution(a, b):
    a = a[::-1]
    b = b[::-1]
    result = []
    carry = 0
    
    for i in range(max(len(a), len(b))):
        new_a = int(a[i]) if i<len(a) else 0
        new_b = int(b[i]) if i<len(b) else 0
        total = new_a + new_b + carry
        result.append(str(total % 10))
        carry = total // 10
    
    if carry:
        result.append(str(carry))
    
    return ''.join(result[::-1])