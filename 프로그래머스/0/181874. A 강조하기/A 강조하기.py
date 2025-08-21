def solution(myString):
    answer = ''
    for s in myString:
        if s=='a' or s=='A':
            s=s.upper()
            answer+=s
        else:
            s=s.lower()
            answer+=s
    return answer