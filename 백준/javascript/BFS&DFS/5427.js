const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

let idx = 0;
const T = Number(input[idx++]);

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

for (let t = 0; t < T; t++) {
  const [w, h] = input[idx++].split(" ").map(Number); // w=열, h=행
  const board = [];
  for (let i = 0; i < h; i++) {
    board.push(input[idx++].split(""));
  }

  // 초기 불 위치 큐에 저장, 시작 위치 저장
  const fireQ = [];
  const fire = Array.from({ length: h }, () => Array(w).fill(1e9));
  let head = 0;
  let startX = 0;
  let startY = 0;
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (board[i][j] === "*") {
        fireQ.push([i, j, 0]);
        fire[i][j] = 0;
      }
      if (board[i][j] === "@") {
        startX = i;
        startY = j;
      }
    }
  }

  while (fireQ.length > head) {
    const [x, y, time] = fireQ[head++];

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
      if (board[nx][ny] === "#" || fire[nx][ny] !== 1e9) continue;
      fire[nx][ny] = time + 1;
      fireQ.push([nx, ny, time + 1]);
    }
  }
  const queue = [[startX, startY, 0]];
  let qHead = 0;
  board[startX][startY] = "#"; // 방문 처리
  let escaped = false;

  while (queue.length > qHead) {
    const [x, y, time] = queue[qHead++];

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx < 0 || ny < 0 || nx >= h || ny >= w) {
        console.log(time + 1);
        escaped = true;
        break;
      }
      if (board[nx][ny] === "#") continue;
      if (time + 1 >= fire[nx][ny]) continue;

      board[nx][ny] = "#"; // 방문 처리
      queue.push([nx, ny, time + 1]);
    }
    if (escaped) break;
  }

  if (!escaped) console.log("IMPOSSIBLE");
}
