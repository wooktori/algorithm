import sys

input = sys.stdin.readline
arr = list(map(int, input().rstrip()))

arr.sort(reverse=True)
ans = 1

for i in range(len(arr)):
    if arr[i] == 0:
        break
    if arr[i] == 1:
        ans += arr[i]
    else:
        ans *= arr[i]
        
print(ans)