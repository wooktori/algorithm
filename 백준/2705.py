import sys

input = sys.stdin.readline

t = int(input())
arr = [1, 2, 2, 4, 4]
for _ in range(t):
    n = int(input())
    if n <= len(arr):
        print(arr[n - 1])
    else:
        for i in range(len(arr), n):
            if i // 2:
                arr.append(arr[(i - 1) // 2] + arr[i - 2])
            else:
                arr.append(arr[i - 1] + 2)
        print(arr[n - 1])
print(arr)
