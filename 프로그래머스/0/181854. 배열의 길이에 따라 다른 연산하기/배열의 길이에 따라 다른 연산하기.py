def solution(arr, n):
    return [x+n if (i % 2) != (len(arr) % 2) else x for i, x in enumerate(arr)]