def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += price * (i + 1)
        print(answer)
    if answer - money >= 0:
        return answer - money
    else:
        return 0
