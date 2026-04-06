// 핵심 아이디어 : 한 칸을 4칸으로 나눠서 내부, 외부를 구분해야함.

function solution(rectangle, characterX, characterY, itemX, itemY) {
  const MAX = 103;
  const arr = Array.from({ length: MAX }, () => Array(MAX).fill(0));
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  // 1로 전부 채우기
  rectangle.forEach(([x1, y1, x2, y2]) => {
    for (let x = x1 * 2; x <= x2 * 2; x++) {
      for (let y = y1 * 2; y <= y2 * 2; y++) {
        arr[x][y] = 1;
      }
    }
  });

  // 내부 0으로 채우기
  rectangle.forEach(([x1, y1, x2, y2]) => {
    for (let x = x1 * 2 + 1; x <= x2 * 2 - 1; x++) {
      for (let y = y1 * 2 + 1; y <= y2 * 2 - 1; y++) {
        arr[x][y] = 0;
      }
    }
  });

  // 두배를 해줬기 때문에 좌표값 잘 생각해서 넣기
  const visited = Array.from({ length: MAX }, () => Array(MAX).fill(false));
  let head = 0;
  const queue = [[characterX * 2, characterY * 2, 0]];
  visited[characterX * 2][characterY * 2] = true;

  while (queue.length > head) {
    const [x, y, count] = queue[head++];
    if (x === itemX * 2 && y === itemY * 2) return count / 2;

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (nx < 0 || ny < 0 || nx >= MAX || ny >= MAX) continue;
      if (visited[nx][ny] || !arr[nx][ny]) continue;

      queue.push([nx, ny, count + 1]);
      visited[nx][ny] = true;
    }
  }
}
