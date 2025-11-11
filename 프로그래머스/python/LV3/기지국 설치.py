def solution(n, stations, w):
    answer = 0
    start = 1
    for i in stations:
        end = i - w
        if (end - start) % (2 * w + 1):
            answer += (end - start) // (2 * w + 1) + 1
        else:
            answer += (end - start) // (2 * w + 1)
        start = i + w + 1
    if (n + 1 - start) % (2 * w + 1):
        answer += (n + 1 - start) // (2 * w + 1) + 1
    else:
        answer += (n + 1 - start) // (2 * w + 1)

    return answer
