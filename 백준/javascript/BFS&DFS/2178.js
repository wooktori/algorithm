// 최단거리 -> bfs
// 최단거리를 묻는 문제일때는 큐에 거리값까지 넣어서 거리를 증가시키면서 값 확인하기.

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].split("").map(Number));
}

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const visited = Array.from({ length: n }, () => Array(m).fill(false));
const queue = [[0, 0, 1]];
visited[0][0] = true;

while (queue.length > 0) {
  const [x, y, dist] = queue.shift();

  if (x === n - 1 && y === m - 1) {
    console.log(dist);
  }

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];

    if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
    if (!board[nx][ny] || visited[nx][ny]) continue;

    queue.push([nx, ny, dist + 1]);
    visited[nx][ny] = true;
  }
}
