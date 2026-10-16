def solution(num_list):
    srt = sorted(num_list)
    result = []
    for x in srt:
        result.append(x)
        if len(result) == 5:
            return result