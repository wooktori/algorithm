const input = require('fs').readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'test.txt').toString().trim().split('\n');

const target = input[1].split(' ').map(Number);
const arr = input[3].split(' ').map(Number);

const set = new Set(target);

let answer = [];

for (let element of arr) {
    answer.push(set.has(element) ? 1 : 0);
}

console.log(answer.join('\n'));