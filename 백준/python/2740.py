n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

x,y = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(x)]

ans = [[0]*y for _ in range(n)]

for i in range(n):
  for j in range(y):
    for k in range(m):
      ans[i][j] += a[i][k] * b[k][j]

for i in range(n):
  for j in range(y):
    print(ans[i][j], end=' ')
  print()