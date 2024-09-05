import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    files = list(map(int, input().split()))
    count = 0
    while files:
        if files[0] < max(files):
            file = files.pop(0)
            files.append(file)
            if m == 0:
                m = len(files) - 1
            else:
                m -= 1
        else:
            files.pop(0)
            if m == 0:
                break
            m -= 1
            count += 1

    print(count + 1)
