def solution(a, b):
    arr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(12):
        if a > i + 1:
            day += arr[i]
        elif a == (i + 1):
            day += b
            break

    if day % 7 == 0:
        return "THU"
    elif day % 7 == 1:
        return "FRI"
    elif day % 7 == 2:
        return "SAT"
    elif day % 7 == 3:
        return "SUN"
    elif day % 7 == 4:
        return "MON"
    elif day % 7 == 5:
        return "TUE"
    else:
        return "WED"
