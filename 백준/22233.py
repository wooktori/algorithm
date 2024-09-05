import sys

input = sys.stdin.readline

n, m = map(int, input().split())
keywords = set()
for _ in range(n):
    keyword = input().rstrip()
    keywords.add(keyword)

for i in range(m):
    word = list(input().rstrip().split(","))
    for j in range(len(word)):
        if word[j] in keywords:
            keywords.remove(word[j])
    print(len(keywords))
