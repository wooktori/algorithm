def solution(line):
    answer = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a * d - b * c == 0:
                continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            if int(x) == x and int(y) == y:
                answer.append([int(x), int(y)])
    maxX = max([i[0] for i in answer])
    minX = min([i[0] for i in answer])
    maxY = max([i[1] for i in answer])
    minY = min([i[1] for i in answer])
    arr = []

    for j in range(maxY, minY - 1, -1):
        temp = ""
        for i in range(minX, maxX + 1):
            if [i, j] in answer:
                temp += "*"
            else:
                temp += "."
        arr.append(temp)
    return arr
