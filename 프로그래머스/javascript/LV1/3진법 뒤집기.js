function solution(n) {
  return parseInt(n.toString(3).split("").reverse().join(""), 3);
}

// 숫자.toString(3) ==> 3진법으로 변환.
// parseInt(문자열, 진법) ==> 해당 진법의 수를 10진수로 변환.
