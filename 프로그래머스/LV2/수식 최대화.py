from itertools import permutations
from re import split


def solution(expression):
    answer = 0

    for priority in permutations(["-", "+", "*"], 3):
        operands = list(map(int, split("[\*\+\-]", expression)))
        operators = [x for x in expression if x in "-+*"]

        for j in priority:
            while j in operators:
                index = operators.index(j)

                if j == "-":
                    temp = operands[index] - operands[index + 1]
                elif j == "+":
                    temp = operands[index] + operands[index + 1]
                else:
                    temp = operands[index] * operands[index + 1]

                operands[index] = temp
                operators.pop(index)
                operands.pop(index + 1)

        if abs(operands[0]) > answer:
            answer = abs(operands[0])

    return answer
