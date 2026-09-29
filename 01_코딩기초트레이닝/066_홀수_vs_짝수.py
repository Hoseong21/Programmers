def solution(num_list):
    odd = 0
    even = 0
    for i, k in enumerate(num_list):
        if i % 2 == 0:
            even += k
        else:
            odd += k
    return max(even, odd)