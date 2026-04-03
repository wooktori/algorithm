const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].split(" ").map(Number));
}

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
let answer = 0;
const max = Math.max(...board.map((row) => Math.max(...row)));

for (let h = 0; h < max; h++) {
  const wboard = board.map((row) => row.map((v) => (v <= h ? 0 : 1)));
  const visited = Array.from({ length: n }, () => Array(n).fill(false));
  let count = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (visited[i][j] || !wboard[i][j]) continue;

      visited[i][j] = true;
      const queue = [[i, j]];
      let head = 0;
      count++;
      while (queue.length > head) {
        const [x, y] = queue[head++];

        for (let k = 0; k < 4; k++) {
          const nx = x + dx[k];
          const ny = y + dy[k];

          if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
          if (!wboard[nx][ny] || visited[nx][ny]) continue;

          queue.push([nx, ny]);
          visited[nx][ny] = true;
        }
      }
    }
  }
  answer = Math.max(answer, count);
}

console.log(answer);
