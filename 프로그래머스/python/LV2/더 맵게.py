import heapq


def solution(S, K):
    heapq.heapify(S)
    cnt = 0

    while S[0] < K:
        heapq.heappush(S, heapq.heappop(S) + heapq.heappop(S) * 2)
        cnt += 1

        if len(S) == 1 and S[0] < K:
            return -1
    return cnt
