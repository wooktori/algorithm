// 연결 요소 탐색 -> bfs
// 가장 기본적인 bfs 사용 문제로, 반복문과 큐를 이용해 적절한 값 도출하기.

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].split(" ").map(Number));
}

let maxSize = 0;
let count = 0;

const visited = Array.from({ length: n }, () => Array(m).fill(false));
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === 0 || visited[i][j]) continue;
    const queue = [[i, j]];
    count++;
    visited[i][j] = true;
    let size = 1;

    while (queue.length > 0) {
      const [x, y] = queue.shift();
      for (let k = 0; k < 4; k++) {
        const nx = x + dx[k];
        const ny = y + dy[k];

        if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
        if (board[nx][ny] === 0 || visited[nx][ny]) continue;

        queue.push([nx, ny]);
        visited[nx][ny] = true;
        size++;
      }
    }
    maxSize = Math.max(maxSize, size);
  }
}

console.log(count, maxSize);
