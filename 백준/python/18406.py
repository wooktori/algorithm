import sys

input = sys.stdin.readline

arr = list(map(int, input().rstrip()))
forward = 0
back = 0
for i in range(len(arr) // 2):
    forward += arr[i]
    back += arr[i + len(arr) // 2]

print(forward, back)
if forward == back:
    print("LUCKY")
else:
    print("READY")
