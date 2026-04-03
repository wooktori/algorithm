const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].split("").map(Number));
}

let count = 0;
let area = [];

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const visited = Array.from({ length: n }, () => Array(n).fill(false));

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (!board[i][j] || visited[i][j]) continue;

    const queue = [[i, j]];
    let head = 0;
    visited[i][j] = true;
    count++;
    while (queue.length > head) {
      const [x, y] = queue[head++];
      for (let k = 0; k < 4; k++) {
        const nx = x + dx[k];
        const ny = y + dy[k];

        if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
        if (!board[nx][ny] || visited[nx][ny]) continue;

        queue.push([nx, ny]);
        visited[nx][ny] = true;
      }
    }
    area.push(head);
  }
}
area.sort((a, b) => a - b);

console.log(count);
for (let i = 0; i < area.length; i++) {
  console.log(area[i]);
}
