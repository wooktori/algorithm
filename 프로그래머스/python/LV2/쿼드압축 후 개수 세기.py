def solution(arr):
    result = [0, 0]
    length = len(arr)

    def quad(x, y, len):
        start = arr[x][y]

        for i in range(x, x + len):
            for j in range(y, y + len):
                if arr[i][j] != start:
                    len = len // 2
                    quad(x, y, len)
                    quad(x, y + len, len)
                    quad(x + len, y, len)
                    quad(x + len, y + len, len)
                    return

        result[start] += 1

    quad(0, 0, length)

    return result
