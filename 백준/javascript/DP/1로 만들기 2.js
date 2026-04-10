const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);

const dp = Array(n + 1).fill(0);
const path = Array(n + 1).fill(0);

for (let i = 2; i <= n; i++) {
  dp[i] = dp[i - 1] + 1;
  path[i] = i - 1;

  if (i % 2 === 0 && dp[i / 2] + 1 < dp[i]) {
    dp[i] = dp[i / 2] + 1;
    path[i] = i / 2;
  }
  if (i % 3 === 0 && dp[i / 3] + 1 < dp[i]) {
    dp[i] = dp[i / 3] + 1;
    path[i] = i / 3;
  }

  console.log(path);
}

// 경로 역추적
const result = [];
let cur = n;
while (cur !== 0) {
  result.push(cur);
  cur = path[cur];
}

console.log(dp[n]);
console.log(result.join(" "));
