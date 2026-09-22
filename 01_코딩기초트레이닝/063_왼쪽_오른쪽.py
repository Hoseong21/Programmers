def solution(str_list):
    for i, ch in enumerate(str_list):
        if ch == 'l':
            return str_list[:i]
        elif ch == 'r':
            return str_list[i+1:]
    if 'l' or 'r' not in str_list:
        return []