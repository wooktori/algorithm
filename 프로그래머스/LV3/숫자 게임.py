from collections import deque


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    q = deque(B)
    index = 0
    while q:
        b = q.popleft()
        if A[index] < b:
            answer += 1
            index += 1

    return answer
