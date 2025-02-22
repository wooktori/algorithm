def solution(r1, r2):
    answer = 0
    big = 0
    small = 0
    temp = 0
    for i in range(r1 + 1):
        small += int((r1**2 - i**2) ** 0.5)
        if ((r1**2 - i**2) ** 0.5) % 1 == 0:
            temp += 1
    for i in range(r2 + 1):
        big += int((r2**2 - i**2) ** 0.5)

    small = small * 4 + 1
    big = big * 4 + 1
    return big - small + 4 if temp == 2 else big - small + temp * 4 - 4
