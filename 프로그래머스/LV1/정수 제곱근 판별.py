def solution(n):
    answer = 0
    for i in range(n + 1):
        if i * i == n:
            return (i + 1) ** 2
    return -1
