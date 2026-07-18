def solution(numbers):
    answer = -1
    sum = 0
    sum2 = 0
    for i in numbers:
        sum += i
    for n in range(10):
        sum2 += n
    answer = sum2 - sum
    return answer