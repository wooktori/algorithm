import sys

input = sys.stdin.readline

k = int(input())
node = list(map(int, input().split()))

ans = [[] for _ in range(k)]


def recursion(arr, n):
    mid = len(arr) // 2
    ans[k - n].append(arr[mid])

    if n == 1:
        return
    recursion(arr[:mid], n - 1)
    recursion(arr[mid + 1 :], n - 1)


recursion(node, k)

for i in range(k):
    for j in range(len(ans[i])):
        print(ans[i][j], end=" ")
    print()
