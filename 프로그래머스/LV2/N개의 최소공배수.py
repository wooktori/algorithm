import math


def solution(arr):
    arr.sort()
    answer = arr[0]
    for i in range(len(arr) - 1):
        answer = answer * arr[i + 1] // math.gcd(answer, arr[i + 1])
    return answer
