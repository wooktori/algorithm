# 문제오류 있는듯
def solution(number, k):
    stack = []
    for n in number:
        while len(stack) > 0 and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    if k:
        for _ in range(k):
            stack.pop()
            return "".join(stack)
    else:
        return "".join(stack)
