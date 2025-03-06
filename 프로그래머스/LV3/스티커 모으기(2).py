def solution(sticker):
    n = len(sticker)
    if n <= 2:
        return max(sticker)

    dp_1o = [0] * n
    dp_1x = [0] * n
    dp_1o[0] = sticker[0]
    dp_1o[1] = sticker[0]
    dp_1x[0] = 0
    dp_1x[1] = sticker[1]

    for i in range(2, n - 1):
        dp_1o[i] = max(dp_1o[i - 2] + sticker[i], dp_1o[i - 1])

    for i in range(2, n):
        dp_1x[i] = max(dp_1x[i - 2] + sticker[i], dp_1x[i - 1])

    return max(max(dp_1o), max(dp_1x))
