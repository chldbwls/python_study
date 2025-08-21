def solution(num_list):
    n1=''
    n2=''
    for i in num_list:
        if i%2==0:
            n1+=str(i)
        else:
            n2+=str(i)
    return int(n1)+int(n2)