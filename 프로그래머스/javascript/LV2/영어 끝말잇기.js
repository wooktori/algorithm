function solution(n, words) {
  let target = -1;
  for (let i = 1; i < words.length; i++) {
    // 끝말잇기 실패
    if (words[i - 1].slice(-1) !== words[i][0]) {
      target = i;
      break;
    }
    // 중복된 단어
    if (words.indexOf(words[i]) !== i) {
      target = i;
      break;
    }
  }

  if (target === -1) return [0, 0];

  return [(target % n) + 1, Math.floor(target / n) + 1];
}
