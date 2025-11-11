from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque()

    while truck_weights or on_bridge:
        for i in on_bridge:
            i[1] += 1

        if on_bridge and on_bridge[0][1] == bridge_length:
            on_bridge.popleft()

        if (
            truck_weights
            and sum([i[0] for i in on_bridge]) + truck_weights[0] <= weight
        ):
            truck = truck_weights.popleft()
            on_bridge.append([truck, 0])

        answer += 1

    return answer
