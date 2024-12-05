import sys

input = sys.stdin.readline

S = input().rstrip()
ans = []
num = 0

for i in S:
    if i.isalpha():
        ans.append(i)
    else:
        num += int(i)

ans.sort()

if num:
    ans.append(str(num))

print("".join(ans))
