def solution(phone_number):
    length = len(phone_number)
    i = 0
    phone_list = list(phone_number)
    while i < (length - 4) :
        phone_list[i] = "*"
        i+=1
    answer = "".join(phone_list)
    return answer