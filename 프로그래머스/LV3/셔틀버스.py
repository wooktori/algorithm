from collections import deque


def solution(n, t, m, timetable):
    answer = ""
    startTime = 540
    lastTime = 0
    lastCount = 0
    timetable.sort()

    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    q = deque(timetable)

    for i in range(n):
        count = 0
        while q and count < m:
            crew = q[0]
            if crew <= startTime:
                q.popleft()
                count += 1
                lastTime = crew
            else:
                break
        startTime += t
        lastCount = count

    def change(minutes):
        h, m = divmod(minutes, 60)
        return f"{h:02}:{m:02}"

    if lastCount == m:
        return change(lastTime - 1)
    else:
        return change(startTime - t)
    return answer
