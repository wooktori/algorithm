function solution(x) {
  let hashad = (x + "")
    .split("")
    .map((e) => +e)
    .reduce((acc, cur) => acc + cur, 0);
  return x % hashad ? false : true;
}

// 숫자를 배열로 변환해 여러 함수를 이용해 조작하기.
