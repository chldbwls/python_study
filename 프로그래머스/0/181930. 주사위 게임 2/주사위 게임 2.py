def solution(a, b, c):
    n = len({a,b,c})
    if n==3:
        return a+b+c
    elif n==2:
        return (a+b+c)*(a*a+b*b+c*c)
    else:
        return (a+b+c)*(a*a+b*b+c*c)*(a*a*a+b*b*b+c*c*c)