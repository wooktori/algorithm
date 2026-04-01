const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const board = [];
for (let i = 1; i <= n; i++) {
  board.push(input[i].split(""));
}

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

// 적록색맹일 경우와 아닐 경우를 구분하기 위해 변수값으로 처리
function countFn(isSpecial) {
  let count = 0;
  const visited = Array.from({ length: n }, () => Array(n).fill(false));
  // 적록색맹이라면, 적색과 녹색은 S라는 문자열로 치환해서 계산
  const myColor = (value) => (isSpecial && value !== "B" ? "S" : value);

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (visited[i][j]) continue;
      const queue = [[i, j]];
      visited[i][j] = true;
      let head = 0;

      while (queue.length > head) {
        const [x, y] = queue[head++];

        for (let k = 0; k < 4; k++) {
          const nx = x + dx[k];
          const ny = y + dy[k];

          if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
          if (visited[nx][ny]) continue;
          if (myColor(board[nx][ny]) !== myColor(board[x][y])) continue;

          visited[nx][ny] = true;
          queue.push([nx, ny]);
        }
      }
      count++;
    }
  }
  return count;
}

console.log(countFn(false), countFn(true));
