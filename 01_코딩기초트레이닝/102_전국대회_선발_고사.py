def solution(rank, attendance):
    di = {}
    for i, x in enumerate(rank):
        di[i] = x
    for i, bo in enumerate(attendance):
        if bo is False:
            di.pop(i)
    sorted_rank = sorted(di.items(), key=lambda x:x[1])
    a, b, c = sorted_rank[0][0], sorted_rank[1][0], sorted_rank[2][0]
    return 10000*a + 100*b + c