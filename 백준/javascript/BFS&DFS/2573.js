const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
let board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].split(" ").map(Number));
}

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

let time = 0;
while (true) {
  time++;
  const newBoard = board.map((row) => [...row]);

  // 테두리에서는 실행 X
  for (let x = 1; x < n - 1; x++) {
    for (let y = 1; y < m - 1; y++) {
      const value = board[x][y];
      if (!value) continue;

      for (let k = 0; k < 4; k++) {
        const nx = x + dx[k];
        const ny = y + dy[k];
        if (board[nx][ny] === 0 && newBoard[x][y] > 0) newBoard[x][y]--;
      }
    }
  }

  const visited = Array.from({ length: n }, () => Array(m).fill(false));

  let count = 0;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (!newBoard[i][j] || visited[i][j]) continue;

      const queue = [[i, j]];
      visited[i][j] = true;
      let head = 0;

      while (queue.length > head) {
        const [x, y] = queue[head++];

        for (let k = 0; k < 4; k++) {
          const nx = x + dx[k];
          const ny = y + dy[k];

          if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
          if (!newBoard[nx][ny] || visited[nx][ny]) continue;

          queue.push([nx, ny]);
          visited[nx][ny] = true;
        }
      }
      count++;
    }
  }

  if (newBoard.every((row) => row.every((v) => v === 0))) {
    console.log(0);
    process.exit();
  }

  if (count >= 2) {
    console.log(time);
    process.exit();
  }

  board = newBoard;
}
