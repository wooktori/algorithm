function solution(n) {
  let answer = 0;
  answer += [...String(n)].reduce((acc, cur) => acc + parseInt(cur), 0);
  return answer;
}

// 1.
// reduce 함수란 ? 배열에 존재하는 값들 더해줌.
// reduce 사용법 => arr.reduce((acc,cur) => acc + cur, 초기값);

// 2.
// 숫자를 문자열로 변환할 때, String(num)도 있지만 num+''도 가능하다.
