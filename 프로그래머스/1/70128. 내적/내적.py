def solution(a, b):
    answer = 0
    i = 0
    while i < len(a):
        prod = a[i] * b[i]
        answer += prod
        i+=1
    return answer