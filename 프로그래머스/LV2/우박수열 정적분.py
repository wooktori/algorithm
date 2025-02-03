def solution(k, ranges):
    answer = []
    rain = [k]
    while k > 1:
        if k % 2:
            k = k * 3 + 1
            rain.append(k)
        else:
            k //= 2
            rain.append(k)

    n = len(rain) - 1
    for i in ranges:
        start, end = i
        end += n
        total = 0

        if start > end:
            answer.append(-1)
            continue

        for j in range(start, end):
            total += (rain[j] + rain[j + 1]) / 2

        answer.append(total)

    return answer
