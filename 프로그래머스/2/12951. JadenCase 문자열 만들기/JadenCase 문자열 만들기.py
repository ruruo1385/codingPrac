def solution(s):
    answer = ''
    sub = ''
    lowered = s.lower()
    ls = list(lowered.split(' '))
    arr = []
    i = 0
    length = len(ls)
    for alp in ls:
        if alp != "":
            arr.append(alp[0].swapcase()+alp[1:])
        else:
            arr.append(alp)
    answer = " ".join(arr)
    return answer