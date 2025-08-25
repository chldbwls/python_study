def solution(my_s):
    stack=[]
    for s in my_s:
        if s==")":
            if stack and stack[-1]=="(":
                stack.pop()
            else: stack.append(s)
        else: stack.append(s)
    return True if len(stack)==0 else False
    
        