// 올바른 괄호 문자열인지 확인
function isCorrect(str) {
  let stack = [];
  for (const a of str) {
    if (a === "[" || a === "{" || a === "(") {
      stack.push(a);
    } else {
      if (a === "]" && stack[stack.length - 1] === "[") {
        stack.pop();
      } else if (a === "}" && stack[stack.length - 1] === "{") {
        stack.pop();
      } else if (a === ")" && stack[stack.length - 1] === "(") {
        stack.pop();
      }
    }
  }

  return stack.length === 0;
}

function solution(s) {
  let answer = 0;
  if (s.length % 2) return 0;

  for (let i = 0; i < s.length; i++) {
    let str = s.slice(i) + s.slice(0, i);
    if (isCorrect(str)) answer++;
  }

  return answer;
}
