function solution(A, B) {
  let answer = 0;
  A.sort((a, b) => a - b);
  B.sort((a, b) => a - b);

  let flag = 0;
  let pa = 0;
  while (flag < B.length) {
    if (A[pa] < B[flag]) {
      answer++;
      pa++;
    }
    flag++;
  }
  return answer;
}
