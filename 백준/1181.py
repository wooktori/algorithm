import sys

input = sys.stdin.readline

n = int(input())
arr = list(set([input().rstrip() for _ in range(n)]))

arr.sort(key=lambda x: (len(x), x))

for i in range(len(arr)):
    print(arr[i])
