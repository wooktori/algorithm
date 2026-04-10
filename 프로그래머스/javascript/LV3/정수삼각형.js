function solution(triangle) {
  const dp = Array.from({ length: triangle.length }, (_, i) =>
    Array(i + 1).fill(0),
  );
  dp[0][0] = triangle[0][0];

  for (let i = 1; i < triangle.length; i++) {
    for (let j = 0; j < triangle[i].length; j++) {
      if (j === 0) {
        dp[i][j] = dp[i - 1][0] + triangle[i][j];
      } else if (j === triangle[i].length - 1) {
        dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
      } else {
        dp[i][j] = Math.max(
          dp[i - 1][j - 1] + triangle[i][j],
          dp[i - 1][j] + triangle[i][j],
        );
      }
    }
  }
  return Math.max(...dp[dp.length - 1]);
}
