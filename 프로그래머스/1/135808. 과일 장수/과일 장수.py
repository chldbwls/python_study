def solution(k, m, score):
    score.sort()
    start=len(score)%m
    arr=score[start::m]
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]*m
    return sum