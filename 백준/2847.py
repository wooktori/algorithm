import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(i + 1, n):
        while True:
            if arr[i] >= (arr[j] - (j - i - 1)):
                count += 1
                arr[i] -= 1
            else:
                break

print(count)
