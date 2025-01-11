from itertools import permutations


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    arr = list(numbers)
    nums = set()

    for i in range(1, len(arr) + 1):
        temp = list(permutations(arr, i))
        for j in temp:
            nums.add(int("".join(j)))

    for i in nums:
        if prime(i):
            answer += 1

    return answer
