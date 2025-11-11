def solution(s):
    for i in s:
        if "0" <= i <= "9":
            continue
        else:
            return False

    if len(s) == 4 or len(s) == 6:
        return True
    return False


# s.isdigit() => 문자열 숫자로 이루어져있는지 판별 가능
