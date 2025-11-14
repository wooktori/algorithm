function solution(n) {
  let answer = [];
  for (let i = 1; i <= n; i++) {
    if (n % i === 0) {
      answer.push(i);
    }
  }
  return answer.reduce((acc, cur) => acc + cur, 0);
}

// reduct를 활용한 배열의 합 구하기.
// n이 엄청 커지면 시간복잡도에 걸릴 듯 => 로직을 바꿀 필요가 있다. => 절반 탐색 후 두배 해주기
