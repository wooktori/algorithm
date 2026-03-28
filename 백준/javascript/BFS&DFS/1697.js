const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "test.txt")
  .toString()
  .trim()
  .split("\n");

const [start, target] = input[0].split(" ").map(Number);
const MAX = 100001;
const dist = new Array(MAX).fill(-1);

const queue = [start];
dist[start] = 0;

let head = 0;
while (head < queue.length) {
  const cur = queue[head++];
  if (cur === target) {
    console.log(dist[target]);
    break;
  }
  for (const next of [cur - 1, cur + 1, cur * 2]) {
    if (next >= 0 && next < MAX && dist[next] === -1) {
      dist[next] = dist[cur] + 1;
      queue.push(next);
    }
  }
}
