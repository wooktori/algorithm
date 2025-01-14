def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    start_X, start_Y = 0, 0
    num = 1
    while n > 0:
        for i in range(start_X, n):
            if answer[i][start_Y] == 0:
                answer[i][start_Y] = num
                num += 1
        for i in range(start_Y, n - start_Y):
            if answer[n - 1][i] == 0:
                answer[n - 1][i] = num
                num += 1
        for i in range(n - 1, start_X, -1):
            if answer[i][i - start_Y] == 0:
                answer[i][i - start_Y] = num
                num += 1

        start_X += 2
        start_Y += 1
        n -= 1

    arr = []
    for i in answer:
        for j in i:
            arr.append(j)
    return arr
