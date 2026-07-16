def solution(arr):
    sum = 0
    answer = 0
    for i in arr:
        sum+=i
    answer = sum / len(arr)
    return answer