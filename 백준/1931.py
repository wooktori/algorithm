N = int(input())

arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[1], x[0]))
answer = 0
end = 0
start = 0
for i in arr:
    if i[0] >= start:
        answer += 1
        start = i[1]


print(answer)
