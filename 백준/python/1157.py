word = input().upper()
arr = [0] * 26


for i in range(len(word)):
    arr[ord(word[i]) - 65] += 1

maxV = 0
index = 0
for i in range(26):
    if arr[i] > maxV:
        maxV = arr[i]
        index = i

for i in range(26):
    if index != i and maxV == arr[i]:
        print("?")
        index = -1
        break

if index != -1:
    print(chr(index + 65))
