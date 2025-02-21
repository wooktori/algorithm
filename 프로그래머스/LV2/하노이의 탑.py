def solution(n):
    answer = []

    def hanoi(start, end, rest, n):
        if n == 1:
            answer.append([start, end])
            return
        hanoi(start, rest, end, n - 1)
        hanoi(start, end, rest, 1)
        hanoi(rest, end, start, n - 1)

    hanoi(1, 3, 2, n)
    return answer
