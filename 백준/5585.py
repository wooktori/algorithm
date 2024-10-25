import sys

input = sys.stdin.readline

price = int(input())
arr = [500, 100, 50, 10, 5, 1]
money = 1000 - price
ans = 0

for i in range(6):
    temp = money // arr[i]
    ans += temp
    money -= arr[i] * temp

print(ans)
