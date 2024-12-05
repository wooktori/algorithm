import sys

input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
people.sort()

ans = 0
count = 0

for i in people:
    count += 1
    if count >= i:
        ans += 1
        count = 0
    
print(ans)