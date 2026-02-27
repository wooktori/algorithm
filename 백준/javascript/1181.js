const input = require('fs').readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'test.txt').toString().trim().split('\n');

const answer = [...new Set(input.slice(1))].sort((a,b)=>{
    if(a.length===b.length){
        return a.localeCompare(b);
    }
    return a.length-b.length;
})

console.log(answer.join('\n'));