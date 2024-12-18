def check(m, park, i, j):
    for a in range(i, i + m):
        for b in range(j, j + m):
            if a < len(park) and b < len(park[0]):
                if park[a][b] != "-1":
                    return False
            else:
                return False
    return True


def solution(mats, park):
    answer = 0
    mats.sort(reverse=True)
    for m in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if check(m, park, i, j):
                    return m
    return -1
