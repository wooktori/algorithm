import sys

input = sys.stdin.readline

n = int(input())
count = 0
arr = [0]
for i in range(n):
    x, y = map(int, input().split())
    if y > arr[len(arr) - 1]:
        count += 1
        arr.append(y)
    else:
        while arr[len(arr) - 1] > y:
            arr.pop()
        if arr[len(arr) - 1] < y:
            count += 1
            arr.append(y)

print(count)
