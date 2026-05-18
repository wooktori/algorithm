// board[i][j]를 오른쪽 아래 꼭짓점이라고 생각하고 문제풀이
function solution(board) {
  const m = board.length;
  const n = board[0].length;
  let max = 0;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 1) {
        if (i > 0 && j > 0) {
          board[i][j] =
            Math.min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1;
        }
        max = Math.max(max, board[i][j]);
      }
    }
  }

  return max * max; // 넓이 반환
}
