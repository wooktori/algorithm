const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

let idx = 0;
const T = Number(input[idx++]);

for (let t = 0; t < T; t++) {
  const [m, n, k] = input[idx++].split(" ").map(Number); // m=열, n=행
  const board = Array.from({ length: n }, () => Array(m).fill(0));

  for (let i = 0; i < k; i++) {
    const [x, y] = input[idx++].split(" ").map(Number);
    board[y][x] = 1;
  }

  let count = 0;
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  const visited = Array.from({ length: n }, () => Array(m).fill(false));

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (!board[i][j] || visited[i][j]) continue;

      const queue = [[i, j]];
      let head = 0;
      visited[i][j] = true;

      while (head < queue.length) {
        const [x, y] = queue[head++];

        for (let k = 0; k < 4; k++) {
          const nx = x + dx[k];
          const ny = y + dy[k];
          if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
          if (!board[nx][ny] || visited[nx][ny]) continue;

          visited[nx][ny] = true;
          queue.push([nx, ny]);
        }
      }
      count++;
    }
  }
  console.log(count);
}
