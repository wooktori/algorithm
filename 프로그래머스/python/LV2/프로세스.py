from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))

    while len(q) != 0:
        process = q.popleft()
        if len(q) == 0:
            break

        max_value = max(i[0] for i in q)

        if max_value > process[0]:
            q.append(process)
        else:
            if process[1] == location:
                break
            answer += 1
    return answer + 1
