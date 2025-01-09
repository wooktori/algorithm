def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        target = numbers[i]

        while stack and numbers[stack[-1]] < target:
            temp = stack.pop()
            answer[temp] = target

        stack.append(i)

    return answer
