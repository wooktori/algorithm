from itertools import product


def solution(word):
    answer = []
    arr = ["A", "E", "I", "O", "U"]
    for i in range(1, 6):
        for j in product(arr, repeat=i):
            answer.append("".join(j))
        answer.sort()

    for i in range(len(answer)):
        if answer[i] == word:
            return i + 1
