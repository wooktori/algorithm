n = int(input())

dict = {}
for _ in range(n):
    book = input()
    if book not in dict:
        dict[book] = 1
    else:
        dict[book] += 1

ans = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
print(ans[0][0])
