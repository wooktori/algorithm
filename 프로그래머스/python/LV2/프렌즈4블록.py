def pull(i, j, board):
    while i != 0:
        board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
        i -= 1
    return board


def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    answer = 0
    rm_set = set()

    while True:
        # 2*2 블록 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                target = board[i][j]
                if (
                    board[i][j] != "0"
                    and board[i + 1][j] == target
                    and board[i][j + 1] == target
                    and board[i + 1][j + 1] == target
                ):
                    rm_set.add((i, j))
                    rm_set.add((i + 1, j))
                    rm_set.add((i, j + 1))
                    rm_set.add((i + 1, j + 1))

        if len(rm_set) == 0:
            return answer
        answer += len(rm_set)

        # 제거된 블록 변환하기
        for i, j in rm_set:
            board[i][j] = "0"

        rm_set = set()

        # 블록 내리기
        for i in range(m):
            for j in range(n):
                if board[i][j] == "0":
                    board = pull(i, j, board)
