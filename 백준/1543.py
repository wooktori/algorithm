import sys

input = sys.stdin.readline

word = input().rstrip()
search = input().rstrip()

count = 0
start = 0

while start <= len(word) - len(search):
    if word[start : start + len(search)] == search:
        count += 1
        start += len(search)
    else:
        start += 1

print(count)
