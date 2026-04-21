function solution(topping) {
  const a = new Set();
  const b = {};

  let answer = 0;
  let check = 0;

  // b에 1번토핑:4개 의 형식으로 데이터 저장
  for (let i = 0; i < topping.length; i++) {
    if (b[topping[i]]) {
      b[topping[i]]++;
    } else {
      b[topping[i]] = 1;
      check++;
    }
  }

  // a에 토핑을 하나씩 넣으면서 체크
  for (let i = 0; i < topping.length; i++) {
    a.add(topping[i]);
    b[topping[i]]--;

    if (!b[topping[i]]) check--;
    if (a.size === check) answer++;
  }

  return answer;
}
