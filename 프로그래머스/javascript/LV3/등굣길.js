function solution(m, n, puddles) {
  const board = Array.from({ length: n }, () => Array(m).fill(0));
  const dp = Array.from({ length: n }, () => Array(m).fill(0));
  dp[0][0] = 1;
  for (const [x, y] of puddles) {
    board[y - 1][x - 1] = 1;
  }

  // 각 단계에서 나머지를 구해야 효율성 테스트 통과
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (i === 0 && j === 0) continue;
      if (board[i][j] === 1) continue;
      if (i === 0) {
        dp[i][j] = dp[i][j - 1] % 1000000007;
      } else if (j === 0) {
        dp[i][j] = dp[i - 1][j] % 1000000007;
      } else {
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007;
      }
    }
  }
  return dp[n - 1][m - 1];
}
