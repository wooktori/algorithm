function solution(bridge_length, weight, truck_weights) {
    // 다리를 큐로 표현 (길이만큼 0으로 초기화)
    const bridge = Array(bridge_length).fill(0);
    let time = 0;
    let bridgeWeight = 0; // 현재 다리 위 트럭 무게 합
    let idx = 0;          // 다음에 올라갈 트럭 인덱스

    // 모든 트럭이 올라가고, 다리 위에도 없을 때까지 반복
    while (idx < truck_weights.length || bridgeWeight > 0) {
        time++;

        // 다리 맨 앞 칸 제거 (1초마다 한 칸씩 이동)
        bridgeWeight -= bridge.shift();

        // 다음 트럭이 올라갈 수 있으면 진입
        if (idx < truck_weights.length && bridgeWeight + truck_weights[idx] <= weight) {
            bridge.push(truck_weights[idx]);
            bridgeWeight += truck_weights[idx];
            idx++;
        } else {
            bridge.push(0); // 트럭 없으면 빈 칸(0) 채움
        }
    }

    return time;
}
