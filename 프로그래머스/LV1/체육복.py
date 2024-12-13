def solution(n, lost, reserve):
    answer = 0
    arr = [1] * n
    for i in lost:
        arr[i - 1] -= 1
    for i in reserve:
        arr[i - 1] += 1
    print(arr)

    if arr[0] == 0 and arr[1] == 2:
        arr[0] += 1
        arr[1] -= 1
    if arr[len(arr) - 1] == 0 and arr[i - 1] == 2:
        arr[i] += 1
        arr[i - 1] -= 1

    for i in range(1, len(arr) - 1):
        if arr[i] == 0 and arr[i - 1] == 2:
            arr[i] += 1
            arr[i - 1] -= 1
        elif arr[i] == 0 and arr[i + 1] == 2:
            arr[i] += 1
            arr[i + 1] -= 1

    for i in arr:
        if i == 0:
            answer += 1
    print(arr)
    return n - answer
