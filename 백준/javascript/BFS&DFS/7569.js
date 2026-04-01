const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [m, n, h] = input[0].split(" ").map(Number);
const board = [];
let idx = 1;
for (let i = 0; i < h; i++) {
  const layer = [];
  for (let j = 0; j < n; j++) {
    layer.push(input[idx++].split(" ").map(Number));
  }
  board.push(layer);
}

let day = 0;
const dx = [-1, 1, 0, 0, 0, 0];
const dy = [0, 0, -1, 1, 0, 0];
const dz = [0, 0, 0, 0, -1, 1];

const queue = [];
let head = 0;

for (let i = 0; i < h; i++) {
  for (let j = 0; j < n; j++) {
    for (let k = 0; k < m; k++) {
      if (board[i][j][k] === 1) {
        queue.push([i, j, k, 0]);
      }
    }
  }
}

while (queue.length > head) {
  const [x, y, z, value] = queue[head++];

  for (let i = 0; i < 6; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    const nz = z + dz[i];

    if (nx < 0 || ny < 0 || nz < 0 || nx >= h || ny >= n || nz >= m) continue;
    if (board[nx][ny][nz]) continue;

    board[nx][ny][nz] = 1;
    queue.push([nx, ny, nz, value + 1]);
    day = Math.max(day, value + 1);
  }
}

const isFail = board.some((arr) => arr.some((row) => row.includes(0)));
console.log(isFail ? -1 : day);
