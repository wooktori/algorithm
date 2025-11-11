def solution(dirs):
    road = set()
    answer = 0
    xy = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}
    x, y = 0, 0

    for i in dirs:
        dx, dy = xy[i]
        nx = x + dx
        ny = y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            road.add(((x, y), (nx, ny)))
            road.add(((nx, ny), (x, y)))
            x = nx
            y = ny

    return len(road) // 2
