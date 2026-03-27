const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [m, n] = input[0].split(" ").map(Number); // m=열, n=행 순서 주의
const board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].split(" ").map(Number));
}

// let day = 0;
// const dx = [-1, 1, 0, 0];
// const dy = [0, 0, -1, 1];
// const visited = Array.from({ length: n }, () => Array(m).fill(false));

// while (true) {
//   const tomato = [];
//   for (let i = 0; i < n; i++) {
//     for (let j = 0; j < m; j++) {
//       if (board[i][j] === 1 && !visited[i][j]) {
//         tomato.push([i, j]);
//       }
//     }
//   }
//   if (tomato.length === 0) break;

//   let flag = false;
//   while (tomato.length > 0) {
//     const [x, y] = tomato.shift();
//     visited[x][y] = true;
//     for (let i = 0; i < 4; i++) {
//       const nx = x + dx[i];
//       const ny = y + dy[i];
//       if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
//       if (board[nx][ny] !== 0 || visited[nx][ny]) continue;
//       board[nx][ny] = 1;
//       flag = true;
//     }
//   }
//   if (flag) day++;
// }

// const isFail = board.some(row => row.includes(0));
// console.log(isFail ? -1 : day);

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const queue = [];

// 초기 익은 토마토 queue에 삽입.
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === 1) queue.push([i, j, 0]);
  }
}

let day = 0;
let head = 0; // shift() 대신 포인터 사용

while (head < queue.length) {
  const [x, y, dist] = queue[head++]; // shift() 대신

  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
    if (board[nx][ny] !== 0) continue;

    board[nx][ny] = 1;
    day = Math.max(day, dist + 1);
    queue.push([nx, ny, dist + 1]);
  }
}

// 익지 않은 토마토가 있는 경우 예외처리.
const isFail = board.some((row) => row.includes(0));
console.log(isFail ? -1 : day);
