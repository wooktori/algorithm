import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
newArr = sorted(set(arr))
dict = {newArr[i]: i for i in range(len(newArr))}

for i in range(n):
    print(dict[arr[i]], end=" ")
