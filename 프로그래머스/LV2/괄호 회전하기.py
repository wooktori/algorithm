def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == "[" and s[j] == "]":
                    stack.pop()
                elif stack[-1] == "{" and s[j] == "}":
                    stack.pop()
                elif stack[-1] == "(" and s[j] == ")":
                    stack.pop()
                else:
                    stack.append(s[j])
            else:
                stack.append(s[j])
        if len(stack) == 0:
            answer += 1
        s.append(s.pop(0))

    return answer
