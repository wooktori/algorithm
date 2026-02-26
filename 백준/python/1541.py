import sys

input = sys.stdin.readline

sen = input().rstrip().split("-")
ans = 0

for i in range(len(sen)):
    if "+" in sen[i]:
        newArr = sen[i].split("+")
        temp = 0
        for sen[i] in newArr:
            temp += int(sen[i])
        if i == 0:
            ans += temp
        else:
            ans -= temp
    else:
        if i == 0:
            ans += int(sen[i])
        else:
            ans -= int(sen[i])
print(ans)
