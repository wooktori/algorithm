def solution(a):
    answer = 0
    left = [0] * len(a)
    right = [0] * len(a)

    left[0] = a[0]
    right[-1] = a[-1]

    for i in range(1, len(a)):
        left[i] = min(left[i - 1], a[i])

    for i in range(len(a) - 2, -1, -1):
        right[i] = min(right[i + 1], a[i])

    for i in range(len(a)):
        if a[i] == left[i] or a[i] == right[i]:
            answer += 1

    return answer
