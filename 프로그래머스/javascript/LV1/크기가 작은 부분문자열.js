function solution(t, p) {
  let answer = 0;
  for (let i = 0; i < t.length - p.length + 1; i++) {
    if (p >= t.slice(i, i + p.length)) {
      answer += 1;
    }
  }

  return answer;
}

// slice(a,b) => a부터 b-1 까지 문자열 자르기.
