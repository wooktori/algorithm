n = int(input())

dict = {}
for _ in range(n):
    data = input().split(".")
    if data[1] in dict:
        dict[data[1]] += 1
    else:
        dict[data[1]] = 1

ans = sorted(dict.items(), key=lambda x: x[0])

for i in range(len(ans)):
    print(ans[i][0], ans[i][1])
