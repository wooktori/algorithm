function solution(d, budget) {
  let answer = 0;
  let i = 0;
  d.sort((a, b) => a - b);
  while (budget > 0) {
    if (i === d.length) {
      break;
    }
    budget -= d[i];
    if (budget < 0) {
      break;
    }
    answer += 1;
    i++;
  }
  return answer;
}

// 참고 코드
// 정렬 후, reduce 함수를 이용해 조건을 만족하면 count 값을 1씩 올려 반환.
function solution(d, budget) {
  return d
    .sort((a, b) => a - b)
    .reduce((count, price) => {
      return count + ((budget -= price) >= 0);
    }, 0);
}
