const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [T, W] = input[0].split(" ").map(Number);
const plum = input.slice(1).map(Number); // 각 초마다 자두가 떨어지는 나무 번호

// dp[i][j] = i초에 j번 이동했을 때 받는 최대 자두 수
const dp = Array.from({ length: T + 1 }, () => Array(W + 1).fill(0));

for (let i = 1; i <= T; i++) {
  for (let j = 0; j <= W; j++) {
    // j번 이동했을 때 현재 위치: 짝수 → 1번, 홀수 → 2번
    const position = j % 2 === 0 ? 1 : 2;
    const isCatch = plum[i - 1] === position ? 1 : 0;

    if (j === 0) {
      dp[i][j] = dp[i - 1][j] + isCatch;
    } else {
      dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - 1]) + isCatch;
    }
  }
}

console.log(Math.max(...dp[T]));
