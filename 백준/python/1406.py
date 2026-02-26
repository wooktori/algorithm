import sys

input = sys.stdin.readline


# word = list(input().rstrip())
# n = int(input())
# index = len(word)

# for _ in range(n):
#     data = input().split()
#     if data[0] == "P":
#         word.insert(index, data[1])
#         index += 1

#     elif data[0] == "L":
#         if index == 0:
#             continue
#         index -= 1

#     elif data[0] == "D":
#         if index == len(word):
#             continue
#         index += 1

#     else:
#         if index == 0:
#             continue
#         word.pop(index - 1)
#         index -= 1

# print("".join(word))


left = list(input().rstrip())
n = int(input())
right = []

for _ in range(n):
    data = input().split()
    if data[0] == "P":
        left.append(data[1])
    elif data[0] == "L" and len(left) != 0:
        x = left.pop()
        right.append(x)
    elif data[0] == "D" and len(right) != 0:
        x = right.pop()
        left.append(x)
    elif data[0] == "B" and len(left) != 0:
        left.pop()

ans = left + right[::-1]
print("".join(ans))
