import sys

input = sys.stdin.readline

arr = []


def push(n):
    global arr
    arr.append(n)


def pop():
    global arr
    if len(arr) != 0:
        a = arr.pop()
        print(a)
    else:
        print(-1)


def size():
    global arr
    return len(arr)


def empty():
    global arr
    if len(arr) != 0:
        return 0
    else:
        return 1


def top():
    global arr
    if len(arr) == 0:
        return -1
    return arr[len(arr) - 1]


n = int(input())
for _ in range(n):
    data = input().split()
    if data[0] == "push":
        push(int(data[1]))
    elif data[0] == "pop":
        pop()
    elif data[0] == "size":
        print(size())
    elif data[0] == "top":
        print(top())
    else:
        print(empty())


# 링크드리스트 구현해서 풀어보기
# 링크드리스트 vs array
