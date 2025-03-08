from collections import defaultdict


def solution(tickets):
    answer = []
    graph = defaultdict(list)

    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)

    def dfs(start):
        while graph[start]:
            next = graph[start].pop()
            dfs(next)
        answer.append(start)

    dfs("ICN")
    return answer[::-1]
