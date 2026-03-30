const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].split(""));
}

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const MAX = 1e9;

// 불이 몇초 뒤에 도착하는지에 대한 정보 저장 로직.
const fire = Array.from({ length: n }, () => Array(m).fill(MAX));
const fireQueue = [];
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === "F") {
      fireQueue.push([i, j, 0]);
      fire[i][j] = 0;
    }
  }
}
let flag = 0;
while (fireQueue.length > flag) {
  const [x, y, time] = fireQueue[flag++];
  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
    if (board[nx][ny] === "#" || fire[nx][ny] !== MAX) continue;
    fire[nx][ny] = time + 1;
    fireQueue.push([nx, ny, time + 1]);
  }
}

// 초기 시작 좌표 찾기.
let startX = 0;
let startY = 0;

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === "J") {
      startX = i;
      startY = j;
    }
  }
}

// 위에서 만든 불의 시간 보드와 비교해 탈출 경로 찾기.
const queue = [[startX, startY, 0]];
flag = 0;

while (flag < queue.length) {
  const [x, y, time] = queue[flag++];
  for (let i = 0; i < 4; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
      console.log(time + 1);
      process.exit();
    }
    if (board[nx][ny] !== ".") continue;
    // 불과 사람이 동시에 같은 칸에 도착한 경우에는 사람이 먼저로 판단.
    if (time + 1 < fire[nx][ny]) {
      queue.push([nx, ny, time + 1]);
      board[nx][ny] = "J";
    } else {
      board[nx][ny] = "F";
    }
  }
}

console.log("IMPOSSIBLE");
