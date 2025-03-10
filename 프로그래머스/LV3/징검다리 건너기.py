def solution(stones, k):
    answer = 0
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        count = 0
        copyStones = stones.copy()
        for stone in copyStones:
            stone -= mid
            if stone <= 0:
                count += 1
            else:
                count = 0
            if count == k:
                answer = mid
                break
        if count == k:
            right = mid - 1
        elif count < k:
            left = mid + 1
    return answer
