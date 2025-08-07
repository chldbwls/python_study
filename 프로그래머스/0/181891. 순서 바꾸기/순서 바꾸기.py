def solution(num_list, n):
    answer = []
    for i in range(n):
        answer.append(num_list.pop(0))
    return num_list+answer