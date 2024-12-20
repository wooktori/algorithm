def rec(n, a, b, ans):
    if abs(a - b) == 1 and a // 2 != b // 2:
        return ans

    a = a // 2 if a % 2 == 0 else a // 2 + 1
    b = b // 2 if b % 2 == 0 else b // 2 + 1

    return rec(n // 2, a, b, ans + 1)


def solution(n, a, b):

    return rec(n, a, b, 0) + 1
