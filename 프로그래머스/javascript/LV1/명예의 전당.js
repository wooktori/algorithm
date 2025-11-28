function solution(k, score) {
  let answer = [];
  let crown = [];
  for (let i = 0; i < score.length; i++) {
    if (crown.length < k) {
      crown.push(score[i]);
    } else {
      if (crown[0] < score[i]) {
        crown[0] = score[i];
      }
    }
    crown.sort((a, b) => a - b);
    answer.push(crown[0]);
  }
  return answer;
}
