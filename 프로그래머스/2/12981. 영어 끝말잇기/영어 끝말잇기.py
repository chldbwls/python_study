def solution(n, words):
    s=[]
    s.append(words[0])
    for i in range (1,len(words)):
        if words[i].strip()[0]!=words[i-1].strip()[-1]:
            return [i%n+1, (i+n)//n]
        else:
            if words[i] in s:
                return [i%n+1, (i+n)//n]
            else:
                s.append(words[i])
    return [0,0]