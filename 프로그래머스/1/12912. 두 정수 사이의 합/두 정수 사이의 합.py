def solution(a, b):
    i = 0
    if (a == b):
        answer = a
        return answer
    elif(a > b):
        x = range(b,a+1)
        for n in x:
            i+=n
        answer = i
        return answer
    else:
        x = range(a,b+1)
        for n in x:
            i+=n
        answer = i
        return answer
     