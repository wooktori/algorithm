def solution(numbers):
    answer = ""
    numbers = sorted([str(i) for i in numbers], key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))
