const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .split("\n");

let idx = 0;
while (true) {
  const [l, r, c] = input[idx++].split(" ").map(Number);
  if (l === 0 && r === 0 && c === 0) break;

  const board = [];
  for (let i = 0; i < l; i++) {
    const layer = [];
    for (let j = 0; j < r; j++) {
      layer.push(input[idx++].split(""));
    }
    board.push(layer);
    idx++; // 빈 줄 스킵
  }

  // 출발 위치 찾기
  let sl, sr, sc;
  for (let i = 0; i < l; i++)
    for (let j = 0; j < r; j++)
      for (let k = 0; k < c; k++)
        if (board[i][j][k] === "S") [sl, sr, sc] = [i, j, k];

  const dl = [1, -1, 0, 0, 0, 0];
  const dr = [0, 0, 1, -1, 0, 0];
  const dc = [0, 0, 0, 0, 1, -1];

  const visited = Array.from({ length: l }, () =>
    Array.from({ length: r }, () => Array(c).fill(false)),
  );
  visited[sl][sr][sc] = true;
  const queue = [[sl, sr, sc, 0]];
  let head = 0;
  let escaped = false;

  while (queue.length > head) {
    const [z, x, y, dist] = queue[head++];

    if (board[z][x][y] === "E") {
      console.log(`Escaped in ${dist} minute(s).`);
      escaped = true;
      break;
    }

    for (let i = 0; i < 6; i++) {
      const nz = z + dl[i];
      const nx = x + dr[i];
      const ny = y + dc[i];

      if (nz < 0 || nx < 0 || ny < 0 || nz >= l || nx >= r || ny >= c) continue;
      if (board[nz][nx][ny] === "#" || visited[nz][nx][ny]) continue;

      visited[nz][nx][ny] = true;
      queue.push([nz, nx, ny, dist + 1]);
    }
  }

  if (!escaped) console.log("Trapped!");
}
