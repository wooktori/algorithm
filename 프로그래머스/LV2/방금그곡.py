def change_str(s):
    change = {"C": "Z", "D": "Y", "F": "X", "G": "W", "A": "V"}
    arr = s.split("#")
    changed_s = ""
    for i in range(len(arr)):
        temp = arr[i]
        if i != len(arr) - 1 and arr[i][-1] in change:
            temp = arr[i][:-1] + change[arr[i][-1]]
        changed_s += temp
    return changed_s


def solution(m, musicinfos):
    m = change_str(m)

    answer = []
    for info in musicinfos:
        start, end, title, song = info.split(",")
        song = change_str(song)
        time = int(end[:2]) * 60 + int(end[3:]) - (int(start[:2]) * 60 + int(start[3:]))
        temp = ""
        q = time // len(song)
        r = time % len(song)
        temp = song * q + song[:r]
        if m in temp:
            if len(answer) == 0 or answer[1] < time:
                answer = [title, time]

    return answer[0] if len(answer) != 0 else "(None)"
