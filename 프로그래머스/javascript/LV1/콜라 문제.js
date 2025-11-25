function solution(a, b, n) {
  let answer = 0;
  while (n >= a) {
    answer += parseInt(n / a) * b;
    n = parseInt(n / a) * b + (n % a);
  }
  return answer;
}

// 수학 문제라 매력적이지 않음.
