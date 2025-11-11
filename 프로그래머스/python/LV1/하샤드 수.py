def solution(x):
    div = sum(list(int(i) for i in str(x)))
    if x % div:
        return False
    else:
        return True
