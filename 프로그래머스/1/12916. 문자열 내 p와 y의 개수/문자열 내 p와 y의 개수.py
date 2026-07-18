def solution(s):
    answer = True
    if s.lower().count("p") == s.lower().count("y"):
        return answer
    elif s.lower().count("p")==0 and s.lower().count("y")==0:
        return answer
    else: 
        answer = False
    return answer
   