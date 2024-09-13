import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(N):
    tempArr = arr[:i] + arr[i + 1 :]
    left = 0
    right = len(tempArr) - 1

    while left < right:
        total = tempArr[left] + tempArr[right]
        if arr[i] == total:
            ans += 1
            break
        elif arr[i] > total:
            left += 1
        else:
            right -= 1
print(ans)
