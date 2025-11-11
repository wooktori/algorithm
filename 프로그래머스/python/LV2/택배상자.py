from collections import deque


def solution(order):
    answer = 0
    container = deque([i for i in range(1, len(order) + 1)])
    index = 0
    subContainer = []

    while container:
        item = container.popleft()
        if item != order[index]:
            subContainer.append(item)
        else:
            index += 1
            answer += 1
            while (
                index < len(order)
                and len(subContainer) > 0
                and subContainer[-1] == order[index]
            ):

                subContainer.pop()
                index += 1
                answer += 1

    return answer
