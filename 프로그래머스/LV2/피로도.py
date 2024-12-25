import itertools


def solution(k, dungeons):
    permutation_list = list(itertools.permutations(dungeons))

    answer = []
    for p in permutation_list:
        total = 0
        temp = k
        for i, j in p:
            if i > temp:
                break
            else:
                temp = temp - j
                total += 1

        answer.append(total)

    return max(answer)
