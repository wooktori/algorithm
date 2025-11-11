def distance(place):
    arr = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                arr.append((i, j))

    for x1, y1 in arr:
        for x2, y2 in arr:
            dis = abs(x1 - x2) + abs(y1 - y2)
            if dis == 0 or dis > 2:
                continue
            if dis == 1:
                return 0
            elif x1 == x2 and place[x1][(y1 + y2) // 2] != "X":
                return 0
            elif y1 == y2 and place[(x1 + x2) // 2][y1] != "X":
                return 0
            elif x1 != x2 and y1 != y2:
                if place[x1][y2] != "X" or place[x2][y1] != "X":
                    return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(distance(place))
    return answer
