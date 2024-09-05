n = int(input())

log = {}

for _ in range(n):
    name, check = input().split()
    if check == "enter":
        log[name] = check
    else:
        del log[name]

ans = sorted(log.keys(), reverse=True)

for i in ans:
    print(i)
