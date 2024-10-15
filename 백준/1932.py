import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(arr[i])):
        if i == 1:
            arr[i][j] = arr[0][0] + arr[i][j]
        else:
            if j == 0:
                arr[i][j] = arr[i - 1][0] + arr[i][j]
            elif j == len(arr[i]) - 1:
                arr[i][j] = arr[i - 1][len(arr[i]) - 2] + arr[i][j]
            else:
                arr[i][j] = max(
                    arr[i - 1][j - 1] + arr[i][j], arr[i - 1][j] + arr[i][j]
                )

print(max(arr[n - 1]))
