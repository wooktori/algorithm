import sys

input = sys.stdin.readline
word = input().rstrip()
bomb = input().rstrip()

arr = []
for i in range(len(word)):
    arr.append(word[i])
    if "".join(arr[-len(bomb) :]) == bomb:
        for _ in range(len(bomb)):
            arr.pop()

if len(arr) == 0:
    print("FRULA")
else:
    print("".join(arr))
