n = int(input())

ans = set()
count = 0
for i in range(n):
    chat = input()
    if chat == "ENTER":
        ans.clear()
    else:
        if chat not in ans:
            ans.add(chat)
            count += 1

print(count)
