def solution(cards):
    answer = []
    check = [0] * len(cards)
    for i in range(len(cards)):
        if cards[i] == i + 1:
            answer.append(1)
            check[i] = 1

    while 0 in check:
        temp = 1
        index = check.index(0)
        check[index] = 1
        while True:
            value = cards[index]
            if check[value - 1] == 1:
                break
            temp += 1
            check[value - 1] = 1
            index = value - 1
        if temp != 1:
            answer.append(temp)

    answer.sort(reverse=True)
    return answer[0] * answer[1] if len(answer) != 1 else 0
