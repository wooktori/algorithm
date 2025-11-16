function solution(n) {
  let a = Math.sqrt(n);
  return Number.isInteger(a) ? (a + 1) ** 2 : -1;
}

// 1. Math.sqrt() 를 이용해 제곱근.
// 2. Number.isInteger() 을 이용해 정수인지 아닌지 판별.
