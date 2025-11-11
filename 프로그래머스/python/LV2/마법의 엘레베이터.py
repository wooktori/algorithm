def solution(storey):
    answer = 0

    while storey:
        i = storey % 10
        j = (storey // 10) % 10
        if i > 5:
            answer += 10 - i
            storey = (storey // 10) + 1
        elif i < 5:
            answer += i
            storey //= 10

        else:
            if j >= 5:
                answer += 10 - i
                storey = (storey // 10) + 1
            else:
                answer += i
                storey //= 10

    return answer
