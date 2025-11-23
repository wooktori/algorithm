function solution(s) {
  let answer = [];
  let obj = {};
  for (let i = 0; i < s.length; i++) {
    if (s[i] in obj) {
      answer.push(i - obj[s[i]]);
      obj = { ...obj, [s[i]]: i };
    } else {
      answer.push(-1);
      obj = { ...obj, [s[i]]: i };
    }
  }
  return answer;
}
