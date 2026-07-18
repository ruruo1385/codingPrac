def solution(s):
    answer = ''
    ls = s.split()
    ls.sort(key = int)
    answer= "{} {}".format(ls[0],ls[-1])
    
    return answer