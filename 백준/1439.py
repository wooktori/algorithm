import sys

input = sys.stdin.readline

arr = list(map(int, input().rstrip()))

ans0 = 0
ans1 = 0

if arr[0] == 0:
    ans1 += 1
else:
    ans0 += 1
    
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        if arr[i + 1] == 0:
            ans1 += 1
        else:
            ans0 += 1

print(min(ans0, ans1))