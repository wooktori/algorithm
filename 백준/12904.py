import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()


def first(word):
    return word + S


def second(word):
    return word[::-1] + T
