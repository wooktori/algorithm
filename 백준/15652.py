import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []


def ans(num):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(num, N + 1):
        arr.append(i)
        ans(i)
        arr.pop()


ans(1)
