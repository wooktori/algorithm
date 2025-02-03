def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        temp = s[:i]
        count = 1
        ans = ""
        for j in range(i, len(s) + i, i):
            if temp == s[j : j + i]:
                count += 1
            else:
                if count == 1:
                    ans += temp
                else:
                    ans += str(count) + temp

                temp = s[j : j + i]
                count = 1

        answer.append(len(ans))
    return min(answer)
