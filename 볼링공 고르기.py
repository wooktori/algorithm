import sys

input = sys.stdin.readline


def combi(N):
    return N * (N - 1) // 2


N, K = map(int, input().split())
arr = list(map(int, input().split()))
count = [0] * (N + 1)
ans = combi(N)

for i in arr:
    count[i] += 1

arr.sort()

for i in range(len(count)):
    if count[i] > 1:
        ans -= combi(count[i])

print(ans)
