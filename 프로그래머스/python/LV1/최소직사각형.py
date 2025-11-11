def solution(sizes):
    answer = 0
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    sizes.sort()
    for i in sizes:
        if i[1] > answer:
            answer = i[1]
    return answer * sizes[-1][0]
