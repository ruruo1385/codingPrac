def solution(s):
    answer = True
    length = len(s)
    print(len(s))
    if length == 4 or length == 6:
        if s.isdigit() == True:
            answer = True
        else:
            answer = False    
    else:
        answer = False 
    return answer