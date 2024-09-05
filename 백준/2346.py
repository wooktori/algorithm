from collections import deque

n = int(input())
numbers = list(map(int, input().split()))

q = deque()
for i in range(1, n+1):
  q.append(i)

start = numbers[0]
while q:
  q.popleft()
  