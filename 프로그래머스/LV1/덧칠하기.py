def solution(n, m, section):
    answer = 0
    value = section[0]

    for i in section:
        if i >= value:
            value = i + m
            answer += 1

    return answer
