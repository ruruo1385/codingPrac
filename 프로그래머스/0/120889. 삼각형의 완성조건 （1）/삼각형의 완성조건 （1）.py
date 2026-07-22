def solution(sides):
    answer = 0
    biggest = 0
    sum = 0 
    for i in range(len(sides)):
        if i == 0:
            biggest = sides[i]
        else:
            if sides[i] > biggest:
                sum += biggest
                biggest = sides[i]
            else:
                sum += sides[i]
    if biggest < sum:
        answer = 1
    else:
        answer = 2
    return answer