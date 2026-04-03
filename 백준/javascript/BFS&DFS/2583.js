const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [m, n, k] = input[0].split(" ").map(Number); // m=행, n=열
const board = Array.from({ length: m }, () => Array(n).fill(0));

for (let i = 1; i <= k; i++) {
  const [x1, y1, x2, y2] = input[i].split(" ").map(Number);
  for (let y = y1; y < y2; y++) {
    for (let x = x1; x < x2; x++) {
      board[m - 1 - y][x] = 1; // y축 반전 (아래→위 좌표계)
    }
  }
}

let count = 0;
const arr = [];

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const visited = Array.from({ length: m }, () => Array(n).fill(false));

for (let i = 0; i < m; i++) {
  for (let j = 0; j < n; j++) {
    if (visited[i][j] || board[i][j]) continue;

    const queue = [[i, j]];
    visited[i][j] = true;
    let head = 0;
    while (queue.length > head) {
      const [x, y] = queue[head++];

      for (let k = 0; k < 4; k++) {
        const nx = x + dx[k];
        const ny = y + dy[k];
        if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
        if (board[nx][ny] || visited[nx][ny]) continue;

        queue.push([nx, ny]);
        visited[nx][ny] = true;
      }
    }
    count++;
    arr.push(head);
  }
}

console.log(count);
console.log(arr.sort((a, b) => a - b).join(" "));
