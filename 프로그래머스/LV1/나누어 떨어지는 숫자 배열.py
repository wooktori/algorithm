def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if not arr[i] % divisor:
            answer.append(arr[i])
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer
