const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const t = Number(input[0]);
let idx = 1;

for (let i = 0; i < t; i++) {
  const n = Number(input[idx++]);
  const row1 = input[idx++].split(" ").map(Number);
  const row2 = input[idx++].split(" ").map(Number);
  const arr = [[...row1], [...row2]];

  const dp = Array.from({ length: 2 }, () => Array(row1.length).fill(0));
  dp[0][0] = arr[0][0];
  dp[1][0] = arr[1][0];
  dp[0][1] = Math.max(dp[1][0] + arr[0][1], arr[0][0]);
  dp[1][1] = Math.max(dp[0][0] + arr[1][1], arr[1][0]);

  for (let j = 2; j < n; j++) {
    dp[0][j] = Math.max(dp[1][j - 1], dp[0][j - 2], dp[1][j - 2]) + arr[0][j];
    dp[1][j] = Math.max(dp[0][j - 1], dp[0][j - 2], dp[1][j - 2]) + arr[1][j];
  }

  console.log(Math.max(dp[0][n - 1], dp[1][n - 1]));
}
