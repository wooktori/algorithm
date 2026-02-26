import sys

input = sys.stdin.readline


def sol():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()

    ans = 1
    maxV = arr[0][1]
    for i in range(1, n):
        if maxV > arr[i][1]:
            ans += 1
            maxV = arr[i][1]
    return ans


t = int(input())
for _ in range(t):
    print(sol())
