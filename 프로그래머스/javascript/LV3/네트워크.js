function solution(n, computers) {
  let answer = 0;
  const visited = Array(n).fill(false);

  for (let i = 0; i < n; i++) {
    // 첫번째 컴퓨터부터 연결된 모든 컴퓨터 탐색
    if (visited[i]) continue;

    const queue = [i];
    visited[i] = true;
    let head = 0;

    while (queue.length > head) {
      const x = queue[head++];

      for (let y = 0; y < n; y++) {
        if (visited[y] || !computers[x][y]) continue;
        queue.push(y);
        visited[y] = true;
      }
    }

    answer++;
  }

  return answer;
}
