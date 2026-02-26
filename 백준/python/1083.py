import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
S = int(input())

for i in range(N):
    maxIndex = arr.index(max(arr[i: min(N, i + S + 1)]))

    for j in range(maxIndex, i, -1):
        arr[j], arr[j - 1] = arr[j - 1], arr[j] 
    S -= (maxIndex - i)
    if S <= 0: break
    
    
for num in arr:
    print(num, end=" ")
    