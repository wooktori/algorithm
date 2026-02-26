import sys

input = sys.stdin.readline

n = int(input())
word = input().rstrip()
word2 = input().rstrip()

con1, con2, con3 = False, False, False

if sorted(word) == sorted(word2):
    con1 = True
if word[0] == word2[0] and word[-1] == word2[-1]:
    con2 = True

for i in "aeiou":
    word = word.replace(i, "")
    word2 = word2.replace(i, "")

if word == word2:
    con3 = True

if con1 and con2 and con3:
    print("YES")
else:
    print("NO")
