function solution(n, wires) {
    let answer = n;

    const graph = Array.from({ length: n + 1 }, () => []);
    for (const [s, e] of wires) {
        graph[s].push(e);
        graph[e].push(s);
    }

    function bfs(start, exclude) {
        const visited = Array(n + 1).fill(false);
        const queue = [start];
        visited[start] = true;
        visited[exclude] = true; // 제거한 간선의 반대편 노드 차단
        let count = 1;

        while (queue.length) {
            const cur = queue.shift();
            for (const next of graph[cur]) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.push(next);
                    count++;
                }
            }
        }
        return count;
    }

    for (const [s, e] of wires) {
        const count = bfs(s, e);
        answer = Math.min(answer, Math.abs(n - count * 2));
    }

    return answer;
}
