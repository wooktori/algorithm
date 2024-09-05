import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

ans = []
q = deque()
for i in range(1, n + 1):
    q.append(i)

while q:
    for i in range(k - 1):
        x = q.popleft()
        q.append(x)
    num = q.popleft()
    ans.append(num)

for i in range(len(ans)):
    ans[i] = str(ans[i])

word = "<" + ", ".join(ans) + ">"
print(word)
