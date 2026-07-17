def solution(money):
    answer = []
    rem = money % 5500
    coff = money // 5500
    answer.append(coff)
    answer.append(rem)
    return answer