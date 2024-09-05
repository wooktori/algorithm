import sys

input = sys.stdin.readline

arr = [0] * 10
isused = [False] * 10


def sol(x):
    if x == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()

    start = 1
    if x != 0:
        start = arr[x - 1] + 1
    for i in range(start, n + 1):
        if isused[i] == False:
            arr[x] = i
            isused[i] = True
            sol(x + 1)
            isused[i] = False


n, m = map(int, input().split())
sol(0)
