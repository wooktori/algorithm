def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    node = set([costs[0][0]])

    while len(node) != n:
        for start, end, value in costs:
            if start in node and end in node:
                continue
            if start in node or end in node:
                node.add(start)
                node.add(end)
                answer += value
                break
    return answer
