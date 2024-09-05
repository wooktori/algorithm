import sys

input = sys.stdin.readline


def changeValue(k):
    if switches[k - 1] == 0:
        switches[k - 1] = 1
    else:
        switches[k - 1] = 0


def sol(sex, index):
    if sex == 1:
        for i in range(1, n + 1):
            if i % index == 0:
                changeValue(i)
    else:
        changeValue(index)
        for i in range(n):
            if index - 1 - i < 0 or index - 1 + i >= n:
                break
            if switches[index - 1 - i] == switches[index - 1 + i]:
                changeValue(index - i)
                changeValue(index + i)
            else:
                break


n = int(input())
switches = list(map(int, input().split()))
students = int(input())

for i in range(students):
    sex, index = map(int, input().split())
    sol(sex, index)

for i in range(n):
    print(switches[i], end=" ")
    if (i + 1) % 20 == 0 and i != 0:
        print()
