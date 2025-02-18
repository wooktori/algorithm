from math import gcd


def solution(arrayA, arrayB):
    answer = 0
    gcdA = 0
    gcdB = 0

    for i in range(len(arrayA)):
        gcdA = gcd(gcdA, arrayA[i])
        gcdB = gcd(gcdB, arrayB[i])

    for i in range(len(arrayA)):
        if arrayB[i] % gcdA == 0:
            gcdA = 1
        if arrayA[i] % gcdB == 0:
            gcdB = 1

    if gcdA == 1 and gcdB == 1:
        return 0

    return max(gcdA, gcdB)
