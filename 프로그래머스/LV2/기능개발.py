def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    while len(progresses) > 0:
        if (progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            else:
                day += 1
    answer.append(count)
    return answer
