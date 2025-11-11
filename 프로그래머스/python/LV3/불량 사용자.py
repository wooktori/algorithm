from itertools import permutations


def check(name, ban):
    if len(name) == len(ban):
        for i in range(len(ban)):
            if ban[i] == "*":
                continue
            elif name[i] != ban[i]:
                return False
    else:
        return False
    return True


def solution(user_id, banned_id):
    arr = []
    for i in permutations(user_id, len(banned_id)):
        flag = True
        for j in range(len(banned_id)):
            if not check(i[j], banned_id[j]):
                flag = False
        if flag:
            if set(i) not in arr:
                arr.append(set(i))
    return len(arr)
