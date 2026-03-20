// 최단거리 → BFS

function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;
  const dx = [-1, 1, 0, 0]; // 상하좌우
  const dy = [0, 0, -1, 1];

  const visited = Array.from({ length: n }, () => Array(m).fill(false));
  const queue = [[0, 0, 1]]; // [행, 열, 거리] - 시작 칸도 1로 카운트
  visited[0][0] = true;

  while (queue.length > 0) {
    const [x, y, dist] = queue.shift();

    if (x === n - 1 && y === m - 1) return dist;

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      // 범위 초과, 이미 방문, 벽이면 스킵
      if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
      if (visited[nx][ny] || maps[nx][ny] === 0) continue;

      visited[nx][ny] = true;
      queue.push([nx, ny, dist + 1]);
    }
  }

  return -1; // 도달 불가
}
