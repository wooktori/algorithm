function counter(number) {
  let answer = 0;
  for (let i = 1; i <= number; i++) {
    if (number % i === 0) {
      answer += 1;
    }
  }
  return answer;
}

function solution(left, right) {
  let total = 0;
  for (let i = left; i <= right; i++) {
    if (counter(i) % 2 === 0) {
      total += i;
    } else {
      total -= i;
    }
  }
  return total;
}
