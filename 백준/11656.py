import sys

input = sys.stdin.readline

S = input().rstrip()
arr = []

for i in range(len(S)):
    arr.append(S[i:])

arr.sort()
for i in arr:
    print(i)
