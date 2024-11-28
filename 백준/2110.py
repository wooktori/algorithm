import sys

input = sys.stdin.readline

N, C = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = arr[0]
    count = 1
    for i in range(1, N):
        if arr[i] >= mid + value:
            value = arr[i]
            count += 1

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
