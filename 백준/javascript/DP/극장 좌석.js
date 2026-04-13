// 로직 도출까지는 잘 했지만, 엣지케이스를 제대로 파악하지 않아 여러번 실패.

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const m = Number(input[1]);
const pairs = [];

if (n === 1) {
  console.log(1);
  process.exit();
}
if (m === 0) pairs.push(n);

for (let i = 2; i < 2 + m; i++) {
  const num = Number(input[i]);
  const prevNum = Number(input[i - 1]);

  if (i === 2) pairs.push(num - 1);
  else pairs.push(num - prevNum - 1);

  if (i === 1 + m) pairs.push(n - num);
}

const dp = Array(n + 1).fill(0);
dp[0] = 1;
dp[1] = 1;
dp[2] = 2;

for (let i = 3; i <= n; i++) {
  dp[i] = dp[i - 1] + dp[i - 2];
}

let answer = 1;

for (let i = 0; i < pairs.length; i++) {
  answer *= dp[pairs[i]];
}

console.log(answer);
