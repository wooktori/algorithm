const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [F, S, G, U, D] = input[0].split(" ").map(Number);

const dx = [U, -D];
const visited = Array(F + 1).fill(false);
visited[S] = true;
const queue = [[S, 0]];
let head = 0;

while (queue.length > head) {
  const [floor, count] = queue[head++];
  if (floor === G) {
    console.log(count);
    process.exit();
  }
  for (let i = 0; i < 2; i++) {
    const nextFloor = floor + dx[i];

    if (nextFloor <= 0 || nextFloor > F) continue;
    if (visited[nextFloor]) continue;

    queue.push([nextFloor, count + 1]);
    visited[nextFloor] = true;
  }
}

console.log("use the stairs");
