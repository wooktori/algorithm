def recursive(n):
    if n == 1:
        return "-"

    side = recursive(n // 3)
    center = " " * (n // 3)
    return side + center + side


while True:
    try:
        N = int(input())
        print(recursive(3**N))
    except:
        break
