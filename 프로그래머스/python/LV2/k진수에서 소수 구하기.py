def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    temp = ""
    ans = 0

    while n:
        temp = str(int(n % k)) + temp
        n //= k

    arr = temp.split("0")
    nums = []
    for i in arr:
        if len(i):
            nums.append(int(i))

    for i in nums:
        if prime(i):
            ans += 1

    return ans
