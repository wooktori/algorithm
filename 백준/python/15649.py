import sys

input = sys.stdin.readline


def sol(x):
    if x == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()

    for i in range(1, n + 1):
        if isused[i] == False:
            arr[x] = i
            isused[i] = True
            sol(x + 1)
            isused[i] = False


n, m = map(int, input().split())
arr = [0] * 10
isused = [False] * 10
sol(0)
